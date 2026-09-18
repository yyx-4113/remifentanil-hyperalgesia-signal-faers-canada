# -*- coding: utf-8 -*-
"""A5：负对照暴露（negative-control exposure）分析。
问题：作者说“差异来自用药场景/适应证，而非药理”。若如此，瑞芬太尼对同一场景下的
非阿片类围术期药物（丙泊酚/咪达唑仑/氯胺酮/罗库溴铵）也应同样低报 PAIN。
若只对阿片类低报，则“场景/适应证”不足以解释。
输出：每种对照药 PAIN 的 a、总报告数，以及 remifentanil/该药的 PAIN RORR。
"""
import json, os, time, math, urllib.request, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_a5_nce_cache.json")
BASE = "https://api.fda.gov/drug/event.json"
cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

def call(search, count=None):
    key = search + ("||C=" + count if count else "")
    if key in cache: return cache[key]
    p = {"search": search, "limit": 1000 if count else 1}
    if count: p["count"] = count
    url = BASE + "?" + urllib.parse.urlencode(p)
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                d = json.loads(r.read().decode())
            val = ({x["term"]: x["count"] for x in d.get("results", [])} if count
                   else d["meta"]["results"]["total"])
            cache[key] = val; json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
            return val
        except urllib.error.HTTPError as e:
            if e.code == 404:
                cache[key] = 0; json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False); return 0
            time.sleep(4)
        except Exception:
            time.sleep(4)
    return None

def dq(name):
    return 'patient.drug.activesubstance.activesubstancename.exact:("%s")' % name

DRUGS = ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE",
         "PROPOFOL", "MIDAZOLAM", "KETAMINE", "ROCURONIUM", "VECURONIUM", "SEVOFLURANE"]
tot, pain = {}, {}
for d in DRUGS:
    tot[d] = call(dq(d))
    cnt = call(dq(d), "patient.reaction.reactionmeddrapt.exact") or {}
    pain[d] = cnt.get("PAIN", 0) if isinstance(cnt, dict) else 0
    print("%-12s total=%-8s PAIN=%-6s (%.2f%%)" % (d, tot[d], pain[d],
          100.0 * pain[d] / tot[d] if tot[d] else float("nan")), flush=True)

print("\n=== remifentanil 对各药的 PAIN 头对头比值（层内=全体报告）===")
for d in DRUGS:
    if d == "REMIFENTANIL": continue
    ar, tr, ac, tc = pain["REMIFENTANIL"], tot["REMIFENTANIL"], pain[d], tot[d]
    if min(ar, ac, tr - ar, tc - ac) <= 0:
        print("  vs %-12s 不可算 (a_r=%s a_c=%s)" % (d, ar, ac)); continue
    br, bc = tr - ar, tc - ac
    lr = (ar * bc) / (br * ac)
    se = (1/ar + 1/br + 1/ac + 1/bc) ** 0.5
    print("  vs %-12s %.3f (95%%CI %.3f-%.3f)  a_r=%d a_c=%d" % (
        d, lr, math.exp(math.log(lr) - 1.96 * se), math.exp(math.log(lr) + 1.96 * se), ar, ac))
