<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="Harness Library"></p>
<h1 align="center">Harness Library</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">发现、安装并分享可复用的智能体 harness。</p>
<p align="center"><a href="https://openrootdev.github.io/harness-library/">浏览库目录</a> · <a href="https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml">提交 harness</a> · <a href="CONTRIBUTING.md">提交指南</a></p>

这是一个开放目录，收录帮助智能体完成特定任务的指令、技能、工具和工作流。harness 可以只是几个文件，也可以是一套更完整的工具配置。每个条目都说明安装方式、需要手动配置的内容，以及所需的源代码仓库范围。

首批条目为 [Smooth Motion Graphics](https://github.com/Ker102/smooth-motion-graphics) 和 [ViperMesh for Blender](https://github.com/OpenRootdev/vipermesh-blender)。ViperMesh 的现有仓库和发布版本保持不变。Harneloop 并非必需；使用它构建的 harness 可在审核后展示相关署名。

## 查看 harness 的实际效果

Harneloop 讲解视频展示了库中 [Smooth Motion Graphics harness](https://openrootdev.github.io/harness-library/harnesses/smooth-motion-graphics/) 的动画风格：清晰易读的场景、曲线连接和舒缓的过渡。视频也解释了 Harneloop 如何构建和改进 harness 单元。

<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4"><img src="https://harneloop.kaelux.dev/media/harneloop-video-poster.png" alt="观看无声的 Harneloop 动态图形演示" width="860"></a></p>
<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4">观看完整视频 · 3:40 · 无声，附屏幕文字讲解</a></p>

视频单独托管。请从对应条目查看 harness 自身的安装包和示例渲染器。

## 提交 harness

**欢迎提交新条目。** 我们希望收录适用于编程、研究、数据、创作、Blender 和运维的实用 harness。几个技能也可能足够；不要求使用 Harneloop。

1. [打开简短的 GitHub 提交表单](https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml)，填写仓库及其帮助智能体完成的任务。
2. 提供清晰的安装步骤、类别、许可证、版本与分发范围，以及所有手动设置要求。组件数量和测试证据为可选内容。
3. 维护者审核配置，必要时在你的 issue 中跟进，并发布获批条目。

**不需要 fork、pull request 或 Harness Library 账号。** 使用表单需要 GitHub 账号。也可以通过 PR 在 `data/listings/` 中添加一个 JSON 文件。参见[公开提交指南](https://openrootdev.github.io/harness-library/submit/)、[CONTRIBUTING.md](CONTRIBUTING.md) 和[模板](../../../docs/listing.example.json)。

包含混合内容的仓库必须提供专门的安装包或独立的 harness 分支。提交者不能设置验证或推广标签。维护者会在发布条目前审核配置、范围和任何证据。“Artifacts checked”表示已检查文档所列的产物；并不意味着所有模型、平台或使用场景都能正常运行。

## 免费徽章计划

在源仓库 README 的前 30 行内添加准确的“Listed in Harness Library”徽章及指向条目的回链。验证后，你的条目将获得**一次为期 14 天的社区推广**，并在目录中明确标注。推广影响排序，不影响审核状态。该计划免费、自愿参与，且自动到期。移除再重新添加徽章不会重新开始推广期。参见[政策与验证](docs/badge-program.md)。

## 开发

无需前端依赖或后端服务。Python 3.11+ 用于运行验证器和构建器；界面使用原生 HTML、CSS 和 JavaScript。

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -c "import shutil; shutil.copytree('dist', '.preview/harness-library', dirs_exist_ok=True)"
python -m http.server 4201 --directory .preview
```

打开 `http://localhost:4201/harness-library/`。预览副本会正确提供生产环境的基础路径；每次重新构建后请更新副本。资源和导航路径有意与 GitHub Pages 项目 URL 保持一致。

`site/layout.html`、`site/style.css` 和 `scripts/publishing.py` 为目录、每个 harness、提交指南以及关于页面生成完整 HTML 页面。JavaScript 渐进式增强搜索、筛选和复制功能；没有 JavaScript 时，安装内容和导航仍然可用。构建还会发布 sitemap、页面的 Markdown 镜像、`llms.txt` 和经过审核的 JSON 目录。所有者设置及抓取细节请参见[发现与索引](docs/discovery.md)。

`python scripts/catalog.py refresh` 通过读取 GitHub 上的公开 README 内容，验证自愿参与的徽章。它绝不执行提交的代码。GitHub Pages 发布经过审核的 main 分支；每日工作流刷新徽章记录并重新构建。外部 PR 检查仅有只读权限。

源数据和审核记录保存在本仓库中。harness 源代码及发布资源保存在各自仓库中。Harneloop 框架不会附带安装任何 harness 视频、依赖或私有开发记录。
