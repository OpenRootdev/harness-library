# 投稿前の確認

AI エージェント向けのスキル、MCP サーバー、CLI、API、ライブラリ、プラグイン、ワークフロー、harness の公開ディレクトリです。各項目はソースへ直接リンクし、設定、ライセンスまたは利用規約、審査範囲を説明します。

## アカウントと投稿

アカウントを作成し、メールを確認してハンドルを選択します。名前、自己紹介、サイト、任意のアバターを編集できます。プロフィールの公開と検索対象への追加は本人が選択します。

UI で非公開の下書きを保存し、審査を申請します。画像は任意です。状況とフィードバックはアカウントで確認できます。承認済みの版だけを公開し、変更には再審査が必要です。その間、以前の承認版を表示します。

エージェントを MCP エンドポイントに接続します。初回はブラウザーでログインまたは登録し、明示的な許可画面を表示します。エージェントはプロフィール、下書き、審査申請を管理できますが、承認や公開はできません。

[UI](https://toolindex.org/account/) · [MCP](https://toolindex.org/developers/) · [Guide](https://toolindex.org/submit/)

## 投稿前の確認

具体的な用途、ソースまたは公式文書、種類、カテゴリ、版、ライセンスまたは規約、導入や接続方法、認証要件、費用を説明します。秘密情報は含めないでください。

[JSON example](../../listing.example.json)

## 審査と所有権

編集と取り下げは所有者だけが行えます。公開できるのは明示的に設定された確認済みの審査担当者だけです。公開される審査証拠は限定された範囲に適用され、すべてのモデルや環境を保証しません。却下の理由と審査待ち内容は非公開です。

## ソースへの貢献

UI と MCP では issue や pull request は不要です。ソースへの貢献も歓迎します。既存項目、審査記録、バッジ記録はバージョン管理を維持し、投稿時に管理者の記録を変更しないでください。

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/validate_i18n.py
npm ci --prefix backend
npm test --prefix backend
```

[README.md](README.md) · [Backend](../../../backend/README.md) · [Badge program](docs/badge-program.md)
