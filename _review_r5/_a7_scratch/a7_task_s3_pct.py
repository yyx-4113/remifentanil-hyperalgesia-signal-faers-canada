# -*- coding: utf-8 -*-
"""A7 补充：Table S3 全部百分比逐格 = 稿件显示值 vs n/队列（独立算），并列全部原始分数。"""
import csv, os, re, decimal
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
N = {"REMIFENTANIL": 111, "FENTANYL": 4881, "SUFENTANIL": 63, "MORPHINE": 7675}
sub = {}
for r in csv.DictReader(open(os.path.join(ROOT, "cv", "cv_subgroups.csv"), encoding="utf-8-sig")):
    sub[(r["Drug"], r["Category"], r["Value"])] = (int(r["Count"]), float(r["Pct_of_drug"]))
ROWS = [
    ("Serious report", "serious", "Serious"),
    ("Reporter: other health professional", "reporter", "Other health professional"),
    ("Reporter: physician", "reporter", "Physician"),
    ("Reporter: consumer or other non-health professional", "reporter", "Consumer/other non health professional"),
    ("Reporter: lawyer", "reporter", "Lawyer"),
    ("Reporter: not stated", "reporter", ""),
    ("Age 18-64", "age", "18-64"),
    ("Age <18", "age", "<18"),
    ("Age >=65", "age", ">=65"),
    ("Age not stated", "age", "unk"),
    ("Female", "gender", "Female"),
    ("Male", "gender", "Male"),
    ("Sex not stated", "gender", ""),
]
def rhu(x, d):
    return float(decimal.Decimal(repr(x)).quantize(decimal.Decimal('1.' + '0'*d), rounding=decimal.ROUND_HALF_UP))
# 稿件 Table S3 原文解析
text = open(os.path.join(ROOT, "I_正文_IMRaD_en.md"), encoding="utf-8").read()
i = text.index("### Table S3 (supplementary). Canada Vigilance cohorts")
j = text.index("### Table S4 (supplementary)")
shown = {}
for line in text[i:j].splitlines():
    line = line.strip()
    if not line.startswith("|"): continue
    c = [x.strip() for x in line.strip("|").split("|")]
    if set("".join(c)) <= set("-: "): continue
    if c[0].startswith("Characteristic"): continue
    for k, drug in enumerate(["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"], start=1):
        m = re.match(r"^(\d+)\s*\(([\d.]+)\)$", c[k].replace("\u2009", "").replace(" ", ""))
        if m: shown[(c[0], drug)] = (int(m.group(1)), float(m.group(2)))
        else: shown[(c[0], drug)] = (int(re.sub(r"\D", "", c[k]) or 0), None)

print("%-56s %-12s %6s %6s %9s %8s %8s %s" % ("Table S3 行", "药物", "稿件n", "源n", "n/队列%", "正确1位", "稿件pct", "判定"))
bad = []
for label, cat, val in ROWS:
    for drug in ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]:
        src = sub.get((drug, cat, val))
        srcn = src[0] if src else 0
        sn, sp = shown.get((label, drug), (None, None))
        indep = 100.0 * srcn / N[drug]
        good = rhu(indep, 1)
        verdict = "OK"
        if sn != srcn: verdict = "n不同"
        if sp is not None and abs(good - sp) > 1e-9:
            verdict = "pct错:应%.1f" % good; bad.append((label, drug, sn, indep, good, sp))
        print("%-56s %-12s %6s %6d %9.4f %8.1f %8s %s"
              % (label[:56], drug, sn, srcn, indep, good, ("%.1f" % sp) if sp is not None else "-", verdict))
print("\nTable S3 百分比错误条目：")
for b in bad:
    print("   %s / %s : 稿件 %.1f ，n=%d / 队列 → %.4f%% → 正确值 %.1f" % (b[0], b[1], b[5], b[2], b[3], b[4]))
print("合计 %d 条" % len(bad))
