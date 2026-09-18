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
    19_leave2024_hyperaesthesia.csv        the two paragraphs that follow 4C
    20_2024cluster_membership.csv
    21_alternative_proxy_terms.csv         the substitution in the Table S5 note

Numbers are read from the files; nothing is hard-coded here except three
corpus constants that no shipped artefact carries (see CONSTANTS below).

Splice discipline (changed in v1.7.1, after a destructive run)
    Earlier versions replaced everything between "### Table 4A." and
    "### Table S1", and everything between "### Table S5" and
    "## Figure legends". Both regions have since grown prose that the script
    does not own — Table 5 and Tables S6-S9 with Appendix S1 — so those runs
    silently deleted 240 lines of reviewed text. The script now replaces only
    the regions it emits and refuses to run if either region contains a
    heading it does not recognise, so new content can never be swallowed.
"""

from __future__ import annotations

import csv
import os
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")

PS = os.path.join(HERE, "04_sensitivity_ps_only.csv")
YR_PAIN = os.path.join(HERE, "04_sensitivity_year_pain.csv")
YR_HYPE = os.path.join(HERE, "04_sensitivity_year_hyperaesthesia.csv")
MAIN = os.path.join(HERE, "01_faers_results.csv")
LEAVE = os.path.join(HERE, "19_leave2024_hyperaesthesia.csv")
CLUSTER = os.path.join(HERE, "20_2024cluster_membership.csv")
ALTPROXY = os.path.join(HERE, "21_alternative_proxy_terms.csv")

DASH = "\u2014"
HEAD_4A = "### Table 4A."
HEAD_T5 = "### Table 5."
HEAD_S5 = "### Table S5"
HEAD_S6 = "### Table S6"

# Three corpus constants that no shipped CSV carries. They are asserted by
# _check_consistency.py, so a change here cannot pass the gate unnoticed.
SERIOUS_SUBSET_N = 11_882_968
SERIOUS_SUBSET_REMI = 5_270
REMI_COHORT_N = 5_375
INADEQUATE_ANALGESIA_TOTAL = 8_465

# The category column of 01_faers_results.csv has carried "negative-control"
# since the first run; section 2.3 now disclaims that reading, so the printed
# label is the one the text defends. Keeping the mapping here means a
# regeneration cannot silently restore a label the manuscript rejects.
LABEL = {"OIH-narrow": "OIH-narrow",
         "OIH-wide": "OIH-wide",
         "dictionary-proxy": "dictionary-proxy",
         "negative-control": "comparator term"}

WORD = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen"}


def rows(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main_row(pt):
    for x in rows(MAIN):
        if x["PT"] == pt:
            return x
    raise SystemExit(f"{pt} missing from 01_faers_results.csv")


def grp(n) -> str:
    """Thousands separated by a space, matching the rest of the manuscript."""
    return f"{int(n):,}".replace(",", " ")


def dp(value, places=2) -> str:
    """Round half up, so 0.015 prints as 0.02 rather than 0.01."""
    q = Decimal(1).scaleb(-places)
    return str(Decimal(str(value)).quantize(q, rounding=ROUND_HALF_UP))


def n3(v):
    return DASH if v in ("", None) else f"{float(v):.3f}"


def ci(v):
    # source files write "0.05-2.78"; the manuscript uses an en dash
    return DASH if v in ("", None) else str(v).replace("-", "\u2013")


def ci2(v):
    """Same, but rounded to two decimals as the note paragraphs print it."""
    return DASH if v in ("", None) else "\u2013".join(dp(p) for p in str(v).split("-"))


def yesno(v):
    return "yes" if str(v).strip().lower() == "true" else "no"


def andlist(items):
    items = [str(i) for i in items]
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def build_4a():
    r = rows(PS)
    out = [f"### Table 4A. Sensitivity analysis: FAERS restricted to serious reports, "
           f"all {len(r)} terms",
           "",
           "| Preferred term | Group | Remifentanil a | Remifentanil OR | Signal | "
           "RORR vs fentanyl (95% CI) | RORR vs morphine (95% CI) |",
           "|---|---|---:|---|---|---|---|"]
    for x in r:
        out.append(
            f"| {x['PT']} | {LABEL[x['category']]} | {x['REMIFENTANIL_a']} | {n3(x['REMIFENTANIL_ROR'])} | "
            f"{yesno(x['REMIFENTANIL_signal'])} | {n3(x['RORR_REMI_vs_FENTANYL'])} "
            f"({ci(x['RORR_CI_FENTANYL'])}) | {n3(x['RORR_REMI_vs_MORPHINE'])} "
            f"({ci(x['RORR_CI_MORPHINE'])}) |")
    hype = next(x for x in r if x["PT"] == "HYPERAESTHESIA")
    out += ["",
            "OR = reporting odds ratio; RORR = ratio of reporting odds ratios; CI = confidence "
            f"interval. Serious-report subset contained {grp(SERIOUS_SUBSET_N)} reports. "
            f"Remifentanil contributed {grp(SERIOUS_SUBSET_REMI)} of its {grp(REMI_COHORT_N)} "
            f"reports ({SERIOUS_SUBSET_REMI / REMI_COHORT_N * 100:.1f}%) to this subset. The signal "
            "criterion is the one used in the primary analysis (three or more reports with the "
            "lower confidence bound above one, or a proportional reporting ratio of two or more "
            "with a chi-squared above four, or an information component lower bound above zero). "
            f"All {WORD[int(hype['REMIFENTANIL_a'])]} remifentanil HYPERAESTHESIA reports are in "
            "this subset, so the corrected signal survives serious-report restriction.",
            ""]
    return "\n".join(out)


def build_4b():
    r = rows(YR_PAIN)
    est = [x for x in r if x.get("RORR_REMI_vs_FENTANYL") not in ("", None)]
    empty_years = [x["Year"] for x in r if str(x["REMIFENTANIL_a"]).strip() in ("", "0")]
    pooled = main_row("PAIN")
    pooled_a = int(pooled["REMIFENTANIL_a"])
    in_window = sum(int(x["REMIFENTANIL_a"]) for x in r)
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
            f"interval. Pooled whole-corpus values were {n3(pooled['RORR_REMI_vs_FENTANYL'])} "
            f"versus fentanyl and {n3(pooled['RORR_REMI_vs_MORPHINE'])} versus morphine. An "
            f"estimate was possible in {len(est)} of the ten years: in {andlist(empty_years)} "
            f"remifentanil had no PAIN report, so no estimate was possible. Of the {pooled_a} "
            f"pooled PAIN reports, {in_window} fall in 2015–2024 and {pooled_a - in_window} "
            f"outside it or have no date, so this table covers {in_window}.",
            ""]
    return "\n".join(out)


def build_4c():
    r = rows(YR_HYPE)
    est = [x for x in r if x.get("RORR_REMI_vs_FENTANYL") not in ("", None)]
    pooled = main_row("HYPERAESTHESIA")
    in_window = sum(int(x["REMIFENTANIL_a"]) for x in r)
    y2024 = next(int(x["REMIFENTANIL_a"]) for x in r if x["Year"] == "2024")
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
            f"interval. Pooled whole-corpus values were {n3(pooled['REMIFENTANIL_ROR'])} for "
            f"remifentanil, {n3(pooled['RORR_REMI_vs_FENTANYL'])} versus fentanyl and "
            f"{n3(pooled['RORR_REMI_vs_MORPHINE'])} versus morphine. An estimate was possible in "
            f"only {len(est)} of the ten years, because remifentanil contributed no report of the "
            f"term in {WORD[len(r) - len(est)]} of them; {WORD[in_window]} reports carry a usable "
            f"receivedate in 2015–2024 ({WORD[y2024]} of them in 2024), so the remifentanil column "
            f"sums to {WORD[in_window]}. In 2024 both head-to-head ratios exceed one with intervals that "
            f"exclude it. The pooled finding that remifentanil's signal is the weakest of the four "
            f"is therefore an average over a corpus in which the term is almost entirely reported "
            f"in a single recent year, and it is not stable across years.",
            ""]
    return "\n".join(out)


def build_4c_prose():
    """The two paragraphs that follow Table 4C, both derived from artefacts."""
    lv = {r["definition"]: r for r in rows(LEAVE)}
    whole = next(v for k, v in lv.items() if k.startswith("whole corpus"))
    window = next(v for k, v in lv.items() if k.startswith("calendar window"))
    pooled = main_row("HYPERAESTHESIA")["REMIFENTANIL_ROR"]
    dropped = int(whole["cohort_n"]) - int(window["cohort_n"])

    cl = {r["query"]: int(r["reports"]) for r in rows(CLUSTER)}
    remi = cl["remifentanil_with_term_2024"]
    suf = cl["sufentanil_with_term_2024"]
    suf_in = cl["sufentanil_with_term_2024_also_remifentanil"]
    fen = cl["fentanyl_with_term_2024"]
    fen_in = cl["fentanyl_with_term_2024_also_remifentanil"]
    mor = cl["morphine_with_term_2024"]
    if cl["morphine_with_term_2024_also_remifentanil"] != 0:
        raise SystemExit("morphine 2024 HYPERAESTHESIA reports now overlap the series: "
                         "the 'none of morphine's' clause is no longer true")

    p1 = ("Two restrictions of this table were examined and they are not the same thing. "
          f"Removing the 2024 reports from the whole corpus, which is the correct reading of "
          f"*leave 2024 out*, leaves {WORD[int(whole['a'])]} remifentanil reports in a cohort of "
          f"{grp(whole['cohort_n'])} against a background of {grp(whole['corpus_N'])}: reporting "
          f"odds ratio {dp(whole['ROR'])} (95% CI {dp(whole['ROR_CI_low'])}\u2013"
          f"{dp(whole['ROR_CI_high'])}), an interval that no longer contains the pooled {pooled} "
          f"and so shows the pooled comparison to be carried by the 2024 reports. Restricting the "
          f"analysis instead to the calendar window 2015\u20132023 \u2014 which also discards the "
          f"{grp(dropped)} remifentanil reports received before 2015 and replaces the background "
          f"with {grp(window['corpus_N'])} \u2014 leaves {WORD[int(window['a'])]} report in "
          f"{grp(window['cohort_n'])}: {dp(window['ROR'])} ({dp(window['ROR_CI_low'])}\u2013"
          f"{dp(window['ROR_CI_high'])}), a ratio against fentanyl of {dp(window['RORR_vs_fentanyl'])} "
          f"({ci2(window['RORR_CI'])}), and an interval wide enough to contain the pooled estimate, "
          f"which makes it uninformative rather than reassuring. The second restriction was "
          f"mislabelled as leave-2024-out in an earlier version of this analysis. Both are "
          f"recomputed in `19_leave2024_hyperaesthesia.csv`.")

    p2 = ("For the same reason, the 2024 elevation is not four cohorts' worth of reports: "
          f"conjunctive queries on the same corpus show that the case series of §3.3 supplies "
          f"{remi} of the {remi} remifentanil, {suf_in} of the {suf} sufentanil and {fen_in} of "
          f"the {fen} fentanyl HYPERAESTHESIA reports received in 2024, but none of morphine's "
          f"{mor} (`20_2024cluster_membership.csv`).")
    return p1 + "\n\n" + p2 + "\n"


def build_s5():
    r = rows(MAIN)
    comparators = [x for x in r if x["category"] == "negative-control"]
    pairs = [(x, d) for x in comparators for d in ("FENTANYL", "SUFENTANIL", "MORPHINE")]
    computable = [(x, d) for x, d in pairs if x[f"RORR_REMI_vs_{d}"] not in ("", None)]
    below = [(x, d) for x, d in computable if float(x[f"RORR_REMI_vs_{d}"]) < 1]
    above = [(x, d) for x, d in computable if float(x[f"RORR_REMI_vs_{d}"]) >= 1]
    if len(above) != 1:
        raise SystemExit(f"Table S5 note expects exactly one comparator ratio at or above one; "
                         f"found {len(above)}")
    (ex, exd), = above
    alt = {x["DRUG"]: x for x in rows(ALTPROXY)}

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
            "for the drug carrying the term. Every ratio uses the 2×2 convention of section 2.4, "
            f"so each can be recomputed from the counts alone. Across the {WORD[len(comparators)]} "
            f"comparator terms, {WORD[len(below)]} of the {WORD[len(computable)]} computable ratios "
            f"are below one; the exception is {ex['PT']} versus {exd.lower()} "
            f"({n3(ex[f'RORR_REMI_vs_{exd}'])}, {ci(ex[f'RORR_CI_{exd}'])}), whose interval "
            f"includes one. The substitution noted in section 4.4 is recomputed in "
            f"`21_alternative_proxy_terms.csv`: on INADEQUATE ANALGESIA "
            f"({grp(INADEQUATE_ANALGESIA_TOTAL)} reports in the corpus) remifentanil gives "
            f"{alt['REMIFENTANIL']['a']} reports and a reporting odds ratio of "
            f"{alt['REMIFENTANIL']['ROR']} ({ci(alt['REMIFENTANIL']['ROR_CI95'])}), against "
            f"{alt['SUFENTANIL']['ROR']} ({ci(alt['SUFENTANIL']['ROR_CI95'])}) for sufentanil and "
            f"{alt['MORPHINE']['ROR']} ({ci(alt['MORPHINE']['ROR_CI95'])}) for morphine, so the "
            f"ordering across those three opioids reverses; it stays below fentanyl, "
            f"{alt['FENTANYL']['ROR']} ({ci(alt['FENTANYL']['ROR_CI95'])}) on "
            f"{alt['FENTANYL']['a']} reports, the ratio against fentanyl being "
            f"{alt['REMI_vs_FENTANYL']['ROR']} ({ci(alt['REMI_vs_FENTANYL']['ROR_CI95'])}). The "
            f"ratios against sufentanil and morphine are {alt['REMI_vs_SUFENTANIL']['ROR']} "
            f"({ci(alt['REMI_vs_SUFENTANIL']['ROR_CI95'])}) and {alt['REMI_vs_MORPHINE']['ROR']} "
            f"({ci(alt['REMI_vs_MORPHINE']['ROR_CI95'])}), point estimates above one with intervals "
            f"that include it.",
            ""]
    return "\n".join(out)


def splice(text, start, end, new, expect_heads, label):
    """Replace [start, end) with `new`, after checking the region is ours."""
    i = text.index(start)
    j = text.index(end, i)
    heads = [l for l in text[i:j].splitlines() if l.startswith(("# ", "## ", "### "))]
    if len(heads) != len(expect_heads) or not all(
            h.startswith(p) for h, p in zip(heads, expect_heads)):
        raise SystemExit(
            f"{label}: refusing to overwrite {len(heads)} headings "
            f"({heads}) where {len(expect_heads)} were expected. The region has grown "
            f"content this script does not own; widen the generator instead of deleting it.")
    return text[:i] + new + text[j:]


def main() -> int:
    text = open(MS, encoding="utf-8").read()

    new4 = (build_4a() + "\n" + build_4b() + "\n" + build_4c() + "\n"
            + build_4c_prose() + "\n")
    text = splice(text, HEAD_4A, HEAD_T5, new4,
                  [HEAD_4A, "### Table 4B.", "### Table 4C."], "Tables 4A-4C")

    text = splice(text, HEAD_S5, HEAD_S6, build_s5() + "\n---\n\n",
                  [HEAD_S5], "Table S5")

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
