#!/usr/bin/env python3
"""Round-5 revision, step 3: final trim of the main text to <=4000 words.

Inline (unique-substring) replacements only, so nothing else in the file moves.
Every number and every table cross-reference is preserved; what goes is
framing prose.  The script reports the word count before and after and warns
if any pattern failed to match.
"""

from __future__ import annotations

import re
import sys

SRC = "_body_v5.md"
DST = "_body_v6.md"

REPL = [
    # 1 Introduction
    (
        "and the principal clinical reviews take that position [13], though the phenomenon",
        "and the principal clinical reviews agree [13], though the phenomenon",
    ),
    # 2.1
    (
        "spontaneous adverse event reports, with a second national database analysed in parallel. "
        "The design follows current recommendations [16], and the study is reported in accordance with "
        "READUS-PV [17, 18].",
        "spontaneous adverse event reports, with a second national database analysed in parallel, following "
        "current recommendations [16] and reported in accordance with READUS-PV [17, 18].",
    ),
    # 2.3
    (
        "PAIN therefore carries no information about hyperalgesia in either direction, and the syndrome's",
        "PAIN therefore carries no information about hyperalgesia, and the syndrome's",
    ),
    # 2.4
    (
        "Because more than one rule can fire, the star in Table 2 marks any term meeting any of them, and "
        "Table 2 gives the counts from which each rule can be re-run.",
        "The star in Table 2 marks any term meeting any of these rules, and Table 2 gives the counts from "
        "which each can be re-run.",
    ),
    (
        "Appendix S1 gives the algebra of the shared remainder, the covariance induced by the common "
        "corpus, and the interval algorithms.",
        "Appendix S1 gives the remaining algebra and the interval algorithms.",
    ),
    # 2.5
    (
        "Because a report may record more than one indication the strata are not mutually exclusive, and "
        "the indication is free text, so they are approximate.",
        "The strata are not mutually exclusive and the indication is free text, so they are approximate.",
    ),
    (
        "Two further FAERS restrictions are reported as robustness checks: to reports containing at least "
        "one record flagged primary suspect, and to reports that have never been revised "
        "(`safetyreportversion` = 1).",
        "Two further FAERS restrictions are reported as robustness checks: at least one record flagged "
        "primary suspect, and reports never revised (`safetyreportversion` = 1).",
    ),
    # 3.3
    (
        "111 reports have no power for a term this rare, but the Canadian absence is the more informative "
        "observation, because that extract removes duplicates at source.",
        "111 reports have no power for such a rare term, but the Canadian absence is more informative, "
        "because that extract removes duplicates at source.",
    ),
    # 3.4
    (
        "and every computable head-to-head ratio was below 1 \u2014 0.066 versus fentanyl",
        "with every computable head-to-head ratio below 1 \u2014 0.066 versus fentanyl",
    ),
    (
        "The same direction held for the comparator terms against fentanyl and morphine, and for nausea, "
        "vomiting and constipation against sufentanil:",
        "The same direction held for the comparator terms against fentanyl and morphine and for nausea, "
        "vomiting and constipation against sufentanil:",
    ),
    # 3.5
    (
        "1.07 against fentanyl and 0.39 against morphine; nausea, pruritus and constipation had an empty "
        "remifentanil cell.",
        "1.07 against fentanyl and 0.39 against morphine; the others had an empty remifentanil cell.",
    ),
    # 3.6
    (
        "Two further analyses locate the difference in the reporting process rather than in the drug. "
        "Restricting the Canadian comparison",
        "Restricting the Canadian comparison",
    ),
    (
        "from unity (Table 5). Reporting depth behaves the same way. Remifentanil's Canadian reports carry",
        "from unity (Table 5). Remifentanil's Canadian reports carry",
    ),
    # 3.7
    (
        "cardiac and vascular classes, and reduced reporting in gastrointestinal (0.101), skin (0.143) and "
        "general disorders (0.361); no class compatible with hyperalgesia or abnormal pain perception "
        "showed excess (Table S1). The immune ratio rests on 532 anaphylactic-shock reports, 9.9% of the "
        "remifentanil cohort against 0.28% for fentanyl, and demonstrates only that the pipeline detects a "
        "real class difference: anaphylaxis is an expected event in monitored anaesthesia, so this is not "
        "evidence about remifentanil and it is not carried into the Discussion.",
        "cardiac and vascular classes and reduced reporting in gastrointestinal (0.101), skin (0.143) and "
        "general disorders (0.361), with no excess in any class compatible with hyperalgesia or abnormal "
        "pain perception (Table S1). The immune ratio rests on 532 anaphylactic-shock reports \u2014 9.9% of "
        "the remifentanil cohort against 0.28% for fentanyl \u2014 and demonstrates only that the pipeline "
        "detects a real class difference, not anything about remifentanil: anaphylaxis is expected in "
        "monitored anaesthesia, so this is not carried into the Discussion.",
    ),
    # 4.1
    (
        "recorded none; the corrected picture is not a weak signal but no estimable signal.",
        "recorded none: the corrected picture is no estimable signal.",
    ),
    # 4.4
    (
        "A reader who stops at the first query reports a structural absence; one who checks finds a "
        "term-level excess that is not pain-specific and, on inspection, is one case.",
        "A reader who stops at the first query reports a structural absence; one who checks finds a "
        "term-level excess that is one case.",
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
        text = text.replace(old, new)
    open(DST, "w", encoding="utf-8", newline="\n").write(text)

    before = count(open(SRC, encoding="utf-8").read())
    after = count(text)
    print(f"{SRC}: {before} words -> {DST}: {after} words  (delta {after - before:+d})")
    print(f"headroom to 4000: {4000 - after} words")
    return 0


if __name__ == "__main__":
    sys.exit(main())
