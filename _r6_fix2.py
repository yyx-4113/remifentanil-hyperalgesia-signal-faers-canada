#!/usr/bin/env python3
"""Round-5 revision, step 6: final prose shave to land under the 4000-word ceiling."""

from __future__ import annotations

import re
import sys

SRC = "_body_v8.md"
DST = "_body_v9.md"

REPL = [
    (
        "single national database analysed in parallel, following current recommendations [16] and reported "
        "in accordance with READUS-PV [17, 18].",
        "single national database analysed in parallel, following current recommendations [16] and reported "
        "per READUS-PV [17, 18].",
    ),
    (
        "That comparison does not survive inspection of the ten reports behind it. Nine are separate safety",
        "That comparison does not survive inspection of the reports behind it. Nine are separate safety",
    ),
    (
        "except that an adjacent-token search on CHRONIC PAIN returned one hit; mechanically identical "
        "queries on common terms returned large counts (PAIN alone 607 176).",
        "except that an adjacent-token search on CHRONIC PAIN returned one hit; identical queries on common "
        "terms returned large counts (PAIN alone 607 176).",
    ),
    (
        "Cohort composition explains the pattern without invoking pharmacology. Remifentanil's Canadian",
        "Cohort composition explains the pattern. Remifentanil's Canadian",
    ),
    (
        "the signature of a drug reported from monitored perioperative care.",
        "the signature of monitored perioperative care.",
    ),
    (
        "the same clinical setting the deficit is no longer distinguishable from unity (Table 5).",
        "the same setting the deficit is no longer distinguishable from unity (Table 5).",
    ),
    (
        "both are North American, sharing MedDRA coding and much of the same drug market \u2014 so this is a "
        "comparison, not a confirmation.",
        "both are North American, sharing MedDRA coding and much of the drug market \u2014 so this is a "
        "comparison, not a confirmation.",
    ),
    (
        "and 0.39 against morphine; the others had an empty remifentanil cell.",
        "and 0.39 against morphine; the others were empty.",
    ),
    (
        "for immune disorders (2.363; 1.792 versus fentanyl), rests on 532 anaphylactic-shock reports \u2014 9.9% "
        "of the remifentanil cohort against 0.28% for fentanyl \u2014 and demonstrates only that the pipeline "
        "detects a real class difference, not anything about remifentanil: anaphylaxis is expected in "
        "monitored anaesthesia, so this is not carried into the Discussion.",
        "for immune disorders (2.363; 1.792 versus fentanyl), rests on 532 anaphylactic-shock reports \u2014 9.9% "
        "of the remifentanil cohort against 0.28% for fentanyl \u2014 and demonstrates only that the pipeline "
        "detects a real class difference, not anything about remifentanil, since anaphylaxis is expected in "
        "monitored anaesthesia.",
    ),
    (
        "so the pooled comparison rests on one case, and \u00a73.3 is the correct reading.",
        "so the pooled comparison rests on one case.",
    ),
    (
        "remifentanil under-reports PAIN and eleven of the twelve computable comparator-term ratios, "
        "stably across serious-report restriction and the eight estimable years \u2014 a property of the "
        "reporting setting, not of the drug.",
        "remifentanil under-reports PAIN and eleven of the twelve computable comparator-term ratios, "
        "stably across serious-report restriction and the eight estimable years \u2014 a property of the "
        "setting, not the drug.",
    ),
    (
        "clinical recognition or reporting [24]. Under the correct preferred term the corpora contain the "
        "concept for every opioid and show no remifentanil-specific excess, so the two sources are "
        "compatible: a real but modest phenomenon, coded rarely.",
        "clinical recognition or reporting [24]; spontaneous reports show a concept was coded, not its "
        "incidence. Under the correct preferred term the corpora contain the concept for every opioid with "
        "no remifentanil-specific excess, so the sources are compatible: a real but modest phenomenon, "
        "coded rarely.",
    ),
    (
        "the search is report-level, so remifentanil, which has no oral or transdermal formulation, received "
        "oral-route assignment in 21.1% of its reports.",
        "the search is report-level, so remifentanil, which has no oral formulation, received oral-route "
        "assignment in 21.1% of its reports.",
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
        "source, recorded none. Remifentanil's low reporting of pain is more robust \u2014 large, stable, "
        "reproduced in Canada, and reduced towards unity once indication and reporting depth are held "
        "constant \u2014 so it is read as a property of perioperative reporting, not of the drug.",
    ),
    (
        "the concept returns reports in both and is coded disproportionately for fentanyl, sufentanil, "
        "morphine and, in the larger database, remifentanil.",
        "the concept returns reports in both and is coded disproportionately for all four opioids.",
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
