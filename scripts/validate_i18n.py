"""Check documentation mirrors locally; never fetch URLs or stamp review hashes."""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'https://github.com/OpenRootdev/toolindex'
LOCALES = ('es', 'zh-CN', 'fr', 'ja', 'de', 'pt-BR')
LABELS = ('English', 'Espa\u00f1ol', '\u7b80\u4f53\u4e2d\u6587', 'Fran\u00e7ais',
          '\u65e5\u672c\u8a9e', 'Deutsch', 'Portugu\u00eas (Brasil)')
INTERNAL_NAMES = {'agents.md', 'claude.md', 'task.md', 'progress.md', 'memory.md',
                  'implementation-plan.md', 'session.md'}
EXCLUDED_PARTS = {'i18n', 'plans', 'internal', 'runs', 'run-records', 'evidence',
                  'private', 'vendor', 'generated', 'historical', 'archive', 'archives'}
INLINE = re.compile(r'(?<!`)(`+)(?!`)(.*?)\1(?!`)', re.DOTALL)
LINK = re.compile(
    r'!?\[(?:[^\[\]]|\[[^\]]*\])*\]\(\s*'
    r'(?:<([^>]+)>|([^\s()]+(?:\([^\s()]*\)[^\s()]*)*))'
    r'\s*(?:["\'][^"\']*["\']\s*)?\)'
)
REFERENCE = re.compile(r'^ {0,3}\[([^\]]+)\]:\s*(?:<([^>]+)>|(\S+))', re.MULTILINE)
URL = re.compile(r'https?://[^\s<>"\'`)\]\u3002\uff0c\uff1b\u3001]+')


def source_hash(content):
    return hashlib.sha256(content.replace('\r\n', '\n').encode('utf-8')).hexdigest()


def public_sources(root):
    candidates = list(root.glob('*.md'))
    for directory in ('docs', '.github'):
        candidates.extend((root / directory).rglob('*.md'))
    return {
        path.relative_to(root).as_posix() for path in candidates
        if path.name.lower() not in INTERNAL_NAMES
        and not (set(part.lower() for part in path.relative_to(root).parts[:-1]) & EXCLUDED_PARTS)
    }


def fenced(content):
    blocks, prose, current = [], [], []
    marker = None
    for line in content.splitlines(keepends=True):
        if marker is None:
            opening = re.match(r'^ {0,3}(`{3,}|~{3,})([^\n]*)', line)
            if opening:
                marker = opening.group(1)
                current = [line]
            else:
                prose.append(line)
        else:
            current.append(line)
            closing = r'^ {0,3}' + re.escape(marker[0]) + '{' + str(len(marker)) + r',}\s*$'
            if re.fullmatch(closing, line):
                blocks.append(''.join(current))
                marker = None
    if marker is not None:
        raise ValueError('unclosed fence')
    return blocks, ''.join(prose)


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls, self.ids, self.anchors = [], set(), []
        self.current_anchor = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if attrs.get(key):
                self.urls.append(attrs[key])
        for key in ('id', 'name'):
            if attrs.get(key):
                self.ids.add(attrs[key])
        if tag == 'a':
            self.current_anchor = [attrs.get('href', ''), '']

    def handle_data(self, data):
        if self.current_anchor is not None:
            self.current_anchor[1] += data

    def handle_endtag(self, tag):
        if tag == 'a' and self.current_anchor is not None:
            self.anchors.append(tuple(self.current_anchor))
            self.current_anchor = None


def links(prose):
    prose = re.sub(r'<!--.*?-->', '', prose, flags=re.DOTALL)
    prose = INLINE.sub('', prose)
    result = [match.group(1) or match.group(2) for match in LINK.finditer(prose)]
    references = {m.group(1).casefold(): m.group(2) or m.group(3)
                  for m in REFERENCE.finditer(prose)}
    prose = REFERENCE.sub('', prose)
    for match in re.finditer(r'!?\[([^\]]+)\]\[([^\]]*)\]', prose):
        key = (match.group(2) or match.group(1)).casefold()
        if key not in references:
            raise ValueError(f'undefined link reference: {key}')
        result.append(references[key])
    # Include defined shortcut references, without treating ordinary brackets as links.
    shortcut_prose = LINK.sub('', re.sub(r'!?\[[^\]]+\]\[[^\]]*\]', '', prose))
    for match in re.finditer(r'!?\[([^\]]+)\]', shortcut_prose):
        if match.group(1).casefold() in references:
            result.append(references[match.group(1).casefold()])
    result.extend(re.findall(r'<(https?://[^>]+)>', prose))
    parser = HTMLLinks()
    parser.feed(prose)
    result.extend(parser.urls)
    return [unescape(url) for url in result]


def anchors(content):
    _, prose = fenced(content)
    parser = HTMLLinks()
    parser.feed(INLINE.sub(lambda m: m.group(2), prose))
    result = set(parser.ids)
    counts = Counter()
    headings = re.findall(r'^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$', prose, re.MULTILINE)
    headings.extend(re.findall(r'<h[1-6]\b[^>]*>(.*?)</h[1-6]>', prose, re.DOTALL))
    for heading in headings:
        heading = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = re.sub(r'<[^>]+>', '', heading).replace('`', '')
        slug = re.sub(r'[^\w\- ]', '', unescape(heading).lower()).replace(' ', '-')
        occurrence = counts[slug]
        result.add(slug if not occurrence else f'{slug}-{occurrence}')
        counts[slug] += 1
    return result


def switcher_line(content):
    return [line for line in content.splitlines(keepends=True) if all(label in line for label in LABELS)]


def without_switcher(content):
    return ''.join(line for line in content.splitlines(keepends=True)
                   if not all(label in line for label in LABELS))


def safe_path(root, path):
    if not isinstance(path, str) or not path or '\\' in path:
        return False
    posix = PurePosixPath(path)
    return (not posix.is_absolute() and '..' not in posix.parts and ':' not in path
            and posix.as_posix() == path and (root / path).resolve().is_relative_to(root))


def local_target(root, document, url):
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    target = ((root / path.lstrip('/')) if path.startswith('/')
              else (document.parent / path) if path else document).resolve()
    if not target.is_relative_to(root):
        raise ValueError(f'link escapes repository: {url}')
    return target, unquote(parsed.fragment)


def check_links(root, document, prose, errors):
    targets = []
    for url in links(prose):
        resolved = local_target(root, document, url)
        if resolved is None:
            continue
        target, fragment = resolved
        targets.append(target)
        if not target.exists():
            errors.append(f'{document.relative_to(root)}: missing target {url}')
        elif fragment and target.suffix == '.md':
            if fragment not in anchors(target.read_text(encoding='utf-8')):
                errors.append(f'{document.relative_to(root)}: missing anchor {url}')
    return targets


def check_switcher(root, document, content, errors):
    lines = switcher_line(content)
    if len(lines) != 1:
        errors.append(f'{document.relative_to(root)}: expected one native-language switcher')
        return
    parser = HTMLLinks()
    parser.feed(lines[0])
    expected = [root / 'README.md'] + [root / f'docs/i18n/{locale}/README.md' for locale in LOCALES]
    if [label.strip() for _, label in parser.anchors] != list(LABELS):
        errors.append(f'{document.relative_to(root)}: switcher labels/order differ')
    targets = []
    for url, _ in parser.anchors:
        parsed = urlsplit(url)
        resolved = local_target(root, document, url)
        if parsed.scheme or parsed.netloc or parsed.path.startswith('/') or not resolved:
            errors.append(f'{document.relative_to(root)}: switcher must use relative links')
        else:
            targets.append(resolved[0])
            if not resolved[0].is_file():
                errors.append(f'{document.relative_to(root)}: missing switcher target {url}')
    if targets != [path.resolve() for path in expected]:
        errors.append(f'{document.relative_to(root)}: switcher targets differ')


def check_pair(root, source, mirror, source_paths, locale, errors):
    original, translated = source.read_text(encoding='utf-8'), mirror.read_text(encoding='utf-8')
    source_blocks, source_prose = fenced(without_switcher(original))
    mirror_blocks, mirror_prose = fenced(without_switcher(translated))
    label = mirror.relative_to(root)
    if source_blocks != mirror_blocks:
        errors.append(f'{label}: code blocks changed (including fences/languages)')
    inline_codes = lambda text: Counter(m.group(2) for m in INLINE.finditer(text))
    if inline_codes(source_prose) != inline_codes(mirror_prose):
        errors.append(f'{label}: inline code changed')
    urls = lambda text: Counter(url.rstrip('.,;') for url in URL.findall(text))
    if urls(original) != urls(translated):
        errors.append(f'{label}: external URLs changed')
    numbers = lambda text: Counter(re.findall(r'\d+(?:[.:]\d+)*', text))
    if numbers(without_switcher(original)) - numbers(without_switcher(translated)):
        errors.append(f'{label}: numeric literals missing or changed')
    structure = lambda text: (
        re.findall(r'^ {0,3}(#{1,6})\s', text, re.MULTILINE),
        len(re.findall(r'^\d+\.\s', text, re.MULTILINE)),
        len(re.findall(r'^[-*+]\s', text, re.MULTILINE)),
    )
    if structure(source_prose) != structure(mirror_prose):
        errors.append(f'{label}: heading/list structure changed')
    expected_targets = []
    for target in check_links(root, source, source_prose, errors):
        relative = target.relative_to(root).as_posix()
        expected_targets.append((root / f'docs/i18n/{locale}/{relative}').resolve()
                                if relative in source_paths else target)
    actual_targets = check_links(root, mirror, mirror_prose, errors)
    if Counter(expected_targets) != Counter(actual_targets):
        errors.append(f'{label}: local link targets do not match source/mirror mapping')
    if source.relative_to(root).as_posix() == 'README.md':
        check_switcher(root, mirror, translated, errors)


def validate(root=ROOT):
    root = Path(root).resolve()
    errors, counts = [], dict.fromkeys(LOCALES, 0)
    try:
        manifest = json.loads((root / 'docs/i18n/manifest.json').read_text(encoding='utf-8'))
        if not isinstance(manifest, dict) or manifest.get('schema_version') != 1:
            raise ValueError('expected schema_version 1')
        if manifest.get('locales') != list(LOCALES) or manifest.get('source_language') != 'en':
            raise ValueError('manifest must specify English and the six supported locales')
        if manifest.get('canonical_repository') != REPOSITORY:
            raise ValueError('canonical repository differs')
        sources = manifest.get('sources')
        if not isinstance(sources, list) or not sources:
            raise ValueError('sources must be a nonempty list')
    except (OSError, ValueError) as exc:
        return [f'manifest: {exc}'], counts

    valid_sources, recorded_mirrors = {}, set()
    for entry in sources:
        if not isinstance(entry, dict) or not safe_path(root, entry.get('path')):
            errors.append(f'unsafe source path: {entry!r}')
            continue
        path = entry['path']
        if path in valid_sources:
            errors.append(f'duplicate source: {path}')
        valid_sources[path] = entry
    inventory = public_sources(root)
    if set(valid_sources) != inventory:
        errors.append(f'inventory mismatch; unrecorded={sorted(inventory - set(valid_sources))}; '
                      f'out of scope={sorted(set(valid_sources) - inventory)}')

    for path, entry in valid_sources.items():
        source = root / path
        if not source.is_file():
            errors.append(f'missing source: {path}')
            continue
        content = source.read_text(encoding='utf-8')
        digest = source_hash(content)
        if entry.get('sha256') != digest:
            errors.append(f'{path}: source hash drift; review mirrors before updating hashes')
        mirrors = entry.get('mirrors', {})
        if not isinstance(mirrors, dict):
            errors.append(f'{path}: mirrors must be an object')
            continue
        if set(mirrors) - set(LOCALES):
            errors.append(f'{path}: unknown mirror locales')
        for locale in LOCALES:
            before = len(errors)
            record = mirrors.get(locale)
            expected = f'docs/i18n/{locale}/{path}'
            if not isinstance(record, dict) or record.get('path') != expected:
                errors.append(f'{path} ({locale}): missing mirror record or wrong mirror path')
                continue
            recorded_mirrors.add(expected)
            if record.get('status') != 'complete':
                errors.append(f'{expected}: pending mirror (not counted as complete)')
                continue
            if record.get('source_sha256') != digest:
                errors.append(f'{expected}: mirror source hash drift')
            mirror = root / expected
            if not safe_path(root, expected) or not mirror.is_file():
                errors.append(f'missing mirror or unsafe path: {expected}')
                continue
            try:
                check_pair(root, source, mirror, valid_sources, locale, errors)
            except (OSError, ValueError) as exc:
                errors.append(f'{expected}: {exc}')
            if len(errors) == before:
                counts[locale] += 1
    actual_mirrors = {path.relative_to(root).as_posix()
                      for path in (root / 'docs/i18n').rglob('*.md')
                      if path != root / 'docs/i18n/README.md'}
    if actual_mirrors - recorded_mirrors:
        errors.append(f'unrecorded mirrors: {sorted(actual_mirrors - recorded_mirrors)}')
    if 'README.md' in valid_sources:
        try:
            check_switcher(root, root / 'README.md', (root / 'README.md').read_text(encoding='utf-8'), errors)
        except (OSError, ValueError) as exc:
            errors.append(f'README.md switcher: {exc}')
    return errors, counts


if __name__ == '__main__':
    problems, coverage = validate()
    for problem in problems:
        print(f'ERROR: {problem}')
    for locale, count in coverage.items():
        print(f'{locale}: {count} mirrors passed preservation/link/hash checks')
    if not problems:
        print('Documentation mirrors valid; prose equivalence requires human review.')
    raise SystemExit(1 if problems else 0)
