# -*- coding: utf-8 -*-
"""
R6-19: MedDRA term-level verification, dictionary side.

Reads the ADReCS ADR ontology (v3.3) — an independent adverse-reaction ontology
that carries MedDRA codes for every ADR term — and extracts every term in the
hyperalgesia / hyperaesthesia / allodynia conceptual family, with its MedDRA code,
its MedDRA hierarchy path and its synonym list.

The load-bearing question: does any ADR term named "Hyperalgesia" carry a MedDRA
code of its own, or is the concept subsumed under HYPERAESTHESIA (10020568)?

The file is downloaded from the public ADReCS download page; it is not
redistributed with this repository, in the same way as the two source corpora.

    https://www.bio-add.org/ADReCS/download.jsp
    https://www.bio-add.org/ADReCS/download/v3.3/ADR_ontology_v3.3.xlsx

Usage:
    python _r6_term_dictionary_check.py [path/to/ADR_ontology_v3.3.xlsx]

Output: `_r6_term_dictionary_check.csv` — matched rows, verbatim, plus a verdict
block. Parsing is done directly from the xlsx zip container so that the script
does not depend on a spreadsheet library.

The verdict block ends with a DECLARED_EXTERNAL_PROXIES section. Those four rows
are not computed here: they are transcribed by hand from Cochrane's linked-data
export and from MeSH, and are kept in the artifact so that the manuscript's
Table S4 note can be bound to a file. They are proxies, because MedDRA itself is
subscription-only.
"""

import csv
import io
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_r6_term_dictionary_check.csv")
DEFAULT_SRC = os.path.join(HERE, "cv", "adrecs_ADR_ontology_v3.3.xlsx")

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NEEDLES = ("ALGES", "AESTH", "ALLODYN", "HYPERA", "HYPOAESTH", "HYPERESTH")

# --------------------------------------------------------------------------- #
# Declared external proxies — read by hand from public sources, NOT computed.
#
# MedDRA is a subscription dictionary maintained by the MSSO and is not
# redistributable, so the LLT-to-PT hierarchy cannot be shown from a first-party
# extract. The two rows below are the public, checkable substitutes: Cochrane's
# linked-data export attaches a MedDRA code to the condition "Hyperalgesia", and
# MeSH keeps hyperalgesia and hyperaesthesia as separate descriptors. Both are
# reported in the manuscript as proxies, never as a MedDRA extract.
#
# Re-check by opening the two URLs; the values are transcribed verbatim.
# --------------------------------------------------------------------------- #
EXTERNAL_PROXIES = [
    ("cochrane_meddra_code_for_Hyperalgesia", "10020573",
     "https://data.cochrane.org/concepts/r4hp39n833dx", "18/09/2026"),
    ("cochrane_meddra_code_for_parent_PT_HYPERAESTHESIA", "10020568",
     "https://data.cochrane.org/concepts/r4hp39n833dx", "18/09/2026"),
    ("mesh_descriptor_for_Hyperalgesia", "D006930",
     "https://meshb.nlm.nih.gov/record/ui?ui=D006930", "18/09/2026"),
    ("mesh_descriptor_for_Hyperesthesia", "D006941",
     "https://meshb.nlm.nih.gov/record/ui?ui=D006941", "18/09/2026"),
]


def shared_strings(zf):
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    out = []
    for si in root.findall(NS + "si"):
        out.append("".join(t.text or "" for t in si.iter(NS + "t")))
    return out


def col_index(ref):
    letters = re.match(r"[A-Z]+", ref or "A").group(0)
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def read_sheet(path):
    zf = zipfile.ZipFile(path)
    shared = shared_strings(zf)
    sheets = sorted(n for n in zf.namelist()
                    if re.match(r"xl/worksheets/sheet\d+\.xml$", n))
    rows = []
    for name in sheets:
        root = ET.fromstring(zf.read(name))
        for row in root.iter(NS + "row"):
            cells = {}
            for c in row.findall(NS + "c"):
                idx = col_index(c.get("r"))
                v = c.find(NS + "v")
                if c.get("t") == "inlineStr":
                    is_el = c.find(NS + "is")
                    val = "".join(t.text or "" for t in is_el.iter(NS + "t")) if is_el is not None else ""
                elif v is None:
                    val = ""
                elif c.get("t") == "s":
                    val = shared[int(v.text)]
                else:
                    val = v.text or ""
                cells[idx] = val
            if cells:
                width = max(cells) + 1
                rows.append([cells.get(i, "") for i in range(width)])
    zf.close()
    return rows


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC
    if not os.path.exists(src):
        print("ABORT: ontology file not found:", src)
        print("Download it first, e.g.")
        print("  curl -L -o cv/adrecs_ADR_ontology_v3.3.xlsx "
              "https://www.bio-add.org/ADReCS/download/v3.3/ADR_ontology_v3.3.xlsx")
        return 2

    rows = read_sheet(src)
    print("rows read:", len(rows))
    if not rows:
        return 3
    header = rows[0]
    print("header:", header)
    print("first data row:", rows[1] if len(rows) > 1 else None)

    # Locate the columns by header name rather than by position.
    def find(*names):
        for i, h in enumerate(header):
            if (h or "").strip().upper() in names:
                return i
        return None

    i_term = find("ADR_TERM")
    i_syn = find("ADR_SYNONYMS")
    i_code = find("MEDDRA_CODE")
    if i_term is None or i_code is None:
        print("ABORT: expected columns ADR_TERM / MEDDRA_CODE not found")
        return 4
    print("columns: ADR_TERM=%s ADR_SYNONYMS=%s MEDDRA_CODE=%s" % (i_term, i_syn, i_code))

    def term_of(row):
        return (row[i_term] or "").strip().upper() if i_term < len(row) else ""

    def syn_of(row):
        return (row[i_syn] or "") if (i_syn is not None and i_syn < len(row)) else ""

    def code_of(row):
        return (row[i_code] or "").strip() if i_code < len(row) else ""

    matched = []
    for r in rows[1:]:
        joined = (term_of(r) + " | " + syn_of(r).upper())
        if any(n in joined for n in NEEDLES):
            matched.append(r)

    # Rows whose ADR TERM is itself a hyperalgesia string (i.e. the concept would
    # have an entry, and a MedDRA code, of its own).
    exact_hyperalgesia = [r for r in rows[1:] if term_of(r).startswith("HYPERALG")]
    # Rows that mention hyperalgesia anywhere but are named something else
    # (i.e. the concept is carried as a synonym of another term).
    carried_as_synonym = [r for r in matched
                          if "HYPERALG" in syn_of(r).upper()
                          and not term_of(r).startswith("HYPERALG")]
    with_code = [r for r in matched if re.fullmatch(r"\d{8}", code_of(r))]

    # The ontology holds several entries for some concepts (one per ADReCS node),
    # so "rows" overstates the number of distinct preferred terms. Count the
    # distinct (term, MedDRA code) pairs as well, and report those to the
    # manuscript; the row count alone would inflate the carrier list.
    carrier_pairs = sorted({(term_of(r), code_of(r)) for r in carried_as_synonym})

    with open(OUT, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        for r in matched:
            w.writerow(r)
        w.writerow([])
        w.writerow(["VERDICT", "value"])
        w.writerow(["source_file", os.path.basename(src)])
        w.writerow(["source_url",
                    "https://www.bio-add.org/ADReCS/download/v3.3/ADR_ontology_v3.3.xlsx"])
        w.writerow(["rows_in_ontology", len(rows) - 1])
        w.writerow(["terms_matching_concept_family", len(matched)])
        w.writerow(["entries_named_HYPERALG*", len(exact_hyperalgesia)])
        w.writerow(["entries_carrying_hyperalgesia_as_synonym", len(carried_as_synonym)])
        w.writerow(["distinct_carriers_of_hyperalgesia_as_synonym", len(carrier_pairs)])
        w.writerow(["entries_carrying_a_MedDRA_code", len(with_code)])
        for r in exact_hyperalgesia:
            w.writerow(["ENTRY_NAMED_HYPERALG", term_of(r), code_of(r)])
        for r in carried_as_synonym:
            w.writerow(["CARRIER_ENTRY", term_of(r), code_of(r)])
        for term, code in carrier_pairs:
            w.writerow(["DISTINCT_CARRIER", term, code])

        # ------------------------------------------------------------------ #
        # Declared external proxies. NOT computed by this script: these are
        # values read by hand from two public sources on 18 September 2026 and
        # recorded here so that the manuscript's table note can be bound to a
        # file rather than to an unbacked assertion. MedDRA itself is a
        # subscription dictionary, so no first-party extract of the LLT-to-PT
        # hierarchy can be redistributed with this repository; the proxies are
        # the strongest public substitute and are labelled as proxies.
        # ------------------------------------------------------------------ #
        w.writerow([])
        w.writerow(["DECLARED_EXTERNAL_PROXIES", "value", "source_url",
                    "accessed"])
        for row in EXTERNAL_PROXIES:
            w.writerow(row)

    print()
    print("VERDICT")
    print("  ontology rows (excl. header)             :", len(rows) - 1)
    print("  matching the concept family              :", len(matched))
    print("  entries named HYPERALG* (own code)       :", len(exact_hyperalgesia))
    print("  entries carrying hyperalgesia as synonym :", len(carried_as_synonym))
    print("  distinct carrier terms                   :", len(carrier_pairs))
    print("  entries carrying a MedDRA code           :", len(with_code))
    for r in exact_hyperalgesia:
        print("   NAMED:", term_of(r), code_of(r))
    for r in carried_as_synonym:
        print("   CARRIER:", term_of(r), code_of(r),
              "| synonyms contain HYPERALG:", "HYPERALG" in syn_of(r).upper())
    print()
    print("  declared external proxies (read by hand, not computed):")
    for row in EXTERNAL_PROXIES:
        print("   ", row[0], "=", row[1])
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
