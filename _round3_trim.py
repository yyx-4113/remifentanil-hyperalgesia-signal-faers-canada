# -*- coding: utf-8 -*-
p = 'I_正文_IMRaD_en.md'
s = open(p, encoding='utf-8').read()
reps = [
    # L137 tighter
    ("remifentanil contributed no HYPERAESTHESIA report in eight of the ten years; eight of the nine reports with a usable receivedate within 2015\u20132024 fall in 2024, the tenth having no usable receivedate and being excluded from this table, and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06\u20135.90; 3.495, 1.52\u20138.05).",
     "remifentanil contributed no report in eight of the ten years; of the ten, eight are dated to 2024 and one has no usable receivedate (so the year table holds nine), and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06\u20135.90; 3.495, 1.52\u20138.05)."),
    # L366 tighter (current text has no trailing CI after "exclude it")
    ("nine reports carry a usable receivedate within 2015\u20132024, eight of them in 2024; the tenth has no usable receivedate and is excluded from this table, so it holds nine rows. In 2024 both head-to-head ratios exceed one with intervals that exclude it.",
     "nine reports carry a usable receivedate in 2015\u20132024 (eight in 2024); the tenth has none and is omitted, so the table holds nine rows. In 2024 both head-to-head ratios exceed one with intervals that exclude it."),
    # L349 tighter
    ("Of the 23 remifentanil PAIN reports in the pooled analysis, 13 carry a usable receivedate within 2015\u20132024 and 10 fall outside that window or have none, so this year-stratified table covers 13 reports.",
     "Of the 23 pooled PAIN reports, 13 fall in 2015\u20132024 and 10 outside it or have no date, so this table covers 13."),
    # L181 tighter
    ("where about 85% of signals overlap at the preferred-term level [30] (that figure is the EVDAS-referenced median preferred-term overlap across the three databases, not a pairwise or symmetric measure).",
     "where about 85% of signals overlap at the preferred-term level [30] (the EVDAS-referenced median PT-level overlap, not a pairwise figure)."),
    # L161 tighter
    ("For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME at least part of the low reporting is likely physiological rather than a reporting artefact: remifentanil has no oral or transdermal formulation and an ultrashort half-life, so true tolerance and physical withdrawal are clinically uncommon, and a component of those low counts is therefore probably real.",
     "For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal clinically uncommon."),
    # L167 tighter
    ("differs from clinical intuition about remifentanil, though it cannot be read as evidence about pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition, so it carries reporting context as well as the syndrome.",
     "differs from clinical intuition about remifentanil, though it cannot be read as evidence of pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition."),
    # L193 tighter conclusion
    ("Its low reporting of pain, by contrast, is large, stable across serious-report restriction and the eight calendar years in which an estimate was possible, and its direction was reproduced in the Canadian database; its low reporting of the four negative controls was stable across the same FAERS restrictions but could not be tested in Canada, whose cohorts were too small for those ratios to be computed.",
     "Its low reporting of pain, by contrast, is large, stable and reproduced in Canada (\u00a74.1); the four negative controls are stable within FAERS but could not be tested in Canada, whose cohorts were too small."),
    # L109 tighter (accurate: 8 in 2024, 1 in 2021, 1 undated)
    ("and eight of the nine dated reports (eight of all ten) fall in 2024 (\u00a73.8).",
     "and eight of the ten reports fall in 2024, one dated to 2021 and one undated (\u00a73.8)."),
]
for a, b in reps:
    c = s.count(a)
    assert c == 1, "EXPECTED 1 got %d: %s" % (c, a[:60])
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("trim applied, %d edits" % len(reps))
