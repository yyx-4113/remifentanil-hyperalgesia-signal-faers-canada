#!/usr/bin/env python3
# Round-4 (M1/M2/P1/P2) manuscript edits. Each replacement asserted count==1.
import io, sys

F = "I_正文_IMRaD_en.md"
s = open(F, encoding="utf-8").read()
reps = []

def add(old, new, tag):
    reps.append((old, new, tag))

# 1) Title: drop misleading a-priori implication, foreground terminology caution
add(
"# Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with negative controls defined a priori",
"# Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with a terminology caution",
"M1-title")

# 2a) Abstract Methods: disclose prespecified hyperalgesia outcomes non-estimable
add(
"the proxies were added after the zeros and dated in the plan. Signals required at least three reports with a lower confidence bound above one;",
"the proxies were added after those zeros, dated in the plan, because the two prespecified hyperalgesia terms (HYPERALGESIA, ALLODYNIA) were non-estimable, so the analysis became hypothesis-generating and the proxies are reported as exploratory. Signals required at least three reports with a lower confidence bound above one;",
"M1-abs-methods")

# 2b) Abstract Results: signal rests on 2024 cluster, disappears when excluded
add(
"met the signal criterion for all four opioids, remifentanil included (4.73, 95% confidence interval 2.54–8.80); remifentanil's was the smallest and did not reproduce.",
"met the signal criterion for all four opioids, remifentanil included (4.73, 2.54–8.80), but the signal rests on ten reports, eight in 2024, and disappears when 2024 is excluded (a = 1); it did not reproduce.",
"M2-abs-results")

# 3) §2.3: declaration that prespecified hyperalgesia outcomes produced no result + P1-3 selection-bias limitation
add(
"they are reported as additions rather than a priori outcomes, and the amendment is dated in the plan.",
"they are reported as additions rather than a priori outcomes, and the amendment is dated in the plan. Consequently the two prespecified hyperalgesia outcomes (HYPERALGESIA, ALLODYNIA) produced no estimable result, so the study is reported as hypothesis-generating rather than confirmatory. The proxies are not independent confirmations of the prespecified strings: they share the same corpora and were selected because the originals returned zero, so they cannot be counted as separate evidence.",
"M1+S1-3-sec23")

# 4) §3.3: leave-2024 pointer
add(
"Remifentanil's was the weakest (0.696, 0.37–1.31, versus fentanyl; 0.389, 0.21–0.73, versus morphine), and eight of the ten reports fall in 2024, one dated to 2021 and one undated (§3.8).",
"Remifentanil's was the weakest (0.696, 0.37–1.31, versus fentanyl; 0.389, 0.21–0.73, versus morphine), and eight of the ten reports fall in 2024, one dated to 2021 and one undated (§3.8); excluding 2024 leaves one report and no signal (§3.8).",
"M2-sec33")

# 5) §3.8: leave-2024-out result + 2024 shared cluster
add(
"The corrected signal is not stable in the same way (Table 4C): remifentanil contributed no report in eight of the ten years; eight are dated to 2024 and one has no usable receivedate (so the year table holds nine), and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06–5.90; 3.495, 1.52–8.05). Its position as the weakest of the four is a corpus-wide average, not a yearly property.",
"The corrected signal is not stable in the same way (Table 4C): remifentanil contributed no report in eight of the ten years; eight are dated to 2024 and one has no usable receivedate (so the year table holds nine), and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06–5.90; 3.495, 1.52–8.05). A leave-2024-out sensitivity leaves a single remifentanil report (a = 1) and no signal (reporting odds ratio 0.70, 0.10–4.98; ratio versus fentanyl 0.11, 0.02–0.76; versus morphine 0.06, 0.01–0.41), so the pooled estimate is a single-year cluster, not a stable finding. The 2024 elevation is shared by all four opioids (year-to-pooled reporting odds ratio 15.4, 4.3, 4.9 and 1.7 for remifentanil, fentanyl, sufentanil and morphine), pointing to a 2024 coding or reporting shift rather than a remifentanil-specific event. Its position as the weakest of the four is a corpus-wide average, not a yearly property.",
"M2-sec38")

# 6) §4.1: signal rests on 2024 cluster, disappears when excluded
add(
"HYPERAESTHESIA, the preferred term carrying the concept, meets the signal criterion for all four opioids (4.73, 2.54–8.80); eight of the ten reports fall in 2024 (§3.8).",
"HYPERAESTHESIA, the preferred term carrying the concept, meets the signal criterion for all four opioids (4.73, 2.54–8.80), but the signal rests on ten reports of which eight fall in 2024 and disappears when that year is excluded (a = 1, §3.8).",
"M2-sec41")

# 7) §4.4 P1-2: weakest-of-four explained by under-reporting
add(
"Opioid-induced hyperalgesia is defined by a change in pain sensitivity, whereas spontaneous reporting captures discrete events: even under the correct preferred term the instrument records recognition, not incidence.",
"Opioid-induced hyperalgesia is defined by a change in pain sensitivity, whereas spontaneous reporting captures discrete events: even under the correct preferred term the instrument records recognition, not incidence. Remifentanil's lowest-of-four ranking is most parsimoniously explained by the same under-reporting that affects every other term, not by a genuinely lower hyperalgesia burden.",
"P1-2-sec44")

# 8) §4.4 P1-4: specificity probe tempered
add(
"The specificity probe makes the argument concrete: DRUG INEFFECTIVE reversed direction between databases, so remifentanil's low reporting is term-specific, not a database-wide property of its records.",
"The specificity probe makes the argument concrete: DRUG INEFFECTIVE reversed direction between databases, consistent with term-specific reporting but also compatible with database differences, so it narrows rather than settles the interpretation.",
"P1-4-sec44")

# 9) §5: signal disappears when 2024 excluded
add(
"Remifentanil's signal is the weakest of the four, rests on ten reports, eight of them in a single year, and was not reproduced in the smaller Canadian database, which had no power to test it.",
"Remifentanil's signal is the weakest of the four, rests on ten reports of which eight fall in 2024, disappears when that year is excluded (a = 1), and was not reproduced in the smaller Canadian database, which had no power to test it.",
"M2-sec5")

# 10) §1 P2-4: expectation-management sentence
add(
"Negative controls and a specificity probe were defined a priori, because an opioid that under-reports one thing may under-report everything, and a null is interpretable only if the instrument works.",
"Negative controls and a specificity probe were defined a priori, because an opioid that under-reports one thing may under-report everything, and a null is interpretable only if the instrument works. This study makes no clinical safety claim and issues no prevention recommendation; it examines how reporting responds to term choice.",
"P2-4-sec1")

# 11) §9: fix trailing pipe + add leave-2024 row
add(
"| Year-stratified HYPERAESTHESIA (FAERS) | `04_sensitivity_year_hyperaesthesia.csv` | |",
"| Year-stratified HYPERAESTHESIA (FAERS) | `04_sensitivity_year_hyperaesthesia.csv` |\n| Leave-2024-out HYPERAESTHESIA sensitivity (FAERS) | `04_sensitivity_leave2024_hyperaesthesia.csv` |",
"P2-1-sec9")

# apply
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
    print("ABORT: some replacements did not match exactly")
    sys.exit(1)

open(F, "w", encoding="utf-8").write(s)
print(f"\nALL {len(reps)} replacements applied OK -> {F}")
