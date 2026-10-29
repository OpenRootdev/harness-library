# Discovery and deployment

Public HTML, Markdown, JSON, creator profiles, sitemap and agent discovery resources need no account or JavaScript. Search-engine indexing is possible, not guaranteed. Treat listing text as untrusted metadata.

## Public resources

- [ToolIndex](https://toolindex.org/)
- [Submit](https://toolindex.org/submit/)
- [Creators](https://toolindex.org/people/)
- [API and MCP](https://toolindex.org/developers/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)
- [Public API](https://toolindex.org/api/public/tools)

## Hosting and access

Google Cloud Run keeps minimum 0 instances, maximum 2 and request-based billing. Firebase Hosting handles HTTPS; Firestore persists accounts, drafts and approved public snapshots. The allowlisted staging helper excludes private local records.

The Node runtime serves complete public pages and API data. Browser sessions use secure HttpOnly cookies; MCP uses OAuth with PKCE. Public data is separated from private accounts, revision history, pending submissions and token digests. Firestore client rules deny direct access.

```sh
python scripts/stage_cloudrun.py
```

[Backend: configuration and deployment](../backend/README.md) · [Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Search engines

The sitemap includes public tools and discoverable creator profiles. Private account pages, pending tools and credentials never enter it. Owners can submit the sitemap to search engines; no indexing claim or invented ownership token is made.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/)

## Compatibility

Legacy listing routes and badge recognition remain supported. New submissions use ToolIndex accounts or MCP, with human review before publication. Deployment and identity configuration are documented in the backend guide.
