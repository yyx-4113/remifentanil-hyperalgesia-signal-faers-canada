# -*- coding: utf-8 -*-
"""Round-7 trim, fourth pass: the last 69 words, plus the gate-driven wording fixes.

Recorded as a script rather than left in shell history because the project keeps one
direction — script -> artifact — and because the two edits here that were forced by gate
failures (the summary's all-caps term, the "pre-specified" ban, the duplicated
"negative control" phrase) are exactly the kind of change that is easy to lose track of.

Idempotent: the replacements have already been applied, so a re-run reports them as
already-applied and exits 0. If a source string is found twice the script stops.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")

PAIRS = [
    # ---- last 69 words of the budget ----
    ("stratified the comparison by recorded indication: all reports, perioperative anaesthesia, and pain (Table 5)",
     "stratified the comparison by recorded indication (Table 5)"),
    ("In FAERS we restricted the analysis to serious reports with the reference set restricted correspondingly",
     "In FAERS we restricted to serious reports, the reference set restricted correspondingly"),
    ("so a term has two to four times more opportunity to appear in a comparator report",
     "so a term has several times more opportunity to appear in a comparator report"),
    ("so the rise is real in the corpus but is not specific to remifentanil",
     ": the rise is real in the corpus but not specific to remifentanil"),
    ("were much smaller for remifentanil (111) and sufentanil (63) but substantial for fentanyl (4 881) and morphine (7 675)",
     "were much smaller for remifentanil (111) and sufentanil (63), substantial for fentanyl (4 881) and morphine (7 675)"),
    ("(Table S7). A case series such as that in §3.3 is not removable by any query.\n\n**Canada Vigilance.**",
     "(Table S7).\n\n**Canada Vigilance.**"),
    ("specified in a dated analytical plan archived with the repository (ANALYSIS_PLAN.md)",
     "specified in a dated analytical plan (ANALYSIS_PLAN.md)"),
    ("zero among 20 692 687 FAERS reports and zero among 1 154 017 Canadian reports",
     "zero among 20 692 687 FAERS and 1 154 017 Canadian reports"),
    ("Remifentanil was the lowest reporter of PAIN of all four opioids (Table 2): 23 FAERS reports (0.14, 0.09–0.21) against 7 349 for fentanyl, 98 for sufentanil and 4 794 for morphine, with every computable head-to-head ratio below 1",
     "Remifentanil reported PAIN least of all four opioids (Table 2): 23 FAERS reports (0.14, 0.09–0.21) against 7 349 for fentanyl, 98 for sufentanil and 4 794 for morphine, with every computable ratio below 1"),
    ("Assignment was role-agnostic: because the search matches any element of the `patient.drug` array",
     "Assignment was role-agnostic: the search matches any element of the `patient.drug` array"),
    ("Because 29.3% of remifentanil reports also name fentanyl, the ratio is additionally reported on a remifentanil set with co-reported comparator reports removed (Table S8)",
     "Because 29.3% of remifentanil reports also name fentanyl, the ratio is also reported with co-reported comparator reports removed (Table S8)"),
    ("so the clinical word alone manufactures a gap the dictionaries do not contain (Table S4)",
     "so the clinical word manufactures a gap the dictionaries do not contain (Table S4)"),
    ("prospective studies with quantitative sensory testing remain the appropriate instrument [27]",
     "prospective studies with quantitative sensory testing remain the instrument [27]"),
    # ---- forced by gate failures ----
    ("whereas the proxy carrying it (HYPERAESTHESIA, a generic sensory term) met the signal criterion",
     "whereas the proxy term carrying it — a generic sensory term rather than a pain-sensitisation term — met the signal criterion"),
    ("the only proxy with a ratio above 1 and added post hoc, so it is not a pre-specified test and is not read as a drug finding",
     "the only proxy with a ratio above 1 and added post hoc, so it was not specified in the analytical plan and is not read as a drug finding"),
    ("They are not negative controls in the causal sense: a ratio below one shows that remifentanil is reported less, not that it causes less. Nor are they informative negative controls: remifentanil's short exposure genuinely yields fewer such events than chronic morphine,",
     "They are not negative controls in the causal sense, nor informative ones: a ratio below one shows that remifentanil is reported less, not that it causes less, and its short exposure genuinely yields fewer such events than chronic morphine,"),
    ("HYPERPATHIA a concept sibling, and CHRONIC PAIN SYNDROME 2012 free text that is not a preferred term (Tables S4, S6)",
     "HYPERPATHIA a concept sibling, and CHRONIC PAIN SYNDROME, whose single 2012 occurrence is uncoded free text (Tables S4, S6)"),
    # ---- one number, corrected from the authoritative results file ----
    ("against 328 048 across 121 819 fentanyl (2.69) and 257 029 across 56 501 morphine (4.55)",
     "against 328 048 across 121 819 fentanyl (2.69) and 257 108 across 56 501 morphine (4.55)"),
    ("16 857 for sufentanil and 257 029 for morphine",
     "16 857 for sufentanil and 257 108 for morphine"),
]

txt = io.open(MS, encoding="utf-8").read()
applied, pending = [], []
for old, new in PAIRS:
    n = txt.count(old)
    if n > 1:
        sys.exit(f"ABORT: source found {n}x:\n{old[:100]}")
    if n == 1:
        txt = txt.replace(old, new)
        applied.append(old[:48])
    else:
        pending.append(old[:48])

if applied:
    io.open(MS, "w", encoding="utf-8", newline="").write(txt)
print(f"applied {len(applied)}, already-applied {len(pending)}")
for a in applied:
    print("  now:", a)
