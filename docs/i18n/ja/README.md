<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">AI エージェントのためのツール。明確な設定手順。ソースへの直接リンク。</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml">ツールを提出する</a></p>

ToolIndex は AI エージェントが使えるスキル、MCP サーバー、CLI、API、ライブラリ、プラグイン、ワークフロー、ハーネスの公開ディレクトリです。アクセス方法、料金、条件が明確であれば、ローカルパッケージ、ホスト型サービス、商用ツールも対象です。

## 対象となるツール

小さなスキルフォルダーからサービス API まで、具体的な作業に役立つツールを扱います。各掲載ページはソースリポジトリまたは公式ドキュメントに直接リンクし、インストールや接続、手動設定、ライセンスや条件、バージョン、レビュー範囲を説明します。

## ツールを提出する

1. GitHub フォームにツール名、種類、ソース、目的を記入します。
2. パッケージやサービス、インストールやアクセス手順、バージョン、ライセンスや条件、必要な認証情報と料金を説明します。秘密情報は提出しないでください。
3. ロゴやカスタム画像は任意です。使用する場合は URL、出典、代替テキストを記載します。画像がなければ中立的な頭文字を表示します。
4. メンテナーが確認し、承認した項目を公開します。fork、pull request、ToolIndex アカウントは不要ですが、フォームには GitHub アカウントが必要です。

[CONTRIBUTING.md](CONTRIBUTING.md) · [JSON](../../../docs/listing.example.json)

## レビュー済みの例

ブランド動画のスキルと Blender MCP コネクターが二つの対象形式を示しています。ソースとリリースは各ツールのリポジトリに残ります。

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

## ビルドとプレビュー

Python 3.11+ で静的サイトを生成します。フロントエンドは HTML、CSS、JavaScript で、検索は段階的な拡張です。JavaScript が無効でもページを読めます。

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -m http.server 4201 --directory dist
```

`http://localhost:4201/`

## Google Cloud ホスティング

Cloud Run で最小 0、最大 2 インスタンス、リクエストベースの課金を使用します。Firebase Hosting がカスタムドメインの HTTPS を処理し、Cloud Run に転送します。公開ファイルだけを準備するスクリプトはワークスペースの私有ファイルを除外します。ドメイン有効化には DNS と証明書の検証が必要です。

`python scripts/stage_cloudrun.py` · [`firebase.json`](../../../firebase.json) · [docs/discovery.md](docs/discovery.md)

## レビューとコミュニティバッジ

設定や成果物の確認は具体的な証拠を示すもので、全モデルやプラットフォームの互換性保証ではありません。任意のバッジにより透明な 14 日間のコミュニティ表示優遇を一度受けられます。Harneloop の帰属表示は任意で、特定フレームワークは必須ではありません。

[docs/badge-program.md](docs/badge-program.md)
