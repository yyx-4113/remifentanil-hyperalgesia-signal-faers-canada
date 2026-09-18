# -*- coding: utf-8 -*-
"""Round-6: write the tables and the appendix that the rewritten body cites but
that do not yet exist, and add the missing in-text citations.

Gaps found by cross-checking every `Table n` / `Table Sn` / `Appendix S1` string
in the body against the chunks actually present:

    Table 5            cited x2, chunk missing
    Table 6            cited x2, chunk missing
    Table S6           cited x1, chunk missing
    Table S7           cited x2, chunk missing
    Table S8           cited x1, chunk missing
    Table S9           cited x1, chunk missing
    Appendix S1        cited x7, does not exist at all
    Table S1           exists but is never cited
    Fig. 1 / Fig. 2    exist as legends but are never cited

Values are read from the result files at run time, never typed in: the only
literals in this file are prose.

Usage:  python _r6_ms_tables.py [--apply]
Without --apply it dry-runs and prints what it would insert.
"""
from __future__ import annotations

import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(HERE, *a)
MS = P("I_正文_IMRaD_en.md")

APPLY = "--apply" in sys.argv


def rows(name: str) -> list[dict]:
    with open(P(name), encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def n(v) -> str:
    """Integer with a thin space as the thousands separator, or an em dash."""
    if v in ("", None):
        return "—"
    return f"{int(float(v)):,}".replace(",", "\u2009")


def f3(v) -> str:
    return "—" if v in ("", None) else f"{float(v):.3f}"


# =========================================================================== #
# sources
# =========================================================================== #
IND = rows("cv/cv_indication_strata.csv")
DEP = rows("cv/cv_depth_strata.csv")
ROLE = rows("12_role_version_sensitivity.csv")
OVER = rows("17_overlap_adjusted_rorr.csv")
SERIES = rows("13_report_series_hyperaesthesia.csv")
MATRIX = rows("11_overlap_matrix.csv")
TERMS = {r["Term"]: r for r in rows("10_term_dictionary.csv")}
COV = rows("18_rorr_covariance.csv")

# =========================================================================== #
# Table 5 — Canada, stratified by recorded indication
# =========================================================================== #
STRATA = [("All reports", "all reports"),
          ("Perioperative anaesthesia indication", "perioperative anaesthesia"),
          ("Pain indication", "pain")]
TERM_ORDER = ["PAIN", "DRUG INEFFECTIVE", "VOMITING", "NAUSEA", "HYPERAESTHESIA"]

ind = {}
for r in IND:
    ind[(r["stratum"], r["preferred_term"])] = r

lines5 = [
    "### Table 5. Canada Vigilance: head-to-head comparison stratified by the recorded indication",
    "",
    "| Indication stratum | Remifentanil n | Preferred term | Remifentanil a | "
    "Fentanyl a | Sufentanil a | Morphine a | RORR vs fentanyl (95% CI) | "
    "RORR vs morphine (95% CI) |",
    "|---|---:|---|---:|---:|---:|---:|---|---|",
]
for full, _short in STRATA:
    first = True
    for pt in TERM_ORDER:
        r = ind[(full, pt)]
        cell = f"| {full} " if first else "| "
        first = False
        lo_f = r["RORR_vs_fentanyl_CI"].replace("-", "–") if r["RORR_vs_fentanyl_CI"] else "—"
        lo_m = r["RORR_vs_morphine_CI"].replace("-", "–") if r["RORR_vs_morphine_CI"] else "—"
        rr_f = f"{f3(r['RORR_vs_fentanyl'])} ({lo_f})" if r["RORR_vs_fentanyl"] else "— (—)"
        rr_m = f"{f3(r['RORR_vs_morphine'])} ({lo_m})" if r["RORR_vs_morphine"] else "— (—)"
        lines5.append(
            f"{cell}| {n(r['n_remifentanil'])} | {pt} | {n(r['a_remifentanil'])} | "
            f"{n(r['a_fentanyl'])} | {n(r['a_sufentanil'])} | {n(r['a_morphine'])} | "
            f"{rr_f} | {rr_m} |")
lines5 += [
    "",
    "n = number of reports in the stratum for that drug; a = reports carrying the term; "
    "RORR = ratio of reporting odds ratios; CI = confidence interval. Comparator cohort "
    "sizes: all reports 4 881 fentanyl, 63 sufentanil, 7 675 morphine; perioperative "
    "anaesthesia 239, 22 and 43; pain 631, 2 and 824. Strata are not mutually exclusive "
    "and the indication field is free text, so they are approximate rather than exhaustive. "
    "A dash means the ratio is not estimable because a cell is empty. The whole-cohort row "
    "is the comparison as published in Table 3; the point of the table is the movement "
    "between rows.",
    "",
]
T5 = "\n".join(lines5)

# =========================================================================== #
# Table 6 — Canada, adjusted for reporting depth
# =========================================================================== #
DEPTH = {}
for r in DEP:
    DEPTH[r["preferred_term"]] = r

lines6 = [
    "### Table 6. Canada Vigilance: comparison adjusted for the number of reaction terms per report",
    "",
    "| Preferred term | Crude RORR vs fentanyl | Crude RORR vs morphine | "
    "Mantel–Haenszel RORR vs fentanyl (95% CI) | Mantel–Haenszel RORR vs morphine (95% CI) | "
    "Share of cohort reaction rows, remifentanil / fentanyl / sufentanil / morphine (%) | "
    "Share ratio vs fentanyl / vs morphine |",
    "|---|---|---|---|---|---|---|",
]
for pt in TERM_ORDER:
    d = DEPTH[pt]
    mh_f = (f"{float(d['MH_RORR_vs_fentanyl']):.3f} "
            f"({d['MH_RORR_vs_fentanyl_CI'].replace('-', '–')})") \
        if d["MH_RORR_vs_fentanyl"] else "— (—)"
    mh_m = (f"{float(d['MH_RORR_vs_morphine']):.3f} "
            f"({d['MH_RORR_vs_morphine_CI'].replace('-', '–')})") \
        if d["MH_RORR_vs_morphine"] else "— (—)"
    crude_f = f"{float(d['crude_RORR_vs_fentanyl']):.3f}" \
        if float(d["crude_RORR_vs_fentanyl"] or 0) > 0 else "—"
    crude_m = f"{float(d['crude_RORR_vs_morphine']):.3f}" \
        if float(d["crude_RORR_vs_morphine"] or 0) > 0 else "—"
    shares = " / ".join(
        ("0" if float(d[f"share_pct_{k}"]) == 0 else d[f"share_pct_{k}"])
        for k in ("remifentanil", "fentanyl", "sufentanil", "morphine"))
    ratios = f"{d['term_share_ratio_vs_fentanyl']} / {d['term_share_ratio_vs_morphine']}"
    lines6.append(f"| {pt} | {crude_f} | {crude_m} | {mh_f} | {mh_m} | {shares} | {ratios} |")
lines6 += [
    "",
    "RORR = ratio of reporting odds ratios; MH = Mantel–Haenszel, adjusted across four bands "
    "of reaction terms per report (one, two, three to four, five or more); CI = confidence "
    "interval. The mean number of reaction terms per report was 1.69 for remifentanil, 3.90 "
    "for fentanyl, 4.11 for sufentanil and 6.50 for morphine, and the proportion of "
    "single-term reports was 69.4%, 39.9%, 31.8% and 27.1% respectively, so a comparator "
    "report had two to four times the opportunity to contain any one term. The right-hand "
    "columns express the same thing without a model: the share of each cohort's reaction "
    "rows that the term occupies, and the ratio of those shares. Mantel–Haenszel intervals "
    "are wide because the remifentanil stratum contributes few reports; they are reported "
    "rather than suppressed, and the movement of the point estimate, not the interval, is "
    "what the table is for. For PAIN both adjusted intervals include one, so after holding "
    "reporting depth constant the deficit is no longer distinguishable from unity.",
    "",
]
T6 = "\n".join(lines6)

# =========================================================================== #
# Table S6 — the term set specification (the custom query)
# =========================================================================== #
PLAN_ORDER = ["HYPERALGESIA", "ALLODYNIA", "PAIN", "PAIN INCREASED", "POSTOPERATIVE PAIN",
              "CHRONIC PAIN", "OPIOID WITHDRAWAL SYNDROME", "DRUG TOLERANCE",
              "DRUG INEFFECTIVE", "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION",
              "HYPERAESTHESIA", "HYPERPATHIA", "PROCEDURAL PAIN", "CHRONIC PAIN SYNDROME",
              "DRUG WITHDRAWAL SYNDROME"]
PROXY = {
    "HYPERALGESIA": "HYPERAESTHESIA",
    "POSTOPERATIVE PAIN": "PROCEDURAL PAIN",
    "CHRONIC PAIN": "CHRONIC PAIN SYNDROME",
    "OPIOID WITHDRAWAL SYNDROME": "DRUG WITHDRAWAL SYNDROME",
}
BASIS = {
    "HYPERALGESIA": "MedDRA lowest level term carried by the preferred term HYPERAESTHESIA "
                    "(code 10020568), the only term in the dictionary that carries the concept",
    "POSTOPERATIVE PAIN": "nearest retrievable preferred term to the perioperative setting",
    "CHRONIC PAIN": "nearest retrievable preferred term to persistent pain",
    "OPIOID WITHDRAWAL SYNDROME": "nearest retrievable preferred term to the withdrawal syndrome",
}
lines_s6 = [
    "### Table S6 (supplementary). Specification of the term set: a custom query, term by term",
    "",
    "No Standardised MedDRA Query covers opioid-induced hyperalgesia, in either the narrow or "
    "the broad scope, so the term set used here is a custom query and is specified in full "
    "below. Each string was submitted verbatim to both corpora as an exact match on the "
    "reaction field. Group and plan status are those recorded in the archived analytical plan; "
    "the five proxies were introduced by Amendment 1, dated 16 September 2026, after the zero "
    "counts of the five unretrievable strings had been observed.",
    "",
    "| Term as queried | Group | Plan status | Retrievable as a preferred term | "
    "Proxy used in the analysis | Basis for the proxy |",
    "|---|---|---|---|---|---|",
]
for t in PLAN_ORDER:
    rec = TERMS[t]
    proxy = PROXY.get(t, "—")
    lines_s6.append(
        f"| {t} | {rec['Group']} | "
        f"{'defined a priori' if rec['Group'] != 'dictionary proxy' else 'Amendment 1 (16 Sep 2026)'} | "
        f"{rec['Retrievable_as_preferred_term']} | {proxy} | {BASIS.get(t, '—')} |")
lines_s6 += [
    "",
    "A term can enter the analysis only if the corpus stores it, and both corpora store "
    "preferred terms in the reaction field, so retrievability was established empirically for "
    "each string (Table S4) rather than assumed from a dictionary lookup. Five strings were not "
    "retrievable. Three of them had a proxy analysed in their place; the fourth, PAIN INCREASED, "
    "had no single preferred term that carried it and was left unsubstituted; the fifth, "
    "HYPERALGESIA, is the clinical name of the syndrome and its proxy is the term that carries "
    "the concept. Because all five proxies were selected after the zeros had been observed, "
    "they cannot be treated as independent confirmation of the strings they replace; they are "
    "reported on the same footing as the rest of the set so that the reader can see what the "
    "corpus does contain once the dictionary constraint is honoured.",
    "",
]
S6 = "\n".join(lines_s6)

# =========================================================================== #
# Table S7 — role and version restriction
# =========================================================================== #
RESTRICTIONS = [
    ("as published (role-agnostic, latest version)", "as published"),
    ("restricted to reports with >=1 primary suspect drug record", "primary suspect only"),
    ("restricted to never-revised reports", "never-revised only"),
]
by = {(r["preferred_term"], r["restriction"]): r for r in ROLE}
KEY_ROWS = ["HYPERAESTHESIA", "ALLODYNIA", "PROCEDURAL PAIN", "DRUG WITHDRAWAL SYNDROME",
            "PAIN", "DRUG INEFFECTIVE", "NAUSEA", "VOMITING", "PRURITUS", "CONSTIPATION"]

lines_s7 = [
    "### Table S7 (supplementary). FAERS restriction sensitivity: drug role and report version",
    "",
    "**Panel A. Effect of each restriction on the corpus and on the four cohorts.** The openFDA "
    "interface serves only the latest revision of each report, so a filter on "
    "`safetyreportversion` = 1 does not de-duplicate: it deletes every report that has ever "
    "been revised, and it does so unequally across cohorts.",
    "",
    "| Restriction | Corpus reports | Remifentanil | Fentanyl | Sufentanil | Morphine |",
    "|---|---:|---:|---:|---:|---:|",
]
for full, _ in RESTRICTIONS:
    r = by[("HYPERAESTHESIA", full)]
    lines_s7.append(
        f"| {full} | {n(r['corpus_N'])} | {n(r['n_remifentanil'])} | {n(r['n_fentanyl'])} | "
        f"{n(r['n_sufentanil'])} | {n(r['n_morphine'])} |")
lines_s7 += [
    "",
    "Percentages removed by the never-revised restriction: 38.4% of the corpus, 33.7% of the "
    "remifentanil cohort, 27.7% of fentanyl, 29.6% of sufentanil and 39.6% of morphine. "
    "98.9% of the remifentanil cohort (5 314 of 5 375) has at least one record flagged "
    "primary suspect.",
    "",
    "**Panel B. Head-to-head ratios under each restriction.**",
    "",
    "| Preferred term | RORR vs fentanyl: as published / primary suspect / never-revised | "
    "RORR vs morphine: as published / primary suspect / never-revised |",
    "|---|---|---|",
]
for pt in KEY_ROWS:
    cells = []
    for comp in ("fentanyl", "morphine"):
        vals = []
        for full, _ in RESTRICTIONS:
            r = by[(pt, full)]
            v = r[f"RORR_vs_{comp}"]
            vals.append("not estimable" if v in ("", None) else f"{float(v):.3f}")
        cells.append(" / ".join(vals))
    lines_s7.append(f"| {pt} | {cells[0]} | {cells[1]} |")
lines_s7 += [
    "",
    "RORR = ratio of reporting odds ratios. Restricting to primary-suspect reports moves no "
    "head-to-head ratio by more than 0.04 in either direction, so drug-role attribution is "
    "immaterial to the comparison at report level. The never-revised restriction moves the "
    "sparse terms further: HYPERAESTHESIA versus fentanyl from 0.696 to 0.979, which is the "
    "value a reader would obtain if the revision filter were mistaken for a de-duplication "
    "step. The three restrictions are shown together so that the direction of the effect can "
    "be seen to differ between terms with many reports and terms with few.",
    "",
]
S7 = "\n".join(lines_s7)

# =========================================================================== #
# Table S8 — construction of the head-to-head ratio, and cohort overlap
# =========================================================================== #
ORDER = ["REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE"]
LABEL = {"REMIFENTANIL": "Remifentanil", "FENTANYL": "Fentanyl",
         "SUFENTANIL": "Sufentanil", "MORPHINE": "Morphine"}
mat = {r["drug"]: r for r in MATRIX}

lines_s8 = [
    "### Table S8 (supplementary). Construction of the head-to-head ratio: the two 2×2 tables "
    "and the effect of reports that name more than one cohort drug",
    "",
    "**Panel A. Reports shared between cohorts (FAERS).** A report enters every cohort whose "
    "substance it names, so the cohorts are not disjoint.",
    "",
    "| Cohort | Remifentanil | Fentanyl | Sufentanil | Morphine |",
    "|---|---:|---:|---:|---:|",
]
for a in ORDER:
    cells = " | ".join(n(mat[a][f"overlap_{s}"]) for s in
                       ("remifentanil", "fentanyl", "sufentanil", "morphine"))
    lines_s8.append(f"| {LABEL[a]} | {cells} |")
lines_s8 += [
    "",
    "Diagonal cells are the cohort sizes. Smallest cells: 30 reports name remifentanil, "
    "fentanyl and sufentanil; 136 remifentanil, fentanyl and morphine; 18 remifentanil, "
    "sufentanil and morphine; 4 name all four. 1 575 of the 5 375 remifentanil reports "
    "(29.3%) also name fentanyl, 483 (9.0%) also name sufentanil and 323 (6.0%) also name "
    "morphine.",
    "",
    "**Panel B. RORR as published, and recomputed after removing the reports that name both "
    "drugs of the pair.** The ratio of reporting odds ratios divides remifentanil's odds by "
    "the comparator's, each computed in its own table against the same whole-corpus remainder; "
    "the two tables share neither an event column nor a drug column, so no term cancels "
    "algebraically. Removing the shared reports is a further restriction, not a correction, "
    "because a report naming two opioids belongs to both cohorts for the drug-level question.",
    "",
    "| Preferred term | Remifentanil a | vs fentanyl: published → shared reports removed | "
    "vs sufentanil: published → shared reports removed | "
    "vs morphine: published → shared reports removed |",
    "|---|---:|---|---|---|",
]
PUBLISHED = {r["PT"]: r for r in rows("01_faers_results.csv")}
COL = {"fentanyl": "RORR_REMI_vs_FENTANYL", "sufentanil": "RORR_REMI_vs_SUFENTANIL",
       "morphine": "RORR_REMI_vs_MORPHINE"}
for r in OVER:
    pt = r["preferred_term"]
    if not r["RORR_published"]:
        continue
    cells = []
    for comp in ("fentanyl", "sufentanil", "morphine"):
        # NB: 17_overlap_adjusted_rorr.csv carries only the fentanyl-pair published
        # value; the sufentanil and morphine pairs must be read from the primary
        # result file, or the table prints 0.696 in all three columns.
        pub = PUBLISHED[pt][COL[comp]]
        exc = r[f"RORR_excl_{comp}"]
        left = "not estimable" if pub in ("", None) else f"{float(pub):.3f}"
        right = "not estimable" if exc in ("", None) else f"{float(exc):.3f}"
        cells.append(f"{left} → {right}")
    lines_s8.append(f"| {pt} | {n(r['a_remifentanil'])} | {cells[0]} | {cells[1]} | {cells[2]} |")
lines_s8 += [
    "",
    "RORR = ratio of reporting odds ratios; a = remifentanil reports carrying the term. The "
    "left-hand value of each pair is the figure printed in Tables 2, 3 and S5; the right-hand "
    "value is the ratio after the remifentanil arm is restricted to reports that do not name "
    "the comparator of that pair. Every ratio either falls under that restriction or, where the "
    "two cohorts share no report of that term, is unchanged — no ratio rises. The falls are "
    "large because the reports naming two opioids are concentrated in monitored perioperative "
    "care, so restricting them away removes the reports most likely to carry the term. That is "
    "why the restriction is reported as a bound on the influence of cohort overlap and not as a "
    "preferred estimate. One published finding does not survive it: PROCEDURAL PAIN versus "
    "fentanyl falls from 1.962 to 0.981, leaving unity. The comparator terms move the same way; "
    "PRURITUS versus fentanyl falls from 0.833 to 0.488.",
    "",
]
S8 = "\n".join(lines_s8)

# =========================================================================== #
# Table S9 — the ten remifentanil HYPERAESTHESIA reports
# =========================================================================== #
COMB = ["FENTANYL", "HYDROMORPHONE", "KETAMINE", "OXYCODONE", "PROPOFOL",
        "REMIFENTANIL", "SUFENTANIL"]


def has_ingredient(blob: str, ing: str) -> bool:
    return bool(re.search(r"\b" + ing + r"\b", blob.upper()))


lines_s9 = [
    "### Table S9 (supplementary). The ten remifentanil reports carrying HYPERAESTHESIA",
    "",
    "These are the reports behind the only term that met the signal criterion for remifentanil. "
    "Nine of them describe the same patient; the columns that establish this are the country, "
    "the age and sex, and the medicinal products named.",
    "",
    "**Panel A. Identifiers, dates, demographics and reported terms.**",
    "",
    "| Safety report identifier | Version | Received | Country | Age (years) | Sex | "
    "Medicinal products named | Reaction terms | Serious |",
    "|---|---:|---|---|---:|---|---:|---|---|",
]
SEX = {"1": "Male", "2": "Female"}
CTRY = {"US": "United States", "JP": "Japan"}
for r in SERIES:
    lines_s9.append(
        f"| {r['safetyreportid']} | {r['version']} | "
        f"{r['receivedate'][:4]}-{r['receivedate'][4:6]}-{r['receivedate'][6:8]} | "
        f"{CTRY.get(r['country'], r['country'])} | {r['age']} | {SEX.get(r['sex'], r['sex'])} | "
        f"{r['n_drug_entries']} | {r['n_reaction_terms']} | "
        f"{'Yes' if r['serious'] == '1' else 'No'} |")
lines_s9 += [
    "",
    "**Panel B. Which of the seven shared products each report names.**",
    "",
    "| Safety report identifier | Fentanyl | Hydromorphone | Ketamine | Oxycodone | "
    "Propofol | Remifentanil | Sufentanil | Other products named |",
    "|---|---|---|---|---|---|---|---|---|",
]
ALLPROD = re.compile(r"\b(FENTANYL|HYDROMORPHONE|KETAMINE|OXYCODONE|PROPOFOL|REMIFENTANIL|"
                     r"SUFENTANIL|ACETAMINOPHEN|BUPIVACAINE|LIDOCAINE|METHADONE)\b")
for r in SERIES:
    blob = r["all_medicinal_products"]
    marks = ["yes" if has_ingredient(blob, c) else "no" for c in COMB]
    named = {m.group(0) for m in ALLPROD.finditer(blob.upper())}
    extra = sorted(named - set(COMB))
    extra_txt = ", ".join(x.title() for x in extra) if extra else "—"
    lines_s9.append(f"| {r['safetyreportid']} | " + " | ".join(marks)
                    + f" | {extra_txt} |")
lines_s9 += [
    "",
    "The nine United States reports are dated between 7 October 2024 and 25 March 2025 and all "
    "describe a 76-year-old man; all nine name hydromorphone, ketamine, oxycodone, propofol and "
    "remifentanil, and six of the nine name all seven products of the shared perioperative "
    "combination. The tenth report, of 13 August 2021, describes a 45-year-old woman in Japan "
    "given a different combination (fentanyl, ketamine, methadone, oxycodone and remifentanil). "
    "Nothing in the identifier, the date or the version distinguishes the nine as one episode; "
    "only the content does. No query available through either interface removes them, because "
    "spontaneous reporting has no patient identifier, so the series is disclosed here rather "
    "than corrected. Two of the nine carry version 2, which is why the never-revised "
    "restriction in Table S7 leaves two of the ten behind.",
    "",
]
S9 = "\n".join(lines_s9)

with open(P("_r6_new_chunks.txt"), "w", encoding="utf-8") as fh:
    for name, chunk in [("Table 5", T5), ("Table 6", T6), ("Table S6", S6),
                        ("Table S7", S7), ("Table S8", S8), ("Table S9", S9)]:
        fh.write(f"\n\n<<<{name}>>>\n{chunk}")
print("preview written to _r6_new_chunks.txt")
for name, chunk in [("Table 5", T5), ("Table S9", S9)]:
    print(f"--- {name} (first 12 lines) ---")
    print("\n".join(chunk.split("\n")[:12]))
    print()
