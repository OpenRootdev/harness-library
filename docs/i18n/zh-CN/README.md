<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">面向 AI 智能体的工具。清晰的设置说明。直接链接来源。</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml">提交工具</a></p>

ToolIndex 是开放的 AI 智能体工具目录，收录技能、MCP 服务器、CLI、API、库、插件、工作流和 harness。只要明确说明访问方式、价格和条款，本地软件包、托管服务与商业工具均可提交。

## 收录范围

适用于具体任务的实用工具，从小型技能文件夹到服务 API。每个条目直接链接到源代码仓库或官方文档，并说明安装或连接方式、手动设置、许可证或条款、版本和审核范围。

## 提交工具

1. 打开 GitHub 表单，填写工具名称、类型、来源和用途。
2. 说明软件包或服务、安装或访问步骤、版本、许可证或条款、所需凭据及费用。切勿提交秘密信息。
3. 标志或自定义图片是可选的。提供图片时应附上 URL、来源和替代文本；否则显示中性的名称首字母。
4. 维护者审核后发布获批条目。不需要 fork、pull request 或 ToolIndex 账号；使用表单需要 GitHub 账号。

[CONTRIBUTING.md](CONTRIBUTING.md) · [JSON](../../../docs/listing.example.json)

## 已审核示例

品牌动画技能和 Blender MCP 连接器展示两种可收录的工具类型。源码与发布版本仍保留在各自仓库。

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

## 构建与预览

使用 Python 3.11+ 构建静态站点。前端使用 HTML、CSS 和 JavaScript；搜索是渐进增强功能，禁用 JavaScript 后页面仍可阅读。

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -m http.server 4201 --directory dist
```

`http://localhost:4201/`

## Google Cloud 托管

站点由 Cloud Run 提供服务，最小实例数为 0，最大为 2，按请求计费。Firebase Hosting 处理自定义域名 HTTPS 并将请求转发至 Cloud Run。部署准备脚本只包含公开文件，排除工作区私有文件。域名启用仍需完成 DNS 与证书验证。

`python scripts/stage_cloudrun.py` · [`firebase.json`](../../../firebase.json) · [docs/discovery.md](docs/discovery.md)

## 审核与社区徽章

设置审核与产物检查只描述具体证据，并不保证所有模型或平台兼容。可选徽章提供一次透明的 14 天社区展示提升。Harneloop 署名为可选项，不要求使用特定框架。

[docs/badge-program.md](docs/badge-program.md)
