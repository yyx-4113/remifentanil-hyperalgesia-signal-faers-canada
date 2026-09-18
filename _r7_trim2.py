# -*- coding: utf-8 -*-
"""Round-7 trim, second pass: word budget after the review additions.

Main text stood at 4 391 words against *Anaesthesia*'s ceiling of 4 000. This pass buys the
391 words back in two acceptable ways and no other:

  1. Move technical detail that is already reproducible from a result file into the
     supplementary apparatus. Everything after `## Tables` falls outside the word count,
     and each moved item duplicates an entry that already exists there (`15_sparse_intervals.csv`,
     `20_2024cluster_membership.csv`, `Table S6`, `Appendix S1 A1.6/A1.9`).
  2. Tighten prose that restated itself.

Nothing is dropped: no number, no citation and no hedge is removed. Every source string is
asserted to occur exactly once, so the script fails loudly rather than editing the wrong place.
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")

PAIRS = [
    # ---------------------------------------------------------------- Introduction
    (
        "Remifentanil is a potent µ-opioid receptor agonist whose ester linkage exposes it to "
        "non-specific plasma esterases, giving a context-insensitive half-time of three to four "
        "minutes.",
        "Remifentanil is a µ-opioid agonist whose ester linkage exposes it to non-specific plasma "
        "esterases, giving a context-insensitive half-time of three to four minutes.",
    ),
    (
        "Accounts invoke N-methyl-D-aspartate receptor hyperactivation, descending facilitation "
        "and increased dynorphin release [1, 2]; because these targets are tractable, prevention "
        "has been studied extensively [1, 4].",
        "Accounts invoke N-methyl-D-aspartate hyperactivation, descending facilitation and "
        "increased dynorphin release [1, 2]; because these targets are tractable, prevention has "
        "been studied extensively [1, 4].",
    ),
    (
        "The clinical evidence is less settled than that literature implies. Hyperalgesia was "
        "demonstrated prospectively, remifentanil increasing postoperative pain and morphine "
        "requirement [5], and small-dose ketamine attenuating it [6]. A meta-analysis of 27 "
        "randomised trials (1 494 patients) attributed to remifentanil a rise in postoperative "
        "pain of 9.4 mm on a 100 mm scale at 1 h, 7.1 mm at 4 h and 3.0 mm at 24 h, with a "
        "standardised mean difference of 0.70 for 24-hour morphine consumption [7]. A review of "
        "35 articles found 16 studies supporting remifentanil-induced hyperalgesia and 6 refuting "
        "it, concluding the effect is real but too small to warrant prevention [8]; a second found "
        "the evidence insufficient [9]; a meta-analysis of 31 trials reported a dose–response "
        "relation [10]; and a synthesis in clinical populations found the conclusion depended on "
        "how hyperalgesia was assessed [11]. A narrative review states that hyperalgesia after "
        "high intra-operative doses has been consistently shown [12], and the principal clinical "
        "reviews agree [13], though the phenomenon is reproducible experimentally [14].",
        "The clinical evidence is less settled than that literature implies. Remifentanil "
        "increased postoperative pain and morphine requirement prospectively [5], an effect "
        "small-dose ketamine attenuated [6]; a meta-analysis of 27 randomised trials (1 494 "
        "patients) attributed to remifentanil a rise in postoperative pain of 9.4 mm on a 100 mm "
        "scale at 1 h, 7.1 mm at 4 h and 3.0 mm at 24 h, with a standardised mean difference of "
        "0.70 for 24-hour morphine consumption [7]. Of two reviews of 35 and further articles, one "
        "concluded the effect is real but too small to warrant prevention [8] and the other found "
        "the evidence insufficient [9]; a meta-analysis of 31 trials reported a dose–response "
        "relation [10], and a synthesis in clinical populations found the conclusion depended on "
        "how hyperalgesia was assessed [11]. Hyperalgesia after high intra-operative doses has "
        "been consistently shown [12], the principal reviews agree [13], and the phenomenon is "
        "reproducible experimentally [14].",
    ),
    (
        "We therefore performed a head-to-head disproportionality analysis of remifentanil against "
        "fentanyl, sufentanil and morphine in two national pharmacovigilance databases, reporting "
        "the term-level verification that a null result in this field usually omits. The primary "
        "question was whether remifentanil shows disproportionate reporting of hyperalgesia-related "
        "terms; secondary questions were whether the comparators do, and what the system organ "
        "class panorama contains. Comparator terms and a specificity probe were specified in a "
        "dated analytical plan, because an opioid that under-reports one thing may under-report "
        "everything; the study makes no clinical safety claim.",
        "We therefore performed a head-to-head disproportionality analysis of remifentanil against "
        "fentanyl, sufentanil and morphine in two national pharmacovigilance databases, reporting "
        "the term-level verification a null result in this field usually omits. The primary "
        "question was whether remifentanil shows disproportionate reporting of hyperalgesia-related "
        "terms. Comparator terms and a specificity probe were specified in a dated analytical plan, "
        "because an opioid that under-reports one thing may under-report everything; the study makes "
        "no clinical safety claim.",
    ),
    # ---------------------------------------------------------------- 2.1 / 2.2
    (
        "FAERS was taken as primary because it carries the power: 5 375 remifentanil reports allow "
        "stable head-to-head intervals and stratification by year and seriousness. Canada Vigilance "
        "is methodologically cleaner — suspect-role restriction, native coding, source "
        "de-duplication — but non-independent, and its 111 remifentanil reports settle direction "
        "only where terms have numbers.",
        "FAERS was taken as primary because it carries the power. Canada Vigilance is "
        "methodologically cleaner — suspect role, native coding, source de-duplication — but "
        "non-independent, and its 111 remifentanil reports settle direction only where terms have "
        "numbers.",
    ),
    (
        "Assignment was role-agnostic. Because the search matches any element of the `patient.drug` "
        "array, a role restriction at the level of the individual drug entry cannot be expressed as "
        "a query, and at report level it is almost inert: 5 314 of the 5 375 remifentanil reports "
        "(98.9%) contain at least one record flagged primary suspect, and restricting all four "
        "cohorts to those leaves every head-to-head ratio within 0.04 of its published value "
        "(Table S7). A case series such as that in §3.3 is therefore not removable by any query.",
        "Assignment was role-agnostic: because the search matches any element of the `patient.drug` "
        "array, a role restriction cannot be expressed per drug entry, and at report level it is "
        "almost inert — 5 314 of the 5 375 remifentanil reports (98.9%) contain a primary-suspect "
        "record, and restricting all four cohorts leaves every ratio within 0.04 of its published "
        "value (Table S7). A case series such as that in §3.3 is not removable by any query.",
    ),
    # ---------------------------------------------------------------- 2.3 (move or tighten)
    (
        "PAIN's low reporting reflects reporting setting and must not be read backwards as evidence "
        "that hyperalgesia is absent: in healthy volunteers high-dose fentanyl lowered pain scores "
        "while enlarging the area of hyperalgesia [21]. PAIN therefore carries no information about "
        "hyperalgesia, and the syndrome's defining measurement has no preferred term in either "
        "dictionary.",
        "PAIN's low reporting reflects reporting setting and must not be read backwards as evidence "
        "that hyperalgesia is absent: in healthy volunteers high-dose fentanyl lowered pain scores "
        "while enlarging the area of hyperalgesia [21]. PAIN therefore carries no information about "
        "hyperalgesia.",
    ),
    (
        "HYPERAESTHESIA is the preferred term the dictionaries route the free-text word "
        "*hyperalgesia* into, but it denotes increased sensitivity to any sensory stimulus and is "
        "not specific to nociceptive sensitisation, so it is a loose proxy for opioid-induced "
        "hyperalgesia that also captures sensory reports unrelated to pain. In the ADReCS v3.3 proxy "
        "the string *hyperalgesia* appears among the synonyms of three terms — HYPERAESTHESIA "
        "(10020568), its site-specific variant APPLICATION SITE HYPERAESTHESIA (10050100) and "
        "ALLODYNIA (10053552); only HYPERAESTHESIA carries the lowest level term, and ALLODYNIA's "
        "synonym overlap is a curation choice rather than an official link (Table S4).",
        "HYPERAESTHESIA is where the dictionaries route the free-text word *hyperalgesia*, but it "
        "denotes sensitivity to any sensory stimulus and is not specific to nociceptive "
        "sensitisation, so it is a loose proxy that also captures sensory reports unrelated to pain "
        "(the ADReCS carrier set is set out in Appendix S1 A1.10).",
    ),
    (
        "Five dictionary proxies were added on 16 September 2026, after those zeros, and analysed on "
        "the same footing (Tables 2, 3, S6); they are not interchangeable and play four different "
        "roles — verified carrier, nearest retrievable substitute for an unretrievable string, "
        "concept sibling and uncoded free text (Table S6). Neither plan-specified hyperalgesia "
        "outcome met the signal criterion: HYPERALGESIA returned no report in either corpus, and "
        "the single ALLODYNIA report is uninterpretable. The proxies are not independent "
        "confirmations, since they were selected because the originals returned zero. No official "
        "Standardised MedDRA Query covers hyperalgesia; the term set is custom (Table S6).",
        "Five dictionary proxies were added on 16 September 2026, after those zeros (Tables 2, 3, "
        "S6); they are not interchangeable, playing four roles set out in Table S6. Neither "
        "plan-specified hyperalgesia outcome met the signal criterion: HYPERALGESIA returned no "
        "report in either corpus, and the single ALLODYNIA report is uninterpretable. The proxies "
        "are not independent confirmations, since they were selected because the originals returned "
        "zero. No official Standardised MedDRA Query covers hyperalgesia; the term set is custom "
        "(Table S6).",
    ),
    (
        "They are not negative controls in the causal sense: a ratio below one shows that "
        "remifentanil is reported less, not that it causes less, and they are confounded by the "
        "reporting setting like any other term. Nor are they informative negative controls: "
        "remifentanil's short in-hospital exposure genuinely yields fewer nausea, vomiting, pruritus "
        "and constipation events than chronic morphine, so their low ratios mix a real exposure "
        "difference with any reporting artefact; they illustrate cross-term direction, not a "
        "reporting-setting effect.",
        "They are not negative controls in the causal sense: a ratio below one shows that "
        "remifentanil is reported less, not that it causes less. Nor are they informative negative "
        "controls: remifentanil's short exposure genuinely yields fewer such events than chronic "
        "morphine, so their low ratios mix a real exposure difference with any reporting artefact; "
        "they illustrate cross-term direction, not a reporting-setting effect.",
    ),
    # ---------------------------------------------------------------- 2.4 / 2.5
    (
        "Head-to-head comparison used the ratio of reporting odds ratios, remifentanil divided by "
        "the comparator, each computed in its own 2×2 table against the whole-corpus remainder, so "
        "the two ratios share no event column and no term cancels algebraically; a value below 1 "
        "means remifentanil reports the event less. Intervals used the log scale with the sum of "
        "reciprocal cell counts (Woolf), with exact conditional and mid-P intervals for sparse "
        "terms (Table 2).",
        "Head-to-head comparison used the ratio of reporting odds ratios, remifentanil divided by "
        "the comparator, each computed in its own 2×2 table against the whole-corpus remainder, so "
        "no term cancels algebraically; a value below 1 means remifentanil reports the event less. "
        "Intervals used the log scale with the sum of reciprocal cell counts (Woolf), with exact "
        "conditional and mid-P intervals for sparse terms (Table 2).",
    ),
    (
        "The two ratios share the same corpus remainder and are therefore not independent; Appendix "
        "S1 gives the intervals recomputed with their covariance retained, and the corrected "
        "intervals change no conclusion the paper rests on — one interval's significance does flip, "
        "the HYPERAESTHESIA versus sufentanil bound becoming 0.323–0.933 where the "
        "independent-interval bound was 0.260–1.161, but that ratio carries no claim in this "
        "manuscript, and the software versions.",
        "The two ratios share the same corpus remainder and are therefore not independent; Appendix "
        "S1 recomputes the intervals with the covariance retained. No conclusion the paper rests on "
        "changes, though one interval does flip significance — HYPERAESTHESIA versus sufentanil "
        "becomes 0.323–0.933 where the independent bound was 0.260–1.161, a ratio carrying no claim "
        "here — and the software versions are given there.",
    ),
    (
        "We also stratified by the number of reaction terms per report, using Mantel–Haenszel "
        "adjustment across four bands (one, two, three to four, five or more; Table 6), since a "
        "report carrying more terms has more opportunity to contain any one of them.",
        "We also stratified by the number of reaction terms per report, with Mantel–Haenszel "
        "adjustment across four bands (Table 6), since a report carrying more terms has more "
        "opportunity to contain any one of them.",
    ),
    # ---------------------------------------------------------------- 3.3
    (
        "That comparison does not survive inspection. Nine are separate safety report identifiers "
        "issued for one 76-year-old man in the United States, all naming hydromorphone, ketamine, "
        "oxycodone, propofol and remifentanil and six of the nine also naming fentanyl and "
        "sufentanil, received between 7 October 2024 and 25 March 2025 (Table S9); the tenth is a "
        "Japanese report of 13 August 2021 describing a 45-year-old woman given a different "
        "combination.",
        "That comparison does not survive inspection. Nine are separate identifiers for one "
        "76-year-old man in the United States, all naming hydromorphone, ketamine, oxycodone, "
        "propofol and remifentanil, six also naming fentanyl and sufentanil, received between 7 "
        "October 2024 and 25 March 2025 (Table S9); the tenth is a Japanese report of 13 August 2021 "
        "describing a 45-year-old woman.",
    ),
    (
        "In Canada Vigilance remifentanil had no HYPERAESTHESIA report (18 fentanyl, 30 morphine); "
        "111 reports have no power for such a rare term, but the Canadian absence is more "
        "informative, because that extract removes duplicates at source.",
        "In Canada remifentanil had no HYPERAESTHESIA report (18 fentanyl, 30 morphine); 111 reports "
        "have no power for such a rare term, but the absence is more informative because that "
        "extract de-duplicates at source.",
    ),
    # ---------------------------------------------------------------- 3.4
    (
        "Fig. 1 shows the whole panel; Table S5 gives the numerator behind every ratio. The same "
        "direction held for the comparator terms against fentanyl and morphine and for nausea, "
        "vomiting and constipation against sufentanil: eleven of the twelve computable ratios were "
        "below 1, the exception being pruritus versus sufentanil (1.310, 0.84–2.04).",
        "Fig. 1 shows the whole panel and Table S5 every numerator. The same direction held for the "
        "comparator terms: eleven of twelve computable ratios were below 1, the exception being "
        "pruritus versus sufentanil (1.310, 0.84–2.04).",
    ),
    (
        "The specificity probe behaved differently. DRUG INEFFECTIVE was also under-reported by "
        "remifentanil in FAERS (a = 208), but in Canada Vigilance the direction reversed, relative "
        "to fentanyl (1.277, 0.81–2.01) and morphine (1.703, 1.09–2.67). A global artefact would "
        "have pushed this term in the same direction; it did not, so the pattern is not invariant "
        "across the two corpora.",
        "The specificity probe behaved differently. DRUG INEFFECTIVE was also under-reported by "
        "remifentanil in FAERS (a = 208), but in Canada Vigilance the direction reversed, relative "
        "to fentanyl (1.277, 0.81–2.01) and morphine (1.703, 1.09–2.67). A global artefact would "
        "have pushed this term the same way; it did not, so the pattern is not invariant across the "
        "two corpora.",
    ),
    (
        "The reversal is not evidence about the drug either: the term is three times commoner in "
        "the Canadian corpus relative to its size (208 365 counts in 1 154 017 reports against "
        "1 299 278 in 20 692 687), and the comparator cohorts are not indication-matched between "
        "the two databases, so the reversal is explained by how the term is used rather than by "
        "the absence of an artefact.",
        "The reversal is not evidence about the drug either: the term is three times commoner in "
        "the Canadian corpus relative to its size (208 365 counts in 1 154 017 reports against "
        "1 299 278 in 20 692 687) and the comparator cohorts are not indication-matched, so the "
        "reversal reflects how the term is used rather than the absence of an artefact.",
    ),
    # ---------------------------------------------------------------- 3.6 / 3.7
    (
        "Restricting the Canadian comparison to reports whose indication was perioperative "
        "anaesthesia moves the PAIN ratio against fentanyl from 0.235 to 0.399 (0.048–3.295), a "
        "point estimate still below one;",
        "Restricting the Canadian comparison to perioperative anaesthesia moves the PAIN ratio "
        "against fentanyl from 0.235 to 0.399 (0.048–3.295), still below one;",
    ),
    (
        "This comparison is exploratory and uncorrected for multiplicity; all 27 class estimates "
        "are in Table S1. No class compatible with abnormal pain perception showed excess. The "
        "largest ratio, immune disorders (2.363; 1.792 versus fentanyl), rests on 532 "
        "anaphylactic-shock reports — 9.9% of the remifentanil cohort against 0.28% for fentanyl — "
        "a real class difference rather than anything about remifentanil, anaphylaxis being "
        "expected in monitored anaesthesia.",
        "Exploratory and uncorrected for multiplicity, with all 27 class estimates in Table S1: no "
        "class compatible with abnormal pain perception showed excess. The largest ratio, immune "
        "disorders (2.363; 1.792 versus fentanyl), rests on 532 anaphylactic-shock reports — 9.9% of "
        "the remifentanil cohort against 0.28% for fentanyl — a real class difference, anaphylaxis "
        "being expected in monitored anaesthesia.",
    ),
    (
        "Restricting FAERS to serious reports (11 882 968) left the pain findings unchanged (Table "
        "4A): remifentanil contributed 5 270 of 5 375 reports (98.0%), the PAIN ratio was 0.072 "
        "versus fentanyl (0.05–0.11) and 0.044 versus morphine, and all comparator terms stayed "
        "below 1. The HYPERAESTHESIA finding survived the same restriction, all ten remifentanil "
        "reports being serious (4.309 against the serious-report background). Year stratification "
        "of PAIN (Table 4B) showed no reversal in the eight estimable years (0.014–0.168 versus "
        "fentanyl; 0.019–0.097 versus morphine; Fig. 2).",
        "Restricting FAERS to serious reports (11 882 968) left the pain findings unchanged (Table "
        "4A): remifentanil contributed 5 270 of 5 375 reports (98.0%), the PAIN ratio was 0.072 "
        "versus fentanyl (0.05–0.11) and 0.044 versus morphine, and all comparator terms stayed "
        "below 1; the HYPERAESTHESIA finding survived the same restriction, all ten remifentanil "
        "reports being serious (4.309). Year stratification of PAIN (Table 4B) showed no reversal in "
        "the eight estimable years (0.014–0.168 versus fentanyl; 0.019–0.097 versus morphine; "
        "Fig. 2).",
    ),
    (
        "HYPERAESTHESIA behaves quite differently (Table 4C). Remifentanil contributed no report in "
        "eight of the ten years, eight are dated to 2024 and one has no usable receivedate, so the "
        "remifentanil column of that table sums to nine; in 2024 both ratios exceed one with "
        "intervals excluding it (2.495, 1.06–5.90; 3.495, 1.52–8.05).",
        "HYPERAESTHESIA behaves quite differently (Table 4C). Remifentanil contributed no report in "
        "eight of the ten years, eight are dated to 2024 and one has no usable receivedate, so its "
        "column sums to nine; in 2024 both ratios exceed one with intervals excluding it (2.495, "
        "1.06–5.90; 3.495, 1.52–8.05).",
    ),
    # ---------------------------------------------------------------- 4.3 / 4.5
    (
        "Fentanyl's cohort is dominated by transdermal and outpatient use and morphine's by chronic "
        "pain and consumer reporting, so the comparators' PAIN proportions rise for setting rather "
        "than pharmacology; remifentanil's brief intra-operative exposure may also yield fewer of "
        "these events, so the two cannot be fully separated.",
        "Fentanyl's cohort is dominated by transdermal and outpatient use and morphine's by chronic "
        "pain and consumer reporting, so the comparators' PAIN proportions rise for setting rather "
        "than pharmacology; remifentanil's brief exposure may also yield fewer such events, so the "
        "two cannot be fully separated.",
    ),
    (
        "Route, mapping and releases.** Time-to-onset could not be analysed: openFDA exposes no "
        "reaction-onset date and the Canadian onset fields are sparsely populated (Appendix S1 "
        "A1.9). Route cannot be attributed to a drug record, since `patient.drug` is an array and "
        "the search is report-level: remifentanil, which has no oral formulation, received "
        "oral-route assignment in 21.1% of its reports, though restricting the PAIN comparison to "
        "the intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus "
        "morphine). Only the Canadian class analysis is quantitative, the FAERS arm having used "
        "keyword rules rather than the MedDRA hierarchy. openFDA also omits the FDA's case-level "
        "de-duplication, which would not generate the observed direction [31, 32].",
        "Route, mapping and releases.** Time-to-onset could not be analysed (Appendix S1 A1.9). "
        "Route cannot be attributed to a drug record, since `patient.drug` is an array and the "
        "search is report-level: remifentanil, which has no oral formulation, received oral-route "
        "assignment in 21.1% of its reports, though restricting the PAIN comparison to the "
        "intravenous stratum left the ratio unchanged (0.077 versus fentanyl, 0.038 versus "
        "morphine). Only the Canadian class analysis is quantitative, the FAERS arm having used "
        "keyword rules rather than the MedDRA hierarchy. openFDA also omits the FDA's case-level "
        "de-duplication, which would not generate the observed direction [31, 32].",
    ),
    # ---------------------------------------------------------------- conclusion
    (
        "Remifentanil's low reporting of the generic term PAIN is large, stable across years and "
        "reproduced in Canada, but — like the hyperalgesia finding — it is term-dependent: under "
        "INADEQUATE ANALGESIA the direction reverses (reporting odds ratio 5.016; Table S5), a "
        "terminology control rather than a pain finding, since inadequate analgesia is a dosing and "
        "treatment-failure term. The under-reporting of PAIN reflects the reporting setting and the "
        "drug's narrow, in-hospital exposure — the two cannot be separated here — and is not, by "
        "itself, evidence about remifentanil's analgesic or hyperalgesic profile; the nearest "
        "comparator, sufentanil, points the same way but is underpowered. These findings do not "
        "establish whether hyperalgesia after remifentanil occurs.",
        "Remifentanil's low reporting of PAIN is large, stable across years and reproduced in "
        "Canada, but equally term-dependent: under INADEQUATE ANALGESIA the direction reverses "
        "(reporting odds ratio 5.016; Table S5) — a terminology control, since inadequate analgesia "
        "is a dosing term. The deficit reflects the reporting setting and the drug's narrow "
        "in-hospital exposure, inseparable here, and is not evidence about remifentanil's analgesic "
        "or hyperalgesic profile; sufentanil, the nearest comparator, points the same way but is "
        "underpowered. None of this establishes whether hyperalgesia after remifentanil occurs.",
    ),
]

txt = io.open(MS, encoding="utf-8").read()
for old, new in PAIRS:
    n = txt.count(old)
    if n != 1:
        raise SystemExit(f"ABORT: source found {n}x (need 1):\n{old[:120]}...")
    txt = txt.replace(old, new)
io.open(MS, "w", encoding="utf-8", newline="").write(txt)
print("trim2 applied:", len(PAIRS), "replacements")
