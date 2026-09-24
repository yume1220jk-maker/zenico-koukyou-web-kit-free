# ZENICO Buffer → X 自動投稿

**現状:** GitHub Actions は導入済み。ただし、本人による Buffer 登録・X 認可・Buffer API キー登録が済むまで自動投稿しません。

## 最小セットアップ（有料ブラウザ不要）

1. Buffer Free で登録する: https://login.buffer.com/signup?plan=free&product=buffer
2. Buffer 内から運用対象の **X** アカウントを接続し、本人による認証と権限承認を完了する。
3. Buffer API settings で **Personal API Key** を作成する: https://publish.buffer.com/settings/api
4. GitHub リポジトリの **Settings → Secrets and variables → Actions → New repository secret** に、名前 `ZENICO_BUFFER_API_KEY` でキーを保存する。チャットや公開ファイルへキーを貼らない。

これで Buffer に接続した X チャンネルが **1つだけ** なら ID を自動認識する。複数の X チャンネルがある場合は、意図しない投稿を防止するため自動投稿を停止し、`ZENICO_BUFFER_CHANNEL_ID` を追加指定する。任意で `ZENICO_BUFFER_EXPECTED_ACCOUNT` を Repository Variables に設定すると名前の照合もできる。

## 動作

- 平日 10:17 JST に GitHub Actions が起動し、未送信の投稿を1件だけ Buffer のキューに入れる。
- 送信前にローカルの状態ファイルへ claim を記録。API 応答が不明な場合は再送をせず `manual_check_required` で停止する。
- 投稿文案は `automation/buffer_posts.json` にある既存の公共Web案件探索ガイド向け8件。
- 最初の8件が終了した時点で **自動的には新しい文章を生成しない**。その追加開発と運用は別途必要。画像の自動生成・投稿、フォロワー対応、アフィリエイト販売の自動化も本リポジトリでは未実装。
- 投稿はプラットフォーム規約を遵守し、重複投稿を避けること。
- GitHub Actions workflow: `.github/workflows/buffer_autopost.yml`
