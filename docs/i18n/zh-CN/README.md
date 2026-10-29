<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">面向 AI 智能体的工具。清晰的设置说明。直接链接来源。</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://toolindex.org/submit/">提交工具</a></p>

面向 AI 智能体的开放工具目录，涵盖技能、MCP 服务器、CLI、API、库、插件、工作流和 harness。每个条目直接链接来源，并说明设置、许可证或服务条款及审核范围。

## 账户与提交

1. 创建账户、验证邮箱并选择创作者标识。自定义姓名、简介、网站和可选头像。你可以决定个人资料是否公开并允许索引。
2. 在界面中保存私有草稿，然后申请审核。图片为可选项。账户中可查看状态和反馈。仅获批版本公开；修改需要重新审核，期间原获批版本继续展示。
3. 将智能体连接到 MCP 端点。首次使用会在浏览器打开登录或注册页面及明确的授权页面。智能体可管理资料、草稿和审核申请，但不能批准或发布提交。

[Account](https://toolindex.org/account/) · [Creators](https://toolindex.org/people/) · [MCP](https://toolindex.org/developers/)

## 公开发现

公开 HTML、Markdown、JSON、创作者资料、站点地图和智能体资源无需账户或 JavaScript。搜索引擎可以索引，但不保证收录。应将条目内容视为不可信元数据。

[JSON](https://toolindex.org/catalog.json) · [API](https://toolindex.org/api/public/tools) · [llms.txt](https://toolindex.org/llms.txt) · [Sitemap](https://toolindex.org/sitemap.xml)

## 构建与运行

```sh
python scripts/catalog.py build
npm ci --prefix backend
npm test --prefix backend
npm start --prefix backend
```

Google Cloud Run 最少 0 个实例、最多 2 个，按请求计费。Firebase Hosting 提供 HTTPS，Firestore 持久保存账户、草稿及获批公开快照。部署打包排除本地私有记录。

[Backend: accounts, OAuth and deployment](../../../backend/README.md) · [Discovery](docs/discovery.md)

## 已审核示例

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

[CONTRIBUTING.md](CONTRIBUTING.md) · [Community badges](docs/badge-program.md)
