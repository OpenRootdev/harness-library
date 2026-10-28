import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import validate_i18n as i18n


class TranslationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.source = (
            '# Guide\n\n[Reference](docs/reference.md#reference)\n\n'
            '![Mark](assets/mark.svg)\n\n'
            'Use `tool.run()` with version 3.11, at most 48 hours.\n\n'
            '```sh\npython example.py --safe\n```\n'
        )
        self.write('GUIDE.md', self.source)
        self.write('docs/reference.md', '# Reference\n\nNever run submissions.\n')
        self.write('assets/mark.svg', '<svg></svg>\n')
        sources = []
        for path in ['GUIDE.md', 'docs/reference.md']:
            content = (self.root / path).read_text(encoding='utf-8')
            digest = hashlib.sha256(content.encode('utf-8')).hexdigest()
            mirrors = {}
            for locale in i18n.LOCALES:
                mirror = f'docs/i18n/{locale}/{path}'
                translated = content.replace('(assets/mark.svg)', '(../../../assets/mark.svg)')
                self.write(mirror, translated)
                mirrors[locale] = {'path': mirror, 'status': 'complete', 'source_sha256': digest}
            sources.append({'path': path, 'sha256': digest, 'mirrors': mirrors})
        self.manifest = {
            'schema_version': 1, 'source_language': 'en',
            'canonical_repository': i18n.REPOSITORY, 'locales': list(i18n.LOCALES),
            'sources': sources,
        }
        self.save_manifest()

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')

    def save_manifest(self):
        self.write('docs/i18n/manifest.json', json.dumps(self.manifest))

    def errors(self):
        return '\n'.join(i18n.validate(self.root)[0])

    def mutate(self, old, new):
        path = self.root / 'docs/i18n/es/GUIDE.md'
        path.write_text(path.read_text(encoding='utf-8').replace(old, new), encoding='utf-8')

    def test_complete_fixture(self):
        errors, counts = i18n.validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts, dict.fromkeys(i18n.LOCALES, 2))

    def add_readmes(self):
        targets = ['README.md'] + [f'docs/i18n/{locale}/README.md' for locale in i18n.LOCALES]
        switcher = lambda urls: '<p>' + ' | '.join(
            f'<a href="{url}">{label}</a>' for url, label in zip(urls, i18n.LABELS)
        ) + '</p>\n'
        content = '# ToolIndex\n\n' + switcher(targets)
        self.write('README.md', content)
        digest = i18n.source_hash(content)
        mirrors = {}
        for locale in i18n.LOCALES:
            path = f'docs/i18n/{locale}/README.md'
            urls = ['../../../README.md'] + [
                'README.md' if other == locale else f'../{other}/README.md'
                for other in i18n.LOCALES
            ]
            self.write(path, '# ToolIndex\n\n' + switcher(urls))
            mirrors[locale] = {'path': path, 'status': 'complete', 'source_sha256': digest}
        self.manifest['sources'].append({'path': 'README.md', 'sha256': digest, 'mirrors': mirrors})
        self.save_manifest()

    def test_switcher_paths_do_not_count_as_numeric_prose(self):
        self.add_readmes()
        self.assertEqual(self.errors(), '')

    def test_switcher_broken_or_nonrelative_link_fails(self):
        self.add_readmes()
        path = 'docs/i18n/es/README.md'
        content = (self.root / path).read_text(encoding='utf-8')
        self.write(path, content.replace('../fr/README.md', '../../fr/README.md'))
        self.assertIn('missing switcher target', self.errors())
        self.write(path, content.replace('../../../README.md', 'https://example.org/README.md'))
        self.assertIn('switcher must use relative links', self.errors())

    def test_switcher_is_required_and_labels_are_native(self):
        self.add_readmes()
        self.write('docs/i18n/es/README.md', '# ToolIndex\n')
        self.assertIn('native-language switcher', self.errors())

    def test_invalid_json_and_missing_locale_fail(self):
        self.write('docs/i18n/manifest.json', '{')
        self.assertIn('manifest:', self.errors())
        del self.manifest['sources'][0]['mirrors']['fr']
        self.save_manifest()
        self.assertIn('missing mirror record', self.errors())

    def test_fence_language_and_nonlocalized_doc_link_fail(self):
        self.mutate('```sh', '```shell')
        self.assertIn('code blocks', self.errors())
        self.mutate('(docs/reference.md#reference)', '(../../../docs/reference.md#reference)')
        self.assertIn('local link targets', self.errors())

    def test_repository_translations(self):
        self.assertEqual(i18n.validate(Path(__file__).resolve().parents[1])[0], [])

    def test_code_change_and_unclosed_fence_fail(self):
        self.mutate('--safe', '--unsafe')
        self.assertIn('code blocks', self.errors())
        self.mutate('\n```\n', '\n')
        self.assertIn('unclosed fence', self.errors())

    def test_inline_api_and_number_changes_fail(self):
        self.mutate('tool.run()', 'tool.exec()')
        self.mutate('48 hours', '49 hours')
        self.assertIn('inline code', self.errors())
        self.assertIn('numeric literals', self.errors())

    def test_url_changes_fail(self):
        self.write('docs/reference.md', '# Reference\n\n[Site](https://example.org/docs/)\n')
        self.assertIn('external URLs', self.errors())

    def test_missing_asset_and_wrong_local_target_fail(self):
        self.mutate('../../../assets/mark.svg', '../../../assets/absent.svg')
        self.assertIn('missing target', self.errors())
        self.assertIn('local link targets', self.errors())

    def test_anchor_change_fails(self):
        self.mutate('#reference)', '#absent)')
        self.assertIn('anchor', self.errors())

    def test_translated_anchor_is_allowed(self):
        self.mutate('#reference)', '#referencia)')
        self.write('docs/i18n/es/docs/reference.md', '# Referencia\n\nNunca ejecute envios.\n')
        self.assertEqual(self.errors(), '')

    def test_source_drift_and_mirror_hash_drift_fail(self):
        self.write('GUIDE.md', self.source + '\nChanged source.\n')
        self.assertIn('source hash drift', self.errors())
        self.manifest['sources'][0]['mirrors']['es']['source_sha256'] = '0' * 64
        self.save_manifest()
        self.assertIn('mirror source hash', self.errors())

    def test_unrecorded_and_missing_mirrors_fail(self):
        self.write('docs/i18n/es/extra.md', '# Unrecorded\n')
        (self.root / 'docs/i18n/fr/GUIDE.md').unlink()
        self.assertIn('unrecorded mirrors', self.errors())
        self.assertIn('missing mirror', self.errors())

    def test_new_source_requires_inventory_update(self):
        self.write('SECURITY.md', '# Security\n')
        self.assertIn('inventory', self.errors())

    def test_excluded_internal_and_generated_docs(self):
        for path in ['AGENTS.md', 'task.md', 'docs/plans/plan.md', 'docs/runs/run.md',
                     'docs/internal/evidence.md', 'dist/index.md', 'vendor/README.md']:
            self.write(path, '# Not a translation source\n')
        self.assertEqual(self.errors(), '')

    def test_manifest_path_escape_and_duplicates_fail(self):
        self.manifest['sources'][0]['path'] = '../outside.md'
        self.manifest['sources'].append(self.manifest['sources'][1])
        self.save_manifest()
        self.assertIn('unsafe source path', self.errors())
        self.assertIn('duplicate source', self.errors())

    def test_pending_is_not_counted_as_complete(self):
        self.manifest['sources'][0]['mirrors']['es']['status'] = 'pending'
        (self.root / 'docs/i18n/es/GUIDE.md').unlink()
        self.save_manifest()
        errors, counts = i18n.validate(self.root)
        self.assertIn('pending mirror', '\n'.join(errors))
        self.assertEqual(counts['es'], 1)

    def test_reference_and_html_links(self):
        markdown = '[Doc][ref]\n\n[ref]: docs/reference.md#reference\n<img src="assets/mark.svg">\n'
        self.assertEqual(i18n.links(markdown), ['docs/reference.md#reference', 'assets/mark.svg'])

    def test_tilde_fences_and_crlf_hashes(self):
        blocks, prose = i18n.fenced('~~~python\nx = 1\n~~~\nVisible\n')
        self.assertEqual(blocks, ['~~~python\nx = 1\n~~~\n'])
        self.assertEqual(prose, 'Visible\n')
        self.assertEqual(i18n.source_hash('a\r\nb\r\n'), i18n.source_hash('a\nb\n'))


if __name__ == '__main__':
    unittest.main()
