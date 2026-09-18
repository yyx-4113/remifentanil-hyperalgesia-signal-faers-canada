# -*- coding: utf-8 -*-
"""A5 独立复核：FAERS 侧按报告者类型 / 年龄段 / 性别分层，直接计算 RORR。
所有查询走 openFDA，与作者主分析同一接口、同一药物字符串。结果写入 _a5_strat_cache.json。
"""
import json, os, time, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_a5_strat_cache.json")
BASE = "https://api.fda.gov/drug/event.json"

DRUG = {
    "REMIFENTANIL": 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
    "FENTANYL":     'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
    "SUFENTANIL":   'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
    "MORPHINE":     'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")',
}
PTS = ["PAIN", "HYPERAESTHESIA", "DRUG INEFFECTIVE", "NAUSEA", "VOMITING",
       "PRURITUS", "CONSTIPATION", "PROCEDURAL PAIN", "DRUG TOLERANCE"]

STRATA = {
    "all": None,
    "physician": "primarysource.qualification:1",
    "pharmacist": "primarysource.qualification:2",
    "other_hp": "primarysource.qualification:3",
    "consumer": "primarysource.qualification:5",
    "age_18_64": 'patient.patientonsetage:[18 TO 64] AND patient.patientonsetageunit:801',
    "age_ge65": 'patient.patientonsetage:[65 TO 120] AND patient.patientonsetageunit:801',
    "age_lt18": 'patient.patientonsetage:[0 TO 17] AND patient.patientonsetageunit:801',
    "male": "patient.patientsex:1",
    "female": "patient.patientsex:2",
}

cache = {}
if os.path.exists(CACHE):
    cache = json.load(open(CACHE, encoding="utf-8"))

def get(search, count=None):
    key = search + ("||COUNT=" + count if count else "")
    if key in cache:
        return cache[key]
    p = {"search": search, "limit": 1}
    if count:
        p["count"] = count
    url = BASE + "?" + urllib.parse.urlencode(p)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=45) as r:
                d = json.loads(r.read().decode())
            if count:
                val = {x["term"]: x["count"] for x in d.get("results", [])}
            else:
                val = d["meta"]["results"]["total"]
            cache[key] = val
            json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
            time.sleep(0.25)
            return val
        except urllib.error.HTTPError as e:
            if e.code == 404:      # openFDA 的“零匹配”语义
                val = {} if count else 0
                cache[key] = val
                json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
                return val
            time.sleep(2 + 3 * attempt)
        except Exception:
            time.sleep(2 + 3 * attempt)
    return None

# 1) 各药在各层的总报告数
tot = {}
for s, filt in STRATA.items():
    tot[s] = {}
    for d, dq in DRUG.items():
        search = dq if filt is None else dq + " AND " + filt
        tot[s][d] = get(search)
        print("TOTAL", s, d, tot[s][d], flush=True)

# 2) 各药×各层×各 PT 的 a 值
a = {}
for s, filt in STRATA.items():
    a[s] = {}
    for d, dq in DRUG.items():
        a[s][d] = {}
        for pt in PTS:
            search = dq + ' AND patient.reaction.reactionmeddrapt.exact:"%s"' % pt
            if filt:
                search += " AND " + filt
            a[s][d][pt] = get(search)
        print("A done", s, d, a[s][d], flush=True)

out = {"totals": tot, "a": a}
json.dump(out, open(os.path.join(HERE, "_a5_strat_results.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

def rorr(s, pt, comp="FENTANYL"):
    try:
        a_r = a[s]["REMIFENTANIL"][pt]; t_r = tot[s]["REMIFENTANIL"]
        a_c = a[s][comp][pt];          t_c = tot[s][comp]
        if a_r is None or a_c is None or t_r is None or t_c is None:
            return None
        b_r = t_r - a_r; b_c = t_c - a_c
        if a_r <= 0 or a_c <= 0 or b_r <= 0 or b_c <= 0:
            return None
        lr = (a_r * b_c) / (b_r * a_c)
        se = (1/a_r + 1/b_r + 1/a_c + 1/b_c) ** 0.5
        import math
        return (round(lr, 3), round(math.exp(math.log(lr) - 1.96*se), 3),
                round(math.exp(math.log(lr) + 1.96*se), 3))
    except Exception:
        return None

print("\n=== 分层 RORR（reminfentanil / comparator）===")
print("stratum | PT | vs FEN | vs MOR | vs SUF | a_remi (t_remi)")
for s in STRATA:
    for pt in PTS:
        rf = rorr(s, pt, "FENTANYL"); rm = rorr(s, pt, "MORPHINE"); rs = rorr(s, pt, "SUFENTANIL")
        print("%-11s | %-18s | %-22s | %-22s | %-22s | a=%s (t=%s)" % (
            s, pt, rf, rm, rs, a[s]["REMIFENTANIL"][pt], tot[s]["REMIFENTANIL"]))
