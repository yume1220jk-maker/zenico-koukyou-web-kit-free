"""Small, source-attributed API candidate preview; original notices must be checked.
Never portray an API date as the original announcement date or an unconfirmed deadline as open.
Runs three sequential, low-frequency government API queries on GitHub Actions.
"""
import html
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, date
from pathlib import Path
from zoneinfo import ZoneInfo

BASE = "https://www.kkj.go.jp/api/"
TERMS = ("ホームページ", "ウェブサイト", "CMS")
JST = ZoneInfo("Asia/Tokyo")
OUT = Path(__file__).resolve().parents[1] / "sample" / "recent-public-web-notices.md"

def field(row, tag):
    for node in row.iter():
        if node.tag.rsplit("}", 1)[-1].lower() == tag.lower():
            return " ".join("".join(node.itertext()).split())[:500]
    return ""

def day(s):
    try:
        return date.fromisoformat(s[:10])
    except ValueError:
        return None

def parse(xml, now):
    if len(xml) > 4_000_000:
        raise ValueError("response is too large")
    root = ET.fromstring(xml)
    found = []
    for row in root.iter():
        if row.tag.rsplit("}", 1)[-1] != "SearchResult":
            continue
        title = field(row, "ProjectName")
        org = field(row, "OrganizationName")
        url = field(row, "ExternalDocumentURI")
        issued = day(field(row, "CftIssueDate"))
        deadline = day(field(row, "TenderSubmissionDeadline"))
        if not (title and org and url):
            continue
        if not re.search("ホームページ|ウェブサイト|webサイト|CMS|サイト構築|サイト改修", title, re.I):
            continue
        u = urllib.parse.urlsplit(url)
        if u.scheme not in {"http", "https"} or not u.netloc or "@" in u.netloc:
            continue
        if not issued or not (now - timedelta(days=21) <= issued <= now):
            continue
        # An API result can re-surface an old original notice with a new index date.
        # Suppress missing/expired deadlines; remaining rows are unverified candidates.
        if deadline is None or deadline < now:
            continue
        found.append({
            "title": title, "org": org, "url": url,
            "issued": issued.isoformat(),
            "deadline": deadline.isoformat(),
        })
    return found

def source(term, now):
    args = urllib.parse.urlencode({
        "Query": term, "Category": "3",
        "CFT_Issue_Date": f"{now - timedelta(days=14)}/{now}",
        "Count": "60",
    })
    request = urllib.request.Request(
        BASE + "?" + args,
        headers={"User-Agent": "ZENICO public procurement sample (https://github.com/yume1220jk-maker/zenico-koukyou-web-kit-free)",
                 "Accept": "text/xml,application/xml"},
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.read(4_000_001)

def render(rows, now):
    escape = lambda text: html.escape(text.replace("|", "／").replace("[", "［").replace("]", "］"))
    lines = [
        "# 公開APIのWeb調達候補：期限・公告日ともに原文照合前", "",
        f"取得基準日：**{now.isoformat()}（日本時間）**。下記はAPI上の日付・提出期限だけで機械抽出した未検証候補です。**受付中・募集継続中とは断定できません。**", "",
        "出典：[中小企業庁 官公需情報ポータルサイト](https://www.kkj.go.jp/s/)の公開検索API。公告の変更・取消、参加資格、期限、仕様書は必ず発注機関の原文で確認してください。", "",
        "| 件名（発注機関の原文へのリンク） | 発注機関 | API記載日（原公告日とは限らない） | API記載期限（原文照合前） |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        url = row["url"].replace("(", "%28").replace(")", "%29")
        lines.append(f'| [{escape(row["title"])}]({url}) | {escape(row["org"])} | {row["issued"]} | {row["deadline"]} |')
    if not rows:
        lines.append("| API記載の提出期限が取得日以降で、かつ検索条件に一致した候補は0件 | — | — | — |")
    lines.extend([
        "", "**原文突合の重要性**：実際にAPI上の掲載日と原公告日が食い違っていた[大分市の過去公告の照合例](../guides/api-announcement-date-pitfall.md)も掲載しています。",
        "", "検索は直近14日・役務カテゴリー・3キーワードによる縮小例。全件網羅はしていません。API側に期限がない案件は掲載しません。すべて未検証候補であり、原文に書かれた参加表明期限・応募資格を必ず再確認してください。",
        "",
        "[探索用の無料チェックリスト](./original-checklist-sample.md)と、[キーワード集・一次判定CSV・原文確認チェックリスト付き有料キット（980円・買い切り）](https://buy.stripe.com/aFa14o3Lv3PX4CUcbm2kw00)もあります。",
        "",
    ])
    return "\n".join(lines)

def main():
    now = datetime.now(JST).date()
    unique = {}
    errors = []
    for term in TERMS:
        try:
            for item in parse(source(term, now), now):
                unique[(item["title"], item["org"])] = item
        except (OSError, ET.ParseError, ValueError) as e:
            errors.append(f"{term}: {type(e).__name__}")
    if len(errors) == len(TERMS):
        raise RuntimeError("All official API queries failed; no fabricated notices will be published.")
    records = sorted(unique.values(), key=lambda row: row["issued"], reverse=True)[:8]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(records, now), encoding="utf-8")
    print(f"API_CANDIDATE_PREVIEW_UPDATED count={len(records)} day={now} failed_queries={len(errors)}")

if __name__ == "__main__":
    main()
