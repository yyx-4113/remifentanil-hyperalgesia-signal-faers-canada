# -*- coding: utf-8 -*-
"""A7 补充：Table S1 Panel A 百分比独立核对 + Panel B（FAERS）逐格核对 + 破折号语义统计。"""
import csv, os, re, decimal
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
text = open(os.path.join(ROOT, "I_正文_IMRaD_en.md"), encoding="utf-8").read()
DRUGS = ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]
def round_half_up(x, d):
    return float(decimal.Decimal(repr(x)).quantize(decimal.Decimal('1.' + '0'*d), rounding=decimal.ROUND_HALF_UP))
def get_table(start, stops):
    i = text.index(start); j = len(text)
    for sm in stops:
        k = text.find(sm, i + len(start))
        if k != -1: j = min(j, k)
    out = []
    for line in text[i:j].splitlines():
        line = line.strip()
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if set("".join(cells)) <= set("-: "): continue
        out.append(cells)
    return out

print("=" * 90)
print("Table S1 Panel A：括号内百分比 是否 = n/队列 的正确 1 位四舍五入")
print("=" * 90)
CVPOP = {"REMIFENTANIL": 111, "FENTANYL": 4881, "SUFENTANIL": 63, "MORPHINE": 7675}
rows = get_table("**Panel A. Canada Vigilance, native MedDRA system organ classes", ["**Panel B. FAERS, exploratory,"])
bad = 0; tot = 0
for r in rows[1:]:
    if len(r) < 8: continue
    for col, drug in zip(range(1, 5), DRUGS):
        m = re.match(r"^(\d+)\s*\(([\d.]+)\)$", r[col].replace("\u2009", "").replace(" ", ""))
        if not m: 
            print("  跳过（无数字）%s / %s = %r" % (r[0][:40], drug, r[col])); continue
        n = int(m.group(1)); shown = float(m.group(2)); tot += 1
        indep = 100.0 * n / CVPOP[drug]
        if abs(round_half_up(indep, 1) - shown) > 1e-9:
            print("  ✗ %-58s %-12s n=%-5d 稿件=%.1f 独立算=%.4f→%.1f" % (r[0][:58], drug, n, shown, indep, round_half_up(indep, 1)))
            bad += 1
print("  Panel A 百分比格数 = %d，不自洽 = %d" % (tot, bad))

print("\n" + "=" * 90)
print("Table S1 Panel B（FAERS）：与 03_soc_27.csv 逐格核对")
print("=" * 90)
soc2 = {}
for line in open(os.path.join(ROOT, "03_soc_27.csv"), encoding="utf-8-sig"):
    if not line.strip() or line.startswith("#"): continue
    parts = next(csv.reader([line.rstrip("\n")]))
    if len(parts) >= 12 and parts[0] not in ("SOC", "Drug", "N_total_reactions") and not parts[0].startswith(("Unmapped", "Global")):
        soc2[parts[0]] = parts
P = {"REMIFENTANIL": 5375, "FENTANYL": 121819, "SUFENTANIL": 6513, "MORPHINE": 56501}
rows = get_table("**Panel B. FAERS, exploratory, event-level counts", ["Panel B is event-level:"])
badb = 0; totb = 0
for r in rows[1:]:
    if len(r) < 8: continue
    name = r[0]; src = soc2.get(name)
    if src is None:
        cand = [k for k in soc2 if k.startswith(name[:28])]
        if len(cand) == 1: src = soc2[cand[0]]
        else: print("  未匹配 SOC 名: %r" % name); continue
    for col, drug in zip(range(1, 5), DRUGS):
        m = re.match(r"^(\d[\d\s]*)\s*\(([\d.]+)\)$", r[col])
        if not m: print("  无法解析 %s / %s = %r" % (name[:40], drug, r[col])); continue
        n = int(re.sub(r"\s", "", m.group(1))); shown = float(m.group(2)); totb += 1
        src_n = int(src[1 + DRUGS.index(drug)]); src_pct = float(src[5 + DRUGS.index(drug)])
        indep = 100.0 * n / P[drug]
        tags = []
        if n != src_n: tags.append("n稿件%d≠源%d" % (n, src_n))
        if abs(round_half_up(indep, 1) - shown) > 1e-9:
            tags.append("pct稿件%.1f≠n/队列%.1f(源存%.2f)" % (shown, round_half_up(indep, 1), src_pct))
        if tags:
            print("  ✗ %-50s %-12s %s" % (name[:50], drug, "; ".join(tags))); badb += 1
    for col, idx, key in [(4, 9, "ROR"), (5, 10, "RORRfen"), (6, 11, "RORRmor")]:
        cell = r[col]; sv = src[idx]
        if cell.strip() in ("—", "-", "–", ""):
            if sv != "": print("  ✗ %s / %s 稿件破折号 源=%s" % (name[:40], key, sv)); badb += 1
        else:
            try: v = float(cell)
            except ValueError: print("  ? %s / %s = %r" % (name[:40], key, cell)); continue
            if sv == "" or abs(v - float(sv)) > 5e-4:
                print("  ✗ %s / %s 稿件=%s 源=%s" % (name[:40], key, v, sv)); badb += 1
print("  Panel B 数字格数 = %d / 4 = %d SOC 行，问题 = %d" % (totb, totb // 4, badb))

print("\n" + "=" * 90)
print("破折号语义（不可估计 vs 0）统计")
print("=" * 90)
faers = {r["PT"]: r for r in csv.DictReader(open(os.path.join(ROOT, "01_faers_results.csv"), encoding="utf-8-sig"))}
t2 = get_table("### Table 2. Primary analysis", ["### Table 3.", "OR = reporting odds ratio; RORR"])
n_dash_ok = n_dash_bad = 0
for r in t2[1:]:
    if len(r) < 9: continue
    for col, k in [(3, "REMIFENTANIL_ROR"), (4, "FENTANYL_ROR"), (5, "SUFENTANIL_ROR"), (6, "MORPHINE_ROR")]:
        if r[col].strip() in ("—", "-", "–", ""):
            if faers[r[0]][k] == "": n_dash_ok += 1
            else: n_dash_bad += 1; print("  ✗ T2 %s %s 破折号 但源=%s" % (r[0], k, faers[r[0]][k]))
print("  Table 2 破折号: 源为空(不可估计) %d 处，源非空但写破折号 %d 处" % (n_dash_ok, n_dash_bad))
# 各 PT 的 PT_total，判断"破折号=不可估计"与"整库为 0"
print("\n  18 个 PT 的 PT_total 与 REMI a（用于区分'不可估计'与'全库零'）:")
for r in t2[1:]:
    if len(r) < 9: continue
    s = faers[r[0]]
    print("    %-24s PT_total=%-9s REMI a=%-4s 稿件 OR 列=%-22s 源 ROR=%-8s 源CI=%s"
          % (r[0], s["PT_total"], s["REMIFENTANIL_a"], r[3], s["REMIFENTANIL_ROR"] or "(空)", s["REMIFENTANIL_ROR_CI"] or "(空)"))
