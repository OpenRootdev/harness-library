# Documentation Translations

English documentation is authoritative. Translations are full equivalents of the
maintained sources below, not summaries. The canonical repository is
[Kaelux-Labs/harness-library](https://github.com/OpenRootdev/harness-library).
Translated paths follow `docs/i18n/<locale>/<repo-relative-source-path>`.

## Inventory and Coverage

The explicit source inventory, SHA-256 hashes, supported locales and individually
completed mirror paths are recorded in [manifest.json](manifest.json).

| English source | Scope |
| --- | --- |
| [README.md](../../README.md) | Overview, submission, badge program and development |
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | Submission requirements, review ownership and safety |
| [docs/badge-program.md](../badge-program.md) | Badge verification, promotion limits and migration |
| [docs/discovery.md](../discovery.md) | Public resources, webmaster setup, indexing and migration |

| Locale | Documentation | Complete mirrors |
| --- | --- | --- |
| `es` | [Español](es/README.md) | 4 / 4 |
| `zh-CN` | [简体中文](zh-CN/README.md) | 4 / 4 |
| `fr` | [Français](fr/README.md) | 4 / 4 |
| `ja` | [日本語](ja/README.md) | 4 / 4 |
| `de` | [Deutsch](de/README.md) | 4 / 4 |
| `pt-BR` | [Português (Brasil)](pt-BR/README.md) | 4 / 4 |

This checkout has no separate security, quickstart, review or reference Markdown
guide. Existing submission, review and safety guidance is included in full.
No maintained source files in this inventory are pending. This administrative
index is not itself a recursively translated source.

## Exclusions and Historical Material

Agent instructions (`AGENTS.md`, `CLAUDE.md`), task/progress/memory files, internal
plans, private local evidence, generated run records, vendor documentation and
website UI are outside scope. JSON listings, review/boost receipts and
`docs/listing.example.json` remain shared data, not translated documents. Assets
remain shared originals. Generated `dist/` Markdown pages are build output, not
maintained documentation sources, and are not mirrored here.

No authored historical Markdown documents were found in the public source scope
at inventory time; `untranslated_historical_materials` is therefore empty. If
archived material is introduced under `docs/historical/`, `docs/archive/` or
`docs/archives/`, list its paths and reasons there instead of claiming coverage.
Historical statements within maintained documents remain translated. In
particular, old Ker102 URLs in the English contributor guide and migration history
are preserved verbatim, not silently replaced with current organization URLs.

## Maintenance and Stale Detection

1. Change English first. Keep every section, prerequisite, optional/required
   distinction, safety limitation and policy condition in each translated mirror.
2. Preserve fenced code exactly, including commands, URLs, language labels and
   fences. Preserve inline code, API identifiers, category values, version numbers
   and external URLs. Do not localize literal badge alt text or eligibility labels.
3. Resolve local documentation links to the same-locale mirror. Resolve shared
   assets, JSON templates and other unmirrored files back to the repository
   originals with correct relative paths. Update fragments to match translated
   headings, or retain explicit stable IDs. The README switcher must link to
   English and all six native-language READMEs using relative paths.
4. After reviewing equivalence, update the source entry's `sha256` and only the
   reviewed mirror's `source_sha256`. These are SHA-256 hashes of UTF-8 English
   text with CRLF normalized to LF; no other whitespace is normalized. Hashes
   include the English language switcher. Do not stamp all mirrors with a new
   hash before their review is complete.
5. Use `status: "pending"` for an unfinished mirror, keep its intended path in the
   manifest, and leave its old reviewed source hash. A pending or absent mirror
   never counts as complete and deliberately makes validation fail. Update this
   coverage table when coverage changes.
6. Add newly maintained public Markdown sources to the manifest and all six
   locale inventories. For historical or otherwise excluded material, record
   explicit exclusions instead. Run the checks below before publication.

Run from the repository root:

```sh
python scripts/validate_i18n.py
python -m unittest discover -s tests -v
```

The validator is a local Python standard-library script; it does not fetch URLs,
execute submitted code, regenerate translations or update hashes. It checks the
public Markdown inventory, recorded completion, mirror existence, English source
hash drift, per-mirror reviewed source hashes, fence/code preservation, inline
technical literals, external URL preservation, numeric literal presence,
heading/list structure, relative switchers and local doc/asset links and anchors.
The existing unittest discovery command includes its focused regression tests.
Website rendering and publishing behavior are unchanged.

Link checks cover the inline/reference Markdown and HTML `href`/`src` forms used
in this repository. Markdown heading fragments and explicit HTML IDs are checked
locally; this is not a complete CommonMark parser or a remote URL availability
check. Numeric checks retain source numerals but allow additional numerals when
translating spelled-out numbers. Automatic preservation checks cannot establish
natural-language equivalence or verify factual claims in the English source.
Review negations, limits, dates and safety statements separately; native-speaker
review remains welcome. The initial full translations were checked against the
English sections and policy conditions but are not independently certified.
