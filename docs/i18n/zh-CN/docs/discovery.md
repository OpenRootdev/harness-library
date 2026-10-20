# 发现与索引

自 `2026-10-20` 起，当前地址为 [OpenRootdev/harness-library](https://github.com/OpenRootdev/harness-library) 和[目录网站](https://openrootdev.github.io/harness-library/)。下方历史迁移说明描述的是之前的一次迁移。

公开目录在稳定 URLs 上发布完整 HTML。搜索引擎、禁用 JavaScript 的浏览器和智能体都可以直接读取每个获批 harness 的安装方法、前置条件、来源、分发内容及审核范围。JavaScript 仅增强筛选、复制和旧式 URL 片段导航。

## 公开资源

- [目录](https://openrootdev.github.io/harness-library/)及[提交指南](https://openrootdev.github.io/harness-library/submit/)。
- [Sitemap](https://openrootdev.github.io/harness-library/sitemap.xml)：仅包含规范 HTML 页面。每日徽章检查不会虚构内容修改日期。
- [llms.txt](https://openrootdev.github.io/harness-library/llms.txt)：链接到 Markdown 安装页面和数据的简明指南。
- [llms-full.txt](https://openrootdev.github.io/harness-library/llms-full.txt)：合并后的公开文本。
- [catalog.json](https://openrootdev.github.io/harness-library/catalog.json)：经过审核的条目、规范页面 URLs、安装方法、手动设置及范围明确的证据。
- 每个规范 HTML 页面都有对应的 `index.md`，通过 `rel="alternate" type="text/markdown"` 链接。

每个 HTML 页面都有唯一的标题、描述和规范 URL，以及社交预览元数据和相匹配的 JSON-LD。结构化数据描述真实的目录、维护者和 harness；不会虚构评分、下载量或通用兼容性。未知路径使用 noindex 错误页返回 GitHub Pages 的 404 状态。旧条目的片段链接仍然受支持。

## 所有者设置

1. 在 [Google Search Console](https://search.google.com/search-console) 中为 `https://openrootdev.github.io/harness-library/` 添加一个 **URL 前缀属性**。这样可将属性限制在本项目范围内。使用账号提供的验证方法；在获得准确文件名和内容后，可将 HTML 验证文件放入 `site/`。
2. 在该属性中提交 `sitemap.xml`。检查首页、提交指南及 harness 的 URLs；在工具提供此功能时请求索引。提交是发现提示，不是索引保证。
3. 将同一网站添加到 [Bing Webmaster Tools](https://www.bing.com/webmasters/) 并提交 sitemap。如果账号支持从 Google Search Console 导入，可复用已验证的属性。
4. 部署后再次查看索引报告。根据证据修复报告中的抓取或内容问题。不要将 `site:` 搜索或 Lighthouse 分数当作索引覆盖率或排名的证明。

验证需要所有者账号或账号提供的验证产物。不要发布猜测的验证令牌。如果添加 HTML 验证文件，请将其排除在 sitemap 之外，并在构建中保留它。

## 已发布变更的通知

普通 push 部署完成后，Pages 工作流会使用构建出的 sitemap 中的规范 URLs 通知 [IndexNow](https://www.indexnow.org/documentation)。每日徽章刷新会跳过此通知。本次迁移改变了全部五个页面；对于更大的目录，应仅提交变更页面。Google 使用 Search Console 和常规抓取；不会通过 IndexNow 向 Google 提交。

项目托管 `indexnow-key.txt` 并提供其准确的 `keyLocation`。这将所有权范围限定为 `/harness-library/`，避免涉及共享主机上的无关项目。密钥必须公开提供，以供协议验证；它不是站长账号凭据。无需登录、付费服务或额外依赖。暂时的 API 故障不会撤销成功的网站部署。

如果在工作流之外有意更新内容，先构建，再运行 `python scripts/notify_indexnow.py --dry-run` 检查 URL 列表，或运行 `python scripts/notify_indexnow.py` 提交。HTTP 200 表示已接收；HTTP 202 表示已接收，但密钥验证仍待完成。二者均不证明索引或排名。内容未变时，避免重复提交。

## GitHub Pages 与 robots.txt

robots 规则读取自**主机根目录** `https://openrootdev.github.io/robots.txt`，而不是 `/harness-library/robots.txt`。项目内的文件无法控制共享主机的抓取。项目文件仅提供当前 sitemap 的地址。请通过站长账号提交 sitemap。

如果所有者后来添加根站点仓库或自定义域名，应在部署限制前检查具有权威性的 robots 文件。绝不要随意改变同一主机上其他项目的规则。

## 迁移到组织

仓库和目录于 2026 年 10 月 10 日迁移至 [Kaelux Labs](https://github.com/OpenRootdev/harness-library)。GitHub 会重定向旧仓库 URL。一个小型[账号 Pages 仓库](https://github.com/Ker102/ker102.github.io)通过即时重定向和规范链接保留旧目录页面，并继续提供现有徽章图片。其主机根目录的 `robots.txt` 允许抓取，并链接到当前 sitemap。

使用旧目录 URL 或当前目录 URL 的现有徽章回链仍符合资格。变更这些链接不会重新开始现有的 14 天推广期；原始记录日期仍然具有权威性。

## 智能体发现

智能体可使用普通 HTML、JSON 目录或 Markdown 镜像。`llms.txt` 是一种便利性提案，不是 Google 排名因素或必要条件。Google 表示，其 AI 搜索功能采用与普通搜索相同的基础 SEO 实践。可抓取的文本、清晰的页面链接、准确的证据和有用的内容才是关键；任何配置都不能保证收录或引用。

一手参考资料：[Google JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)、[sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)、[robots 规范](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec)、[AI 功能](https://developers.google.com/search/docs/appearance/ai-features)、[llms.txt 提案](https://llmstxt.org/)。
