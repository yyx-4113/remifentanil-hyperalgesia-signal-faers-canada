# -*- coding: utf-8 -*-
"""Round-8 word-budget pass.

The Round-8 additions (primary citations, the report-not-patient caveat, the
incidence disclaimer, the descriptive-count labels, the PAIN probe framing and
the units correction) took the main text to 4 101 words and the Summary to 310,
against limits of 4 000 and 300.  This script tightens prose back inside them.
No number, citation, hedge or disclosure requested by a reviewer is removed:
what goes is duplicated apparatus that the appendix or a table footnote already
carries, plus wordy wording.  Every replacement is asserted to occur once, and
the script reports the running total.
"""
from __future__ import annotations

import io
import re

MS = "I_正文_IMRaD_en.md"
text = io.open(MS, encoding="utf-8").read()

MAIN_LO = text.index("## 1. Introduction")
MAIN_HI = text.index("## Acknowledgements")
SUM_LO = text.index("## Summary")
SUM_HI = MAIN_LO


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
    after = main_words() + summary_words()
    print("  %-22s %+4d words" % (tag, after - before))


print("before: main %d, summary %d" % (main_words(), summary_words()))

# --- duplicated apparatus --------------------------------------------------
rep("soc-methods",
    "**System organ classes.** Report-level counts were taken from the Canadian native "
    "`SOC_NAME_ENG` field, giving all 27 MedDRA classes without a mapping step (Table S1, panel A); "
    "the treatment of the exploratory FAERS class arm, which the openFDA interface limits to the 500 "
    "commonest terms per drug, is in Appendix S1.",
    "**System organ classes.** Report-level counts came from the Canadian native `SOC_NAME_ENG` field, "
    "giving all 27 classes without a mapping step (Table S1, panel A); the FAERS arm is exploratory "
    "(Appendix S1).")

rep("faers-fieldpath",
    "A report joined a cohort if any drug entry carried the target substance in "
    "`patient.drug.activesubstance.activesubstancename.exact`; the four exact search expressions "
    "are listed in Appendix S1.",
    "A report joined a cohort if any drug entry carried the target substance; the four exact search "
    "expressions are in Appendix S1.")

rep("proxy-independence",
    " The proxies are not independent confirmations, since they were selected because the originals "
    "returned zero.",
    "")   # the same disclosure stands in the Table S6 note and in the sentence above it

rep("star-sentence",
    "The star in Table 2 marks any term meeting these rules, and Table 2 gives the counts from which "
    "each can be re-run.",
    "Table 2 itself carries the counts from which each can be re-run.")

# --- wordy wording ---------------------------------------------------------
rep("hyperaesthesia-wording",
    "but it denotes sensitivity to any sensory stimulus and is not specific to nociceptive "
    "sensitisation, so it is a loose proxy that also captures sensory reports unrelated to pain "
    "(the ADReCS carrier set is set out in Appendix S1 A1.10).",
    "but it denotes sensitivity to any sensory stimulus rather than nociceptive sensitisation, so it "
    "is a loose proxy and also captures sensory reports unrelated to pain (Appendix S1 A1.10).")

rep("plan-specified",
    "Neither plan-specified hyperalgesia outcome met the signal criterion: HYPERALGESIA returned no "
    "report in either corpus, and the single ALLODYNIA report is uninterpretable.",
    "Neither plan-specified outcome met the signal criterion: HYPERALGESIA returned no report, and the "
    "single ALLODYNIA report is uninterpretable.")

rep("comparator-candour",
    "They are not negative controls in the causal sense, nor informative ones: a ratio below one shows",
    "They are not negative controls in the causal sense: a ratio below one shows")

rep("strata",
    "The strata are not mutually exclusive and the indication is free text, so they are approximate.",
    "The strata overlap and the indication is free text, so they are approximate.")

rep("opportunity",
    "since a report carrying more terms has more opportunity to contain any one of them",
    "since a report with more terms has more opportunity to contain any one of them")

rep("robustness",
    "Two further FAERS restrictions are reported as robustness checks: at least one record flagged "
    "primary suspect, and reports never revised (`safetyreportversion` = 1). The second removes",
    "Two further FAERS restrictions are reported as robustness checks: at least one record flagged "
    "primary suspect, and reports never revised (`safetyreportversion` = 1) \u2014 the second removes")

rep("demonstration",
    " Tables 2, 3 and S5 report it as a term-level demonstration, not a signal, and no clinical "
    "inference is drawn from it.",
    " Tables 2, 3 and S5 report it as a term-level demonstration, not a signal.")

rep("canada-power",
    "111 reports have no power for such a rare term, but the absence is more informative because that "
    "extract de-duplicates at source.",
    "111 reports have no power for such a rare term, but that extract de-duplicates at source, which "
    "makes the absence more informative.")

rep("allodynia",
    "ALLODYNIA is not estimable either, on a single remifentanil report whose exact conditional "
    "interval spans 0.088\u201319.39, although fentanyl and morphine both showed strong signals; in "
    "Canada Vigilance remifentanil had none.",
    "ALLODYNIA is not estimable either, on a single remifentanil report whose exact conditional "
    "interval spans 0.088\u201319.39; in Canada Vigilance remifentanil had none.")

rep("probe-reversal",
    "The reversal is not evidence about the drug either:",
    "The reversal is not evidence about the drug:")

rep("prospective",
    "a real but modest phenomenon, coded rarely.",
    "a real but modest and rarely coded phenomenon.")

rep("reads-as",
    "once indication and reporting depth are held constant, and is read as a property of the setting "
    "rather than of the drug.",
    "once indication and reporting depth are held constant, and reads as a property of the setting "
    "rather than of the drug.")

rep("limitation-patients",
    "the corrected hyperalgesia comparison rests on ten reports describing two patients;",
    "the corrected hyperalgesia comparison rests on ten reports appearing to come from at most two "
    "patients;")

rep("route",
    "Route cannot be attributed to a drug record, since `patient.drug` is an array and the search is "
    "report-level:",
    "Route cannot be attributed to a drug record, `patient.drug` being an array searched at report "
    "level:")

rep("mediation",
    "no drug-specific effect can be isolated, and \u00a74.3 is an interpretation consistent with the "
    "subgroup data, not a mediation analysis.",
    "no drug-specific effect can be isolated, and \u00a74.3 is an interpretation consistent with the "
    "subgroup data rather than a mediation analysis.")

rep("geography",
    "Both databases are North American, where about 85% of signals overlap at the preferred-term level "
    "across regions [35]; neither European nor Japanese databases were used.",
    "Both are North American, where about 85% of signals overlap at the preferred-term level across "
    "regions [35]; no European or Japanese database was used.")

rep("conclusion-deficit",
    "The deficit reflects the reporting setting and the drug's narrow in-hospital exposure, "
    "inseparable here, and is not evidence about remifentanil's analgesic or hyperalgesic profile;",
    "The deficit reflects the reporting setting and the drug's narrow in-hospital exposure, "
    "inseparable here, not evidence about remifentanil's analgesic or hyperalgesic profile;")

rep("mech-clause",
    "increased dynorphin release, for which the supporting evidence is preclinical [1, 2, 3, 4];",
    "increased dynorphin release, the supporting evidence being preclinical [1, 2, 3, 4];")

rep("implications",
    "so prevention decisions should rest on the prospective literature [9, 10].",
    "so prevention decisions rest on the prospective literature [9, 10].")

rep("endpoint-url",
    "Reports were retrieved through the openFDA drug/event interface "
    "(`https://api.fda.gov/drug/event.json`) [20];",
    "Reports were retrieved through the openFDA drug/event interface [20];")

# --- Summary --------------------------------------------------------------
# The database name keeps its full form here.  An earlier pass shortened it to
# "the US Food and Drug Administration" to save one word and the gate rejected
# it: the structured Summary may not carry all-caps abbreviations.  One word is
# not worth trading the journal's summary convention for.

rep("summary-probe",
    "\u2014 a general reporting-burden probe, not an opioid-induced-hyperalgesia proxy \u2014",
    "\u2014 a reporting-burden probe, not a syndrome proxy \u2014")

rep("summary-ratios",
    "eleven of twelve computable ratios against the comparator terms were below one,",
    "eleven of twelve computable comparator-term ratios were below one,")

rep("summary-intro",
    "Hyperalgesia after remifentanil has generated a prevention literature, yet the clinical evidence "
    "is contested and its reporting is unexamined.",
    "Hyperalgesia after remifentanil has generated a prevention literature, yet the evidence is "
    "contested and its reporting unexamined.")

io.open(MS, "w", encoding="utf-8", newline="\n").write(text)
print("after : main %d, summary %d" % (main_words(), summary_words()))
