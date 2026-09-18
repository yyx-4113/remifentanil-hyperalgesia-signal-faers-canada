# -*- coding: utf-8 -*-
"""A7 任务5b（优化版）：完全独立的加拿大原始数据重算。
不复用作者任何中间结果；用字节级 split 代替 csv 模块以加速。"""
import os, sys, time
from collections import Counter
DATA = sys.argv[1]
t0 = time.time()
def log(*a): print("[%5.1fs] %s" % (time.time()-t0, " ".join(str(x) for x in a)), flush=True)

T = {"REMIFENTANIL": b"remifentanil", "FENTANYL": b"fentanyl",
     "SUFENTANIL": b"sufentanil", "MORPHINE": b"morphine"}
def match(nm, tgt):
    n = nm.strip().lower()
    return n == tgt or n.startswith(tgt + b" ")

# ---- Pass 1 ----
prod2t = {}
hits = {k: set() for k in T}
with open(os.path.join(DATA, "drug_product_ingredients.txt"), "rb") as fh:
    for line in fh:
        f = line.rstrip(b"\r\n").split(b"$", 5)
        if len(f) < 5: continue
        pid = f[1].strip().strip(b'"'); nm = f[4].strip().strip(b'"')
        for k, tgt in T.items():
            if match(nm, tgt):
                prod2t.setdefault(pid, set()).add(k); hits[k].add(nm)
for k in T:
    log("活性成分命中 %s = %s (product 数 %d)" % (k, sorted(x.decode() for x in hits[k]), len([p for p,s in prod2t.items() if k in s])))
log("prod2t 条目数 = %d" % len(prod2t))

# ---- Pass 2 ----
target_reports = {k: set() for k in T}
nrows = 0
with open(os.path.join(DATA, "report_drug.txt"), "rb") as fh:
    for line in fh:
        nrows += 1
        f = line.split(b"$", 5)
        if len(f) < 5: continue
        if f[4].strip().strip(b'"') != b"Suspect": continue
        ts = prod2t.get(f[2].strip().strip(b'"'))
        if ts:
            rid = f[1].strip().strip(b'"')
            for k in ts: target_reports[k].add(rid)
        if nrows % 5000000 == 0: log("  report_drug 行 %d" % nrows)
log("report_drug 总行数 = %d ; 队列（独立重算）= %s" % (nrows, {k: len(v) for k, v in target_reports.items()}))

# ---- Pass 3 ----
rep_cnt = {k: Counter() for k in T}
ntot = 0
with open(os.path.join(DATA, "reports.txt"), "rb") as fh:
    for line in fh:
        ntot += 1
        f = line.split(b"$", 36)
        if len(f) < 35: continue
        rid = f[0].strip().strip(b'"'); rep = f[34].strip().strip(b'"').decode("utf-8", "replace")
        for k in T:
            if rid in target_reports[k]: rep_cnt[k][rep] += 1
log("reports.txt 总报告数 = %d" % ntot)
for k in T:
    log("  reporter 分布 %-12s n=%d : %s" % (k, len(target_reports[k]), dict(rep_cnt[k].most_common())))

# ---- Pass 4 ----
ASK = ["Immune system disorders", "Gastrointestinal disorders",
       "Psychiatric disorders", "General disorders and administration site conditions"]
ASKb = [s.encode() for s in ASK]
gset = {s: set() for s in ASK}
tset = {k: {s: set() for s in ASK} for k in T}
gvom = set(); tvom = {k: set() for k in T}
nreact = 0
with open(os.path.join(DATA, "reactions.txt"), "rb") as fh:
    for line in fh:
        nreact += 1
        f = line.split(b"$", 8)
        if len(f) < 8: continue
        rid = f[1].strip().strip(b'"'); pt = f[5].strip().strip(b'"').upper(); soc = f[7].strip().strip(b'"')
        if soc in gset: gset[soc].add(rid)
        if pt == b"VOMITING": gvom.add(rid)
        for k in T:
            if rid in target_reports[k]:
                if soc in gset: tset[k][soc].add(rid)
                if pt == b"VOMITING": tvom[k].add(rid)
        if nreact % 5000000 == 0: log("  reactions 行 %d" % nreact)
log("reactions.txt 总行数 = %d" % nreact)
for s in ASK:
    log("  SOC %-62s c=%d  分药=%s" % (s[:62], len(gset[s]), {k: len(tset[k][s]) for k in T}))
log("  PT VOMITING c=%d  分药=%s" % (len(gvom), {k: len(tvom[k]) for k in T}))
