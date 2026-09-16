#!/usr/bin/env python3
"""Regenerate Table S1 (system organ class panorama) in the manuscript from source.

Table S1 is the one table in the manuscript too large to maintain by hand: 27
MedDRA system organ classes x 4 opioids x (count, proportion, one ratio, two
head-to-head ratios) = 216 cells per panel. It is therefore generated rather
than typed. This script reads

    cv/cv_soc_27.csv   Canada Vigilance, report-level, native MedDRA SOCs (panel A)
    03_soc_27.csv      FAERS, event-level, heuristic preferred-term mapping (panel B)

and rewrites the whole "### Table S1" block of I_正文_IMRaD_en.md in place.
Denominators are taken from cv/cv_drug_totals.csv and from the drug rows of
03_soc_27.csv, so the proportions shown are recomputed from the counts rather
than copied from the source files; the script also checks the recomputed
proportions against the ones already in those files and refuses to write if
they disagree.

Run after any change to either result file, then re-run _check_consistency.py,
which re-derives every cell of both panels and compares it with the manuscript.
"""

from __future__ import annotations

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(HERE, "I_正文_IMRaD_en.md")
CV_SOC = os.path.join(HERE, "cv", "cv_soc_27.csv")
CV_TOTALS = os.path.join(HERE, "cv", "cv_drug_totals.csv")
FAERS_SOC = os.path.join(HERE, "03_soc_27.csv")

HEADING = "### Table S1 (supplementary). System organ class panorama"
NEXT = "\n### Table S2"
DASH = "\u2014"

DRUGS = ("REMIFENTANIL", "FENTANYL", "SUFENTANIL", "MORPHINE")
LABEL = {"REMIFENTANIL": "Remifentanil", "FENTANYL": "Fentanyl",
         "SUFENTANIL": "Sufentanil", "MORPHINE": "Morphine"}


# --------------------------------------------------------------------------- #
# source files
# --------------------------------------------------------------------------- #
def read_canada() -> tuple[list[dict], dict[str, int]]:
    with open(CV_TOTALS, encoding="utf-8-sig", newline="") as fh:
        cohorts = {r["Drug"].strip().upper(): int(r["N_suspect_reports"])
                   for r in csv.DictReader(fh)}
    with open(CV_SOC, encoding="utf-8-sig", newline="") as fh:
        rows = [{k.strip(): (v or "").strip() for k, v in r.items()}
                for r in csv.DictReader(fh)]
    return rows, cohorts


def read_faers() -> tuple[list[dict], dict[str, int], int]:
    lines = open(FAERS_SOC, encoding="utf-8-sig").read().splitlines()

    di = next(i for i, l in enumerate(lines) if l.startswith("Drug,"))
    cohorts = {}
    for l in lines[di + 1:di + 1 + len(DRUGS)]:
        name, total, _cov = next(csv.reader([l]))
        cohorts[name.strip().upper()] = int(total)

    hi = next(i for i, l in enumerate(lines) if l.startswith("SOC,"))
    header = next(csv.reader([lines[hi]]))
    rows = []
    for l in lines[hi + 1:]:
        if not l.strip():
            break
        rows.append(dict(zip(header, next(csv.reader([l])))))
    rows = [{k.strip(): (v or "").strip() for k, v in r.items()} for r in rows]

    n_total = next(int(l.split(",")[1]) for l in lines if l.startswith("N_total_reactions,"))
    return rows, cohorts, n_total


# --------------------------------------------------------------------------- #
# formatting
# --------------------------------------------------------------------------- #
def count(n: int) -> str:
    """Thousands separated by a space, matching the rest of the manuscript."""
    return f"{n:,}".replace(",", " ")


def pct(n: int, cohort: int) -> str:
    return f"{n / cohort * 100:.1f}"


def ratio(value: str) -> str:
    return DASH if value == "" else f"{float(value):.3f}"


def cell_pair(n: int, cohort: int) -> str:
    return f"{count(n)} ({pct(n, cohort)})"


def md_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def panel(rows: list[dict], cohorts: dict[str, int], keys: dict) -> list[str]:
    """Build one panel: header, separator, then one row per system organ class."""
    out = [md_row(["System organ class"] + [LABEL[d] for d in DRUGS]
                  + ["ROR", "RORR vs fentanyl", "RORR vs morphine"]),
           "|---|---:|---:|---:|---:|---:|---:|---:|"]

    def order(r):
        ror = r.get(keys["ror"], "")
        return (0, -float(ror)) if ror else (1, 0)

    for r in sorted(rows, key=order):
        out.append(md_row(
            [r[keys["soc"]]]
            + [cell_pair(int(r[keys["n"] % d]), cohorts[d]) for d in DRUGS]
            + [ratio(r.get(keys["ror"], "")),
               ratio(r.get(keys["rr_fen"], "")),
               ratio(r.get(keys["rr_mor"], ""))]))
    return out


# --------------------------------------------------------------------------- #
# self-checks, then splice
# --------------------------------------------------------------------------- #
def verify_source(rows: list[dict], cohorts: dict[str, int], keys: dict,
                  label: str, worst: float = 0.06) -> int:
    """Recomputed proportion must reproduce the proportion already in the file."""
    bad = 0
    for r in rows:
        for d in DRUGS:
            if keys["p"] % d not in r or not r[keys["p"] % d]:
                continue
            got = float(pct(int(r[keys["n"] % d]), cohorts[d]))
            exp = r[keys["p"] % d]
            if abs(got - float(exp)) > worst:
                print(f"  !! {label} {r[keys['soc']]} {d}: recomputed {got} vs file {exp}")
                bad += 1
    return bad


def build_block(cv_rows, cv_cohorts, fd_rows, fd_cohorts, fd_total) -> str:
    cv_panel = panel(cv_rows, cv_cohorts,
                     dict(soc="SOC", n="%s_reports", p="%s_pct", ror="REMI_ROR",
                          rr_fen="RORR_REMI_vs_FEN", rr_mor="RORR_REMI_vs_MOR"))
    fd_panel = panel(fd_rows, fd_cohorts,
                     dict(soc="SOC", n="%s_reports", p="%s_pct", ror="REMI_ROR",
                          rr_fen="RORR_vs_FEN", rr_mor="RORR_vs_MOR"))

    def cohort_list(c):
        return ", ".join(f"{count(c[d])} ({LABEL[d].lower()})" for d in DRUGS)

    return "\n".join([
        HEADING,
        "",
        "Both panels give, for every MedDRA system organ class, the number of reports or "
        "events for each opioid with the proportion of that drug's own cohort in parentheses, "
        "the reporting odds ratio for remifentanil alone, and the head-to-head ratio of "
        "reporting odds ratios for remifentanil against fentanyl and against morphine. "
        f"Cohorts were {cohort_list(cv_cohorts)} reports in Canada Vigilance, and "
        f"{cohort_list(fd_cohorts)} reports in the FAERS analysis, out of "
        f"{count(fd_total)} reactions in total. Proportions are rounded to one decimal place "
        "and ratios to three. Rows are ordered by the remifentanil reporting odds ratio, "
        "descending, with classes in which remifentanil recorded no report listed last; for "
        "those classes no ratio is estimable and the cell carries a dash, so a dash means "
        "\"not estimable\", not zero.",
        "",
        "**Panel A. Canada Vigilance, native MedDRA system organ classes, report-level "
        "(authoritative).**",
        "",
        *cv_panel,
        "",
        "**Panel B. FAERS, exploratory, event-level counts after heuristic preferred-term "
        "mapping.**",
        "",
        *fd_panel,
        "",
        "Panel B is event-level: a report naming several preferred terms that map to the same "
        "class contributes more than once, and the class assignment comes from a heuristic "
        "term mapping rather than from native MedDRA coding, so it is reported for qualitative "
        "corroboration only and panel A is the authoritative one. Preferred terms that the "
        "heuristic could not map are listed in the study repository (`03_soc_27.csv`), with the "
        "counts for the unmapped terms of each drug. Both panels are reproduced in full, cell "
        "by cell, by the study repository.",
        "",
    ])


def main() -> int:
    cv_rows, cv_cohorts = read_canada()
    fd_rows, fd_cohorts, fd_total = read_faers()

    bad = verify_source(cv_rows, cv_cohorts,
                        dict(soc="SOC", n="%s_reports", p="%s_pct"), "Canada")
    bad += verify_source(fd_rows, fd_cohorts,
                         dict(soc="SOC", n="%s_reports", p="%s_pct"), "FAERS")
    if bad:
        print(f"ABORT: {bad} proportion(s) in the source files do not reproduce from the counts")
        return 1

    block = build_block(cv_rows, cv_cohorts, fd_rows, fd_cohorts, fd_total)

    text = open(MS, encoding="utf-8").read()
    start = text.index(HEADING)
    end = text.index(NEXT, start)
    new = text[:start] + block + text[end:]

    changed = new != text
    open(MS, "w", encoding="utf-8", newline="\n").write(new)

    print(f"Canada  : {len(cv_rows)} classes, cohorts " +
          ", ".join(f"{d}={cv_cohorts[d]}" for d in DRUGS))
    print(f"FAERS   : {len(fd_rows)} classes, cohorts " +
          ", ".join(f"{d}={fd_cohorts[d]}" for d in DRUGS) + f", N_total={fd_total}")
    print(f"Table S1 : {len(cv_rows) + len(fd_rows)} data rows + 2 header rows "
          f"= {(len(cv_rows) + len(fd_rows)) * 8} cells")
    print(f"manuscript {'rewritten' if changed else 'already up to date'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
