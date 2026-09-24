# 官公需Web案件探索スターターキット — 自治体ホームページリニューアル・プロポーザル案件の無料サンプル

Web制作会社向けに、**自治体ホームページのリニューアル／プロポーザル案件**を含む、官公庁・自治体のWeb制作・改修・運用保守案件を
**検索 → 一次判定 → 原文確認 → 週次改善** の流れで整理するための無料サンプルです。

「ホームページ リニューアル プロポーザル」「Webサイト 再構築 公募型プロポーザル」「自治体 CMS 更改」など、案件名の表現が揺れる公共Web案件を探しやすくするための探索手順と縮小テンプレートを公開しています。

このリポジトリは、有料版「官公需Web案件探索スターターキット」の一部を
購入前に確認できる縮小版です。

> **購入を検討している方へ**：無料版の `sample/` を先に確認できます。探索キーワード集・案件一次判定CSV・原文確認チェックリスト・週次レビューの4点が必要な場合は、**[980円で買い切り購入（Stripe決済）](https://buy.stripe.com/aFa14o3Lv3PX4CUcbm2kw00)**できます。決済後は有料版の納品ページに移動します。購入前に詳細を確認したい方は[商品説明ページ](https://zenico-koukyou-web-kit.vercel.app/?utm_source=github&utm_medium=organic&utm_campaign=free_repo_readme_direct_cta)をご覧ください。


## 発注機関の原文を直接確認した無料調査（2026年9月24日版）

**[提案期限だけでは判断できない：Web調達の発注機関別原文3例](guides/source-verified-web-procurement-20260924.md)**

国際交流基金のWebサイト設計・運用保守・記事制作案件（**ページ記載の提出期限：2026年10月2日13時**、説明会は終了済み）、横浜市の**参加申請締切済み**案件、大分市の**API記載日と原公告日が食い違った**案件を並べ、元資料を確認する方法を公開しています。**いずれも今から新規参加できると保証するものではありません**。

継続して官公需Web案件の**自動抽出通知**が必要な事業者には[公共Webウォッチ月額980円の既存検証プラン](https://iuycadhbkfmikfrewqjr.supabase.co/functions/v1/zenico-pww-offer?ref=pww25_github_sourceproof_0924)もあります。ただし、この無料の手動照合記事と異なり、同プランは各件の原公告・参加資格を毎回人手で照合するサービスではありません。

**同じ980円でも別商品です。** 自分で案件を探して整理するためのテンプレート一式が必要なら「スターターキット（980円・買い切り）」、候補の自動抽出通知を継続して受けたいなら「公共Webウォッチ（980円・月額）」が対象です。どちらも案件への参加・落札を保証するものではありません。

## 出典付きの実在案件サンプル（自動更新）

**[官公需情報ポータルAPIから取得したWeb調達の未検証候補を見る](sample/recent-public-web-notices.md)**

平日朝に公開APIから少数の候補を取得し、発注機関の原文にリンクします。**API側の掲載日が実際の公告日と異なる例があり、一覧の受付状況は未確認です。** 応募可能性・原公告日・参加表明期限・参加資格は必ず原文で確認してください。更新失敗時は取得基準日を確認してください。下のCSVサンプルは対照的に架空データです。詳しくは[原文突合の実例](guides/api-announcement-date-pitfall.md)。

## 無料サンプルに含まれるもの

- `sample/triage-sample.csv`
  - 公共Web案件を一次整理するCSVの縮小例
- `sample/original-checklist-sample.md`
  - 発注機関の原文を確認するときのチェックリスト縮小版

CSV内の案件名・発注機関はサンプル用の架空データです。

## この無料版でできること

1. 官公需情報からWeb制作・リニューアル・運用保守案件を探す
2. 案件を一次判定して、追う案件と見送る案件を分ける
3. 発注機関の原文で参加条件・期限・仕様を確認する
4. 探索結果をCSVへ残し、次回の検索条件を改善する

案件への応募可否や参加資格を自動判定するものではありません。最終確認は必ず発注機関の公告・仕様書・要領等で行ってください。

## 有料版

**980円・買い切り**

有料版には以下を収録しています。

- 探索キーワード集
- 案件一次判定CSV
- 原文確認チェックリスト
- 週次レビューテンプレート

商品内容・購入条件の確認:
https://zenico-koukyou-web-kit.vercel.app/?utm_source=github&utm_medium=organic&utm_campaign=free_repo_readme

[有料版を980円で直接購入（Stripe・買い切り）](https://buy.stripe.com/aFa14o3Lv3PX4CUcbm2kw00)

直接購入する前に、上の商品ページで収録内容と注意事項をご確認ください。決済後は既存の自動納品導線へ進みます。

無料Webサンプル:
https://zenico-koukyou-web-kit.vercel.app/sample/?utm_source=github&utm_medium=organic&utm_campaign=free_repo_readme

## 無料ガイド

官公需案件の探索手順、検索キーワード、入札公告の読み方を無料公開しています。

- [ホームページリニューアルのプロポーザル案件を探す方法](guides/homepage-renewal-proposal.md)
- 官公需情報ポータルの使い方 — Web制作案件を探す検索手順
  - https://zenico-koukyou-web-kit.vercel.app/guide/kankouju-portal-tsukaikata/
- Web制作の公共案件 — 「一般競争」と「プロポーザル」の違い
  - https://zenico-koukyou-web-kit.vercel.app/guide/proposal-vs-ippan/
- CMS・Webサイト運用保守案件の検索キーワード設計
  - https://zenico-koukyou-web-kit.vercel.app/guide/cms-unyou-hoshu/
- 自治体ホームページ・Webサイトリニューアル公募の探し方
  - https://zenico-koukyou-web-kit.vercel.app/guide/jichitai-renewal/
- 公共Web案件で最初に拾う3つの期限
  - https://zenico-koukyou-web-kit.vercel.app/guide/deadline-shitsumon/
- 公共Web案件の探索台帳をCSVで作る方法
  - https://zenico-koukyou-web-kit.vercel.app/guide/triage-csv/
- Web制作会社向け — 官公庁・自治体の入札案件の探し方
  - https://zenico-koukyou-web-kit.vercel.app/guide/web-seisaku-nyusatsu-sagashikata/
- 官公需でWeb制作案件を探す検索キーワードの組み方
  - https://zenico-koukyou-web-kit.vercel.app/guide/kankouju-keyword/
- Web制作案件の入札公告を読む一次チェックリスト
  - https://zenico-koukyou-web-kit.vercel.app/guide/nyusatsu-checklist/

## 関連する無料チェックリスト：Webサイト公開前の検証証跡

Web制作会社向けに、**公開前の検証項目・証拠・UNKNOWN／残課題の整理方法**をまとめた無料ガイドも公開しています。

- [Webサイト公開前チェックリスト（無料）](guides/koukai-mae-web-evidence-checklist.md)
- 検証証跡を第三者形式の報告書にまとめたい企業向け：[ZENICO 公開前Evidence Audit（9,800円／件、少数B2B試験受付）](https://zenico-evidence-audit.vercel.app/?utm_source=github&utm_medium=owned&utm_campaign=free_repo_release_checklist_20260924)

Evidence Auditは本リポジトリの官公需案件探索スターターキットとは別サービスです。公開・認証不要の権限ある対象のみを扱い、侵入テスト・法令適合性保証は行いません。

## 注意

本リポジトリおよび有料版は、案件探索・情報整理を補助するための資料です。

- 入札参加資格の判定
- 法律・税務・契約上の助言
- 応募可否の最終判断
- 案件の発見、参加、落札の保証

は行いません。

必ず発注機関が公開する最新版の公告・仕様書・要領等を確認してください。

## 権利

© ZENICO Project

このリポジトリは評価用の無料プレビューとして公開しています。
明示的なオープンソースライセンスは付与していません。
