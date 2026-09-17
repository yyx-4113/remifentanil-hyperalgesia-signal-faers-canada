# -*- coding: utf-8 -*-
import io

p = 'I_正文_IMRaD_en.md'
s = open(p, encoding='utf-8').read()

reps = [
    # P1-4 L41 broken sentence
    ("offered as a methodological caution about terminology: we make the term-level check a null result in this field usually omits.",
     "offered as a methodological caution about terminology: we performed the term-level verification that a null result in this field usually omits."),
    # P1-1 L67 overstatement
    ("OPIOID WITHDRAWAL SYNDROME is carried by DRUG WITHDRAWAL SYNDROME;",
     "OPIOID WITHDRAWAL SYNDROME is approximated by the nearest retrievable preferred term, DRUG WITHDRAWAL SYNDROME;"),
    # P0-1 L109
    ("and eight of its ten reports fall in 2024 (\u00a73.8).",
     "and eight of the nine dated reports (eight of all ten) fall in 2024 (\u00a73.8)."),
    # P2-6 L123 Canada four opioids
    ("and remifentanil again reported least of the four opioids for pain.",
     "and remifentanil again reported least among the opioids with computable comparisons for pain."),
    # P0-1 L137 section 3.8
    ("remifentanil contributed no HYPERAESTHESIA report in eight of the ten years, eight of its ten reports fall in 2024, and in that year both ratios exceed one with intervals that exclude it (2.495, 1.06\u20135.90; 3.495, 1.52\u20138.05).",
     "remifentanil contributed no HYPERAESTHESIA report in eight of the ten years; eight of the nine reports with a usable receivedate within 2015\u20132024 fall in 2024, the tenth having no usable receivedate and being excluded from this table, and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06\u20135.90; 3.495, 1.52\u20138.05)."),
    # P2-5 L139 label
    ("### 3.9 Post hoc demonstration that the pipeline detects signals when present",
     "### 3.9 Post hoc, exploratory sanity check that the pipeline detects signals when present"),
    # P2-5 L141
    ("An analysis returning only negatives invites the objection that it is insensitive; the class analysis provided a post hoc check.",
     "An analysis returning only negatives invites the objection that it is insensitive; the class analysis provided a post hoc, exploratory sanity check."),
    # P0-1 L149 section 4.1
    ("though eight of the ten remifentanil reports fall in 2024 (\u00a73.8).",
     "though eight of the nine dated remifentanil reports fall in 2024 (\u00a73.8)."),
    # P1-2 L167 ranking
    ("and the ranking it produces (morphine 12.17, sufentanil 8.61, fentanyl 6.80, remifentanil 4.73) is the reverse of what the clinical literature predicts, so it carries reporting context as well as the syndrome.",
     "and the ranking it produces (morphine 12.17, sufentanil 8.61, fentanyl 6.80, remifentanil 4.73) differs from clinical intuition about remifentanil, though it cannot be read as evidence about pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition, so it carries reporting context as well as the syndrome."),
    # P2-7 L181 Vogel 85%
    ("where about 85% of signals overlap at the preferred-term level [30].",
     "where about 85% of signals overlap at the preferred-term level [30] (that figure is the EVDAS-referenced median preferred-term overlap across the three databases, not a pairwise or symmetric measure)."),
    # P1-3 L193 conclusion
    ("Its low reporting of pain and of four non-paradoxical opioid side effects, by contrast, is large, stable across serious-report restriction and the eight calendar years in which an estimate was possible, and reproduced in both databases.",
     "Its low reporting of pain, by contrast, is large, stable across serious-report restriction and the eight calendar years in which an estimate was possible, and its direction was reproduced in the Canadian database; its low reporting of the four negative controls was stable across the same FAERS restrictions but could not be tested in Canada, whose cohorts were too small for those ratios to be computed."),
    # P2-9 L217 DOI
    ("Every journal reference carries a DOI, as required by *Anaesthesia*.",
     "All journal articles carry a DOI, as required by *Anaesthesia*."),
    # P0-1 Table 4B footnote L349
    ("An estimate was possible in 8 of the ten years: in 2018 and 2019 remifentanil had no PAIN report, so no estimate was possible.",
     "An estimate was possible in 8 of the ten years: in 2018 and 2019 remifentanil had no PAIN report, so no estimate was possible. Of the 23 remifentanil PAIN reports in the pooled analysis, 13 carry a usable receivedate within 2015\u20132024 and 10 fall outside that window or have none, so this year-stratified table covers 13 reports."),
    # P0-1 Table 4C footnote L366 (anchor avoids CI dash-format mismatch)
    ("eight of its ten reports fall in 2024, where both head-to-head ratios exceed one with intervals that exclude it",
     "nine reports carry a usable receivedate within 2015\u20132024, eight of them in 2024; the tenth has no usable receivedate and is excluded from this table, so it holds nine rows. In 2024 both head-to-head ratios exceed one with intervals that exclude it"),
    # P2-2 Table S4 marker label L464
    ("The five rows marked *added* are dictionary proxies introduced by Amendment 1",
     "The five rows labelled *dictionary proxy (added a posteriori, 16 Sep 2026)* are dictionary proxies introduced by Amendment 1"),
    # P2-8 L533 FAERS total citation
    ("| FAERS total N and cohort counts | `01_faers_summary.md`; `_faers_cache.json` |",
     "| FAERS total N | `_faers_cache.json` |"),
    # P1-5 L539 add Table 4C source row
    ("Year-stratified PAIN (FAERS) | `04_sensitivity_year_pain.csv`",
     "Year-stratified PAIN (FAERS) | `04_sensitivity_year_pain.csv`\n| Year-stratified HYPERAESTHESIA (FAERS) | `04_sensitivity_year_hyperaesthesia.csv` |"),
    # P2-4 L161 pharmacologic vs reporting
    ("the comparison establishes only that remifentanil is reported differently, not that the molecule behaves differently.",
     "the comparison establishes only that remifentanil is reported differently, not that the molecule behaves differently. For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME at least part of the low reporting is likely physiological rather than a reporting artefact: remifentanil has no oral or transdermal formulation and an ultrashort half-life, so true tolerance and physical withdrawal are clinically uncommon, and a component of those low counts is therefore probably real."),
]

for a, b in reps:
    c = s.count(a)
    assert c == 1, "EXPECTED 1 but got %d for: %s" % (c, a[:70])
    s = s.replace(a, b)

# P2-3 Table S4 PT-status qualifier (4 occurrences)
c = s.count("not confirmed as a current preferred term")
assert c == 4, "PT qualifier count=%d" % c
s = s.replace("not confirmed as a current preferred term",
              "not confirmed as a current preferred term in these corpora")

open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("ALL %d replacements applied OK" % (len(reps) + 1))
