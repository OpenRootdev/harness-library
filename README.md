<p align="center"><img src="site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="README.md">English</a> · <a href="docs/i18n/es/README.md">Español</a> · <a href="docs/i18n/zh-CN/README.md">简体中文</a> · <a href="docs/i18n/fr/README.md">Français</a> · <a href="docs/i18n/ja/README.md">日本語</a> · <a href="docs/i18n/de/README.md">Deutsch</a> · <a href="docs/i18n/pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Tools for AI agents. Clear setup. Direct source links.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml">Submit a tool</a></p>

ToolIndex is an open directory of skills, MCP servers, CLIs, APIs, libraries, plugins, workflows and harnesses that AI agents can use. Local packages, hosted services and commercial tools are welcome when access, pricing and terms are clear.

## What belongs here

Useful tools for a specific task, from a small skill folder to a service API. Each listing links directly to its source repository or official documentation and explains installation or connection, manual setup, license or terms, version and review scope.

## Submit a tool

1. Open the GitHub form with the tool name, type, source and purpose.
2. Describe the package or service, installation or access steps, version, license or terms, credentials required and any costs. Never submit secrets.
3. A logo or custom image is optional. Supply its URL, source and alt text if available; otherwise the listing uses neutral initials.
4. Maintainers review the submission and publish approved entries. No fork, pull request or ToolIndex account is required; the form needs a GitHub account.

[CONTRIBUTING.md](CONTRIBUTING.md) · [JSON](docs/listing.example.json)

## Reviewed examples

A skill for brand animation and a Blender MCP connector show two supported tool types. Their source and releases remain in their own repositories.

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

## Build and preview

Python 3.11+ builds the static site. The frontend is plain HTML, CSS and JavaScript; search progressively enhances pages that remain readable without JavaScript.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -m http.server 4201 --directory dist
```

`http://localhost:4201/`

## Google Cloud hosting

Cloud Run serves the site with minimum 0 instances, maximum 2 and request-based billing. Firebase Hosting handles custom-domain HTTPS and forwards requests to Cloud Run. The public-only staging helper excludes private workspace files. Domain activation depends on DNS and certificate verification.

`python scripts/stage_cloudrun.py` · [`firebase.json`](firebase.json) · [docs/discovery.md](docs/discovery.md)

## Reviews and community badges

Setup reviews and artifact checks describe specific evidence, not universal model or platform compatibility. Listings can optionally use the badge for one transparent 14-day community boost. Harneloop attribution is optional; no framework is required.

[docs/badge-program.md](docs/badge-program.md)
