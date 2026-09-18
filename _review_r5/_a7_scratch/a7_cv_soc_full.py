# -*- coding: utf-8 -*-
"""A7 任务4强化：完全独立重算加拿大侧 27 SOC 与 PT 表（不复用作者任何中间产物）。

阶段：
  Stage A  Pass1+Pass2 -> 落盘 _a7_cv_target_reports.pkl（rid->bitmask + prod2t）
  Stage B  读 pkl，扫描 reactions.txt，重算：
            - 全局 27 SOC 的 c = |全局该 SOC 报告集|
            - 各药 a = |该药队列 ∩ 该 SOC 报告集|
            - 全局 PT 集合（VOMITING 等）
            - 现场算出 ROR / RORR，并与作者 cv_soc_27.csv、cv_pt_summary.csv 逐格比对
用法：python a7_cv_soc_full.py <DATA_DIR> <OUT_TXT>
"""
import os, sys, time, pickle
from collections import defaultdict, Counter

DATA = sys.argv[1]
OUT = sys.argv[2]
PKL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_a7_cv_target_reports.pkl")
t0 = time.time()
def log(*a):
    s = "[%6.1fs] %s" % (time.time() - t0, " ".join(str(x) for x in a))
    print(s, flush=True)
    with open(OUT, "a", encoding="utf-8") as fh:
        fh.write(s + "\n")

TARGETS = ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]
TG = {k: k.lower().encode() for k in TARGETS}

def match(name_b, tgt):
    n = name_b.strip().lower()
    return n == tgt or n.startswith(tgt + b" ")

if os.path.exists(PKL):
    log("复用已落盘 Pass1+Pass2 结果：%s" % PKL)
    with open(PKL, "rb") as fh:
        bit_of, prod2t = pickle.load(fh)
else:
    # ---------------- Pass 1 ----------------
    log("== Pass1: drug_product_ingredients.txt -> 活性成分命中 ==")
    prod2t = {}
    hits = defaultdict(set)
    with open(os.path.join(DATA, "drug_product_ingredients.txt"), "rb") as fh:
        for line in fh:
            f = line.rstrip(b"\r\n").split(b"$", 5)
            if len(f) < 5:
                continue
            pid = f[1].strip().strip(b'"')
            nm = f[4].strip().strip(b'"')
            for k in TARGETS:
                if match(nm, TG[k]):
                    prod2t.setdefault(pid, set()).add(k)
                    hits[k].add(nm)
    for k in TARGETS:
        log("   %-12s 命中成分=%s  product数=%d" % (k, sorted(x.decode() for x in hits[k]), len([p for p, s in prod2t.items() if k in s])))

    # ---------------- Pass 2 ----------------
    log("== Pass2: report_drug.txt -> 各药 Suspect 报告集合 ==")
    bit_of = {}
    nrows = 0
    with open(os.path.join(DATA, "report_drug.txt"), "rb") as fh:
        for line in fh:
            nrows += 1
            f = line.split(b"$", 5)
            if len(f) < 5:
                continue
            if f[4].strip().strip(b'"') != b"Suspect":
                continue
            ts = prod2t.get(f[2].strip().strip(b'"'))
            if not ts:
                continue
            rid = f[1].strip().strip(b'"')
            m = bit_of.get(rid, 0)
            for k in ts:
                m |= 1 << TARGETS.index(k)
            bit_of[rid] = m
            if nrows % 3000000 == 0:
                log("   report_drug 行 %d" % nrows)
    log("   report_drug 总行数=%d ; 队列规模=%s" % (nrows, {k: sum(1 for v in bit_of.values() if v >> i & 1) for i, k in enumerate(TARGETS)}))
    with open(PKL, "wb") as fh:
        pickle.dump((bit_of, prod2t), fh, protocol=4)
    log("   已落盘 %s" % PKL)

# ---------------- Pass 3：reports.txt 总报告数 N（独立重算） ----------------
log("== Pass3: reports.txt 总报告数 N ==")
N = 0
with open(os.path.join(DATA, "reports.txt"), "rb") as fh:
    for line in fh:
        N += 1
log("   N = %d" % N)

# ---------------- Pass 4：reactions.txt ----------------
log("== Pass4: reactions.txt -> 全局 SOC / 各药 SOC / PT ==")
gset = {}                       # SOC -> set(rid)
gpt = defaultdict(set)          # PT -> set(rid)
tsoc = {k: defaultdict(set) for k in TARGETS}
tpt = {k: defaultdict(set) for k in TARGETS}
soc_order = []
nreact = 0
with open(os.path.join(DATA, "reactions.txt"), "rb") as fh:
    for line in fh:
        nreact += 1
        f = line.split(b"$", 8)
        if len(f) < 8:
            continue
        rid = f[1].strip().strip(b'"')
        # 注意：PT 必须 decode 成 str 再 upper，否则与 str 键查询不匹配（曾因此得到全 0）
        pt = f[5].strip().strip(b'"').decode("utf-8", "replace").upper()
        soc = f[7].strip().strip(b'"').decode("utf-8", "replace")
        if soc:
            if soc not in gset:
                gset[soc] = set()
                soc_order.append(soc)
            gset[soc].add(rid)
        if pt:
            gpt[pt].add(rid)
        m = bit_of.get(rid)
        if m:
            for i, k in enumerate(TARGETS):
                if m >> i & 1:
                    if soc:
                        tsoc[k][soc].add(rid)
                    if pt:
                        tpt[k][pt].add(rid)
        if nreact % 3000000 == 0:
            log("   reactions 行 %d" % nreact)
log("   reactions.txt 总行数=%d ; 全局 SOC 数=%d" % (nreact, len(soc_order)))

# ---------------- 计算 ----------------
def ror(a, b, c, d):
    if min(a, b, c, d) <= 0:
        return None
    return (a * d) / (b * c)

nq = {k: sum(1 for v in bit_of.values() if v >> i & 1) for i, k in enumerate(TARGETS)}
log("== 队列规模（与 cv_drug_totals.csv 比对） ==")
for k in TARGETS:
    log("   %-12s = %d" % (k, nq[k]))
log("   分母 N = %d" % N)

# --- 27 SOC ---
log("== 27 原生 SOC 独立重算（SOC, a_remi, c, ROR_remi, RORR_vs_FEN, RORR_vs_MOR） ==")
mine = {}
for soc in soc_order:
    c = len(gset[soc])
    a = {k: len(tsoc[k][soc]) for k in TARGETS}
    r_remi = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], c, N - c)
    rr_fen = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], a["FENTANYL"], nq["FENTANYL"] - a["FENTANYL"])
    rr_mor = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], a["MORPHINE"], nq["MORPHINE"] - a["MORPHINE"])
    mine[soc] = (a["REMIFENTANIL"], c, r_remi, rr_fen, rr_mor, {k: a[k] for k in TARGETS})
    log("   %-64s a=%4d c=%6d ROR=%s RORR_F=%s RORR_M=%s 分药=%s" % (
        soc[:64], a["REMIFENTANIL"], c,
        ("%.3f" % r_remi) if r_remi else "-",
        ("%.3f" % rr_fen) if rr_fen else "-",
        ("%.3f" % rr_mor) if rr_mor else "-",
        "/".join(str(a[k]) for k in TARGETS)))

# --- PT 关注项 ---
log("== 关注 PT 独立重算（PT, 全局c, a_remi/a_fen/a_suf/a_mor, ROR_remi, RORR_F, RORR_M） ==")
PTS = ["HYPERALGESIA", "ALLODYNIA", "PAIN", "PAIN INCREASED", "DRUG INEFFECTIVE",
       "OPIOID WITHDRAWAL SYNDROME", "DRUG TOLERANCE", "POSTOPERATIVE PAIN", "CHRONIC PAIN",
       "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION",
       "HYPERAESTHESIA", "HYPERPATHIA", "PROCEDURAL PAIN", "CHRONIC PAIN SYNDROME",
       "DRUG WITHDRAWAL SYNDROME"]
for p in PTS:
    s = gpt.get(p, set())
    c = len(s)
    a = {k: len(tpt[k][p]) for k in TARGETS}
    r_remi = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], c, N - c)
    rr_fen = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], a["FENTANYL"], nq["FENTANYL"] - a["FENTANYL"])
    rr_mor = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], a["MORPHINE"], nq["MORPHINE"] - a["MORPHINE"])
    log("   %-26s c=%5d 分药=%s ROR=%s RORR_F=%s RORR_M=%s" % (
        p, c, "/".join(str(a[k]) for k in TARGETS),
        ("%.3f" % r_remi) if r_remi else "-",
        ("%.3f" % rr_fen) if rr_fen else "-",
        ("%.3f" % rr_mor) if rr_mor else "-"))
log("== DONE ==")

# ---------------- 与作者产物逐格比对 ----------------
import csv as _csv
CVDIR = os.path.dirname(os.path.abspath(DATA.rstrip("/\\")))

def num(s):
    s = (s or "").strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return s

log("== 与 cv/cv_soc_27.csv 逐格比对 ==")
with open(os.path.join(CVDIR, "cv_soc_27.csv"), encoding="utf-8-sig", newline="") as fh:
    rows = list(_csv.DictReader(fh))
log("   CSV 行数=%d ；我重算 SOC 数=%d" % (len(rows), len(soc_order)))
mism = 0
for r in rows:
    soc = r["SOC"].strip()
    if soc not in mine:
        log("   !! CSV 中有而我重算里没有的 SOC: %r" % soc)
        mism += 1
        continue
    a_remi, c, r_remi, rr_fen, rr_mor, a = mine[soc]
    checks = [
        ("REMI_a", num(r["REMIFENTANIL_reports"]), a["REMIFENTANIL"]),
        ("FEN_a", num(r["FENTANYL_reports"]), a["FENTANYL"]),
        ("SUF_a", num(r["SUFENTANIL_reports"]), a["SUFENTANIL"]),
        ("MOR_a", num(r["MORPHINE_reports"]), a["MORPHINE"]),
        ("REMI_ROR", num(r["REMI_ROR"]), round(r_remi, 3) if r_remi else None),
        ("RORR_FEN", num(r["RORR_REMI_vs_FEN"]), round(rr_fen, 3) if rr_fen else None),
        ("RORR_MOR", num(r["RORR_REMI_vs_MOR"]), round(rr_mor, 3) if rr_mor else None),
    ]
    for nm, got, exp in checks:
        if got != exp:
            log("   DIFF %-62s %-10s CSV=%s 我=%s" % (soc[:62], nm, got, exp))
            mism += 1
log("   >> SOC 表不一致格数 = %d" % mism)

# 全局 SOC c 与作者脚本口径的一致性
log("== 抽样核对：4 个抽查 SOC 的全局报告数 c（我独立重算） ==")
for s in ["Immune system disorders", "Gastrointestinal disorders",
          "Psychiatric disorders", "General disorders and administration site conditions"]:
    log("   %-62s c=%d  ROR=%s  RORR_F=%s  RORR_M=%s" % (
        s[:62], len(gset.get(s, set())),
        ("%.3f" % mine[s][2]) if mine[s][2] else "-",
        ("%.3f" % mine[s][3]) if mine[s][3] else "-",
        ("%.3f" % mine[s][4]) if mine[s][4] else "-"))

log("== 与 cv/cv_pt_summary.csv 逐格比对 ==")
with open(os.path.join(CVDIR, "cv_pt_summary.csv"), encoding="utf-8-sig", newline="") as fh:
    prows = list(_csv.DictReader(fh))
pm = 0
for r in prows:
    p = r["PT"].strip().upper()
    s = gpt.get(p, set())
    c = len(s)
    a = {k: len(tpt[k][p]) for k in TARGETS}
    r_remi = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], c, N - c)
    rr_fen = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], a["FENTANYL"], nq["FENTANYL"] - a["FENTANYL"])
    rr_mor = ror(a["REMIFENTANIL"], nq["REMIFENTANIL"] - a["REMIFENTANIL"], a["MORPHINE"], nq["MORPHINE"] - a["MORPHINE"])
    checks = [
        ("REMI_a", num(r["REMIFENTANIL_reports"]), a["REMIFENTANIL"]),
        ("FEN_a", num(r["FENTANYL_reports"]), a["FENTANYL"]),
        ("SUF_a", num(r["SUFENTANIL_reports"]), a["SUFENTANIL"]),
        ("MOR_a", num(r["MORPHINE_reports"]), a["MORPHINE"]),
        ("REMI_ROR", num(r["REMI_ROR"]), round(r_remi, 3) if r_remi else None),
        ("RORR_FEN", num(r["RORR_REMI_vs_FEN"]), round(rr_fen, 3) if rr_fen else None),
        ("RORR_MOR", num(r["RORR_REMI_vs_MOR"]), round(rr_mor, 3) if rr_mor else None),
    ]
    bad = []
    for nm, got, exp in checks:
        if got != exp:
            bad.append("%s CSV=%s 我=%s" % (nm, got, exp))
    log("   %-26s c=%5d a=%s  ROR=%s RORR_F=%s RORR_M=%s %s" % (
        p, c, "/".join(str(a[k]) for k in TARGETS),
        ("%.3f" % r_remi) if r_remi else "-",
        ("%.3f" % rr_fen) if rr_fen else "-",
        ("%.3f" % rr_mor) if rr_mor else "-",
        ("  <<< " + " ; ".join(bad)) if bad else ""))
    pm += len(bad)
log("   >> PT 表不一致格数 = %d" % pm)
log("== VERIFY DONE ==")

