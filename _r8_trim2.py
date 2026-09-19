# -*- coding: utf-8 -*-
"""Round-8 word-budget pass, second and final increment.

Main text was 4 012 and the Summary 303 after the first pass, against ceilings of
4 000 and 300.  This pass removes another 15 and 4, all of it wording or
duplication of what the appendix already states; nothing the reviewers asked for
is dropped.
"""
from __future__ import annotations

import io
import re

MS = "I_正文_IMRaD_en.md"
text = io.open(MS, encoding="utf-8").read()


def count(t: str) -> int:
    t = re.sub(r"[`*_>#|]", " ", t)
    return sum(1 for tok in t.split() if re.search(r"[A-Za-z0-9]", tok))


def main_words() -> int:
    return count(text[text.index("## 1. Introduction"):text.index("## Acknowledgements")])


def summary_words() -> int:
    return count(text[text.index("## Summary"):text.index("## 1. Introduction")])


def rep(tag: str, old: str, new: str) -> None:
    global text
    n = text.count(old)
    if n != 1:
        raise SystemExit("[%s] anchor occurs %d times, expected 1:\n%s" % (tag, n, old[:150]))
    before = main_words() + summary_words()
    text = text.replace(old, new, 1)
    print("  %-22s %+4d words" % (tag, (main_words() + summary_words()) - before))


print("before: main %d, summary %d" % (main_words(), summary_words()))

# the first pass turned this into +1; the original phrasing was shorter
rep("revert-prospective",
    "a real but modest and rarely coded phenomenon.",
    "a real but modest phenomenon, coded rarely.")

rep("route-mapping",
    "Only the Canadian class analysis is quantitative, the FAERS arm having used keyword rules "
    "rather than the MedDRA hierarchy.",
    "Only the Canadian class analysis is quantitative, the FAERS arm having used keyword rules "
    "(Appendix S1).")

rep("soc-results",
    "Exploratory and uncorrected for multiplicity, with all 27 class estimates in Table S1: no class "
    "compatible with abnormal pain perception showed excess.",
    "Exploratory and uncorrected for multiplicity (Table S1): no class compatible with abnormal pain "
    "perception showed excess.")

rep("spontaneous-reports",
    "We performed a cross-sectional disproportionality analysis of spontaneous adverse event reports, "
    "with a second national database analysed in parallel,",
    "We performed a cross-sectional disproportionality analysis of spontaneous reports, with a second "
    "national database analysed in parallel,")

rep("four-roles",
    "they are not interchangeable, playing four roles set out in Table S6",
    "they are not interchangeable and play four roles (Table S6)")

rep("summary-generic",
    "\u2014 a generic sensory term rather than a pain-sensitisation term \u2014",
    "\u2014 a generic sensory term, not a pain-sensitisation term \u2014")

rep("summary-setting",
    "remifentanil's low reporting of pain reflects its narrow in-hospital exposure set against the "
    "comparators' chronic and community use \u2014 a setting and indication effect that cannot here be "
    "separated from a true drug effect;",
    "remifentanil's low reporting of pain reflects its narrow in-hospital exposure against the "
    "comparators' chronic and community use \u2014 a setting and indication effect inseparable here "
    "from a true drug effect;")

io.open(MS, "w", encoding="utf-8", newline="\n").write(text)
print("after : main %d, summary %d" % (main_words(), summary_words()))
