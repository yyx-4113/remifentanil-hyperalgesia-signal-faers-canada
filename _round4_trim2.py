#!/usr/bin/env python3
# Round-4 main-text trim pass 2: cut ~75 more words (4074 -> <=4000).
# \u00a7 = section sign. No gated strings touched (verified by grep).
F = "I_正文_IMRaD_en.md"
s = open(F, encoding="utf-8").read()
reps = []
def add(old, new, tag):
    reps.append((old, new, tag))

# A (L39) drop redundant clause
add(
"The question runs both ways: a clinically salient syndrome should surface in reporting, and if it does not, that constrains the plausible real-world burden and exposes a limitation of the source. Whether it surfaces depends on which preferred term is queried, and the name the literature uses is not necessarily the name the dictionary uses.",
"The question runs both ways: a clinically salient syndrome should surface in reporting. Whether it surfaces depends on which preferred term is queried, and the name the literature uses is not necessarily the name the dictionary uses.",
"A")

# B (L103) compress exception + drop query-path tail
add(
"No report in either corpus carried HYPERALGESIA as a reaction preferred term: the string returned zero among 20 692 687 FAERS reports and among 1 154 017 Canadian reports, and so did an adjacent-token search. The other four strings returned no exact match either, with one exception: an adjacent-token search on CHRONIC PAIN returned a single hit, not an exact preferred-term match, which does not alter the conclusion. Mechanically identical queries on common terms returned large counts (PAIN alone 607 176), so the query path was intact (Table S4).",
"No report in either corpus carried HYPERALGESIA as a reaction preferred term: the string returned zero among 20 692 687 FAERS reports and among 1 154 017 Canadian reports, and so did an adjacent-token search. The other four strings returned no exact match either, with one exception (an adjacent-token hit on CHRONIC PAIN, not an exact match). Mechanically identical queries on common terms returned large counts (PAIN alone 607 176).",
"B")

# C (L59) drop role-agnostic rationale sentence; keep \u00a74.5 reference
add(
"Assignment was role-agnostic, so the drug need not have been flagged as suspect; for signal detection this maximises sensitivity, at the cost of admitting reports in which the drug was co-suspected or concomitant. A role-restricted analysis was not possible, the case-level file needed to attribute role being inaccessible (\u00a74.5).",
"Assignment was role-agnostic, so the drug need not have been flagged as suspect. A role-restricted analysis was not possible, the case-level file needed to attribute role being inaccessible (\u00a74.5).",
"C")

# D (L123) tighten exception lead-in
add(
"The one conspicuous exception runs the other way: the FAERS HYPERAESTHESIA signal did not reproduce, because in Canada remifentanil contributed no report of that term while both comparators did.",
"The exception: the FAERS HYPERAESTHESIA signal did not reproduce, because in Canada remifentanil contributed no report of that term while both comparators did.",
"D")

# E (L167) drop redundant ranking list + intuition clause (data already in Table 2)
add(
"rather than to pain, and the ranking it produces (morphine 12.17, sufentanil 8.61, fentanyl 6.80, remifentanil 4.73) differs from clinical intuition about remifentanil, though it cannot be read as evidence of pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition.",
"rather than to pain, though it cannot be read as evidence of pain-specific sensitisation because HYPERAESTHESIA is not pain-specific and the cross-drug ordering is confounded by cohort composition.",
"E")

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
    print("ABORT"); raise SystemExit(1)

open(F, "w", encoding="utf-8").write(s)
print(f"\nALL {len(reps)} trims applied OK")
