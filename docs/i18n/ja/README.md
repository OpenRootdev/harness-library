<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="Harness Library"></p>
<h1 align="center">Harness Library</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">再利用できるエージェント用 harness を見つけ、インストールし、共有しましょう。</p>
<p align="center"><a href="https://openrootdev.github.io/harness-library/">ライブラリを見る</a> · <a href="https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml">harness を投稿する</a> · <a href="CONTRIBUTING.md">投稿ガイド</a></p>

エージェントが特定の仕事を適切にこなすための指示、スキル、ツール、ワークフローを集めたオープンなディレクトリです。harness は数個のファイルだけで構成されることも、大規模なツール設定を含むこともあります。各掲載項目には、インストール方法、手動で設定する内容、ソースリポジトリのどの部分が必要かを記載しています。

最初の掲載項目は [Smooth Motion Graphics](https://github.com/Ker102/smooth-motion-graphics) と [ViperMesh for Blender](https://github.com/OpenRootdev/vipermesh-blender) です。ViperMesh の既存のリポジトリとリリースは変更せずに掲載しています。Harneloop の使用は任意です。Harneloop で作成された harness は、審査後にその表記を表示できます。

## harness の動作を見る

Harneloop の解説動画では、ライブラリの [Smooth Motion Graphics harness](https://openrootdev.github.io/harness-library/harnesses/smooth-motion-graphics/) のモーションスタイルを紹介しています。読みやすいシーン、曲線の接続、落ち着いた切り替えが特徴です。また、Harneloop が harness ユニットを構築・改善する方法も説明しています。

<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4"><img src="https://harneloop.kaelux.dev/media/harneloop-video-poster.png" alt="Harneloop の無音モーショングラフィックスデモを見る" width="860"></a></p>
<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4">動画全編を見る · 3:40 · 無音、画面上の説明付き</a></p>

動画は別の場所でホストされています。harness 自体のインストールパッケージとサンプルレンダラーは、掲載ページから確認してください。

## harness を投稿する

**新しい投稿を歓迎します。** コーディング、調査、データ、創作、Blender、運用に役立つ harness を募集しています。少数のスキルだけでも構いません。Harneloop を使う必要はありません。

1. [短い GitHub 投稿フォーム](https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml)を開き、リポジトリとエージェントにどの仕事をさせるためのものかを記入します。
2. 明確なインストール手順、カテゴリ、ライセンス、バージョン・配布範囲、手動設定を記載します。コンポーネント数とテストの証拠は任意です。
3. メンテナーが設定を審査し、必要に応じて issue で確認したうえで、承認した項目を公開します。

**fork、pull request、Harness Library アカウントは不要です。** フォームには GitHub アカウントが必要です。`data/listings/` に JSON ファイルを1つ追加する PR を送る方法もあります。[公開投稿ガイド](https://openrootdev.github.io/harness-library/submit/)、[CONTRIBUTING.md](CONTRIBUTING.md)、[テンプレート](../../../docs/listing.example.json)を参照してください。

異なる用途の内容が混在するリポジトリでは、用途を絞ったパッケージか harness 専用ブランチを用意する必要があります。投稿者が検証や宣伝のラベルを設定することはできません。メンテナーは公開前に設定、範囲、提示された証拠を審査します。「Artifacts checked」は、文書に記載された成果物を確認したという意味であり、あらゆるモデル、プラットフォーム、用途で動作することを意味しません。

## 無料バッジプログラム

ソース README の最初の 30 行以内に、正確な「Listed in Harness Library」バッジと掲載ページへのリンクを追加してください。検証後、掲載項目には**一度だけ、14 日間のコミュニティブースト**が付与され、ディレクトリ内で明示されます。ブーストは表示順に影響しますが、審査状況には影響しません。無料で、参加は任意、自動的に期限切れになります。バッジを削除して再追加しても期間は再開始しません。[ポリシーと検証](docs/badge-program.md)を参照してください。

## 開発

フロントエンドの依存関係やバックエンドサービスは不要です。Python 3.11+ でバリデーターとビルダーを実行します。UI は通常の HTML、CSS、JavaScript で構成されています。

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -c "import shutil; shutil.copytree('dist', '.preview/harness-library', dirs_exist_ok=True)"
python -m http.server 4201 --directory .preview
```

`http://localhost:4201/harness-library/` を開きます。プレビュー用コピーは本番のベースパスを正しく配信します。再ビルド後はコピーを更新してください。アセットとナビゲーションのパスは、意図的に GitHub Pages のプロジェクト URL と一致させています。

`site/layout.html`、`site/style.css`、`scripts/publishing.py` は、ディレクトリ、各 harness、投稿ガイド、概要ページの完全な HTML ページを生成します。JavaScript は検索、フィルター、コピー機能を段階的に追加します。JavaScript なしでもインストール内容とナビゲーションは利用できます。ビルドでは sitemap、各ページの Markdown ミラー、`llms.txt`、審査済み JSON カタログも公開します。所有者の設定とクロールの詳細は[発見とインデックス登録](docs/discovery.md)を参照してください。

`python scripts/catalog.py refresh` は公開 GitHub README の内容を読み、参加を選択したバッジを検証します。投稿されたコードは決して実行しません。GitHub Pages は審査済みの main を公開します。毎日のワークフローがバッジ記録を更新して再ビルドします。外部 PR のチェックには読み取り専用権限しかありません。

ソースデータと審査記録はこのリポジトリにあります。harness のソースとリリース用アセットはそれぞれのリポジトリにあります。Harneloop のフレームワークと一緒に harness の動画、依存関係、非公開の開発記録がインストールされることはありません。
