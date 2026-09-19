# -*- coding: utf-8 -*-
"""Round-8 wording edits to the manuscript, one exact-pair replacement each.

Every replacement is asserted to occur exactly once, so a silent no-op or a
double application stops the script.  Items are labelled with the Round-6 issue
number they dispose of.  Run after _r8_ref_insert.py (which renumbers the
citations) and before the trimming pass.
"""
from __future__ import annotations

import io

MS = "I_正文_IMRaD_en.md"
text = io.open(MS, encoding="utf-8").read()
applied = []


def rep(tag: str, old: str, new: str) -> None:
    global text
    n = text.count(old)
    if n != 1:
        raise SystemExit("[%s] anchor occurs %d times, expected 1:\n%s" % (tag, n, old[:140]))
    applied.append(tag)
    text = text.replace(old, new, 1)


# --- R6-22: the mechanism account needs its primary evidence ----------------
rep("R6-22/refs",
    "increased dynorphin release [1, 2]; because these targets are tractable",
    "increased dynorphin release, for which the supporting evidence is preclinical "
    "[1, 2, 3, 4]; because these targets are tractable")

# --- R6-23a: quote the meta-analysis in the units it published --------------
rep("R6-23/VAS",
    "a rise in postoperative pain of 9.4 mm on a 100 mm scale at 1 h, 7.1 mm at 4 h and 3.0 mm at 24 h,",
    "a rise in postoperative pain of 9.4 cm on a 100 cm visual analogue scale at 1 h, "
    "7.1 cm at 4 h and 3.0 cm at 24 h,")

# --- R6-23b: PAIN is a reporting-burden probe, not an OIH proxy -------------
rep("R6-23/plan",
    "and PAIN, as a pragmatic proxy [22].",
    "and PAIN, as a pragmatic reporting-burden probe [22].")

rep("R6-23/disclaimer",
    "PAIN therefore carries no information about hyperalgesia.",
    "PAIN is therefore not a proxy for opioid-induced hyperalgesia, and its level "
    "carries no information about it.")

# --- R6-12: the signal floor counts reports, not patients ------------------
rep("R6-12/floor",
    "the lower bound of the information component exceeded zero) [28].",
    "the lower bound of the information component exceeded zero) [28]. The floor "
    "counts reports rather than patients, because spontaneous reporting carries no "
    "patient identifier, so a single case filed repeatedly can satisfy it (\u00a73.3).")

# --- R6-15: the two-patient count is an inference from content -------------
rep("R6-15/a",
    "The ten reports therefore describe two patients, and the excess reflects one case",
    "The ten reports therefore appear to describe at most two patients, and the excess reflects one case")

rep("R6-15/b",
    "the ten remifentanil reports behind it describe two patients once identifiers are checked",
    "the ten remifentanil reports behind it appear to describe at most two patients once identifiers are checked")

rep("R6-15/c",
    "the ten remifentanil reports describe two patients, eight dated to 2024",
    "the ten remifentanil reports appear to describe at most two patients, eight dated to 2024")

# --- R6-18: the eleven-of-twelve count is descriptive, not a test ----------
rep("R6-18/count",
    "the exception being pruritus versus sufentanil (1.310, 0.84\u20132.04).",
    "the exception being pruritus versus sufentanil (1.310, 0.84\u20132.04). That count "
    "is descriptive, not a test: the twelve ratios are correlated with one another and "
    "several of the terms were added after the zeros had been seen.")

# --- R6-03: the rarity range must match Table 2's own footnote -------------
rep("R6-03/range",
    "one report in 200 to 500, depending on the drug (Table 2)",
    "roughly one report in 216 to 540, depending on the drug (Table 2)")

# --- R6-14: the incidence disclaimer belongs with the conclusion ----------
rep("R6-14/disclaimer",
    "None of this establishes whether hyperalgesia after remifentanil occurs.",
    "None of this establishes whether hyperalgesia after remifentanil occurs: "
    "spontaneous reporting cannot address its incidence in either direction, so that "
    "remains a question for prospective quantitative sensory testing.")

# --- R6-23c: carry the probe framing into the Summary ----------------------
rep("R6-23/summary",
    "Remifentanil reported pain least of the four opioids (0.066,",
    "Remifentanil reported its pain term \u2014 a general reporting-burden probe, not an "
    "opioid-induced-hyperalgesia proxy \u2014 least of the four opioids (0.066,")

io.open(MS, "w", encoding="utf-8", newline="\n").write(text)
print("applied %d edits:" % len(applied))
for t in applied:
    print("   ", t)
