#!/usr/bin/env python
"""Round-6, T0-6: apply the term-substitution pressure test to the paper's own
pain conclusion, and fix the single wrong cell found in 14_faers_pt_distribution.csv.

Round 5 (T0-6, A4) showed that substituting INADEQUATE ANALGESIA for the chosen
proxy reverses the ordering - remifentanil 5.016 against sufentanil 3.761 and
morphine 3.576. That is the strongest possible support for the paper's own thesis
(term choice decides the answer), and it had not been written up. It is now
recomputed from live queries (21_alternative_proxy_terms.csv) and reported.

Also: the same check caught one wrong cell in 14_faers_pt_distribution.csv
(MORPHINE x INADEQUATE ANALGESIA recorded as 0; the true count is 82), which
changes the morphine per-report sum quoted in section 3.6 and Appendix A1.6
from 256 947 to 257 029.

Every replacement is asserted unique. Run with --apply to write.
"""
import sys

MS = "I_正文_IMRaD_en.md"
APPLY = "--apply" in sys.argv

EDITS = [
    # ---- 1. the corrected per-report sums (one wrong cell, +82) -------------
    ("against 328 048 across 121 819 fentanyl reports (2.69) and 256 947 across "
     "56 501 morphine reports (4.55)",
     "against 328 048 across 121 819 fentanyl reports (2.69) and 257 029 across "
     "56 501 morphine reports (4.55)"),
    ("12 104 for remifentanil, 328 048 for fentanyl, 16 857 for sufentanil and "
     "256 947 for morphine",
     "12 104 for remifentanil, 328 048 for fentanyl, 16 857 for sufentanil and "
     "257 029 for morphine"),

    # ---- 2. §4.4: the paper's own pain conclusion fails its own test --------
    ("In a field with an active prevention literature that difference is not "
     "academic [29, 30]; any analysis of a syndrome whose clinical name is not "
     "its coded name needs the verification in §2.3.",
     "The pain conclusion fails the same test: substituting INADEQUATE ANALGESIA "
     "reverses the order (Table S5). In a field with an active prevention "
     "literature that difference is not academic [29, 30]; such an analysis needs "
     "the verification of §2.3."),

    # ---- 3. Table S5 note: the numbers behind that sentence -----------------
    ("whose interval includes one.",
     "whose interval includes one. The substitution noted in section 4.4 is "
     "recomputed in `21_alternative_proxy_terms.csv`: on INADEQUATE ANALGESIA "
     "(8 465 reports in the corpus) remifentanil gives 11 reports and a reporting "
     "odds ratio of 5.016 (2.78–9.07), against 3.761 (2.02–7.00) for "
     "sufentanil and 3.576 (2.88–4.45) for morphine, so the ordering across "
     "the opioids reverses; the ratios against sufentanil and morphine are 1.334 "
     "(0.57–3.14) and 1.403 (0.75–2.64), point estimates above one "
     "with intervals that include it."),
]


def main() -> int:
    text = open(MS, encoding="utf-8").read()
    bad = [(text.count(o), o) for o, _ in EDITS if text.count(o) != 1]
    if bad:
        for n, o in bad:
            print(f"!! {n} matches: {o[:90]}")
        return 1
    for o, n in EDITS:
        text = text.replace(o, n, 1)
    if APPLY:
        open(MS, "w", encoding="utf-8").write(text)
    print(f"{len(EDITS)} edits {'written' if APPLY else '(dry run)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
