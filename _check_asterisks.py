#!/usr/bin/env python3
"""Cross-check every signal asterisk in manuscript Table 2 against the source booleans.

Table 2 prints one column per drug (remifentanil, fentanyl, sufentanil, morphine) with
an asterisk marking a signal. Those asterisks were typed by hand, so this script re-derives
them from 01_faers_results.csv and reports any disagreement. Run it after any edit to
Table 2, and keep the equivalent assertion in _check_consistency.py.
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")
SRC = os.path.join(HERE, "01_faers_results.csv")

DRUGS = [("REMIFENTANIL", 3), ("FENTANYL", 4), ("SUFENTANIL", 5), ("MORPHINE", 6)]  # column index in the md row

def table2_rows(text):
    i = text.index("### Table 2.")
    j = text.index("### Table 3.", i)
    block = text[i:j]
    out = {}
    for line in block.splitlines():
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 9 or cells[0] in ("Preferred term",) or set(cells[0]) <= set("- "):
            continue
        out[cells[0]] = cells
    return out


def main():
    src = {r["PT"]: r for r in csv.DictReader(open(SRC, encoding="utf-8-sig"))}
    md = table2_rows(open(MS, encoding="utf-8").read())

    bad = 0
    checked = 0
    for pt, cells in md.items():
        if pt not in src:
            print(f"  !! {pt}: in manuscript Table 2 but not in source")
            bad += 1
            continue
        for drug, idx in DRUGS:
            cell = cells[idx]
            has_star = "*" in cell
            want = str(src[pt][f"{drug}_signal"]).strip().lower() == "true"
            # a dash means the ratio was not estimable; no asterisk expected
            estimable = cell not in ("—", "") and not cell.startswith("—")
            if estimable:
                checked += 1
                if has_star != want:
                    print(f"  MISMATCH {pt:24s} {drug:12s} md_star={has_star} source_signal={want}  cell={cell!r}")
                    bad += 1
            elif has_star:
                print(f"  MISMATCH {pt:24s} {drug:12s} asterisk on a non-estimable cell {cell!r}")
                bad += 1
    print(f"\nchecked {checked} estimable cells across {len(md)} terms; mismatches = {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
