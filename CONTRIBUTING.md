# Submission checklist

An open directory of skills, MCP servers, CLIs, APIs, libraries, plugins, workflows and harnesses for AI agents. Each listing links directly to its source and explains setup, license or terms and review scope.

## Accounts and submissions

Create an account, verify your email and choose a creator handle. Customize your name, bio, website and optional avatar. You decide whether your profile is public and available for indexing.

Save a private tool draft in the UI, then request review. Images are optional. Follow status and feedback in your account. Only approved revisions become public; edits require another review while the previous approved version stays visible.

Connect an agent to the MCP endpoint. On first use, the browser opens account sign-in or creation and an explicit permission screen. The agent can manage your profile, drafts and review requests. It cannot approve or publish a submission.

[UI](https://toolindex.org/account/) · [MCP](https://toolindex.org/developers/) · [Guide](https://toolindex.org/submit/)

## Submission checklist

Describe a useful task, source or official docs, tool type, category, version, license or service terms, installation or connection steps, authentication requirements and costs. Never include secrets.

[JSON example](docs/listing.example.json)

## Review and ownership

Only the owner can edit or withdraw a submission. Only an explicitly configured verified reviewer can publish it. Public review evidence is scoped and does not guarantee every model or platform. Rejection feedback and pending content stay private.

## Source contributions

The UI and MCP do not require an issue or pull request. Source contributions remain welcome. Existing seed listings, review receipts and badge grants remain in source control; do not change maintainer review or boost records in a submission.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/validate_i18n.py
npm ci --prefix backend
npm test --prefix backend
```

[README.md](README.md) · [Backend](backend/README.md) · [Badge program](docs/badge-program.md)
