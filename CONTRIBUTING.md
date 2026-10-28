# Submit a tool

ToolIndex includes any tool AI agents can use: skills, MCP servers, CLIs, APIs, libraries, plugins, workflows and harnesses. Hosted and commercial tools are welcome when access, pricing, authentication and terms are clear. Every listing links directly to its source repository or official documentation.

A logo or custom image is optional. Supply its source and alt text if available; otherwise the listing uses neutral initials. Choose a tool type and explain installation or service access. Non-GitHub sources are accepted; automatic README badge checks currently support GitHub only.

**New submissions are welcome.** We’re looking for practical, reusable agent setups, including small skill folders. Harneloop is optional.

The simplest route needs no fork or pull request:

1. [Open the GitHub submission form](https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml). Share the repository, name and task/category.
2. Explain installation, focused distribution, version/license and any manual connections. Extra composition and test evidence are optional.
3. Maintainers review your issue, ask for missing details there if needed, and publish approved entries. Later changes can be submitted in another issue or PR.

You only need a GitHub account to use the form. The [website guide](https://toolindex.org/submit/) explains the same process.

For a PR, copy `docs/listing.example.json` to `data/listings/your-slug.json`. Use the same lowercase slug in the filename and `id`. Run `python scripts/catalog.py validate` and the tests described in the README.

Required information:

- Name, short summary, category, source repository, license and version or pinned revision.
- Focused distribution URL, what it contains and whether the source repo also contains irrelevant material. Use a downloadable package or a dedicated tool branch for mixed repos; do not require users to clone a large unrelated project.
- Clear, ordered installation instructions. State working directory, prerequisites, agent/client integration and how to begin. Link client-specific guidance where discovery differs.
- Manual connections/configuration, required MCPs or tools, credentials if any, and additional notes. Use empty lists when none are required. Never submit secrets.

Optional: skill/reference/file counts, top-level MCP tool count, execution tools, detailed composition and a “Built with Harneloop” attribution with evidence. Distinguish optional tools from required ones and top-level dispatch tools from downstream operations.

Allowed categories: Creative, 3D & Blender, Coding, Research, Data, Operations, Other. Suggest a new category in the issue if none fits.

Do not add review or boost fields to your listing, or modify maintainer receipts. Maintainers own `data/reviews.json` and `data/boosts.json`. Source attribution and test claims need evidence; a released package alone is not proof that it runs correctly. Maintainers inspect instructions, source scope, licenses, URLs and claimed artifacts; submission scripts are never automatically executed.

Please keep changes focused. Updates to source packages or installation steps should include the version and what changed. Reports about broken installs can use a normal issue.
