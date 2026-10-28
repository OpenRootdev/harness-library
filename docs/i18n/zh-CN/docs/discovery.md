# 发现与部署

ToolIndex 发布完整 HTML、Markdown 镜像和经审核的 JSON 目录。搜索引擎与智能体无需 JavaScript 即可读取安装或访问说明、来源链接、许可证和审核范围。

## 公开资源

- [ToolIndex](https://toolindex.org/)
- [submit/](https://toolindex.org/submit/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)

## Google Cloud 托管

Cloud Run 在 europe-west1 提供服务，最小实例数为 0，最大为 2，按请求计费。Firebase Hosting 提供自定义域名 HTTPS 并转发请求。DNS 应使用 Firebase Hosting 的记录，而非 GitHub Pages。准备脚本只复制公开构建内容和容器配置；将其输出路径用于 PUBLIC_CONTEXT。部署需要已授权的 Google Cloud 和 Firebase CLI。

```sh
python scripts/stage_cloudrun.py
gcloud run deploy toolindex --source PUBLIC_CONTEXT --project toolindex-org --region europe-west1 --min 0 --max 2 --min-instances 0 --max-instances 2 --cpu-throttling --memory 512Mi --execution-environment gen2 --service-account toolindex-runtime@toolindex-org.iam.gserviceaccount.com --build-service-account projects/toolindex-org/serviceAccounts/toolindex-build@toolindex-org.iam.gserviceaccount.com --allow-unauthenticated
firebase deploy --only hosting --project toolindex-org
```

[Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## 搜索引擎

使用所有者提供的验证文件确认 toolindex.org 的 URL 前缀属性，然后在 Search Console 和 Bing Webmaster Tools 提交 sitemap.xml。不要猜测验证令牌，也不要把提交视为已索引的证据。根目录 robots.txt 允许抓取。IndexNow 通知是可选的，只有对应所有权文件与页面上线后才发送。

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)

## 兼容性与审核

旧 /harnesses/ 页面重定向至 /tools/。原徽章 URL 与标签仍被认可，不会重置一次性的 14 天展示提升。GitHub 将旧仓库重定向至 OpenRootdev/toolindex。审核记录只说明有限范围的证据。CI 不会执行提交工具的代码或安装其依赖。
