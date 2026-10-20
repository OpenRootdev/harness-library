# 発見とインデックス登録

`2026-10-20` 以降の現在の移転先は [OpenRootdev/harness-library](https://github.com/OpenRootdev/harness-library) と[ディレクトリ](https://openrootdev.github.io/harness-library/)です。以下の過去の移転記録は、その前の移転を説明しています。

公開ディレクトリは安定した URLs で完全な HTML を公開します。検索エンジン、JavaScript を無効にしたブラウザー、エージェントは、承認済み harness のインストール方法、前提条件、ソース、配布内容、審査範囲を直接読めます。JavaScript はフィルタリング、コピー、従来のハッシュナビゲーションを拡張するだけです。

## 公開リソース

- [ディレクトリ](https://openrootdev.github.io/harness-library/)と[投稿ガイド](https://openrootdev.github.io/harness-library/submit/)。
- [Sitemap](https://openrootdev.github.io/harness-library/sitemap.xml)：正規 HTML ページのみ。毎日のバッジ確認では、内容の更新日を作り上げません。
- [llms.txt](https://openrootdev.github.io/harness-library/llms.txt)：Markdown のインストールページとデータにリンクする簡潔なガイド。
- [llms-full.txt](https://openrootdev.github.io/harness-library/llms-full.txt)：公開テキストをまとめたもの。
- [catalog.json](https://openrootdev.github.io/harness-library/catalog.json)：審査済み掲載項目、正規ページ URLs、インストール、手動設定、範囲を明確にした証拠。
- 各正規 HTML ページには対応する `index.md` があり、`rel="alternate" type="text/markdown"` でリンクされています。

各 HTML ページは固有のタイトル、説明、正規 URL、ソーシャルプレビューのメタデータ、それらに一致する JSON-LD を持ちます。構造化データは実際のディレクトリ、メンテナー、harness を記述し、評価、ダウンロード数、あらゆる環境での互換性を捏造しません。不明なパスは、noindex のエラーページで GitHub Pages の 404 ステータスを返します。古い掲載項目のハッシュリンクも引き続き対応しています。

## 所有者の設定

1. [Google Search Console](https://search.google.com/search-console) に `https://openrootdev.github.io/harness-library/` の **URL プレフィックス プロパティ**を追加します。これにより対象をこのプロジェクトに限定できます。アカウントに提示される確認方法を使ってください。正確なファイル名と内容が提供された後で、HTML 確認ファイルを `site/` に配置できます。
2. そのプロパティで `sitemap.xml` を送信します。ホーム、投稿ガイド、harness の URLs を検査し、ツールで可能な場合にインデックス登録をリクエストします。送信は発見の手がかりであり、登録の保証ではありません。
3. [Bing Webmaster Tools](https://www.bing.com/webmasters/) にも同じサイトを追加して sitemap を送信します。アカウントで Google Search Console からのインポートが利用できる場合、確認済みプロパティを再利用できます。
4. デプロイ後にインデックス登録レポートを再確認します。報告されたクロールや内容の問題は、証拠に基づいて修正してください。`site:` 検索や Lighthouse スコアを、インデックス登録の網羅性や順位の証拠と見なさないでください。

確認には所有者のアカウント、またはそこから提供された確認用成果物が必要です。推測した確認トークンを公開しないでください。HTML 確認ファイルを追加した場合、sitemap には含めず、ビルドでは保持してください。

## 公開変更の通知

通常の push がデプロイされた後、Pages ワークフローはビルドした sitemap の正規 URLs を [IndexNow](https://www.indexnow.org/documentation) に通知します。毎日のバッジ更新では通知を行いません。今回の移行は全5ページを変更します。大きなディレクトリでは、変更ページだけを送信してください。Google は Search Console と通常のクロールを使います。IndexNow 経由で Google に送信することはありません。

このプロジェクトは `indexnow-key.txt` をホストし、その正確な `keyLocation` を提供します。これにより所有権の範囲を `/harness-library/` に限定し、共有ホストの無関係なプロジェクトを避けます。キーはプロトコルの検証のため公開配信する必要があり、ウェブマスターアカウントの認証情報ではありません。ログイン、有料サービス、追加の依存関係は不要です。API が一時的に失敗しても、成功したサイトのデプロイは取り消されません。

ワークフロー外で意図的に内容を更新する場合は、先にビルドし、`python scripts/notify_indexnow.py --dry-run` で URL 一覧を確認するか、`python scripts/notify_indexnow.py` で送信します。HTTP 200 は受信済み、HTTP 202 は受信済みでキー検証待ちを意味します。どちらもインデックス登録や順位を証明しません。内容が変わっていないときは、繰り返し送信しないでください。

## GitHub Pages と robots.txt

robots ルールは `/harness-library/robots.txt` ではなく、**ホストのルート** `https://openrootdev.github.io/robots.txt` から読み込まれます。プロジェクト内のファイルでは共有ホストのクロールを制御できません。プロジェクトのファイルは現在の sitemap の参照先を示すだけです。ウェブマスターのアカウントから sitemap を送信してください。

所有者が後にルートサイト用リポジトリや独自ドメインを追加する場合、制限をデプロイする前に権威ある robots ファイルを確認してください。同じホストの他のプロジェクトのルールを軽率に変えないでください。

## 組織への移行

リポジトリとディレクトリは、2026 年 10 月 10 日に [Kaelux Labs](https://github.com/OpenRootdev/harness-library) へ移行しました。GitHub は古いリポジトリ URL をリダイレクトします。小さな[アカウントの Pages リポジトリ](https://github.com/Ker102/ker102.github.io)が、即時リダイレクトと正規リンクにより古いディレクトリページを維持し、既存のバッジ画像も引き続き配信します。そのホストルートの `robots.txt` はクロールを許可し、現在の sitemap にリンクします。

旧 URL または現在のディレクトリ URL を使う既存のバッジリンクも引き続き対象です。リンクを変更しても既存の 14 日間のブーストは再開始しません。元の記録の日付が引き続き基準です。

## エージェントによる発見

エージェントは通常の HTML、JSON カタログ、Markdown ミラーを利用できます。`llms.txt` は利便性のための提案であり、Google のランキング要因でも必須条件でもありません。Google は、AI 検索機能も通常の検索と同じ基本的な SEO 手法を使うと説明しています。クロール可能なテキスト、明確なページリンク、正確な証拠、有用な内容が重要です。どの設定も掲載や引用を保証しません。

一次資料：[Google JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)、[sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)、[robots 仕様](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec)、[AI 機能](https://developers.google.com/search/docs/appearance/ai-features)、[llms.txt 提案](https://llmstxt.org/)。
