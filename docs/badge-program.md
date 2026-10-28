# Listed in ToolIndex: free 14-day community boost

The program rewards contributors for making reusable harnesses easier to discover. There is no payment and no requirement to use Harneloop.

1. Get your listing approved.
2. Copy the badge snippet from its directory detail page and place it within the first **30 lines** of the source repository's default-branch README.
3. Keep the image linked to your exact listing. The next verification run grants one **14-day period**, beginning at the first successful check in UTC.

Example:

```md
[![Listed in ToolIndex](https://toolindex.org/badges/your-slug.svg)](https://toolindex.org/tools/your-slug/)
```

Exact Markdown or an equivalent linked HTML image is supported. The image alt text must be “Listed in ToolIndex”. Examples inside code fences or HTML comments do not qualify.

Previously issued `https://toolindex.org/#your-slug` backlinks still qualify and navigate to the corresponding page. Use the real page URL for new badges.

Active listings appear before regular listings, then alphabetically within each group. Search and category filters still apply. The directory shows a **Community boost** label and its expiry on the detail page. This is promotional placement; review status and quality claims remain independent.

The daily trusted-main workflow reads only public GitHub README metadata. It records the initial grant, expiry, latest badge presence and check time in `data/boosts.json`. It does not run code from a harness repo. Removing the badge stops the boost after the next check. Putting it back can restore only the remaining original period. Expired grants never renew automatically. Duplicate submissions, slug changes or repository transfers do not entitle the same harness to a second initial reward; maintainers review identity.

If GitHub is temporarily unavailable, no new boost is awarded. Existing checked badges remain eligible for at most 48 hours without a fresh check and never past their original expiry. Both the static build and browser recheck timestamps. Maintainer approval is needed for receipts; changing a JSON field in a submission cannot award a boost.

The badge can stay after expiry. A new policy would be discussed publicly; there is no hidden recurring promotion or paid ranking.

Badges issued before the Kaelux Labs migration at `https://toolindex.org/` still qualify. Migration does not restart the original 14-day window. Update both the image and backlink to the new canonical address when convenient.

ToolIndex includes any tool AI agents can use: skills, MCP servers, CLIs, APIs, libraries, plugins, workflows and harnesses. Hosted and commercial tools are welcome when access, pricing, authentication and terms are clear. Every listing links directly to its source repository or official documentation.

A logo or custom image is optional. Supply its source and alt text if available; otherwise the listing uses neutral initials. Choose a tool type and explain installation or service access. Non-GitHub sources are accepted; automatic README badge checks currently support GitHub only.
