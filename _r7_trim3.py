# -*- coding: utf-8 -*-
"""Round-7 trim, third pass: the last 111 words.

Two moves only. First, relocate to Appendix S1 (A1.10, new) the two stretches that duplicate
apparatus already printed there — the justification for the primary/secondary split, and the
ADReCS carrier set for *hyperalgesia*. Section A1.10 sits after `## Tables` and so falls
outside the counted main text, exactly as A1.2 already carries the matching rule that the
`Substring matching` sentence below restates. Second, tighten wording that says twice what it
could say once.

Same guard as before: every source string must appear exactly once.
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")

PAIRS = [
    (
        "FAERS was taken as primary because it carries the power. Canada Vigilance is "
        "methodologically cleaner — suspect role, native coding, source de-duplication — but "
        "non-independent, and its 111 remifentanil reports settle direction only where terms have "
        "numbers.",
        "FAERS was taken as primary and Canada Vigilance as the comparison set; A1.10 sets out why.",
    ),
    (
        "Substring matching was rejected because it admits distinct substances sharing a stem.",
        "Substring matching was rejected (A1.2).",
    ),
    (
        "Three findings were reproduced in Canada (Table 3): the five non-retrievable strings "
        "returned zero in both corpora; the PAIN under-reporting direction was the same (0.066 and "
        "0.046 in FAERS against 0.235 and 0.146 in Canada); and remifentanil again reported least "
        "among the opioids with computable pain comparisons. The exception: no Canadian remifentanil "
        "report carried HYPERAESTHESIA while both comparators did. Of the comparator terms only "
        "vomiting could be tested in Canada, where remifentanil contributed three reports and the "
        "ratio was 1.07 against fentanyl and 0.39 against morphine; the others were empty. The two "
        "corpora are not independent, so this is a comparison, not a confirmation.",
        "Three findings were reproduced in Canada (Table 3): the five non-retrievable strings "
        "returned zero; the PAIN direction was the same (0.066 and 0.046 in FAERS against 0.235 and "
        "0.146 in Canada); and remifentanil again reported least among opioids with computable pain "
        "comparisons. The exception: no Canadian remifentanil report carried HYPERAESTHESIA while "
        "both comparators did. Of the comparator terms only vomiting was testable, at 1.07 against "
        "fentanyl and 0.39 against morphine on three reports; the others were empty. The corpora are "
        "not independent, so this is a comparison, not a confirmation.",
    ),
    (
        "The most useful contribution here is terminological. The obvious query, the clinical word "
        "HYPERALGESIA, returns nothing;",
        "The contribution is terminological. The obvious query, the clinical word HYPERALGESIA, "
        "returns nothing;",
    ),
    (
        "For clinicians, these data support neither a large remifentanil-specific hyperalgesia "
        "reporting burden nor its absence — one report in 200 to 500, depending on the drug "
        "(Table 2) — so decisions about prevention should rest on the prospective literature [7, 8]. "
        "For pharmacovigilance the implication is terminological: find which preferred term carries "
        "the concept, and report a clinical-name zero as unretrievable, not reassuring. The "
        "READUS-PV checklist is provided as Supporting Information (Table S2).",
        "For clinicians, these data support neither a large hyperalgesia reporting burden nor its "
        "absence — one report in 200 to 500, depending on the drug (Table 2) — so prevention "
        "decisions should rest on the prospective literature [7, 8]. For pharmacovigilance the "
        "implication is terminological: find which preferred term carries the concept, and report a "
        "clinical-name zero as unretrievable, not reassuring. READUS-PV reporting is in Supporting "
        "Information (Table S2).",
    ),
    (
        "Setting and geographic independence.** The corpora are coded to different releases (the "
        "Canadian extract states v27.1 throughout; FAERS spans releases from 2004), and the "
        "comparators are used in different settings, so differences reflect setting and indication "
        "as much as pharmacology; no drug-specific effect can be isolated, and §4.3 is an "
        "interpretation consistent with the subgroup data, not a mediation analysis. Both databases "
        "are North American, so agreement here is weaker than across regulatory regions, where about "
        "85% of signals overlap at the preferred-term level [33]; neither a European nor a Japanese "
        "database was used.",
        "Setting and geographic independence.** The corpora are coded to different releases (Canada "
        "v27.1 throughout; FAERS spans releases from 2004), and the comparators are used in "
        "different settings, so differences reflect setting and indication as much as pharmacology; "
        "no drug-specific effect can be isolated, and §4.3 is an interpretation consistent with the "
        "subgroup data, not a mediation analysis. Both databases are North American, where about 85% "
        "of signals overlap at the preferred-term level across regions [33]; neither European nor "
        "Japanese databases were used.",
    ),
    (
        "Tables 2, 3 and S5 report it as a term-level demonstration of what the corpus contains, not "
        "as a signal, and no clinical inference is drawn from it.",
        "Tables 2, 3 and S5 report it as a term-level demonstration, not a signal, and no clinical "
        "inference is drawn from it.",
    ),
    (
        "and three measures were computed: the reporting odds ratio, the proportional reporting "
        "ratio [23] and the information component with BCPNN shrinkage [24, 25]; formulae in "
        "Appendix S1.",
        "and three measures computed: the reporting odds ratio, the proportional reporting ratio "
        "[23] and the information component with BCPNN shrinkage [24, 25]; formulae in Appendix S1.",
    ),
    (
        "Remifentanil also under-reports PAIN and eleven of twelve computable comparator-term "
        "ratios, stably across serious-report restriction and the eight estimable years;",
        "Remifentanil also under-reports PAIN and eleven of twelve computable comparator-term "
        "ratios, stably across serious-report restriction and eight estimable years;",
    ),
]

A1_10 = """
**A1.10 Why FAERS is the primary corpus, and which terms carry "hyperalgesia" in ADReCS.** FAERS was taken as primary because it carries the power: 5 375 remifentanil reports allow stable head-to-head intervals and stratification by year and seriousness. Canada Vigilance is methodologically cleaner — suspect-role restriction, native coding, source de-duplication — but it is not independent of the primary analysis, and its 111 remifentanil reports settle direction only where the terms have numbers. Neither was preferred for correctness alone, the two denominators are not comparable in scale, and they were not pooled; only the direction of effects was compared.

In the ADReCS v3.3 proxy the string *hyperalgesia* appears among the synonyms of three terms — HYPERAESTHESIA (10020568), its site-specific variant APPLICATION SITE HYPERAESTHESIA (10050100) and ALLODYNIA (10053552). Only HYPERAESTHESIA carries the corresponding MedDRA lowest level term; the ALLODYNIA overlap is a curation choice of that ontology rather than an official MedDRA link, so Table S6 lists ALLODYNIA as a concept sibling and not as a second carrier. ADReCS does not state which MedDRA release v3.3 is built on, so the negative finding is bridged to v27.1 rather than proven within it (`_r6_term_dictionary_check.csv`, `_r6_term_level_check.csv`). ADReCS v3.3 also carries no entry named Hyperalgesia among its 15 317 entries, so the string has no preferred term of its own anywhere in that coded resource.

"""

txt = io.open(MS, encoding="utf-8").read()
for old, new in PAIRS:
    n = txt.count(old)
    if n != 1:
        raise SystemExit(f"ABORT: source found {n}x (need 1):\n{old[:120]}...")
    txt = txt.replace(old, new)

anchor = "\n## Acknowledgements"
if txt.count(anchor) != 1:
    raise SystemExit("ABORT: Acknowledgements anchor not unique")
txt = txt.replace(anchor, A1_10 + "---\n" + anchor)
io.open(MS, "w", encoding="utf-8", newline="").write(txt)
print("trim3 applied:", len(PAIRS), "replacements + A1.10 inserted")
