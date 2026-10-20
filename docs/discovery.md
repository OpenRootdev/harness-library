# Discovery and indexing

Current home since `2026-10-20`: [OpenRootdev/harness-library](https://github.com/OpenRootdev/harness-library) and the [directory](https://openrootdev.github.io/harness-library/). Earlier migration notes below describe the previous move.

The public directory publishes complete HTML at stable URLs. Search engines, browsers with JavaScript disabled and agents can read every approved harness's installation, prerequisites, source, distribution and review scope directly. JavaScript only enhances filtering, copying and legacy hash navigation.

## Public resources

- [Directory](https://openrootdev.github.io/harness-library/) and [submission guide](https://openrootdev.github.io/harness-library/submit/).
- [Sitemap](https://openrootdev.github.io/harness-library/sitemap.xml): canonical HTML pages only. Daily badge checks do not manufacture content modification dates.
- [llms.txt](https://openrootdev.github.io/harness-library/llms.txt): a compact guide linking to Markdown installation pages and data.
- [llms-full.txt](https://openrootdev.github.io/harness-library/llms-full.txt): combined public text.
- [catalog.json](https://openrootdev.github.io/harness-library/catalog.json): reviewed listings, canonical page URLs, installation, manual setup and scoped evidence.
- Each canonical HTML page has a corresponding `index.md`, linked with `rel="alternate" type="text/markdown"`.

Every HTML page has a unique title, description and canonical URL, social preview metadata and matching JSON-LD. Structured data describes the real directory, maintainer and harnesses; it does not invent ratings, downloads or universal compatibility. Unknown paths return GitHub Pages' 404 status using the noindex error page. Old listing hash links remain supported.

## Owner setup

1. Add a **URL-prefix property** for `https://openrootdev.github.io/harness-library/` in [Google Search Console](https://search.google.com/search-console). This limits the property to the project. Use the verification method provided for your account; an HTML verification file can be placed in `site/` once its exact filename and contents are supplied.
2. Submit `sitemap.xml` in that property. Inspect the home, submission guide and harness URLs; request indexing where the tool offers it. A submission is a discovery hint, not an indexing promise.
3. Add the same site to [Bing Webmaster Tools](https://www.bing.com/webmasters/) and submit the sitemap. If the account offers import from Google Search Console, that can reuse the verified property.
4. Revisit indexing reports after deployment. Fix reported crawl or content issues based on evidence. Do not treat a `site:` search or a Lighthouse score as proof of index coverage or rankings.

Verification requires the owner's account or its provided verification artifact. Do not publish guessed verification tokens. If an HTML verification file is added, keep it out of the sitemap and preserve it in builds.

## Published-change notifications

After a normal push deploys, the Pages workflow notifies [IndexNow](https://www.indexnow.org/documentation) with the canonical URLs from the built sitemap. Daily badge refreshes skip this notification. This migration changes all five pages; for a larger directory, narrow submissions to changed pages. Google uses Search Console and ordinary crawling; it is not being submitted through IndexNow.

The project hosts `indexnow-key.txt` and supplies its exact `keyLocation`. This scopes ownership to `/harness-library/`, avoiding unrelated projects on the shared host. The key must be publicly served for protocol verification; it is not a webmaster account credential. No login, paid service or additional dependency is needed. A temporary API failure does not roll back a successful site deployment.

For a deliberate content update outside the workflow, build first, then run `python scripts/notify_indexnow.py --dry-run` to inspect the URL list, or `python scripts/notify_indexnow.py` to submit it. HTTP 200 means received; HTTP 202 means received with key validation pending. Neither proves indexing or rankings. Avoid repeated submissions when content has not changed.

## GitHub Pages and robots.txt

Robots rules are read from the **host root**, `https://openrootdev.github.io/robots.txt`, not from `/harness-library/robots.txt`. A project-local file cannot control crawling for the shared host. The project file only provides the current sitemap reference. Submit the sitemap through webmaster accounts.

If the owner later adds a root-site repository or a custom domain, check the authoritative robots file before deploying restrictions. Never change rules for other projects on the same host casually.

## Organization migration

The repository and directory moved to [Kaelux Labs](https://github.com/OpenRootdev/harness-library) on October 10, 2026. GitHub redirects the old repository URL. A small [account Pages repository](https://github.com/Ker102/ker102.github.io) preserves the old directory pages with instant redirects and canonical links, and continues serving existing badge images. Its host-root `robots.txt` allows crawling and links to the current sitemap.

Existing badge backlinks using either the old or current directory URL remain eligible. Changing those links does not restart an existing 14-day boost; the original receipt dates remain authoritative.

## Agent discovery

Agents can use ordinary HTML, the JSON catalog or Markdown mirrors. `llms.txt` is a convenience proposal, not a Google ranking factor or requirement. Google says its AI search features use the same foundational SEO practices as ordinary Search. Crawlable text, clear page links, accurate evidence and useful content matter; no configuration guarantees inclusion or citations.

Primary references: [Google JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [robots specification](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec), [AI features](https://developers.google.com/search/docs/appearance/ai-features), [llms.txt proposal](https://llmstxt.org/).
