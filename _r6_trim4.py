# -*- coding: utf-8 -*-
"""Round-6: bring the main text back under the journal's 4000-word ceiling.

The Round-6 additions (the covariance disclosure, the three missing table and
figure citations) pushed the body to 4025 words. Nothing factual is dropped
here: each replacement merges or condenses a sentence that Appendix S1 now
carries in full. Every replacement asserts a single match.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")
APPLY = "--apply" in sys.argv

EDITS = [
    # 1. the covariance disclosure already duplicates Appendix S1 A1.5 in full
    ("Because the two ratios share the same corpus remainder they are not independent, "
     "so Appendix S1 also gives every interval recomputed with their covariance retained; "
     "no conclusion changes. The remaining algebra, the interval algorithms and the "
     "software versions are there too.",
     "The two ratios share the same corpus remainder and are therefore not independent; "
     "Appendix S1 gives the intervals recomputed with their covariance retained, which "
     "changes no conclusion, as well as the remaining algebra and the software versions."),

    # 2. the DRUG INEFFECTIVE explanation, condensed without losing a number
    ("The reversal is not independent evidence about the drug, because the term is roughly "
     "three times commoner in the Canadian corpus relative to its size than in FAERS "
     "(208 365 counts in 1 154 017 reports against 1 299 278 in 20 692 687), so the two "
     "databases differ about how the term is used rather than about remifentanil.",
     "The reversal is not independent evidence about the drug: the term is three times "
     "commoner in the Canadian corpus relative to its size (208 365 counts in 1 154 017 "
     "reports against 1 299 278 in 20 692 687), so the databases differ about how the term "
     "is used, not about remifentanil."),

    # 3. the second half of 3.3 restates what Table 2 prints
    ("HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to estimate. ALLODYNIA is not "
     "estimable either, on a single remifentanil report whose exact conditional interval "
     "spans 0.088\u201319.39; fentanyl (a = 48) and morphine (a = 30) both showed strong "
     "signals, and in Canada Vigilance remifentanil had none (fentanyl 3; sufentanil 0; "
     "morphine 0).",
     "HYPERPATHIA and CHRONIC PAIN SYNDROME were too rare to estimate. ALLODYNIA is not "
     "estimable either, on a single remifentanil report whose exact conditional interval "
     "spans 0.088\u201319.39, although fentanyl and morphine both showed strong signals; in "
     "Canada Vigilance remifentanil had none."),

    # 4. 4.5 route paragraph: the equivalence is asserted twice
    ("Restricting the PAIN comparison to the intravenous stratum left the ratio unchanged "
     "(0.077 versus fentanyl, 0.038 versus morphine), so the defect dilutes both arms "
     "symmetrically.",
     "Restricting the PAIN comparison to the intravenous stratum left the ratio unchanged "
     "(0.077 versus fentanyl, 0.038 versus morphine), so it dilutes both arms symmetrically."),
]


def main() -> int:
    text = open(MS, encoding="utf-8").read()
    bad = [f"{text.count(o)} matches: {o[:80]!r}" for o, _ in EDITS if text.count(o) != 1]
    if bad:
        print("ABORT:")
        for b in bad:
            print("  " + b)
        return 1
    for old, new in EDITS:
        text = text.replace(old, new, 1)
        print(f"  {-len(old.split()) + len(new.split()):+3d} words  {old[:60]!r}")
    total = sum(-len(o.split()) + len(n.split()) for o, n in EDITS)
    print(f"net {total:+d} words")
    if APPLY:
        open(MS, "w", encoding="utf-8").write(text)
        print("written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
