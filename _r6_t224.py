#!/usr/bin/env python
"""Round-6, T2-24 + T2-26 + T2-22 + T3-5: the four items that were still open.

T2-24  The Canadian reaction file does carry onset fields. Counting them shows
       why no time-to-onset analysis was attempted (185 764 of 4 474 922 rows
       populated; 13 of the 523 Hyperaesthesia rows) instead of the old absolute
       "time-to-onset could not be analysed".
T2-26  §4.6 gave clinicians almost nothing. It now gives the order of magnitude
       (one report in 200 to 500), paid for by removing a paragraph in §4.3 that
       duplicated §3.6.
T2-22  Table 2 prints 0 for strings that cannot be retrieved. The footnote now
       says plainly that those zeros are not observed counts and gives the
       one-in-X rendering for HYPERAESTHESIA.
T3-5   The AI declaration gains the dates of use and a privacy/compliance
       sentence (the declarations block is outside the word count).

Run with --apply to write.
"""
import csv
import io
import os
import sys

MS = "I_正文_IMRaD_en.md"
APPLY = "--apply" in sys.argv

# --------------------------------------------------------------------------- #
# 1. the Canadian onset-field completeness, as an artifact
# --------------------------------------------------------------------------- #
SRC = "cv/cvponline_extract_20241130/reactions.txt"
OUT = "cv/cv_reaction_onset_completeness.csv"


def measure() -> list[dict]:
    want = ("hyperaesthesia", "procedural pain", "pain", "hyperalgesia")
    total_rows = 0
    field_hits = {2: 0, 3: 0, 4: 0}
    rows = {w: 0 for w in want}
    dated = {w: 0 for w in want}
    with io.open(SRC, encoding="utf-8", errors="replace", newline="") as fh:
        fh.readline()
        for line in fh:
            total_rows += 1
            parts = line.split('"$"')
            if len(parts) < 7:
                continue
            for i in field_hits:
                if len(parts) > i and parts[i].strip().strip('"'):
                    field_hits[i] += 1
            pt = parts[5].strip().strip('"').lower()
            if pt in rows:
                rows[pt] += 1
                if len(parts) > 2 and parts[2].strip().strip('"'):
                    dated[pt] += 1
    out = [{"row": "reaction rows in reactions.txt", "n": total_rows, "with_onset_date": ""}]
    for i, label in ((2, "field 3 (reaction onset date)"),
                     (3, "field 4"), (4, "field 5")):
        out.append({"row": f"rows with a value in {label}", "n": field_hits[i],
                    "with_onset_date": ""})
    for w in sorted(rows):
        out.append({"row": f"rows for the preferred term {w.title()}", "n": rows[w],
                    "with_onset_date": dated[w]})
    return out


# --------------------------------------------------------------------------- #
# 2. manuscript edits
# --------------------------------------------------------------------------- #
EDITS = [
    # ---- §4.5: replace the absolute statement with the counted reason -------
    ("**Route, mapping and releases.** The FDA case-level files could not be retrieved, "
     "so time-to-onset could not be analysed and route cannot be attributed to a drug "
     "record:",
     "**Route, mapping and releases.** Time-to-onset could not be analysed: openFDA "
     "exposes no reaction-onset date, and the Canadian onset fields are too sparsely "
     "populated to support it (Appendix S1 A1.9). Route cannot be attributed to a drug "
     "record:"),

    # ---- §4.3: this paragraph restated §3.6; trim the duplication -----------
    ("Cohort composition explains the pattern: remifentanil's reports come almost "
     "entirely from monitored perioperative care (91.9% serious in Canada; 98.0% in the "
     "serious-report subset), and among opioids the reporter's professional identity "
     "strongly determines which reactions are recorded [28]. Fentanyl's cohort is",
     "Cohort composition explains the pattern: remifentanil's reports come from "
     "monitored perioperative care, where the reporter's professional identity strongly "
     "determines what is recorded [28]. Fentanyl's cohort is"),

    ("For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the low reporting is "
     "probably physiological:",
     "For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the deficit is probably "
     "physiological:"),

    # ---- §4.4: two words ----------------------------------------------------
    ("Opioid-induced hyperalgesia is defined by a change in pain sensitivity, whereas",
     "Opioid-induced hyperalgesia is a change in pain sensitivity, whereas"),

    # ---- §4.6: give clinicians the order of magnitude (T2-26) ---------------
    ("For clinicians, these data support neither a large remifentanil-specific "
     "hyperalgesia reporting burden nor its absence, so decisions about prevention "
     "should rest on the prospective literature [7, 8].",
     "For clinicians, these data support neither a large remifentanil-specific "
     "hyperalgesia reporting burden nor its absence — one report in 200 to 500, "
     "depending on the drug (Table 2) — so decisions about prevention should rest on "
     "the prospective literature [7, 8]."),

    # ---- Table 2 footnote: the zeros are not observed counts (T2-22) --------
    ("they are not evidence of absence, because no report in either corpus carries "
     "those strings.",
     "they are not evidence of absence: the strings are not preferred terms, so no "
     "report in either corpus can carry them, and the column is numeric and cannot hold "
     "a marker for that; Table S4 gives the retrievability of each string. Expressed as "
     "a rate, HYPERAESTHESIA appears in one report in 538 for remifentanil, one in 387 "
     "for fentanyl, one in 296 for sufentanil and one in 216 for morphine."),

    # ---- Appendix S1: a new section carrying the onset counts ---------------
    ("### Appendix S1 (supplementary). Supplementary methods",
     "### Appendix S1 (supplementary). Supplementary methods"),
]

A19 = """
**A1.9 Why no time-to-onset analysis.** The openFDA indexed fields include
`patient.reaction.reactionmeddrapt` but no reaction-onset date, so a time-to-onset
distribution cannot be constructed from the API. The Canadian reaction file does carry
onset fields, and their completeness was counted directly (`reactions.txt`,
`cv/cv_reaction_onset_completeness.csv`): of 4 474 922 reaction rows, 185 764 carry a
value in the onset-date field and 158 335 in each of the two adjacent fields. For the
terms of interest the counts are 13 of 523 Hyperaesthesia rows, 57 of 1 527 Procedural
pain rows and 1 196 of 49 260 Pain rows. A time-to-onset analysis restricted to a
single-digit number of Hyperaesthesia observations would describe nothing, so none was
attempted; the fields are reported here so that the omission is a counted decision
rather than an unexamined one.

"""


def main() -> int:
    text = open(MS, encoding="utf-8").read()
    bad = [(text.count(o), o) for o, _ in EDITS[:-1] if text.count(o) != 1]
    if bad:
        for n, o in bad:
            print(f"!! {n} matches: {o[:90]}")
        return 1

    rows = measure()
    if APPLY:
        with io.open(OUT, "w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {OUT}")
    for r in rows:
        print("   ", r)

    # A1.9 goes at the end of Appendix S1, i.e. just before the figure legends
    marker = "## Figure legends"
    assert text.count(marker) == 1
    i = text.index(marker)
    text = text[:i] + A19 + "\n---\n\n" + text[i:]

    for o, n in EDITS[:-1]:
        text = text.replace(o, n, 1)
    if APPLY:
        open(MS, "w", encoding="utf-8").write(text)
    print(f"{len(EDITS) - 1} edits + A1.9 {'written' if APPLY else '(dry run)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
