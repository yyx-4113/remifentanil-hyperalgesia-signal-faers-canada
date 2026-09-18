# -*- coding: utf-8 -*-
"""A7 补充 v2：Table S1 Panel B（FAERS）与 03_soc_27.csv 逐格核对（修正列索引）。"""
import csv, os, re, decimal
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
text = open(os.path.join(ROOT, "I_正文_IMRaD_en.md"), encoding="utf-8").read()
DRUGS = ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]
def rhu(x, d):
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

soc2 = {}
for line in open(os.path.join(ROOT, "03_soc_27.csv"), encoding="utf-8-sig"):
    if not line.strip() or line.startswith("#"): continue
    parts = next(csv.reader([line.rstrip("\n")]))
    if len(parts) >= 12 and parts[0] not in ("SOC", "Drug", "N_total_reactions") and not parts[0].startswith(("Unmapped", "Global")):
        soc2[parts[0]] = parts
P = {"REMIFENTANIL": 5375, "FENTANYL": 121819, "SUFENTANIL": 6513, "MORPHINE": 56501}
rows = get_table("**Panel B. FAERS, exploratory, event-level counts", ["Panel B is event-level:"])
print("Panel B 数据行数 =", len(rows) - 1)
bad = 0; tot = 0
for r in rows[1:]:
    if len(r) < 8: continue
    name = r[0]; src = soc2.get(name)
    if src is None:
        cand = [k for k in soc2 if k.startswith(name[:28])]
        if len(cand) == 1: src = soc2[cand[0]]
        else: print("  未匹配 SOC 名: %r" % name); continue
    for col, drug in zip(range(1, 5), DRUGS):
        i = DRUGS.index(drug)
        m = re.match(r"^(\d[\d\s]*)\s*\(([\d.]+)\)$", r[col])
        if not m: print("  无法解析 %s / %s = %r" % (name[:45], drug, r[col])); continue
        n = int(re.sub(r"\s", "", m.group(1))); shown = float(m.group(2)); tot += 1
        src_n = int(src[1 + i]); src_pct = float(src[5 + i])
        indep = 100.0 * n / P[drug]
        tags = []
        if n != src_n: tags.append("COUNT draft=%d src=%d" % (n, src_n))
        if abs(rhu(indep, 1) - shown) > 1e-9:
            tags.append("PCT draft=%.1f n/cohort=%.4f->%.1f (src %.2f)" % (shown, indep, rhu(indep, 1), src_pct))
        if tags:
            print("  X %-50s %-12s %s" % (name[:50], drug, "; ".join(tags))); bad += 1
    for col, idx, key in [(5, 9, "ROR"), (6, 10, "RORRfen"), (7, 11, "RORRmor")]:
        cell = r[col]; sv = src[idx]
        if cell.strip() in ("-", "\u2014", "\u2013", ""):
            if sv != "": print("  X %s / %s dash-but-src=%s" % (name[:45], key, sv)); bad += 1
        else:
            try: v = float(cell)
            except ValueError: print("  ? %s / %s = %r" % (name[:45], key, cell)); continue
            if sv == "" or abs(v - float(sv)) > 5e-4:
                print("  X %s / %s draft=%s src=%s" % (name[:45], key, v, sv)); bad += 1
print("Panel B 数字格数 = %d (应为 27*7=189)，问题 = %d" % (tot, bad))
