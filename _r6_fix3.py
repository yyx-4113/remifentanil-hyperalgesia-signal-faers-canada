#!/usr/bin/env python3
"""Round-5 revision, step 7: repair the SOC sentence left dangling by step 5,
then land the final ~30 words."""

from __future__ import annotations

import re
import sys

SRC = "_body_v9.md"
DST = "_body_v10.md"

REPL = [
    # --- repair the dangling SOC sentence (step 5 left ", The immune ratio rests on") ---
    (
        "No class compatible with hyperalgesia or abnormal pain perception showed excess, and the largest "
        "ratio, for immune disorders (2.363; 1.792 versus fentanyl), The immune ratio rests on 532 "
        "anaphylactic-shock reports \u2014 9.9% of the remifentanil cohort against 0.28% for fentanyl \u2014 and "
        "demonstrates only that the pipeline detects a real class difference, not anything about "
        "remifentanil: anaphylaxis is expected in monitored anaesthesia, so this is not carried into the "
        "Discussion.",
        "No class compatible with hyperalgesia or abnormal pain perception showed excess; the largest ratio, "
        "for immune disorders (2.363; 1.792 versus fentanyl), rests on 532 anaphylactic-shock reports \u2014 "
        "9.9% of the remifentanil cohort against 0.28% for fentanyl \u2014 and demonstrates only that the "
        "pipeline detects a real class difference, not anything about remifentanil, since anaphylaxis is "
        "expected in monitored anaesthesia.",
    ),
    # --- section 5 ---
    (
        "That comparison does not survive inspection of the underlying reports:",
        "That comparison does not survive inspection:",
    ),
    (
        "Remifentanil's low reporting of pain is the more robust observation \u2014 large, stable, reproduced "
        "in Canada, and reduced towards unity once indication and reporting depth are held constant \u2014 so "
        "it is read as a property of perioperative reporting rather than of the drug.",
        "Remifentanil's low reporting of pain is more robust \u2014 large, stable, reproduced in Canada, and "
        "reduced towards unity once indication and reporting depth are held constant \u2014 so it is read as a "
        "property of perioperative reporting, not of the drug.",
    ),
    # --- section 2.1 ---
    (
        "second national database analysed in parallel, following current recommendations [16] and reported "
        "in accordance with READUS-PV [17, 18].",
        "second national database analysed in parallel, following current recommendations [16] and reported "
        "per READUS-PV [17, 18].",
    ),
    (
        "openFDA serves each report in its latest revision; the consequences are set out in \u00a74.5.",
        "openFDA serves each report in its latest revision; see \u00a74.5.",
    ),
    # --- section 2.3 ---
    (
        "The plan was written after data extraction and before any result was interpreted, and was not "
        "prospectively registered.",
        "The plan was written after data extraction and before interpretation, and was not prospectively "
        "registered.",
    ),
    (
        "the term set is a custom query, specified in Table S6.",
        "the term set is a custom query (Table S6).",
    ),
    # --- section 2.4 ---
    (
        "the information component with BCPNN shrinkage [25, 26]; the formulae are in Appendix S1.",
        "the information component with BCPNN shrinkage [25, 26]; formulae in Appendix S1.",
    ),
    # --- section 2.5 ---
    (
        "and stratified the PAIN and HYPERAESTHESIA analyses by calendar year.",
        "and stratified PAIN and HYPERAESTHESIA by calendar year.",
    ),
    # --- section 3.6 ---
    (
        "FAERS shows the same ordering, its 500 commonest reaction terms summing to 12 104 counts across "
        "5 375 remifentanil reports (a lower bound of 2.25 per report), against 328 048 across 121 819 "
        "fentanyl reports (2.69) and 256 947 across 56 501 morphine reports (4.55).",
        "FAERS shows the same ordering: its 500 commonest reaction terms sum to 12 104 counts across 5 375 "
        "remifentanil reports (2.25 per report at minimum), against 328 048 across 121 819 fentanyl reports "
        "(2.69) and 256 947 across 56 501 morphine reports (4.55).",
    ),
    # --- section 3.7 heading ---
    (
        "### 3.7 System organ class panorama and sensitivity analyses",
        "### 3.7 System organ class and sensitivity analyses",
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
    open(DST, "w", encoding="utf-8", newline="\n").write(text)
    before = count(open(SRC, encoding="utf-8").read())
    after = count(text)
    print(f"{SRC}: {before} -> {DST}: {after}  (delta {after - before:+d})")
    print(f"headroom to 4000: {4000 - after}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
