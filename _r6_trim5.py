# -*- coding: utf-8 -*-
"""Round-6, second trim pass: four sentence-level condensations, no fact removed."""
from __future__ import annotations

import os
import sys

MS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "I_正文_IMRaD_en.md")
APPLY = "--apply" in sys.argv

EDITS = [
    ("The prospective literature is contested rather than supportive, and the clinical "
     "magnitude remains uncertain [1, 3, 7, 8, 9].",
     "The prospective literature is contested and the clinical magnitude uncertain "
     "[1, 3, 7, 8, 9]."),

    ("so no ethics approval or informed consent was required; use complies with each "
     "database's terms",
     "so no ethics approval was required; use complies with each database's terms"),

    ("so the comparators' PAIN proportions rise for setting and indication, not pharmacology.",
     "so the comparators' PAIN proportions rise for setting, not pharmacology."),

    ("used the native indication field to stratify the head-to-head comparison by recorded "
     "indication: all reports, perioperative anaesthetic indication, and pain indication "
     "(Table 5).",
     "used the native indication field to stratify the comparison by recorded indication: "
     "all reports, perioperative anaesthesia, and pain (Table 5)."),
]


def main() -> int:
    text = open(MS, encoding="utf-8").read()
    bad = [f"{text.count(o)} matches: {o[:70]!r}" for o, _ in EDITS if text.count(o) != 1]
    if bad:
        print("ABORT:")
        for b in bad:
            print("  " + b)
        return 1
    for old, new in EDITS:
        text = text.replace(old, new, 1)
        print(f"  {-len(old.split()) + len(new.split()):+3d}  {old[:58]!r}")
    if APPLY:
        open(MS, "w", encoding="utf-8").write(text)
        print("written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
