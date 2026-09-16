# -*- coding: utf-8 -*-
"""02 给药途径分层失衡分析（C1：缓解芬太尼透皮/适应症混杂）。
真实 openFDA 计数；复用瑞芬 _faers_cache.json（与 01 同字段口径）。
方法学模板：氯胺酮 faers_route_stratified.py（聚合层 route code 分层）。
关键目标：
  1) 看 4 药途径分布，量化芬太尼透皮(062)占比；
  2) 验证"透皮芬太尼富集 PAIN"假设：FEN_transdermal vs FEN_IV 的 PAIN 信号；
  3) 同途径敏感性：REMI_IV vs FEN_IV / MOR_IV 头对头 RORR（PAIN/ALLODYNIA/阴性对照）；
  4) 确认 OIH 特定 PT 结构性缺失不受途径影响。
输出：02_route_stratified.csv + 控制台打印。
"""
import urllib.request, urllib.parse, json, time, os, csv

BASE = "https://api.fda.gov/drug/event.json"
CACHE = os.path.join(os.path.dirname(__file__), "_faers_cache.json")
SLEEP = 0.8
cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}

ROUTE = "patient.drug.drugadministrationroute.exact"
# 口径与 01_核心FAERS失衡分析.py 严格对齐（含主要盐型变体）；否则队列数会与主分析矛盾。
REMI = 'patient.drug.activesubstance.activesubstancename.exact:("REMIFENTANIL" "REMIFENTANIL HYDROCHLORIDE")'
FEN  = 'patient.drug.activesubstance.activesubstancename.exact:("FENTANYL")'
SUF  = 'patient.drug.activesubstance.activesubstancename.exact:("SUFENTANIL" "SUFENTANIL CITRATE")'
MOR  = 'patient.drug.activesubstance.activesubstancename.exact:("MORPHINE")'

ROUTE_NAME = {
 "045":"Nasal(鼻用)","065":"Unknown(未知/未指定)","048":"Oral(口服)","042":"IV-NOS(静脉,未特指)",
 "041":"IV-drip(静脉点滴)","058":"Subcutaneous(皮下)","061":"Topical(局部)","030":"Intramuscular(肌注)",
 "055":"Resp-inhalation(吸入)","040":"IV-bolus(静脉推注)","050":"Other(其他)","062":"Transdermal(透皮)",
 "054":"Rectal(直肠)","064":"Transplacental(经胎盘)","066":"Urethral(尿道)","047":"Ophthalmic(眼用)",
 "060":"Unspecified(未特指)",
}
# 用于分布普查的 route 码全集
ALL_CODES = list(ROUTE_NAME.keys())

def save():
    json.dump(cache, open(CACHE, "w", encoding="utf-8"))

def total(search, tries=10):
    """search+limit=1 读 meta.total；规避 count 端点限流；404=0。"""
    if search in cache:
        return cache[search]
    q = urllib.parse.urlencode({"search": search, "limit": "1"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(f"{BASE}?{q}", timeout=30) as r:
                t = json.load(r).get("meta", {}).get("results", {}).get("total", 0)
            cache[search] = t; save(); time.sleep(SLEEP); return t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                cache[search] = 0; save(); time.sleep(SLEEP); return 0
            if e.code == 403:
                time.sleep(12 + i * 8); continue
            time.sleep(3)
        except Exception:
            time.sleep(3)
    cache[search] = None; save(); return None

def route_dist(ds):
    """逐 route code 用 total 求计数（不依赖 count 端点）。"""
    return {c: total(f'{ds} AND {ROUTE}:"{c}"') for c in ALL_CODES}

def ror(a, dn, pn, N):
    if None in (a, dn, pn, N):
        return None
    b = dn - a; c = pn - a; d = N - a - b - c
    if min(a, b, c, d) <= 0:
        return None
    return (a * d) / (b * c)

def ror_ci(a, dn, pn, N):
    """ROR 点估计 + 95%CI（Woolf 对数法）。"""
    r = ror(a, dn, pn, N)
    if r is None:
        return (None, None, None)
    b = dn - a; c = pn - a; d = N - a - b - c
    se = (1.0 / a + 1.0 / b + 1.0 / c + 1.0 / d) ** 0.5
    lo = r * (2.718281828459045 ** (-1.96 * se))
    hi = r * (2.718281828459045 ** (1.96 * se))
    return (r, lo, hi)

# ===== 1) 全局与分母 =====
N = total('patient.reaction.reactionmeddrapt:[* TO *]')
print("N(全库 reaction) =", N)
DRUGS = {"REMI": REMI, "FEN": FEN, "SUF": SUF, "MOR": MOR}
drug_tot = {k: total(v) for k, v in DRUGS.items()}
print("药物总数:", drug_tot)

# ===== 2) 途径分布（普查）=====
print("\n== 各药给药途径分布（route code 计数）==")
dist = {}
for k, ds in DRUGS.items():
    d = route_dist(ds)
    dist[k] = d
    known = sum(v for v in d.values() if v)
    tot = drug_tot[k] or 1
    print(f"\n{k} (total={drug_tot[k]}, 有 route 信息={known}, 覆盖率={100*known/tot:.1f}%)")
    for c in sorted(d, key=lambda x: -(d[x] or 0)):
        if d[c]:
            print(f"  {c:4s} {ROUTE_NAME.get(c,'?'):22s} {d[c]:>7} ({100*d[c]/tot:4.1f}% of drug)")

# ===== 3) 关键 PT 全库计数 =====
PTS = ["PAIN", "ALLODYNIA", "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION",
       "PAIN INCREASED", "HYPERALGESIA"]
pt_n = {pt: total(f'patient.reaction.reactionmeddrapt.exact:"{pt}"') for pt in PTS}
print("\nPT 全库计数:", pt_n)

# ===== 4) STRATA 定义 =====
STRATA = {
 "FEN_transdermal": (FEN, ["062"]),
 "FEN_IV":         (FEN, ["042","041","040"]),
 "REMI_IV_IVcodes":(REMI, ["042","041","040"]),         # 严格 IV
 "REMI_IV":        (REMI, ["042","041","040","065"]),   # IV + Unknown(瑞芬纯静脉，Unknown 大概率是 IV)
 "MOR_IV":         (MOR, ["042","041","040"]),
 "MOR_oral":       (MOR, ["048"]),
}
def strata_total(label):
    ds, codes = STRATA[label]
    return sum(total(f'{ds} AND {ROUTE}:"{c}"') for c in codes)
def strata_a(label, pt):
    ds, codes = STRATA[label]
    return sum(total(f'{ds} AND {ROUTE}:"{c}" AND patient.reaction.reactionmeddrapt.exact:"{pt}"') for c in codes)

strata_tot = {s: strata_total(s) for s in STRATA}
print("\nSTRATA 总数:", strata_tot)

# ===== 5) 各 STRATA 内 ROR(药物 vs 背景) =====
print("\n== 各 STRATA 内 ROR(PT) 与 95%CI ==")
rows = []
for pt in PTS:
    pn = pt_n[pt]; row = {"PT": pt}
    for s in STRATA:
        r, lo, hi = ror_ci(strata_a(s, pt), strata_tot[s], pn, N)
        row[s] = (r, lo, hi)
        a = strata_a(s, pt)
        print(f"  {pt:16s} {s:16s} a={a:>5} n={strata_tot[s]:>7} ROR={r} (95%CI {lo},{hi})" if r else f"  {pt:16s} {s:16s} a={a:>5} n={strata_tot[s]:>7} ROR=NA(稀疏)")
    rows.append(row)

# ===== 6) 同途径头对头 RORR（核心敏感性）=====
print("\n== 同途径头对头 RORR（REMI vs 对照，都在 IV）==")
def rorr(reminame, ctrlname):
    out = {}
    for pt in ["PAIN","ALLODYNIA","NAUSEA","VOMITING","PRURITUS","CONSTIPATION"]:
        r_remi, lo_r, hi_r = ror_ci(strata_a(reminame, pt), strata_tot[reminame], pt_n[pt], N)
        r_ctrl, lo_c, hi_c = ror_ci(strata_a(ctrlname, pt), strata_tot[ctrlname], pt_n[pt], N)
        if r_remi and r_ctrl:
            rr = r_remi / r_ctrl
            out[pt] = (r_remi, r_ctrl, rr)
            print(f"  {pt:12s} ROR(REMI_IV)={r_remi:.3f}  ROR({ctrlname})={r_ctrl:.3f}  RORR={rr:.3f}")
        else:
            out[pt] = (r_remi, r_ctrl, None)
            print(f"  {pt:12s} ROR(REMI_IV)={r_remi}  ROR({ctrlname})={r_ctrl}  RORR=NA")
    return out

rorr_fen = rorr("REMI_IV", "FEN_IV")
rorr_mor = rorr("REMI_IV", "MOR_IV")

# 透皮混杂验证：FEN_transdermal vs FEN_IV 内 PAIN/ALLODYNIA ROR
print("\n== 透皮混杂验证：芬太尼透皮 vs 芬太尼 IV 内 ROR ==")
fen_trans = {}; fen_iv = {}
for pt in ["PAIN","ALLODYNIA","NAUSEA","CONSTIPATION"]:
    r_t, lo_t, hi_t = ror_ci(strata_a("FEN_transdermal", pt), strata_tot["FEN_transdermal"], pt_n[pt], N)
    r_i, lo_i, hi_i = ror_ci(strata_a("FEN_IV", pt), strata_tot["FEN_IV"], pt_n[pt], N)
    fen_trans[pt] = r_t; fen_iv[pt] = r_i
    print(f"  {pt:12s} FEN_transdermal ROR={r_t}  FEN_IV ROR={r_i}")

# ===== 7) 写出 CSV =====
out = os.path.join(os.path.dirname(__file__), "02_route_stratified.csv")
with open(out, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["## C1 Route-stratified disproportionality (openFDA aggregate)"])
    w.writerow(["N_total_reactions", N])
    w.writerow([])
    w.writerow(["Drug", "Total(drug)", "RouteCode", "RouteName", "Count", "PctOfDrug", "KnownRouteCoverage%"])
    for k in DRUGS:
        tot = drug_tot[k] or 1
        known = sum(v for v in dist[k].values() if v)
        for c in sorted(dist[k], key=lambda x: -(dist[k][x] or 0)):
            if dist[k][c]:
                w.writerow([k, drug_tot[k], c, ROUTE_NAME.get(c,"?"), dist[k][c],
                            round(100*dist[k][c]/tot,2), round(100*known/tot,1)])
        w.writerow([])
    w.writerow(["PT"] + [f"{s}_ROR" for s in STRATA] + [f"{s}_a" for s in STRATA])
    for row in rows:
        w.writerow([row["PT"]] +
                   [("%.3f" % row[s][0]) if row[s][0] else "NA" for s in STRATA] +
                   [strata_a(s, row["PT"]) for s in STRATA])
    w.writerow([])
    w.writerow(["HeadToHead_RORR", "REMI_IV_vs_FEN_IV", "", "REMI_IV_vs_MOR_IV"])
    w.writerow(["PT", "ROR_REMI", "ROR_FEN_IV", "RORR", "ROR_REMI", "ROR_MOR_IV", "RORR"])
    for pt in ["PAIN","ALLODYNIA","NAUSEA","VOMITING","PRURITUS","CONSTIPATION"]:
        rt, ct, rrt = rorr_fen[pt]; rm, cm, rrm = rorr_mor[pt]
        w.writerow([pt, ("%.3f"%rt) if rt else "NA", ("%.3f"%ct) if ct else "NA",
                    ("%.3f"%rrt) if rrt else "NA",
                    ("%.3f"%rm) if rm else "NA", ("%.3f"%cm) if cm else "NA",
                    ("%.3f"%rrm) if rrm else "NA"])
    w.writerow([])
    w.writerow(["TransdermalConfoundingCheck_FEN", "FEN_transdermal_ROR", "FEN_IV_ROR"])
    for pt in ["PAIN","ALLODYNIA","NAUSEA","CONSTIPATION"]:
        w.writerow([pt, ("%.3f"%fen_trans[pt]) if fen_trans[pt] else "NA",
                    ("%.3f"%fen_iv[pt]) if fen_iv[pt] else "NA"])
print("\n写出:", out)
