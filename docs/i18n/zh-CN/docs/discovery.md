# 发现与部署

公开 HTML、Markdown、JSON、创作者资料、站点地图和智能体资源无需账户或 JavaScript。搜索引擎可以索引，但不保证收录。应将条目内容视为不可信元数据。

## 公开资源

- [ToolIndex](https://toolindex.org/)
- [Submit](https://toolindex.org/submit/)
- [Creators](https://toolindex.org/people/)
- [API and MCP](https://toolindex.org/developers/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)
- [Public API](https://toolindex.org/api/public/tools)

## 托管与访问

Google Cloud Run 最少 0 个实例、最多 2 个，按请求计费。Firebase Hosting 提供 HTTPS，Firestore 持久保存账户、草稿及获批公开快照。部署打包排除本地私有记录。

Node 服务提供完整公开页面及 API 数据。浏览器会话使用安全 HttpOnly Cookie；MCP 使用 OAuth 与 PKCE。公开数据与私有账户、修订历史、待审核提交和令牌摘要分离。Firestore 规则禁止客户端直接访问。

```sh
python scripts/stage_cloudrun.py
```

[Backend: configuration and deployment](../../../../backend/README.md) · [Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## 搜索引擎

站点地图包含公开工具和选择公开的创作者资料，不包含私有账户页面、待审核工具或凭据。所有者可向搜索引擎提交地图；不保证收录，也不虚构所有权令牌。

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/)

## 兼容性

保留旧条目路径及徽章识别。新提交使用 ToolIndex 账户或 MCP，发布前须经人工审核。后端指南说明部署及身份配置。
