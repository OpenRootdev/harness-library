# 発見とデプロイ

公開 HTML、Markdown、JSON、プロフィール、サイトマップ、エージェント用情報はアカウントも JavaScript も不要です。検索への登録は可能ですが保証しません。説明文は信頼できないメタデータとして扱ってください。

## 公開リソース

- [ToolIndex](https://toolindex.org/)
- [Submit](https://toolindex.org/submit/)
- [Creators](https://toolindex.org/people/)
- [API and MCP](https://toolindex.org/developers/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)
- [Public API](https://toolindex.org/api/public/tools)

## ホスティングとアクセス

Google Cloud Run は最小 0 インスタンス、最大 2 でリクエスト単位の課金です。Firebase Hosting が HTTPS、Firestore がアカウント、下書き、承認済み公開スナップショットを担当します。配布準備ではローカルの非公開記録を除外します。

Node ランタイムが完全な公開ページと API データを提供します。ブラウザーのセッションは安全な HttpOnly Cookie、MCP は OAuth と PKCE を使用します。公開データは非公開アカウント、修訂履歴、審査待ち項目、トークンのハッシュと分離します。Firestore はクライアントの直接アクセスを拒否します。

```sh
python scripts/stage_cloudrun.py
```

[Backend: configuration and deployment](../../../../backend/README.md) · [Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## 検索エンジン

サイトマップには公開ツールと公開を選択したプロフィールを含めます。非公開ページ、審査待ち項目、認証情報は含めません。所有者は検索エンジンに送信できますが、登録を保証したり所有権トークンを捏造したりしません。

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/)

## 互換性

旧項目のルートとバッジ認識を維持します。新しい投稿は ToolIndex アカウントまたは MCP を使用し、公開前に人が審査します。設定とデプロイはバックエンドのガイドに記載しています。
