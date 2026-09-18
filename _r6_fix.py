#!/usr/bin/env python3
"""Round-5 revision, step 5.

Two jobs:
  1. REPAIR.  Step 2 replaced whole blank-line-separated blocks by matching a
     mid-block phrase, which silently truncated the two opening blocks of
     section 2.3.  Both are restored here in compressed form.  (Lesson: never
     key a block replacement on a phrase that may sit inside the block rather
     than at its head.)
  2. TRIM.  Compensate for the restoration and get back under 4000 words by
     moving the class-by-class SOC ratios to Appendix S1 and shaving prose.

Every edit is a unique-substring replacement, so nothing outside the matched
span can be lost; any pattern that does not match exactly once is reported.
"""

from __future__ import annotations

import re
import sys

SRC = "_body_v7.md"
DST = "_body_v8.md"

REPL = [
    # ---------- 1. repair section 2.3 ---------------------------------------
    (
        "PAIN's low reporting reflects reporting setting",
        "Three groups of terms were specified in a dated analytical plan archived with the repository "
        "(ANALYSIS_PLAN.md): a narrow group (HYPERALGESIA, ALLODYNIA); a broad group (PAIN INCREASED, "
        "POSTOPERATIVE PAIN, CHRONIC PAIN, OPIOID WITHDRAWAL SYNDROME, DRUG TOLERANCE); and PAIN, as a "
        "pragmatic proxy [21]. The plan was written after data extraction and before any result was "
        "interpreted, and was not prospectively registered. PAIN's low reporting reflects reporting setting",
    ),
    (
        "Five dictionary proxies carrying the same concepts were added",
        "**Term-level verification.** Both corpora store preferred terms in the reaction field, so a zero "
        "can mean either that the event was never reported or that the string is not a preferred term. "
        "Every term was verified against both corpora before any zero was interpreted (Table S4), and five "
        "of the seven hyperalgesia-related terms failed: HYPERALGESIA, a lowest level term mapping to the "
        "preferred term HYPERAESTHESIA [23], returned zero by construction. Five dictionary proxies "
        "carrying the same concepts were added",
    ),
    # ---------- 2. SOC ratios to Appendix S1 --------------------------------
    (
        "In the Canadian report-level analysis remifentanil showed elevated ratios in pregnancy, "
        "respiratory, immune (2.363; 1.792 versus fentanyl), cardiac and vascular classes and reduced "
        "reporting in gastrointestinal (0.101), skin (0.143) and general disorders (0.361), with no excess "
        "in any class compatible with hyperalgesia or abnormal pain perception (Table S1).",
        "The class-by-class ratios are in Appendix S1. No class compatible with hyperalgesia or abnormal "
        "pain perception showed excess, and the largest ratio, for immune disorders (2.363; 1.792 versus "
        "fentanyl),",
    ),
    # ---------- 3. prose shaves --------------------------------------------
    (
        "Intervals used the log scale with the sum of reciprocal cell counts (Woolf), and exact conditional "
        "and mid-P intervals are reported alongside it for sparse terms (Table 2). Because the cohorts are "
        "not independent at report level \u2014 29.3% of remifentanil reports also name fentanyl \u2014 the ratio is "
        "additionally reported on a remifentanil set from which co-reported comparator reports have been "
        "removed (Table S8).",
        "Intervals used the log scale with the sum of reciprocal cell counts (Woolf), with exact conditional "
        "and mid-P intervals for sparse terms (Table 2). Because 29.3% of remifentanil reports also name "
        "fentanyl, the ratio is additionally reported on a remifentanil set with co-reported comparator "
        "reports removed (Table S8).",
    ),
    (
        "so terms were mapped to the 27 classes with heuristic keyword rules and counted at event level, "
        "and the rules are not authoritative, so that arm checks direction only.",
        "so terms were mapped to the 27 classes with heuristic keyword rules and counted at event level, so "
        "that arm checks direction only.",
    ),
    (
        "We also stratified by the number of reaction terms entered per report, since a report carrying "
        "more terms has more opportunity to contain any one of them, using Mantel\u2013Haenszel adjustment "
        "across four bands (one, two, three to four, five or more; Table 6).",
        "We also stratified by the number of reaction terms entered per report, using Mantel\u2013Haenszel "
        "adjustment across four bands (one, two, three to four, five or more; Table 6), since a report "
        "carrying more terms has more opportunity to contain any one of them.",
    ),
    (
        "**Version, role and duplication conventions.** openFDA serves only the latest revision of each "
        "report, so a restriction to `safetyreportversion` = 1 removes the 38.4% of reports that were ever "
        "revised, unequally across cohorts (27.7\u201339.6%). Role attribution is report-level rather than "
        "drug-entry-level. Report-level duplication cannot be removed by any query, so a case series "
        "inflates counts for the drug it names.",
        "**Version, role and duplication conventions.** openFDA serves only the latest revision of each "
        "report, so a restriction to `safetyreportversion` = 1 removes the 38.4% of reports ever revised, "
        "unequally across cohorts (27.7\u201339.6%); role attribution is report-level rather than "
        "drug-entry-level. Duplication cannot be removed by any query, so a case series inflates counts for "
        "the drug it names.",
    ),
    (
        "The FAERS class analysis used keyword rules rather than the MedDRA hierarchy and counted at event "
        "level, so only the Canadian class analysis is quantitative.",
        "Only the Canadian class analysis is quantitative, the FAERS arm having used keyword rules rather "
        "than the MedDRA hierarchy.",
    ),
    (
        "Both databases are North American, sharing MedDRA coding and much of the same drug market, so "
        "agreement here is weaker than across regulatory regions,",
        "Both databases are North American, so agreement here is weaker than across regulatory regions,",
    ),
    (
        "The prospective literature is contested rather than supportive, and the clinical magnitude remains "
        "uncertain [1, 7, 8, 9, 3]. Quantitative sensory testing detects a threshold change but not its "
        "clinical recognition or reporting [24]; reporting data show a concept was coded, not its "
        "incidence. Under the correct preferred term",
        "The prospective literature is contested rather than supportive, and the clinical magnitude remains "
        "uncertain [1, 7, 8, 9, 3]. Quantitative sensory testing detects a threshold change but not its "
        "clinical recognition or reporting [24]. Under the correct preferred term",
    ),
    (
        "needs the verification in \u00a72.3 and Table S4. Opioid-induced hyperalgesia is defined by a change in "
        "pain sensitivity, whereas spontaneous reporting captures discrete events: even under the correct "
        "preferred term the instrument records recognition, not incidence.",
        "needs the verification in \u00a72.3. Opioid-induced hyperalgesia is defined by a change in pain "
        "sensitivity, whereas spontaneous reporting captures discrete events: the instrument records "
        "recognition, not incidence.",
    ),
    (
        "Remifentanil under-reported the comparator terms, PAIN, HYPERAESTHESIA and DRUG WITHDRAWAL "
        "SYNDROME, so analgesic superiority cannot be inferred: that reading would also require superiority "
        "on pruritus and constipation. PROCEDURAL PAIN, the one term it reported more than fentanyl, is a "
        "procedural rather than a pharmacological signal and did not reproduce in Canada.",
        "Remifentanil under-reported the comparator terms, PAIN, HYPERAESTHESIA and DRUG WITHDRAWAL "
        "SYNDROME, so analgesic superiority cannot be inferred: that reading would also require superiority "
        "on pruritus and constipation. PROCEDURAL PAIN, the one term it reported more than fentanyl, did "
        "not reproduce in Canada.",
    ),
    (
        "That comparison does not survive inspection: the ten remifentanil reports describe two patients, "
        "the eight dated to 2024 belong to one of them, and the Canadian database, which de-duplicates at "
        "source, recorded none. Remifentanil's low reporting of pain is the more robust observation \u2014 "
        "large, stable, reproduced in Canada, and reduced towards unity once indication and reporting depth "
        "are held constant \u2014 so it is read as a property of perioperative reporting rather than of the "
        "drug.",
        "That comparison does not survive inspection: the ten remifentanil reports describe two patients, "
        "the eight dated to 2024 belong to one of them, and the Canadian database, which de-duplicates at "
        "source, recorded none. Remifentanil's low reporting of pain is the more robust observation \u2014 "
        "large, stable, reproduced in Canada, and reduced towards unity once indication and reporting depth "
        "are held constant \u2014 so it is read as a property of perioperative reporting, not of the drug.",
    ),
]


def count(text: str) -> int:
    text = re.sub(r"[`*_>#|]", " ", text)
    return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))


def main() -> int:
    text = open(SRC, encoding="utf-8").read()
    for old, new in REPL:
        n = text.count(old)
        if n != 1:
            print(f"!! pattern matched {n} times: {old[:70]!r}")
            continue
        text = text.replace(old, new, 1)

    # Guard: the two restored openings must be present now.
    for probe in ("Three groups of terms were specified", "**Term-level verification.**"):
        print(f"guard {probe[:40]!r}: {'OK' if probe in text else 'MISSING'}")

    open(DST, "w", encoding="utf-8", newline="\n").write(text)
    before = count(open(SRC, encoding="utf-8").read())
    after = count(text)
    print(f"{SRC}: {before} -> {DST}: {after}  (delta {after - before:+d})")
    print(f"headroom to 4000: {4000 - after}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
