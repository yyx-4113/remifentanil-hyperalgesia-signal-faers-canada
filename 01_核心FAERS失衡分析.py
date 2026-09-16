#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01 瑞芬太尼 OIH 信号 FAERS 头对头（核心四算法 + 头对头 RORR）
复用氯胺酮管线的 openFDA 缓存 + 退避机制；适配 4 药（瑞芬/芬太尼/舒芬/吗啡）
× OIH PT（窄/宽）+ 阴性对照 PT。
算法：ROR / PRR / IC(BCPNN) / EBGM(MGPS)。
输出：01_faers_results.csv + 标准输出摘要。
"""
import urllib.request, urllib.parse, json, time, math, os, csv
from _fda_auth import add_key

BASE = "https://api.fda.gov/drug/event.json"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_faers_cache.json")
SLEEP = 0.6
TRIES = 6

cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

def save():
    json.dump(cache, open(CACHE, "w", encoding="utf-8"))

def api_total(search):
    if search in cache and cache[search] is not None:
        return cache[search]
    q = urllib.parse.urlencode(add_key({"search": search, "limit": "1"}))
    for i in range(TRIES):
        try:
            with urllib.request.urlopen(f"{BASE}?{q}", timeout=30) as r:
                t = json.load(r).get("meta", {}).get("results", {}).get("total", 0)
            cache[search] = t; save(); time.sleep(SLEEP); return t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                try:
                    body = e.read().decode("utf-8", "ignore")
                except Exception:
                    body = ""
                if "No matches found" in body:
                    cache[search] = 0; save(); return 0
                back = min(15, 2 ** i * 2); time.sleep(back); continue
            if e.code in (403, 429):
                back = min(20, 2 ** i * 3); print(f"  [{e.code}] 限流退避{i+1}({back}s)"); time.sleep(back); continue
            time.sleep(3)
        except Exception as e:
            print(f"  [err] {type(e).__name__} {str(e)[:30]}"); time.sleep(3)
    cache[search] = None; save(); return None

def api_count_top(field, limit=1000):
    key = f"__TOP__{field}_{limit}"
    if key in cache:
        return cache[key]
    q = urllib.parse.urlencode(add_key({"count": field, "limit": str(limit)}))
    for i in range(TRIES):
        try:
            with urllib.request.urlopen(f"{BASE}?{q}", timeout=60) as r:
                res = json.load(r).get("results", [])
            cache[key] = res; save(); return res
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                back = min(30, 2 ** i * 5); print(f"  [count {e.code}] 退避{i+1}({back}s)"); time.sleep(back); continue
            print("top err:", e); return []
        except Exception as e:
            print("top err:", e); return []
    return []

DRUGS = {
 "REMIFENTANIL":'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")',
 "FENTANYL":'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")',
 "SUFENTANIL":'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")',
 "MORPHINE":'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")',
}
COMPARATORS = ["FENTANYL", "SUFENTANIL", "MORPHINE"]

PTS = [
 # (PT, category, SOC)
 ("HYPERALGESIA", "OIH-narrow", "Nervous system"),
 ("ALLODYNIA", "OIH-narrow", "Nervous system"),
 ("PAIN", "OIH-wide", "General"),
 ("PAIN INCREASED", "OIH-wide", "General"),
 ("DRUG INEFFECTIVE", "OIH-wide", "General"),
 ("OPIOID WITHDRAWAL SYNDROME", "OIH-wide", "Psychiatric"),
 ("DRUG TOLERANCE", "OIH-wide", "General"),
 ("POSTOPERATIVE PAIN", "OIH-wide", "General"),
 ("CHRONIC PAIN", "OIH-wide", "General"),
 ("NAUSEA", "negative-control", "Gastrointestinal"),
 ("VOMITING", "negative-control", "Gastrointestinal"),
 ("PRURITUS", "negative-control", "Skin"),
 ("CONSTIPATION", "negative-control", "Gastrointestinal"),
]

def lnCI(a, b, c, d):
    if min(a, b, c, d) <= 0:
        return (None, None)
    se = math.sqrt(1/a + 1/b + 1/c + 1/d)
    lor = math.log((a*d)/(b*c))
    return (math.exp(lor - 1.96*se), math.exp(lor + 1.96*se))

def metrics(a, drug_n, pt_n, N):
    if None in (a, drug_n, pt_n, N):
        return None
    b = drug_n - a; c = pt_n - a; d = N - a - b - c
    if b < 0 or c < 0 or d < 0:
        return None
    o = {"a": a, "b": b, "c": c, "d": d}
    if a > 0 and b > 0 and c > 0 and d > 0:
        ror = (a*d)/(b*c); lo, hi = lnCI(a, b, c, d)
        o["ROR"] = ror; o["ROR_lo"] = lo; o["ROR_hi"] = hi
        prr = (a/(a+b)) / (c/(c+d)); o["PRR"] = prr
        n = a+b+c+d; exp_a = (a+b)*(a+c)/n
        chi2 = (abs(a-exp_a)-0.5)**2/exp_a if exp_a > 0 else 0.0; o["chi2"] = chi2
        prr_se = math.sqrt((1/a)-(1/(a+b))+(1/c)-(1/(c+d)))
        o["PRR_lo"] = max(0.0, prr - 1.96*prr*prr_se); o["PRR_hi"] = prr + 1.96*prr*prr_se
        ic = math.log2((a*N)/((a+b)*(a+c)))
        var_ic = (1/a + 1/(a+b) + 1/(a+c) + 1/N)/(math.log(2)**2)
        ic025 = ic - 1.96*math.sqrt(var_ic); o["IC"] = ic; o["IC025"] = ic025
        o["signal"] = (a >= 3 and lo is not None and lo > 1) or (prr >= 2 and chi2 >= 4) or (ic025 > 0)
    else:
        o["ROR"] = o["PRR"] = o["IC"] = None; o["signal"] = False
    return o

print("== 01 瑞芬太尼 OIH FAERS 头对头 核心失衡 ==")
N = api_total('patient.reaction.reactionmeddrapt:[* TO *]')
print("总报告数 N =", N)
drug_n = {}
for name, s in DRUGS.items():
    drug_n[name] = api_total(s); print(f"  {name} 报告数 = {drug_n[name]}")

top = api_count_top("patient.reaction.reactionmeddrapt.exact", 1000)
counts = [x["count"] for x in top if x["count"] > 0]
if counts:
    mu = sum(counts)/len(counts); var = sum((x-mu)**2 for x in counts)/len(counts)
    alpha = mu**2/var if var > 0 else 0.5; beta = mu/var if var > 0 else 1.0
else:
    alpha, beta = 0.5, 1.0
print(f"EBGM 先验 Gamma alpha={alpha:.3f} beta={beta:.5f}")

def se_logror(m):
    return math.sqrt(1/m["a"] + 1/m["b"] + 1/m["c"] + 1/m["d"])

def rorr_pair(remi, comp):
    if not (remi and comp and remi.get("ROR") and comp.get("ROR")):
        return (None, None, None)
    rr = remi["ROR"]/comp["ROR"]; sel = se_logror(remi); sek = se_logror(comp)
    se = math.sqrt(sel**2 + sek**2); ln = math.log(rr)
    return (rr, math.exp(ln - 1.96*se), math.exp(ln + 1.96*se))

rows = []
for pt, cat, soc in PTS:
    pt_n = api_total(f'patient.reaction.reactionmeddrapt.exact:"{pt}"')
    m = {}
    for name, s in DRUGS.items():
        a = api_total(f'{s} AND patient.reaction.reactionmeddrapt.exact:"{pt}"')
        mm = metrics(a, drug_n[name], pt_n, N)
        if mm and mm.get("ROR") is not None and pt_n:
            E = drug_n[name]*pt_n/N; mean = (a+alpha)/(E+beta)
            mm["EBGM"] = mean; mm["EB05"] = max(0.0, mean - 1.645*math.sqrt((a+alpha)/((E+beta)**2)))
        m[name] = mm
    row = {"PT": pt, "category": cat, "SOC": soc, "PT_total": pt_n}
    for name in DRUGS:
        mm = m[name]
        row[f"{name}_a"] = mm["a"] if mm else None
        row[f"{name}_ROR"] = round(mm["ROR"], 3) if mm and mm.get("ROR") else ""
        row[f"{name}_ROR_CI"] = (f'{mm["ROR_lo"]:.2f}-{mm["ROR_hi"]:.2f}') if mm and mm.get("ROR_lo") else ""
        row[f"{name}_PRR"] = round(mm["PRR"], 3) if mm and mm.get("PRR") else ""
        row[f"{name}_IC025"] = round(mm["IC025"], 3) if mm and mm.get("IC025") is not None else ""
        row[f"{name}_EBGM"] = round(mm["EBGM"], 3) if mm and mm.get("EBGM") else ""
        row[f"{name}_signal"] = mm.get("signal") if mm else False
    for comp in COMPARATORS:
        rr, lo, hi = rorr_pair(m["REMIFENTANIL"], m[comp])
        row[f"RORR_REMI_vs_{comp}"] = round(rr, 3) if rr else ""
        row[f"RORR_CI_{comp}"] = (f'{lo:.2f}-{hi:.2f}') if lo and hi else ""
    rows.append(row)
    remi_ror = m["REMIFENTANIL"]["ROR"] if m["REMIFENTANIL"] and m["REMIFENTANIL"].get("ROR") else None
    print(f"  {pt:28s} cat={cat:14s} REMI_a={row['REMIFENTANIL_a']} ROR={remi_ror}")

out = os.path.join(HERE, "01_faers_results.csv")
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
save()
print("\n写出:", out)
print("N=%d  REMI=%d FENTA=%d SUFEN=%d MORPH=%d  alpha=%.3f beta=%.5f" % (
    N, drug_n["REMIFENTANIL"], drug_n["FENTANYL"], drug_n["SUFENTANIL"], drug_n["MORPHINE"], alpha, beta))
