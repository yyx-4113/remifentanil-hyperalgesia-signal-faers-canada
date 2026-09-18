# -*- coding: utf-8 -*-
"""
Round-5 主编独立复核：对七份意见中"最严重"的三条发现做一手验证。
不复用作者任何中间产物，直接查 openFDA 与加拿大原始 line-listing。
"""
import json, os, sys, urllib.request, urllib.error, time

API = "https://api.fda.gov/drug/event.json"
CACHE = "_r5_editor_cache.json"
cache = {}
if os.path.exists(CACHE):
    cache = json.load(open(CACHE, encoding="utf-8"))

def q(search, limit=1, count=None, retries=3):
    """search 中的空格替成 %20，保留字面 + （否则 500）"""
    key = f"{search}|{limit}|{count}"
    if key in cache:
        return cache[key]
    parts = [f"search={search.replace(' ', '%20')}", f"limit={limit}"]
    if count:
        parts.append(f"count={count}")
    url = API + "?" + "&".join(parts)
    last = None
    for _ in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                out = json.loads(r.read().decode("utf-8"))
            cache[key] = out
            json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
            return out
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code == 404:
                cache[key] = {"results": []}
                json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
                return {"results": []}
            time.sleep(2)
        except Exception as e:
            last = str(e); time.sleep(2)
    return {"error": last, "results": []}

def total(search):
    d = q(search, limit=1)
    if "error" in d: return None
    return d.get("meta", {}).get("results", {}).get("total", 0)

def records(search, limit=100):
    return q(search, limit=limit).get("results", [])

REMI = '(patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL" OR patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL HYDROCHLORIDE")'
FEN  = 'patient.drug.activesubstance.activesubstancename.exact:"FENTANYL"'
SUF  = '(patient.drug.activesubstance.activesubstancename.exact:"SUFENTANIL" OR patient.drug.activesubstance.activesubstancename.exact:"SUFENTANIL CITRATE")'
MOR  = 'patient.drug.activesubstance.activesubstancename.exact:"MORPHINE"'
HA   = 'patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'

print("=" * 78)
print("【复核 1】HYPERAESTHESIA 在瑞芬太尼队列中的报告（a=10 的构成）")
print("=" * 78)

# 1a. 分盐型计数（验证 a=10 由 REMI 7 + HCL 3 构成）
r_pure = total(f'(patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL") AND {HA}')
r_hcl  = total(f'(patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL HYDROCHLORIDE") AND {HA}')
print(f"REMIFENTANIL              AND HYPERAESTHESIA = {r_pure}")
print(f"REMIFENTANIL HYDROCHLORIDE AND HYPERAESTHESIA = {r_hcl}")
print(f"合计 = {(r_pure or 0) + (r_hcl or 0)}  （稿件 a=10）")
print()

# 1b. 逐条打印（关键：看是不是同一病例簇）
recs = records(f"{REMI} AND {HA}", limit=100)
print(f"逐条明细（返回 {len(recs)} 条）:")
print()
hdr = f"{'safetyreportid':<14}{'ver':<4}{'receivedate':<11}{'country':<12}{'age':<5}{'sex':<4}{'qual':<5}{'#drug':<6}{'#react':<7}"
print(hdr); print("-" * len(hdr))
rows = []
for e in sorted(recs, key=lambda x: str(x.get("receivedate", ""))):
    p = e.get("patient", {})
    age = p.get("patientonsetage", "?")
    sex = {0: "?", 1: "M", 2: "F"}.get(p.get("patientsex"), "?")
    qual = e.get("primarysource", {}).get("qualification", "?")
    drugs = p.get("drug", [])
    reacts = p.get("reaction", [])
    print(f"{e.get('safetyreportid',''):<14}"
          f"{e.get('safetyreportversion',''):<4}"
          f"{str(e.get('receivedate','')):<11}"
          f"{str(e.get('occurcountry','')):<12}"
          f"{str(age):<5}{sex:<4}{str(qual):<5}{len(drugs):<6}{len(reacts):<7}")
    names = sorted({d.get("medicinalproduct", "?").strip().lower() for d in drugs})
    rows.append((e.get("safetyreportid"), e.get("receivedate"), e.get("safetyreportversion"), names))

print()
print("各条报告的全部药品名（用于判断是否同一配伍）:")
for sid, rd, v, names in rows:
    print(f"  {sid} ({rd}, v{v}): {', '.join(names)}")

print()
print("=" * 78)
print("【复核 2】队列重叠：HYPERAESTHESIA 的瑞芬报告中有多少同时含其它阿片")
print("=" * 78)
for label, other in [("FENTANYL", FEN), ("SUFENTANIL (incl. citrate)", SUF), ("MORPHINE", MOR)]:
    n = total(f"{REMI} AND {HA} AND {other}")
    print(f"REMI AND HYPERAESTHESIA AND {label} = {n}")

print()
print("=" * 78)
print("【复核 3】2024 年簇：各药 HYPERAESTHESIA 按年计数（验证 2024-簇不是瑞芬特有）")
print("=" * 78)
for label, exp in [("REMIFENTANIL", REMI), ("FENTANYL", FEN), ("SUFENTANIL", SUF), ("MORPHINE", MOR)]:
    line = [f"{label:<14}"]
    for y in range(2015, 2026):
        n = total(f'{exp} AND {HA} AND receivedate:[{y}0101+TO+{y}1231]')
        line.append(f"{y}:{n}")
    print("  ".join(line))

print()
print("=" * 78)
print("【复核 4】SUFENTANIL 2024 年 HYPERAESTHESIA = 7 是否就是瑞芬簇中带舒芬的那些条")
print("=" * 78)
n_both_2024 = total(f'{REMI} AND {HA} AND {SUF} AND receivedate:[20240101+TO+20241231]')
n_suf_2024  = total(f'{SUF} AND {HA} AND receivedate:[20240101+TO+20241231]')
print(f"REMI AND SUF AND HYPERAESTHESIA 且 2024 年 = {n_both_2024}")
print(f"SUF AND HYPERAESTHESIA 且 2024 年          = {n_suf_2024}")
print(f"→ 重合比例 = {n_both_2024}/{n_suf_2024}")

print()
print("=" * 78)
print("【复核 5】阴性对照 VOMITING 在加拿大是否可算（A7 的 M1）")
print("=" * 78)
import csv
cv = "cv/cv_pt_summary.csv"
if os.path.exists(cv):
    with open(cv, encoding="utf-8") as f:
        rd = list(csv.DictReader(f))
    for row in rd:
        if row.get("PT") in ("VOMITING", "PAIN", "HYPERAESTHESIA", "DRUG INEFFECTIVE"):
            print("  " + "  ".join(f"{k}={v}" for k, v in row.items() if v))
else:
    print("  (cv_pt_summary.csv 未找到)")
print()
print("DONE")
