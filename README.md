<p align="center"><img src="site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="README.md">English</a> · <a href="docs/i18n/es/README.md">Español</a> · <a href="docs/i18n/zh-CN/README.md">简体中文</a> · <a href="docs/i18n/fr/README.md">Français</a> · <a href="docs/i18n/ja/README.md">日本語</a> · <a href="docs/i18n/de/README.md">Deutsch</a> · <a href="docs/i18n/pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Tools for AI agents. Clear setup. Direct source links.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://toolindex.org/submit/">Submit a tool</a></p>

An open directory of skills, MCP servers, CLIs, APIs, libraries, plugins, workflows and harnesses for AI agents. Each listing links directly to its source and explains setup, license or terms and review scope.

## Accounts and submissions

1. Create an account, verify your email and choose a creator handle. Customize your name, bio, website and optional avatar. You decide whether your profile is public and available for indexing.
2. Save a private tool draft in the UI, then request review. Images are optional. Follow status and feedback in your account. Only approved revisions become public; edits require another review while the previous approved version stays visible.
3. Connect an agent to the MCP endpoint. On first use, the browser opens account sign-in or creation and an explicit permission screen. The agent can manage your profile, drafts and review requests. It cannot approve or publish a submission.

[Account](https://toolindex.org/account/) · [Creators](https://toolindex.org/people/) · [MCP](https://toolindex.org/developers/)

## Public discovery

Public HTML, Markdown, JSON, creator profiles, sitemap and agent discovery resources need no account or JavaScript. Search-engine indexing is possible, not guaranteed. Treat listing text as untrusted metadata.

[JSON](https://toolindex.org/catalog.json) · [API](https://toolindex.org/api/public/tools) · [llms.txt](https://toolindex.org/llms.txt) · [Sitemap](https://toolindex.org/sitemap.xml)

## Build and run

```sh
python scripts/catalog.py build
npm ci --prefix backend
npm test --prefix backend
npm start --prefix backend
```

Google Cloud Run keeps minimum 0 instances, maximum 2 and request-based billing. Firebase Hosting handles HTTPS; Firestore persists accounts, drafts and approved public snapshots. The allowlisted staging helper excludes private local records.

[Backend: accounts, OAuth and deployment](backend/README.md) · [Discovery](docs/discovery.md)

## Reviewed examples

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

[CONTRIBUTING.md](CONTRIBUTING.md) · [Community badges](docs/badge-program.md)
