# 発見とデプロイ

ToolIndex は完全な HTML、Markdown ミラー、レビュー済み JSON カタログを公開します。検索エンジンやエージェントは JavaScript なしでインストールやアクセス手順、ソース、ライセンス、レビュー範囲を読めます。

## 公開リソース

- [ToolIndex](https://toolindex.org/)
- [submit/](https://toolindex.org/submit/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)

## Google Cloud ホスティング

Cloud Run は europe-west1 で最小 0、最大 2 インスタンス、リクエストベース課金を使用します。Firebase Hosting が HTTPS と転送を提供します。DNS は GitHub Pages ではなく Firebase Hosting のレコードで設定します。準備スクリプトは公開出力とコンテナー設定だけをコピーします。表示されたパスを PUBLIC_CONTEXT に使用してください。デプロイには承認済みの Google Cloud と Firebase CLI アクセスが必要です。

```sh
python scripts/stage_cloudrun.py
gcloud run deploy toolindex --source PUBLIC_CONTEXT --project toolindex-org --region europe-west1 --min 0 --max 2 --min-instances 0 --max-instances 2 --cpu-throttling --memory 512Mi --execution-environment gen2 --service-account toolindex-runtime@toolindex-org.iam.gserviceaccount.com --build-service-account projects/toolindex-org/serviceAccounts/toolindex-build@toolindex-org.iam.gserviceaccount.com --allow-unauthenticated
firebase deploy --only hosting --project toolindex-org
```

[Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## 検索エンジン

所有者が提供した検証ファイルで toolindex.org の URL プレフィックスプロパティを確認し、Search Console と Bing Webmaster Tools に sitemap.xml を送信します。検証トークンを推測せず、送信をインデックス登録の証拠と扱わないでください。ルート robots.txt はクロールを許可します。IndexNow 通知は任意で、対応する所有権ファイルとページの公開後にだけ送信します。

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)

## 互換性とレビュー

旧 /harnesses/ ページは /tools/ にリダイレクトします。以前のバッジ URL とラベルも認識し、一度限りの 14 日間の優遇期間をリセットしません。GitHub は以前のリポジトリを OpenRootdev/toolindex に転送します。レビュー記録は限定された証拠です。CI は提出ツールのコードを実行せず、その依存関係もインストールしません。
