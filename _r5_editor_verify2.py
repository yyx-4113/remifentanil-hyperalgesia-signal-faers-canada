# -*- coding: utf-8 -*-
"""Round-5 主编复核 · 第二部分：队列重叠的年份定位 + 加拿大 VOMITING"""
import json, os, csv, urllib.request, urllib.error, time

API = "https://api.fda.gov/drug/event.json"
CACHE = "_r5_editor_cache.json"
cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

def total(search):
    key = f"{search}|1|None"
    if key not in cache:
        url = API + "?search=" + search.replace(" ", "%20") + "&limit=1"
        for _ in range(4):
            try:
                with urllib.request.urlopen(url, timeout=90) as r:
                    cache[key] = json.loads(r.read().decode("utf-8"))
                json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
                break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    cache[key] = {"results": []}
                    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
                    break
                time.sleep(3)
            except Exception:
                time.sleep(3)
    d = cache.get(key, {})
    return d.get("meta", {}).get("results", {}).get("total", 0)

REMI = '(patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL" OR patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL HYDROCHLORIDE")'
FEN  = 'patient.drug.activesubstance.activesubstancename.exact:"FENTANYL"'
SUF  = '(patient.drug.activesubstance.activesubstancename.exact:"SUFENTANIL" OR patient.drug.activesubstance.activesubstancename.exact:"SUFENTANIL CITRATE")'
MOR  = 'patient.drug.activesubstance.activesubstancename.exact:"MORPHINE"'
HA   = 'patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'

print("=" * 78)
print("【复核 3b】吗啡 HYPERAESTHESIA 按年（2024 簇是否四药共有）")
print("=" * 78)
for label, exp in [("MORPHINE", MOR), ("FENTANYL", FEN), ("SUFENTANIL", SUF), ("REMIFENTANIL", REMI)]:
    out = [f"{label:<14}"]
    for y in range(2015, 2026):
        out.append(f"{y}:{total(f'{exp} AND {HA} AND receivedate:[{y}0101+TO+{y}1231]')}")
    print("  ".join(out)); 
print()

print("=" * 78)
print("【复核 4】舒芬太尼 2024 年的 7 例是否就是瑞芬簇中带舒芬的那些条")
print("=" * 78)
a = total(f'{REMI} AND {HA} AND {SUF} AND receivedate:[20240101+TO+20241231]')
b = total(f'{SUF} AND {HA} AND receivedate:[20240101+TO+20241231]')
print(f"REMIFENTANIL ∧ SUFENTANIL ∧ HYPERAESTHESIA ∧ 2024 = {a}")
print(f"SUFENTANIL ∧ HYPERAESTHESIA ∧ 2024                = {b}")
print(f"→ 瑞芬簇占舒芬 2024 年 HYPERAESTHESIA 的比例 = {a}/{b} = {a/b*100 if b else 0:.1f}%")
c = total(f'{REMI} AND {HA} AND {FEN} AND receivedate:[20240101+TO+20241231]')
d = total(f'{FEN} AND {HA} AND receivedate:[20240101+TO+20241231]')
print(f"REMIFENTANIL ∧ FENTANYL   ∧ HYPERAESTHESIA ∧ 2024 = {c}")
print(f"FENTANYL ∧ HYPERAESTHESIA ∧ 2024                  = {d}")
print(f"→ 瑞芬簇占芬太尼 2024 年 HYPERAESTHESIA 的比例 = {c}/{d} = {c/d*100 if d else 0:.1f}%")
print()

print("=" * 78)
print("【复核 5】加拿大 VOMITING 可算性（A7 的 M1）——读作者源 CSV")
print("=" * 78)
p = "cv/cv_pt_summary.csv"
if os.path.exists(p):
    with open(p, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row.get("PT") in ("VOMITING", "NAUSEA", "PRURITUS", "CONSTIPATION", "PAIN", "HYPERAESTHESIA", "DRUG INEFFECTIVE"):
                print("  " + " | ".join(f"{k}={v}" for k, v in row.items() if v not in (None, "")))
else:
    print("  未找到 cv/cv_pt_summary.csv")
print()
print("DONE-2")
