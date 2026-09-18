# -*- coding: utf-8 -*-
"""Round-5 主编复核 · 第三部分：2024 簇的跨药归属 + 加拿大 VOMITING（跳过慢查询）"""
import json, os, csv, urllib.request, urllib.error, time

API = "https://api.fda.gov/drug/event.json"
CACHE = "_r5_editor_cache.json"
cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

def total(search):
    key = f"{search}|1|None"
    if key not in cache:
        url = API + "?search=" + search.replace(" ", "%20") + "&limit=1"
        for _ in range(3):
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    cache[key] = json.loads(r.read().decode("utf-8"))
                json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
                break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    cache[key] = {"results": []}
                    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
                    break
                time.sleep(2)
            except Exception:
                time.sleep(2)
    return cache.get(key, {}).get("meta", {}).get("results", {}).get("total", 0)

REMI = '(patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL" OR patient.drug.activesubstance.activesubstancename.exact:"REMIFENTANIL HYDROCHLORIDE")'
FEN  = 'patient.drug.activesubstance.activesubstancename.exact:"FENTANYL"'
SUF  = '(patient.drug.activesubstance.activesubstancename.exact:"SUFENTANIL" OR patient.drug.activesubstance.activesubstancename.exact:"SUFENTANIL CITRATE")'
HA   = 'patient.reaction.reactionmeddrapt.exact:"HYPERAESTHESIA"'
Y24  = 'receivedate:[20240101+TO+20241231]'

print("=" * 78)
print("【复核 4】2024 年 HYPERAESTHESIA 的跨药归属")
print("=" * 78)
a_suf = total(f'{REMI} AND {SUF} AND {HA} AND {Y24}')
b_suf = total(f'{SUF} AND {HA} AND {Y24}')
print(f"REMIFENTANIL ∧ SUFENTANIL ∧ HYPERAESTHESIA ∧ 2024 = {a_suf}")
print(f"SUFENTANIL   ∧ HYPERAESTHESIA ∧ 2024               = {b_suf}")
print(f"→ 瑞芬簇占舒芬 2024 年 HYPERAESTHESIA = {a_suf}/{b_suf}")
print()
a_fen = total(f'{REMI} AND {FEN} AND {HA} AND {Y24}')
b_fen = total(f'{FEN} AND {HA} AND {Y24}')
print(f"REMIFENTANIL ∧ FENTANYL ∧ HYPERAESTHESIA ∧ 2024 = {a_fen}")
print(f"FENTANYL     ∧ HYPERAESTHESIA ∧ 2024            = {b_fen}")
print(f"→ 瑞芬簇占芬太尼 2024 年 HYPERAESTHESIA = {a_fen}/{b_fen}")
print()
# 同一簇内的两条带 fentanyl citrate / sufentanil citrate 的盐型是否也从"盐型"被漏计
print("盐型敏感性（稿件 cohort = name==target OR startswith(target+' ')，故盐型独立计入）：")
print(f"  FENTANYL ∧ HYPERAESTHESIA ∧ 2024（不含 CITRATE 盐型）     = {total(f'patient.drug.activesubstance.activesubstancename.exact:\"FENTANYL\" AND {HA} AND {Y24}')}")
print()

print("=" * 78)
print("【复核 5】加拿大 VOMITING 可算性（A7 的 M1）——读作者源 CSV")
print("=" * 78)
p = "cv/cv_pt_summary.csv"
if os.path.exists(p):
    with open(p, encoding="utf-8-sig") as f:
        rdr = csv.DictReader(f)
        cols = rdr.fieldnames
        print("列名:", cols)
        for row in rdr:
            if row.get("PT") in ("VOMITING", "NAUSEA", "PRURITUS", "CONSTIPATION", "PAIN", "HYPERAESTHESIA", "DRUG INEFFECTIVE"):
                print("  " + " | ".join(f"{k}={v}" for k, v in row.items() if v not in (None, "")))
else:
    print("  未找到 cv/cv_pt_summary.csv")
print()
print("DONE-3")
