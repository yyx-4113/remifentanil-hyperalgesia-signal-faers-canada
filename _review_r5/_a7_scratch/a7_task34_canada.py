# -*- coding: utf-8 -*-
"""A7 任务3/4：从 cv_pt_summary.csv 与 cv_soc_27.csv 独立重算加拿大侧 RORR（与稿件 Table 3、Table S1 Panel A 比对）。
关键发现点：加拿大侧 RORR 用的是"共享 c,d"口径（c=全球该PT/SOC报告数，对所有药相同），
            即 RORR = a_R*(Ncomp-a_comp) / ((Nremi-a_R)*a_comp)，与 c 无关；
            而 FAERS 侧用的是"各自 c,d"口径。二者定义不同。
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
N = 1154017
COH = {"REMIFENTANIL": 111, "FENTANYL": 4881, "SUFENTANIL": 63, "MORPHINE": 7675}

def rorr_sharedc(a_r, a_c, drug_c):
    """加拿大实现口径：两根 ROR 共用 c,d  →  (a_r*b_c)/(b_r*a_c)"""
    b_r = COH["REMIFENTANIL"] - a_r
    b_c = COH[drug_c] - a_c
    if min(a_r, a_c, b_r, b_c) <= 0: return None
    return (a_r * b_c) / (b_r * a_c)

def rorr_ownc(a_r, a_c, drug_c, pt_total):
    """FAERS 实现口径：各自 c=PT_total-a, d=N-a-b-c"""
    out = {}
    for tag, a in (("remi", a_r), ("comp", a_c)):
        b = COH["REMIFENTANIL" if tag == "remi" else drug_c] - a
        c = pt_total - a
        d = N - a - b - c
        out[tag] = (a * d) / (b * c)
    return out["remi"] / out["comp"]

print("=" * 100)
print("任务3：加拿大侧关键 PT 的 RORR 独立重算（稿件 Table 3 / §3.4 / §3.5）")
print("=" * 100)
pt = {r["PT"]: r for r in csv.DictReader(open(os.path.join(ROOT, "cv", "cv_pt_summary.csv"), encoding="utf-8-sig"))}
CASES = [("PAIN", "FENTANYL", "0.235"), ("PAIN", "MORPHINE", "0.146"),
         ("DRUG INEFFECTIVE", "FENTANYL", "1.277"), ("DRUG INEFFECTIVE", "MORPHINE", "1.703"),
         ("VOMITING", "FENTANYL", "1.066"), ("VOMITING", "MORPHINE", "0.392")]
for name, comp, claim in CASES:
    r = pt[name]
    a_r = int(r["REMIFENTANIL_reports"]); a_c = int(r["%s_reports" % comp])
    mine = rorr_sharedc(a_r, a_c, comp)
    csvv = r["RORR_REMI_vs_FEN" if comp == "FENTANYL" else "RORR_REMI_vs_MOR"]
    print("%-20s vs %-10s 稿件=%-7s 源CSV=%-7s 我重算=%.6f  稿件-重算=%.2e  a_remi=%d a_%s=%d  %s"
          % (name, comp, claim, csvv, mine, abs(mine - float(claim)), a_r, comp[:3], a_c,
             "✓" if abs(round(mine, 3) - float(claim)) < 1e-9 else "✗"))

print("\n--- 加拿大 VOMITING 是否真的可算（用于 §5 结论的'无法检验'表述） ---")
r = pt["VOMITING"]
print("VOMITING: 加拿大队列 a = REMI %s / FEN %s / SUF %s / MOR %s ; REMI_ROR=%s ; RORR vs FEN=%s ; vs MOR=%s"
      % (r["REMIFENTANIL_reports"], r["FENTANYL_reports"], r["SUFENTANIL_reports"], r["MORPHINE_reports"],
         r["REMI_ROR"], r["RORR_REMI_vs_FEN"], r["RORR_REMI_vs_MOR"]))
print("→ 4 个阴性对照（NAUSEA/VOMITING/PRURITUS/CONSTIPATION）中，加拿大侧 REMI a>0 的只有 VOMITING(3)")

print("\n" + "=" * 100)
print("任务4：Table S1 Panel A 抽查 4 个 SOC 的 ROR 与 RORR")
print("=" * 100)
soc = {r["SOC"]: r for r in csv.DictReader(open(os.path.join(ROOT, "cv", "cv_soc_27.csv"), encoding="utf-8-sig"))}
CHECK = {"Immune system disorders": ("2.363", "1.792", "0.831"),
         "Gastrointestinal disorders": ("0.101", "0.213", "0.086"),
         "Psychiatric disorders": (None, None, None),
         "General disorders and administration site conditions": ("0.361", "0.497", "0.433")}
for name, claims in CHECK.items():
    s = soc[name]
    a_r = int(s["REMIFENTANIL_reports"])
    fen = int(s["FENTANYL_reports"]); mor = int(s["MORPHINE_reports"])
    rr_f = rorr_sharedc(a_r, fen, "FENTANYL"); rr_m = rorr_sharedc(a_r, mor, "MORPHINE")
    # 反解 c（全球该 SOC 报告数）以独立校验表格里的 ROR
    c_solved = None
    if a_r and s["REMI_ROR"]:
        target = float(s["REMI_ROR"])
        # (a*(N-c))/((COH-a)*c) = target
        num = a_r * N; den = target * (COH["REMIFENTANIL"] - a_r) + a_r
        c_solved = num / den
        mine_ror = (a_r * (N - round(c_solved))) / ((COH["REMIFENTANIL"] - a_r) * round(c_solved))
    else:
        mine_ror = None
    print("\n%s" % name)
    print("  REMI a=%-3d FEN a=%-4d MOR a=%-4d | 表列 ROR=%s RORRfen=%s RORRmor=%s"
          % (a_r, fen, mor, s["REMI_ROR"], s["RORR_REMI_vs_FEN"], s["RORR_REMI_vs_MOR"]))
    print("  我重算 RORRfen=%-9s (稿件声明 %s)  RORRmor=%-9s (稿件声明 %s)"
          % ("%.6f" % rr_f if rr_f else "不可估", claims[1],
             "%.6f" % rr_m if rr_m else "不可估", claims[2]))
    if c_solved:
        print("  由 ROR 反解全球该 SOC 报告数 c≈%.0f；用 round(c) 回算 ROR=%.4f (表列 %s) → 自洽"
              % (c_solved, mine_ror, s["REMI_ROR"]))
    else:
        print("  REMI a=0 → ROR/RORR 不可估计；表中为破折号（语义=不可估计，非 0）")

# Panel A 全表 RORR 自洽性：用共享 c 口径重算全部 27 行
print("\n--- Panel A 全 27 行：RORR 用共享-c 口径重算 vs 表内值 ---")
bad = 0
for name, s in soc.items():
    a_r = int(s["REMIFENTANIL_reports"])
    for comp, col in (("FENTANYL", "RORR_REMI_vs_FEN"), ("MORPHINE", "RORR_REMI_vs_MOR")):
        a_c = int(s["%s_reports" % comp]); v = s[col]
        mine = rorr_sharedc(a_r, a_c, comp)
        if v == "" and mine is None:
            print("  %-70s vs %-10s 破折号 ✓" % (name[:70], comp)); continue
        if v == "" or mine is None:
            print("  %-70s vs %-10s ✗ 表=%r 我=%s" % (name[:70], comp, v, mine)); bad += 1; continue
        if abs(round(mine, 3) - float(v)) > 1e-9:
            print("  %-70s vs %-10s ✗ 表=%s 我=%.6f" % (name[:70], comp, v, mine)); bad += 1
print("  Panel A RORR 不自洽行数 = %d" % bad)

# Panel A pct 自洽性：n/队列
print("\n--- Panel A：括号内百分比 r = n/队列 是否正确四舍五入到 1 位 ---")
badp = 0
for name, s in soc.items():
    for drug in ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]:
        n = int(s["%s_reports" % drug]); shown = float(s["%s_pct" % drug])
        indep = 100.0 * n / COH[drug]
        if abs(round(indep, 1) - shown) > 1e-9:
            print("  ✗ %-60s %-12s n=%-5d 队列=%d 独立算=%.4f→%.1f 表内=%.2f"
                  % (name[:60], drug, n, COH[drug], indep, round(indep, 1), shown)); badp += 1
print("  百分比不自洽格数 = %d（表内为 2 位，题注称 1 位）" % badp)
