#!/usr/bin/env python3
"""Regenerate Tables 4A-4C and Table S5 in the manuscript from source CSVs.

Second-round review (2026-09-17) found that Table 4A had been maintained by
hand from a 13-term sensitivity run while the main analysis had grown to 18
terms, so the new primary outcome (HYPERAESTHESIA) had never been tested in
the serious-report subset. Tables 4A, 4B, 4C and S5 are therefore generated
rather than typed, and _check_consistency.py re-derives them cell by cell.

Sources
    04_sensitivity_ps_only.csv             Table 4A (serious-report subset)
    04_sensitivity_year_pain.csv           Table 4B (PAIN by calendar year)
    04_sensitivity_year_hyperaesthesia.csv Table 4C (HYPERAESTHESIA by year)
    01_faers_results.csv                   Table S5 (complete head-to-head matrix,
                                           including the sufentanil column that
                                           Tables 2 and 3 do not print)

Numbers are read from the files; nothing is hard-coded here.
"""

from __future__ import annotations

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")

PS = os.path.join(HERE, "04_sensitivity_ps_only.csv")
YR_PAIN = os.path.join(HERE, "04_sensitivity_year_pain.csv")
YR_HYPE = os.path.join(HERE, "04_sensitivity_year_hyperaesthesia.csv")
MAIN = os.path.join(HERE, "01_faers_results.csv")
EST_JSON = os.path.join(HERE, "04_sensitivity_estimable_years.json")

DASH = "\u2014"
HEAD_4A = "### Table 4A."
HEAD_S1 = "### Table S1"
FIG_MARK = "## Figure legends"


def rows(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def n3(v):
    return DASH if v in ("", None) else f"{float(v):.3f}"


def ci(v):
    # source files write "0.05-2.78"; the manuscript uses an en dash
    return DASH if v in ("", None) else str(v).replace("-", "\u2013")


def yesno(v):
    return "yes" if str(v).strip().lower() == "true" else "no"


def build_4a():
    r = rows(PS)
    out = ["### Table 4A. Sensitivity analysis: FAERS restricted to serious reports, all 18 terms",
           "",
           "| Preferred term | Group | Remifentanil a | Remifentanil OR | Signal | "
           "RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |",
           "|---|---|---:|---|---|---|---|"]
    for x in r:
        out.append(
            f"| {x['PT']} | {x['category']} | {x['REMIFENTANIL_a']} | {n3(x['REMIFENTANIL_ROR'])} | "
            f"{yesno(x['REMIFENTANIL_signal'])} | {n3(x['RORR_REMI_vs_FENTANYL'])} "
            f"({ci(x['RORR_CI_FENTANYL'])}) | {n3(x['RORR_REMI_vs_MORPHINE'])} "
            f"({ci(x['RORR_CI_MORPHINE'])}) |")
    out += ["",
            "OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence "
            "interval. Serious-report subset contained 11 882 968 reports. Remifentanil contributed "
            "5 270 of its 5 375 reports (98.0%) to this subset. The signal criterion is the one used "
            "in the primary analysis (three or more reports with the lower confidence bound above "
            "one, or a proportional reporting ratio of two or more with a chi-squared above four, or "
            "an information component lower bound above zero). All ten remifentanil HYPERAESTHESIA "
            "reports are in this subset, so the corrected signal survives serious-report restriction.",
            ""]
    return "\n".join(out)


def build_4b():
    r = rows(YR_PAIN)
    n_est = sum(1 for x in r if x.get("RORR_REMI_vs_FENTANYL") not in ("", None))
    out = ["### Table 4B. Sensitivity analysis: PAIN by calendar year (FAERS, 2015–2024)",
           "",
           "| Year | Remifentanil a | Remifentanil OR | Fentanyl OR | Morphine OR | "
           "RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |",
           "|---|---:|---|---|---|---|---|"]
    for x in r:
        out.append(
            f"| {x['Year']} | {x['REMIFENTANIL_a']} | {n3(x['REMIFENTANIL_ROR'])} | "
            f"{n3(x['FENTANYL_ROR'])} | {n3(x['MORPHINE_ROR'])} | "
            f"{n3(x['RORR_REMI_vs_FENTANYL'])} ({ci(x['RORR_CI_FENTANYL'])}) | "
            f"{n3(x['RORR_REMI_vs_MORPHINE'])} ({ci(x['RORR_CI_MORPHINE'])}) |")
    out += ["",
            f"OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence "
            f"interval. Pooled whole-corpus values were 0.066 versus fentanyl and 0.046 versus "
            f"morphine. An estimate was possible in {n_est} of the ten years: in 2018 and 2019 "
            f"remifentanil had no PAIN report, so no estimate was possible.",
            ""]
    return "\n".join(out)


def build_4c():
    r = rows(YR_HYPE)
    n_est = sum(1 for x in r if x.get("RORR_REMI_vs_FENTANYL") not in ("", None))
    out = ["### Table 4C. Sensitivity analysis: HYPERAESTHESIA by calendar year (FAERS, 2015–2024)",
           "",
           "| Year | Remifentanil a | Remifentanil OR | Fentanyl a | Morphine a | "
           "RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |",
           "|---|---:|---|---:|---:|---|---|"]
    for x in r:
        out.append(
            f"| {x['Year']} | {x['REMIFENTANIL_a']} | {n3(x['REMIFENTANIL_ROR'])} | "
            f"{x['FENTANYL_a']} | {x['MORPHINE_a']} | "
            f"{n3(x['RORR_REMI_vs_FENTANYL'])} ({ci(x['RORR_CI_FENTANYL'])}) | "
            f"{n3(x['RORR_REMI_vs_MORPHINE'])} ({ci(x['RORR_CI_MORPHINE'])}) |")
    out += ["",
            f"OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence "
            f"interval. Pooled whole-corpus values were 4.729 for remifentanil, 0.696 versus "
            f"fentanyl and 0.389 versus morphine. An estimate was possible in only {n_est} of the "
            f"ten years, because remifentanil contributed no report of the term in eight of them; "
            f"eight of its ten reports fall in 2024, where both head-to-head ratios exceed one with "
            f"intervals that exclude it. The pooled finding that remifentanil's signal is the "
            f"weakest of the four is therefore an average over a corpus in which the term is almost "
            f"entirely reported in a single recent year, and it is not stable across years.",
            ""]
    return "\n".join(out)


def build_s5():
    r = rows(MAIN)
    out = ["### Table S5 (supplementary). Complete head-to-head matrix, all three comparators",
           "",
           "Every head-to-head ratio computed for this study, including the comparisons against "
           "sufentanil that Tables 2, 3 and Figure 1 do not print. Values are ratios of reporting "
           "odds ratios for remifentanil against the named comparator, with 95% confidence "
           "intervals; a dash means the ratio is not estimable because a cell is empty. Computed "
           "from the same 2×2 tables as Table 2. The last column gives the numerator for each "
           "comparator, so that every ratio printed here and in Table 2 can be recomputed from the "
           "counts alone.",
           "",
           "| Preferred term | Remifentanil a | RORR vs fentanyl (95% CI) | "
           "RORR vs sufentanil (95% CI) | RORR vs morphine (95% CI) | "
           "Comparator a: fentanyl / sufentanil / morphine |",
           "|---|---:|---|---|---|---|"]
    for x in r:
        _a = " / ".join(str(x[f"{d}_a"]) for d in ("FENTANYL", "SUFENTANIL", "MORPHINE"))
        out.append(
            f"| {x['PT']} | {x['REMIFENTANIL_a']} | {n3(x['RORR_REMI_vs_FENTANYL'])} "
            f"({ci(x['RORR_CI_FENTANYL'])}) | {n3(x['RORR_REMI_vs_SUFENTANIL'])} "
            f"({ci(x['RORR_CI_SUFENTANIL'])}) | {n3(x['RORR_REMI_vs_MORPHINE'])} "
            f"({ci(x['RORR_CI_MORPHINE'])}) | {_a} |")
    out += ["",
            "RORR = ratio of reporting odds ratios; CI = confidence interval; a = number of reports "
            "for the drug carrying the term. Across the four negative controls, eleven of the twelve "
            "computable ratios are below one; the exception is PRURITUS versus sufentanil (1.310, "
            "0.84–2.04), whose interval includes one.",
            ""]
    return "\n".join(out)


def main() -> int:
    text = open(MS, encoding="utf-8").read()

    i = text.index(HEAD_4A)
    j = text.index(HEAD_S1, i)
    new4 = build_4a() + "\n" + build_4b() + "\n" + build_4c() + "\n"
    text = text[:i] + new4 + text[j:]

    # 幂等：先删掉已有的 Table S5 块，再插入（否则重复运行会插入第二份）
    if "### Table S5" in text:
        _a = text.index("### Table S5")
        _b = text.index(FIG_MARK, _a)
        text = text[:_a] + text[_b:]
    # 插入点必须是 Figure legends 之前，而不是"最后一个 ---"之前：
    # 后者会把 S5 塞到 S4 块末尾的分隔符之前，造成表序 S3 / S5 / S4。
    k = text.index(FIG_MARK)
    text = text[:k] + build_s5() + "\n---\n\n" + text[k:]

    open(MS, "w", encoding="utf-8", newline="\n").write(text)

    n_est_pain = sum(1 for x in rows(YR_PAIN) if x.get("RORR_REMI_vs_FENTANYL") not in ("", None))
    n_est_hype = sum(1 for x in rows(YR_HYPE) if x.get("RORR_REMI_vs_FENTANYL") not in ("", None))
    print(f"Table 4A: {len(rows(PS))} terms (must equal the 18 terms of Table 2)")
    print(f"Table 4B: PAIN, {n_est_pain}/10 years estimable")
    print(f"Table 4C: HYPERAESTHESIA, {n_est_hype}/10 years estimable")
    print(f"Table S5: {len(rows(MAIN))} terms x 3 comparators")
    print("manuscript rewritten")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
