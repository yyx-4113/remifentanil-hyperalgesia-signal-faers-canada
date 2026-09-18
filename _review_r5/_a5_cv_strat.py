# -*- coding: utf-8 -*-
"""A5 独立复核（加拿大侧）：把“报告者类型”当作分层变量，直接在层内算 RORR。
复刻 cv/cv_process.py 的解析口径，不改变其任何定义，只增加分层。
输出：_a5_cv_strat.json / 控制台表格
"""
import csv, os, json, sys
from collections import Counter, defaultdict

ROOT = r"D:/2026.9/极速交付9月会员日优惠套路/06_FAERS单药物SOC分类安全性评估/瑞芬太尼"
DATA = os.path.join(ROOT, "cv", "cvponline_extract_20241130")
N = 1154017

TARGETS = {"REMIFENTANIL": "remifentanil", "FENTANYL": "fentanyl",
           "SUFENTANIL": "sufentanil", "MORPHINE": "morphine"}
PTS = ["HYPERALGESIA", "ALLODYNIA", "PAIN", "PAIN INCREASED", "DRUG INEFFECTIVE",
       "OPIOID WITHDRAWAL SYNDROME", "DRUG TOLERANCE", "POSTOPERATIVE PAIN",
       "CHRONIC PAIN", "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION",
       "HYPERAESTHESIA", "HYPERPATHIA", "PROCEDURAL PAIN", "CHRONIC PAIN SYNDROME",
       "DRUG WITHDRAWAL SYNDROME"]

def match(name, t):
    n = name.strip().lower()
    return n == t or n.startswith(t + " ")

def log(*a):
    print(*a, flush=True)

def age_band(age, unit):
    try: v = float(age)
    except Exception: return "unk"
    if unit.strip().lower() not in ("years", "années", "year", "an"): return "unk"
    if v < 18: return "<18"
    if v < 65: return "18-64"
    return ">=65"

# pass1
prod2target = {}
with open(os.path.join(DATA, "drug_product_ingredients.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5: continue
        pid, nm = row[1].strip(), row[4].strip()
        for t, tgt in TARGETS.items():
            if match(nm, tgt):
                prod2target.setdefault(pid, set()).add(t)

# pass2
tgt_reports = {t: set() for t in TARGETS}
with open(os.path.join(DATA, "report_drug.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5: continue
        if row[4].strip() != "Suspect": continue
        ts = prod2target.get(row[2].strip())
        if ts:
            for t in ts: tgt_reports[t].add(row[1].strip())
for t in TARGETS: log("cohort", t, len(tgt_reports[t]))

# pass3: reporter / age / sex per report
rep_reporter, rep_age, rep_sex = {}, {}, {}
with open(os.path.join(DATA, "reports.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 40: continue
        rid = row[0].strip()
        rep_reporter[rid] = row[34].strip()
        rep_age[rid] = age_band(row[12].strip(), row[14].strip())
        rep_sex[rid] = row[10].strip()
log("reports parsed")

# pass4: reactions
glob_pt = {p: set() for p in PTS}
tpt = {t: {p: set() for p in PTS} for t in TARGETS}
with open(os.path.join(DATA, "reactions.txt"), encoding="utf-8",
          errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 8: continue
        rid = row[1].strip()
        pt = (row[5].strip() or "").upper()
        if pt in glob_pt: glob_pt[pt].add(rid)
        for t in TARGETS:
            if rid in tgt_reports[t] and pt in tpt[t]:
                tpt[t][pt].add(rid)
log("reactions parsed")

STRATA = {
    "ALL":        lambda r: True,
    "physician":  lambda r: rep_reporter.get(r, "") == "Physician",
    "other_hp":   lambda r: rep_reporter.get(r, "") == "Other health professional",
    "consumer":   lambda r: rep_reporter.get(r, "") == "Consumer/other non health professional",
    "age_18_64":  lambda r: rep_age.get(r, "unk") == "18-64",
    "age_lt18":   lambda r: rep_age.get(r, "unk") == "<18",
    "age_ge65":   lambda r: rep_age.get(r, "unk") == ">=65",
    "female":     lambda r: rep_sex.get(r, "") == "Female",
    "male":       lambda r: rep_sex.get(r, "") == "Male",
}

out = {"totals": {}, "a": {}}
for sname, pred in STRATA.items():
    out["totals"][sname] = {t: sum(1 for r in tgt_reports[t] if pred(r)) for t in TARGETS}
    out["a"][sname] = {t: {p: sum(1 for r in tpt[t][p] if pred(r)) for p in PTS} for t in TARGETS}

import math
def rr(s, pt, comp):
    a_r = out["a"][s]["REMIFENTANIL"][pt]; t_r = out["totals"][s]["REMIFENTANIL"]
    a_c = out["a"][s][comp][pt];            t_c = out["totals"][s][comp]
    b_r, b_c = t_r - a_r, t_c - a_c
    if min(a_r, a_c, b_r, b_c) <= 0: return None
    lr = (a_r * b_c) / (b_r * a_c)
    se = (1/a_r + 1/b_r + 1/a_c + 1/b_c) ** 0.5
    return (round(lr, 3), round(math.exp(math.log(lr)-1.96*se), 3), round(math.exp(math.log(lr)+1.96*se), 3))

log("\n=== 加拿大：分层内 RORR(remifentanil/对照) ===")
for s in STRATA:
    log("-- stratum %s   totals: %s" % (s, out["totals"][s]))
    for pt in PTS:
        line = []
        for comp in ("FENTANYL", "MORPHINE", "SUFENTANIL"):
            line.append("%s=%s" % (comp[:3], rr(s, pt, comp)))
        log("   %-24s a_remi=%-3s a_fen=%-4s %s" % (
            pt, out["a"][s]["REMIFENTANIL"][pt], out["a"][s]["FENTANYL"][pt], " | ".join(line)))

json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "_a5_cv_strat.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
log("done")
