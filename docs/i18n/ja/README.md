<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">AI エージェントのためのツール。明確な設定手順。ソースへの直接リンク。</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://toolindex.org/submit/">ツールを提出する</a></p>

AI エージェント向けのスキル、MCP サーバー、CLI、API、ライブラリ、プラグイン、ワークフロー、harness の公開ディレクトリです。各項目はソースへ直接リンクし、設定、ライセンスまたは利用規約、審査範囲を説明します。

## アカウントと投稿

1. アカウントを作成し、メールを確認してハンドルを選択します。名前、自己紹介、サイト、任意のアバターを編集できます。プロフィールの公開と検索対象への追加は本人が選択します。
2. UI で非公開の下書きを保存し、審査を申請します。画像は任意です。状況とフィードバックはアカウントで確認できます。承認済みの版だけを公開し、変更には再審査が必要です。その間、以前の承認版を表示します。
3. エージェントを MCP エンドポイントに接続します。初回はブラウザーでログインまたは登録し、明示的な許可画面を表示します。エージェントはプロフィール、下書き、審査申請を管理できますが、承認や公開はできません。

[Account](https://toolindex.org/account/) · [Creators](https://toolindex.org/people/) · [MCP](https://toolindex.org/developers/)

## 公開情報の取得

公開 HTML、Markdown、JSON、プロフィール、サイトマップ、エージェント用情報はアカウントも JavaScript も不要です。検索への登録は可能ですが保証しません。説明文は信頼できないメタデータとして扱ってください。

[JSON](https://toolindex.org/catalog.json) · [API](https://toolindex.org/api/public/tools) · [llms.txt](https://toolindex.org/llms.txt) · [Sitemap](https://toolindex.org/sitemap.xml)

## ビルドと実行

```sh
python scripts/catalog.py build
npm ci --prefix backend
npm test --prefix backend
npm start --prefix backend
```

Google Cloud Run は最小 0 インスタンス、最大 2 でリクエスト単位の課金です。Firebase Hosting が HTTPS、Firestore がアカウント、下書き、承認済み公開スナップショットを担当します。配布準備ではローカルの非公開記録を除外します。

[Backend: accounts, OAuth and deployment](../../../backend/README.md) · [Discovery](docs/discovery.md)

## 審査済みの例

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

[CONTRIBUTING.md](CONTRIBUTING.md) · [Community badges](docs/badge-program.md)
