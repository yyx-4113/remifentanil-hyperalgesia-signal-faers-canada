#!/usr/bin/env python3
"""Round-5 revision, step 8: splice the revised body and Summary into the manuscript.

The manuscript file is rebuilt as
    head (title page + "## Summary")  +  NEW SUMMARY  +  revised sections 1-5  +  tail
where "tail" starts at "## Acknowledgements" (declarations, References, Tables,
figure legends, traceability appendix).

Guards: the two boundary markers must each occur exactly once, and the word
count of both the Summary and the main text is printed so the title-page
declaration can be updated to the measured value.
"""

from __future__ import annotations

import re
import sys

MS = "I_正文_IMRaD_en.md"
BODY = "_body_v11.md"
DST = "I_正文_IMRaD_en.md"

SUMMARY = """## Summary

**Introduction.** Hyperalgesia after remifentanil infusion has generated a substantial prevention literature, yet the clinical evidence is contested and real-world reporting of the syndrome has not been examined.

**Methods.** Disproportionality analysis in two national spontaneous reporting databases: the US Food and Drug Administration Adverse Event Reporting System (20 692 687 reports) as primary and the Health Canada Canada Vigilance line-listing (1 154 017 reports) for comparison; cohorts were remifentanil, fentanyl, sufentanil and morphine. Every term was verified as retrievable in both dictionaries before any zero was read, and the five that failed were replaced by proxies. Signals required three or more reports with a lower confidence bound above one; remifentanil was compared with each comparator by the ratio of reporting odds ratios, and the Canadian comparison was stratified by indication and by reaction terms per report.

**Results.** The clinical word is not a preferred term in either dictionary and returned no report, whereas the preferred term carrying it met the signal criterion for all four opioids; nine of the ten remifentanil reports behind it are separate identifiers for one case, leaving two patients: a term-level demonstration, not a signal. Remifentanil reported pain least of the four opioids (0.066, 95% confidence interval 0.04-0.10, versus fentanyl; 0.046 versus morphine; 0.235 and 0.146 in Canada); eleven of the twelve computable ratios against the comparator terms were below one, and the direction held on serious-report restriction, in the eight estimable years, within a common indication stratum and after adjustment for depth. One report in 538 carried the term, against one in 216 for morphine.

**Discussion.** The answer depended on the preferred term chosen: a zero from the clinical name alone is an artefact of terminology, and remifentanil's low reporting of pain reflects the perioperative setting rather than a favourable safety profile."""


def count(text: str) -> int:
    text = re.sub(r"[`*_>#|]", " ", text)
    return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))


def main() -> int:
    ms = open(MS, encoding="utf-8").read()
    body = open(BODY, encoding="utf-8").read().strip()

    for marker in ("## Summary", "## 1. Introduction"):
        n = ms.count(marker)
        print(f"marker {marker!r}: {n}")
        if n != 1:
            print("!! boundary marker is not unique - aborting")
            return 1
    # "## Acknowledgements" also appears inline inside the section-10 notes, so the
    # boundary must be anchored to a line start.
    hits = list(re.finditer(r"(?m)^## Acknowledgements$", ms))
    print(f"marker '## Acknowledgements' at line start: {len(hits)}")
    if len(hits) != 1:
        print("!! boundary marker is not unique - aborting")
        return 1
    ack = hits[0].start()

    head = ms[: ms.index("## Summary")]
    tail = ms[ack:]

    new = head + SUMMARY + "\n\n---\n\n" + body + "\n\n---\n\n" + tail
    open(DST, "w", encoding="utf-8", newline="\n").write(new)

    i = new.index("## 1. Introduction")
    j = new.index("## Acknowledgements")
    print(f"MAIN TEXT  : {count(new[i:j])} words (ceiling 4000)")
    print(f"SUMMARY    : {count(new[new.index('## Summary'):i])} words (250-300)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
