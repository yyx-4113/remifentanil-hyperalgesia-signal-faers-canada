# -*- coding: utf-8 -*-
"""A7 任务5b：完全独立的加拿大原始数据重算（不复用作者任何中间结果）。
目标：
  (1) 各药 Suspect 队列报告数（111 / 4 881 / 63 / 7 675）
  (2) reporter 字段分药计数 —— 检验 Table S3 中"Other health professional"在芬太尼与吗啡两列都是 2 056
      是真巧合还是复制错误
  (3) 4 个抽查 SOC 的 report-level 计数与全体 c（全球该 SOC 报告数），用于独立复核 Table S1 Panel A 的 ROR
  (4) 阴性对照 VOMITING 的分药计数（用于 §5 结论"四个阴性对照在加拿大无法检验"）
"""
import csv, os, sys, time
from collections import Counter
DATA = sys.argv[1] if len(sys.argv) > 1 else "cv/cvponline_extract_20241130"
t0 = time.time()
def log(*a):
    print("[%5.1fs] %s" % (time.time()-t0, " ".join(str(x) for x in a)), flush=True)

TARGETS = {"REMIFENTANIL": "remifentanil", "FENTANYL": "fentanyl",
           "SUFENTANIL": "sufentanil", "MORPHINE": "morphine"}
def match(nm, tgt):
    n = nm.strip().lower()
    return n == tgt or n.startswith(tgt + " ")

# ---- Pass 1: 活性成分 -> 产品 ----
prod2t = {}
hits = {t: set() for t in TARGETS}
with open(os.path.join(DATA, "drug_product_ingredients.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5: continue
        pid, nm = row[1].strip(), row[4].strip()
        for t, tgt in TARGETS.items():
            if match(nm, tgt):
                prod2t.setdefault(pid, set()).add(t); hits[t].add(nm)
for t in TARGETS:
    log("活性成分命中 %s = %s (product 数 %d)" % (t, sorted(hits[t]), len([p for p, s in prod2t.items() if t in s])))

# ---- Pass 2: report_drug -> 各药 Suspect 报告集合 ----
target_reports = {t: set() for t in TARGETS}
with open(os.path.join(DATA, "report_drug.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 5: continue
        if row[4].strip() != "Suspect": continue
        ts = prod2t.get(row[2].strip())
        if ts:
            rid = row[1].strip()
            for t in ts: target_reports[t].add(rid)
log("队列报告数（独立重算）= " + ", ".join("%s=%d" % (t, len(target_reports[t])) for t in TARGETS))

# ---- Pass 3: reports.txt -> reporter + 总数 ----
CAND = ("Serious report", "hprof")
rep_cnt = {t: Counter() for t in TARGETS}
ntot = 0
with open(os.path.join(DATA, "reports.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 40: continue
        ntot += 1
        rid = row[0].strip(); reporter = row[34].strip()
        for t in TARGETS:
            if rid in target_reports[t]:
                rep_cnt[t][reporter] += 1
log("reports.txt 总报告数（独立重算）= %d" % ntot)
log("reporter 字段分药计数（独立重算）:")
for t in TARGETS:
    log("   %-12s n=%d  %s" % (t, len(target_reports[t]), dict(rep_cnt[t].most_common())))

# ---- Pass 4: reactions.txt -> 4 个抽查 SOC + VOMITING PT 的 report-level 计数 ----
ASK_SOC = ["Immune system disorders", "Gastrointestinal disorders",
           "Psychiatric disorders", "General disorders and administration site conditions"]
gset = {s: set() for s in ASK_SOC}
tset = {t: {s: set() for s in ASK_SOC} for t in TARGETS}
gvom = set(); tvom = {t: set() for t in TARGETS}
with open(os.path.join(DATA, "reactions.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        if len(row) < 8: continue
        rid = row[1].strip(); pt = (row[5].strip() or "").upper(); soc = row[7].strip()
        if soc in gset: gset[soc].add(rid)
        if pt == "VOMITING": gvom.add(rid)
        for t in TARGETS:
            if rid in target_reports[t]:
                if soc in ASK_SOC: tset[t][soc].add(rid)
                if pt == "VOMITING": tvom[t].add(rid)
log("抽查 SOC 的全体报告数 c（独立重算）: " + ", ".join("%s=%d" % (s[:22], len(gset[s])) for s in ASK_SOC))
for s in ASK_SOC:
    log("   %-60s %s" % (s[:60], {t: len(tset[t][s]) for t in TARGETS}))
log("VOMITING 全体报告数 c = %d ; 分药 = %s" % (len(gvom), {t: len(tvom[t]) for t in TARGETS}))
