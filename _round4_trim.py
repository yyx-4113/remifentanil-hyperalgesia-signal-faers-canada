#!/usr/bin/env python3
# Round-4 main-text trim: cut ~207 words (4207 -> <=4000) without touching gated strings.
# Unicode escapes: em-dash \u2014, en-dash \u2013, times \u00d7, section \u00a7
F = "I_正文_IMRaD_en.md"
s = open(F, encoding="utf-8").read()
reps = []
def add(old, new, tag):
    reps.append((old, new, tag))

# T2 (L161) compress cohort-composition paragraph; keep 'ultrashort half-life'
add(
"Cohort composition explains the pattern more parsimoniously: remifentanil's reports come almost entirely from monitored perioperative care (91.9% serious in Canada; 98.0% serious in the sensitivity subset), predominantly from health professionals, and among opioids the reporter's professional identity strongly determines which reactions are recorded [25]. Fentanyl's cohort is dominated by transdermal and outpatient use and morphine's by chronic pain and consumer reporting, so the comparators' PAIN proportions rise for reasons of setting and indication rather than pharmacology: the comparison establishes only that remifentanil is reported differently, not that the molecule behaves differently. For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal clinically uncommon.",
"Cohort composition explains the pattern: remifentanil's reports come almost entirely from monitored perioperative care (91.9% serious in Canada; 98.0% in the sensitivity subset), and among opioids the reporter's professional identity strongly determines which reactions are recorded [25]. Fentanyl's cohort is dominated by transdermal and outpatient use and morphine's by chronic pain and consumer reporting, so the comparators' PAIN proportions rise for setting and indication, not pharmacology. For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal clinically uncommon.",
"T2")

# T5 (L181) compress geographic independence; keep 'EVDAS-referenced median'
add(
"**Limited geographic independence.** FAERS and Canada Vigilance are both North American systems sharing MedDRA coding and much the same drug market, so agreement here is weaker evidence than across regulatory regions, where about 85% of signals overlap at the preferred-term level [30] (the EVDAS-referenced median PT-level overlap, not a pairwise figure). Neither a European nor a Japanese database was used here: EudraVigilance releases no bulk line-listing, and retrieval and validation of the Japanese database were not completed. Cross-regional confirmation remains a planned extension, and this is a two-database, single-continent analysis.",
"**Limited geographic independence.** FAERS and Canada Vigilance are both North American systems sharing MedDRA coding and much the same drug market, so agreement here is weaker than across regulatory regions, where about 85% of signals overlap at the preferred-term level [30] (the EVDAS-referenced median PT-level overlap, not a pairwise figure). Neither a European nor a Japanese database was used: EudraVigilance releases no bulk line-listing and Japanese retrieval was not completed, so this is a two-database, single-continent analysis.",
"T5")

# T6 (L141) compress sanity-check; keep 'exploratory sanity check' and em-dash
add(
"An analysis returning only negatives invites the objection that it is insensitive; the class analysis provided a post hoc, exploratory sanity check. Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by anaphylactic shock (532 events) and reaction (367), and the same excess appeared in Canada (2.363). It therefore detects signals, supporting \u2014 not proving \u2014 that the absent hyperalgesia signal reflects the data, not the method.",
"An analysis returning only negatives invites the objection that it is insensitive; the class analysis was a post hoc, exploratory sanity check. Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by anaphylactic shock (532 events) and reaction (367), also seen in Canada (2.363), supporting \u2014 not proving \u2014 that the absent hyperalgesia signal reflects the data, not the method.",
"T6")

# T16 (L127) trim cohort details
add(
"Cohort composition explains the pattern without invoking pharmacology. Remifentanil's Canadian cohort was overwhelmingly serious (102/111, 91.9% against 79.8% for fentanyl and 69.0% for morphine; sufentanil 58/63, 92.1%) and came predominantly from non-physician health professionals (72/111, 64.9%; 17.1% physicians; 5.4% consumers), whereas morphine's included 23.6% consumer and 7.0% physician reports (Table S3): the signature of a drug reported from monitored perioperative care.",
"Cohort composition explains the pattern without invoking pharmacology. Remifentanil's Canadian cohort was overwhelmingly serious (102/111, 91.9% against 79.8% for fentanyl and 69.0% for morphine) and came predominantly from non-physician health professionals (72/111, 64.9%), whereas morphine's included 23.6% consumer and 7.0% physician reports (Table S3): the signature of a drug reported from monitored perioperative care.",
"T16")

# T4 (L177) compress MedDRA releases; keep v27.1 and section sign
add(
"**Heuristic mapping and MedDRA releases.** The exploratory FAERS class analysis used keyword rules rather than the MedDRA hierarchy, and event-level counting; all quantitative class conclusions rest on the Canadian analysis. The two databases are coded to different releases \u2014 the Canadian extract states v27.1 for every reaction row, whereas FAERS spans quarterly releases from 2004 \u2014 so a term could be promoted or demoted between releases, which is why the verification in \u00a72.3 reads what the corpora contain rather than a dictionary.",
"**Heuristic mapping and MedDRA releases.** The exploratory FAERS class analysis used keyword rules rather than the MedDRA hierarchy, and event-level counting; all quantitative class conclusions rest on the Canadian analysis. The two databases are coded to different releases (the Canadian extract states v27.1 throughout; FAERS spans releases from 2004), so a term could shift between releases, which is why \u00a72.3 reads what the corpora contain.",
"T4")

# T3 (L167) compress first two sentences of 4.4; keep em-dashes
add(
"The most useful contribution here is terminological. The most obvious query \u2014 the clinical word HYPERALGESIA \u2014 returns nothing in either database. That zero is not about remifentanil, reporting or the syndrome; it is about the dictionary, because the concept is carried by a preferred term no clinician would type: HYPERAESTHESIA.",
"The most useful contribution here is terminological. The obvious query \u2014 the clinical word HYPERALGESIA \u2014 returns nothing; that zero is about the dictionary, not the syndrome, because the concept is carried by a preferred term no clinician would type: HYPERAESTHESIA.",
"T3")

# T15 (L167) drop explanatory clause before ref
add(
"In a field with an active prevention literature that difference is not academic, because a stream of null results is otherwise read as accumulating evidence of safety [26, 27];",
"In a field with an active prevention literature that difference is not academic [26, 27];",
"T15")

# T1 (L159) drop trailing clause
add(
"Remifentanil under-reported the four negative controls, PAIN, HYPERAESTHESIA and DRUG WITHDRAWAL SYNDROME, so analgesic superiority cannot be inferred: that reading would also require superiority on pruritus and constipation, for which no pharmacological account exists.",
"Remifentanil under-reported the four negative controls, PAIN, HYPERAESTHESIA and DRUG WITHDRAWAL SYNDROME, so analgesic superiority cannot be inferred: that reading would also require superiority on pruritus and constipation.",
"T1")

# T13 (L171) compress risk sentence
add(
"**Spontaneous reporting measures reporting, not risk.** Disproportionality estimates reporting patterns, not incidence, and can neither exclude nor quantify a real pharmacological effect. The corrected hyperalgesia finding rests on ten remifentanil reports, and the 111-report Canadian cohort has no power for a term this rare; prospective studies with quantitative sensory testing remain the appropriate instrument [24].",
"**Spontaneous reporting measures reporting, not risk.** Disproportionality estimates reporting, not incidence, and cannot quantify a real pharmacological effect. The corrected hyperalgesia finding rests on ten remifentanil reports and the 111-report Canadian cohort has no power for a term this rare; prospective studies with quantitative sensory testing remain the appropriate instrument [24].",
"T13")

# T7 (L123) trim Canadian last sentence; keep times sign
add(
"Most Canadian comparisons are uncomputable, a 2\u00d72 cell being empty, so Canada settles direction only where it has the numbers.",
"Most Canadian comparisons are uncomputable (an empty 2\u00d72 cell), so Canada settles direction only where it has numbers.",
"T7")

# T14 (L109) trim Canada sentence
add(
"In Canada Vigilance remifentanil had no HYPERAESTHESIA report, against 18 for fentanyl and 30 for morphine; 111 reports have no power for a term this rare, so Canada neither confirms nor refutes the FAERS signal.",
"In Canada Vigilance remifentanil had no HYPERAESTHESIA report (18 fentanyl, 30 morphine); 111 reports have no power for a term this rare, so Canada neither confirms nor refutes the FAERS signal.",
"T14")

# T8 (L131) drop redundant FAERS class sentence
add(
"no class compatible with hyperalgesia or abnormal pain perception showed excess. The exploratory FAERS analysis agreed in direction (general disorders 0.188; immune disorders 10.951). Full class-by-class values are in Table S1.",
"no class compatible with hyperalgesia or abnormal pain perception showed excess. Full class-by-class values are in Table S1.",
"T8")

# T9 (L149) trim principal-findings filler
add(
"Three findings stand out, the first qualifying the others.",
"Three findings stand out.",
"T9")

# T10 (L187) tighten implications sentence
add(
"For pharmacovigilance the implication is terminological: find which preferred term carries the concept, and report a zero from the clinical name as unretrievable, not reassuring.",
"For pharmacovigilance the implication is terminological: find which preferred term carries the concept and report a clinical-name zero as unretrievable, not reassuring.",
"T10")

# T11 (L135) tighten year-strat sentence
add(
"Year stratification of PAIN (Table 4B) showed no reversal in the eight years in which an estimate was possible (0.014\u20130.168 versus fentanyl; 0.019\u20130.097 versus morphine).",
"Year stratification of PAIN (Table 4B) showed no reversal in the eight estimable years (0.014\u20130.168 versus fentanyl; 0.019\u20130.097 versus morphine).",
"T11")

ok = True
for old, new, tag in reps:
    n = s.count(old)
    if n != 1:
        print(f"FAIL [{tag}] count={n}")
        ok = False
        continue
    s = s.replace(old, new, 1)
    print(f"OK   [{tag}]")

if not ok:
    print("ABORT")
    raise SystemExit(1)

open(F, "w", encoding="utf-8").write(s)
print(f"\nALL {len(reps)} trims applied OK")
