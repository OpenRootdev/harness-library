# 提交清单

面向 AI 智能体的开放工具目录，涵盖技能、MCP 服务器、CLI、API、库、插件、工作流和 harness。每个条目直接链接来源，并说明设置、许可证或服务条款及审核范围。

## 账户与提交

创建账户、验证邮箱并选择创作者标识。自定义姓名、简介、网站和可选头像。你可以决定个人资料是否公开并允许索引。

在界面中保存私有草稿，然后申请审核。图片为可选项。账户中可查看状态和反馈。仅获批版本公开；修改需要重新审核，期间原获批版本继续展示。

将智能体连接到 MCP 端点。首次使用会在浏览器打开登录或注册页面及明确的授权页面。智能体可管理资料、草稿和审核申请，但不能批准或发布提交。

[UI](https://toolindex.org/account/) · [MCP](https://toolindex.org/developers/) · [Guide](https://toolindex.org/submit/)

## 提交清单

说明具体任务、来源或官方文档、类型、分类、版本、许可证或条款、安装或连接步骤、认证要求及费用。切勿提交秘密信息。

[JSON example](../../listing.example.json)

## 审核与所有权

只有所有者可编辑或撤回提交。只有明确配置且邮箱已验证的审核员可发布。公开审核证据仅适用于所述范围，不保证所有模型或平台。拒绝反馈和待审核内容保持私有。

## 源码贡献

界面和 MCP 无需 issue 或 pull request，仍欢迎源码贡献。原始目录、审核记录及徽章记录保留在版本控制中；提交工具时请勿修改维护者记录。

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/validate_i18n.py
npm ci --prefix backend
npm test --prefix backend
```

[README.md](README.md) · [Backend](../../../backend/README.md) · [Badge program](docs/badge-program.md)
