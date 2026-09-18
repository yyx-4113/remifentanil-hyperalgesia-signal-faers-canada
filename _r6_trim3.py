#!/usr/bin/env python3
"""Round-5 revision, step 4: last 50 words off the main text."""

from __future__ import annotations

import re
import sys

SRC = "_body_v6.md"
DST = "_body_v7.md"

REPL = [
    (
        "counts were arranged in the conventional 2\u00d72 table (a: drug and event; b: drug without event; "
        "c: event without drug; d: all remaining), and three measures were computed",
        "counts were arranged in the conventional 2\u00d72 table (a: drug and event; d: all remaining), and "
        "three measures were computed",
    ),
    (
        "so a zero can mean either that the event was never reported or that the string is not a preferred "
        "term in the dictionary that coded that database.",
        "so a zero can mean either that the event was never reported or that the string is not a preferred "
        "term.",
    ),
    (
        "Substring matching was rejected because it admits chemically distinct substances sharing a stem.",
        "Substring matching was rejected because it admits distinct substances sharing a stem.",
    ),
    (
        "January [27]. ",
        "January [27]. ",
    ),
    (
        "A global artefact would have pushed this term in the same direction as everything else; it did not.",
        "A global artefact would have pushed this term in the same direction; it did not.",
    ),
    (
        "This comparison is exploratory, with no multiplicity correction.",
        "This comparison is exploratory, without multiplicity correction.",
    ),
    (
        "so the pooled comparison rests on one case, and \u00a73.3's term-level demonstration, not a signal, is "
        "the correct reading.",
        "so the pooled comparison rests on one case, and \u00a73.3 is the correct reading.",
    ),
    (
        "but it narrows rather than settles the interpretation.",
        "but narrows rather than settles it.",
    ),
    (
        "reports were much smaller for remifentanil (111) and sufentanil (63) but substantial for fentanyl "
        "(4 881) and morphine (7 675).",
        "reports were much smaller for remifentanil (111) and sufentanil (63), and substantial for fentanyl "
        "(4 881) and morphine (7 675).",
    ),
    (
        "released for research use; no ethics approval or informed consent was required. Use complies with "
        "each database's terms: openFDA data for public access, and the Canada Vigilance extract under the "
        "Open Government Licence \u2013 Canada.",
        "released for research use, so no ethics approval or informed consent was required; use complies "
        "with each database's terms (openFDA data for public access; the Canada Vigilance extract under "
        "the Open Government Licence \u2013 Canada).",
    ),
    (
        "Appendix S1 gives the remaining algebra and the interval algorithms. All computations used Python "
        "3.13.14 and matplotlib 3.11.1.",
        "Appendix S1 gives the remaining algebra, the interval algorithms and the software versions.",
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
            if old == new:
                continue
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
