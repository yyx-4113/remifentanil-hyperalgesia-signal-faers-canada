# -*- coding: utf-8 -*-
"""A5：用 openFDA count 端点一次性取回每药×每层的全部 PT 计数（每个组合仅 2 个请求）。"""
import json, os, time, math, urllib.request, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_a5_strat_cache.json")
BASE = "https://api.fda.gov/drug/event.json"
DRUG = {
 "REMIFENTANIL": 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
 "FENTANYL":     'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
 "SUFENTANIL":   'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
 "MORPHINE":     'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")',
}
PTS = ["PAIN","HYPERAESTHESIA","DRUG INEFFECTIVE","NAUSEA","VOMITING","PRURITUS",
       "CONSTIPATION","PROCEDURAL PAIN","DRUG TOLERANCE","ALLODYNIA","DRUG WITHDRAWAL SYNDROME"]
STRATA = {
 "physician": "primarysource.qualification:1",
 "other_hp":  "primarysource.qualification:3",
 "consumer":  "primarysource.qualification:5",
 "age_18_64": 'patient.patientonsetage:[18 TO 64] AND patient.patientonsetageunit:801',
 "age_ge65":  'patient.patientonsetage:[65 TO 120] AND patient.patientonsetageunit:801',
 "age_lt18":  'patient.patientonsetage:[0 TO 17] AND patient.patientonsetageunit:801',
}
cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

def call(search, count=None):
    key = search + ("||C=" + count if count else "")
    if key in cache: return cache[key]
    p = {"search": search, "limit": 1000 if count else 1}
    if count: p["count"] = count
    url = BASE + "?" + urllib.parse.urlencode(p)
    for a in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                d = json.loads(r.read().decode())
            val = ({x["term"]: x["count"] for x in d.get("results", [])} if count
                   else d["meta"]["results"]["total"])
            cache[key] = val; json.dump(cache, open(CACHE,"w",encoding="utf-8"), ensure_ascii=False)
            return val
        except urllib.error.HTTPError as e:
            if e.code == 404:
                cache[key] = {} if count else 0
                json.dump(cache, open(CACHE,"w",encoding="utf-8"), ensure_ascii=False); return cache[key]
            time.sleep(3)
        except Exception:
            time.sleep(3)
    return None

res = {"totals": {}, "a": {}}
for s, f in STRATA.items():
    res["totals"][s] = {}; res["a"][s] = {}
    for d, dq in DRUG.items():
        sstr = dq + " AND " + f
        res["totals"][s][d] = call(sstr)
        cnt = call(sstr, "patient.reaction.reactionmeddrapt.exact") or {}
        res["a"][s][d] = {pt: cnt.get(pt, 0) for pt in PTS}
        print("OK", s, d, res["totals"][s][d], flush=True)

# 补 all 层（缓存里可能只有 a，用同一方式重取以便统一）
res["totals"]["all"] = {}; res["a"]["all"] = {}
for d, dq in DRUG.items():
    res["totals"]["all"][d] = call(dq)
    cnt = call(dq, "patient.reaction.reactionmeddrapt.exact") or {}
    res["a"]["all"][d] = {pt: cnt.get(pt, 0) for pt in PTS}

def rr(s, pt, comp):
    try:
        ar, tr = res["a"][s]["REMIFENTANIL"][pt], res["totals"][s]["REMIFENTANIL"]
        ac, tc = res["a"][s][comp][pt],            res["totals"][s][comp]
        br, bc = tr-ar, tc-ac
        if min(ar,ac,br,bc) <= 0: return None
        lr = (ar*bc)/(br*ac); se = (1/ar+1/br+1/ac+1/bc)**.5
        return (round(lr,3), round(math.exp(math.log(lr)-1.96*se),3), round(math.exp(math.log(lr)+1.96*se),3))
    except Exception: return None

print("\n=== FAERS 分层内 RORR(remifentanil/对照) ===")
for s in res["totals"]:
    print("\n## %s  totals=%s" % (s, res["totals"][s]))
    for pt in PTS:
        print("  %-24s a_r=%-4s a_fen=%-5s a_mor=%-5s a_suf=%-4s | FEN=%-20s MOR=%-20s SUF=%s" % (
            pt, res["a"][s]["REMIFENTANIL"][pt], res["a"][s]["FENTANYL"][pt],
            res["a"][s]["MORPHINE"][pt], res["a"][s]["SUFENTANIL"][pt],
            rr(s,pt,"FENTANYL"), rr(s,pt,"MORPHINE"), rr(s,pt,"SUFENTANIL")))
json.dump(res, open(os.path.join(HERE,"_a5_strat2_results.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
