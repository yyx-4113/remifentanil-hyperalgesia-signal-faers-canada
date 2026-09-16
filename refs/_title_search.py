"""按标题+作者在 Crossref 检索缺失 DOI 的条目（R10-R13）。
只做只读查询，不写任何文件；结果打印供人工核对。
"""
import urllib.request, urllib.parse, json, time

MAILTO = "960856791@qq.com"
BASE = "https://api.crossref.org/works"

QUERIES = [
    ("R10", "Extending the methods used to screen the WHO drug safety database towards analysis of complex associations and improved accuracy for rare events", "Norén"),
    ("R11", "Bayesian data mining in large frequency tables with an application to the FDA spontaneous reporting system", "DuMouchel"),
    ("R12", "Use of proportional reporting ratios PRRs for signal generation from spontaneous adverse drug reaction reports", "Evans Waller Davis"),
    ("R13", "A comparison of measures of disproportionality for signal detection in spontaneous reporting systems for adverse drug reactions", "van Puijenbroek"),
]


def search(title, author):
    params = {
        "query.bibliographic": title,
        "query.author": author,
        "rows": "3",
        "select": "DOI,title,author,container-title,issued,volume,issue,page,type",
        "mailto": MAILTO,
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": f"ref-check/1.0 (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)["message"]["items"]


for tag, title, author in QUERIES:
    print("=" * 90)
    print(f"{tag}  检索: {title[:70]}...  [{author}]")
    try:
        items = search(title, author)
    except Exception as e:
        print("  ERROR:", type(e).__name__, e)
        time.sleep(2)
        continue
    for i, it in enumerate(items, 1):
        t = (it.get("title") or ["?"])[0]
        au = it.get("author", [])
        a1 = au[0].get("family", "?") if au else "?"
        yr = (it.get("issued", {}).get("date-parts", [[None]])[0] or [None])[0]
        print(f"  [{i}] {it.get('DOI')}")
        print(f"      {t[:88]}")
        print(f"      {it.get('container-title',['?'])[0] if it.get('container-title') else '?'} | {yr} ;{it.get('volume','')}({it.get('issue','')}):{it.get('page','')} | {a1} et al | type={it.get('type')}")
    time.sleep(1.5)
