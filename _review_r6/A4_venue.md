# A4 — Venue / reporting-standard review (*Anaesthesia*, Original Article)

**Reviewer role:** journal-editor + reporting-standard auditor (independent, treated as first submission).
**Manuscript:** *Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis* (single author, remifentanil / opioid-induced hyperalgesia, FAERS + Canada Vigilance disproportionality).
**Verdict in brief:** No desk-reject hard-fail found. Word counts, figure spec, AI disclosure, title consistency, READUS-PV completeness and reference DOIs are all in order. Five *minor* items should be reconciled before submission (details below).

---

## Issues

### Issue 1 — READUS-PV "two items not applicable" undercounts/collapses granular checklist items
【Problem】The manuscript states only "two items" are not applicable, but the checklist itself marks **three** case-by-case items (7d, 10, 2e) and the registration item (14d) is *addressed*, not "not applicable".
【Evidence】`I_正文_IMRaD_en.md:451` — "with an explicit note on the **two items** that are not applicable (case-by-case analysis; protocol registration)." Yet `I_TableS2_READUS-PV_checklist.md` maps case-by-case to body items **7d** and **10** plus abstract item **2e** (three separate checklist rows), and item **14d** (protocol registration) is described at line 76 as "reported here rather than left blank because READUS-PV asks for a statement on registration, not for registration itself" — i.e. addressed, not N/A.
【Why it matters】A reporting-standards reviewer counting granular checklist rows sees up to 3 (case-by-case) + 1 (registration) = 4 non-applicable/non-performances, not 2. Calling 14d "not applicable" also slightly mischaracterises it, since the checklist explicitly states it was reported. This is a clarity/honesty nit, not a content error, but it is exactly the kind of claim an Associate Editor verifies line-by-line.
【Specific fix】Rephrase line 451 to enumerate the actual rows:
> "with explicit notes on the items that could not be addressed: case-by-case analysis and causality assessment were not performed (body items 7d and 10; abstract item 2e); prospective registration was absent and is stated rather than implied (body item 14d)."

---

### Issue 2 — Reference 32 lists all seven authors instead of Wiley "first 6 + et al." style
【Problem】`Drug Saf` 2025 reference lists 7 authors with no "et al.", deviating from the Vancouver/ Wiley house style used elsewhere in the list.
【Evidence】`I_正文_IMRaD_en.md:220` — "Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, Muñoz MA." (7 names, no truncation). Other 7-author-free refs follow first-6 + et al. (e.g. none exceed 6 here except this one).
【Why it matters】*Anaesthesia* (Wiley) uses Vancouver style that truncates author lists at six with "et al." This is a copy-edit flag, not a scientific issue, but an inconsistent reference block is a common desk-reject-for-formatting trigger and is trivial to fix now.
【Specific fix】Change to:
> "Janiczak S, Tanveer S, Tom K, Zhang R, Ma Y, Wolf L, et al."

---

### Issue 3 — Figures are saved with an alpha channel (RGBA); line art should be opaque/white background
【Problem】Both TIF figures carry an alpha (transparency) channel; *Anaesthesia* line-art submissions should have a solid white (opaque) background.
【Evidence】`05_figures.py` renders with the Agg backend and never sets a white `figure.facecolor`; PIL reports `I_fig1_rorr_forest.tif` and `I_fig2_year_trend.tif` as **mode=RGBA**, dpi (600,600). Files exist and are ≤10 MB (735 KB / 418 KB), 600 ppi — spec met apart from transparency.
【Why it matters】A transparent background can render incorrectly when placed on the page and some ScholarOne/ingest pipelines reject or warn on alpha in line art. Low severity, but a needless reformatting round-trip.
【Specific fix】In `05_figures.py` after `plt.subplots(...)` add `fig.patch.set_facecolor("white")` (and `ax.set_facecolor("white")`), or composite onto white before saving; re-run so the shipped TIF/PDF are opaque RGB.

---

### Issue 4 — CITATION.cff self-citation placeholder title differs from the manuscript title
【Problem】The self-citation entry inside `CITATION.cff` uses a different title than the submitted manuscript.
【Evidence】`CITATION.cff:47` title = "…a head-to-head disproportionality study with a terminology caution", whereas the canonical title is `CITATION.cff:3` = `I_正文_IMRaD_en.md:1` = `I_投稿信_cover_letter.md:10` = `README.md:9` ("…an observational head-to-head disproportionality analysis"). Line 53 marks it "Manuscript in preparation."
【Why it matters】A self-citation whose title disagrees with the article is confusing for the DOI record and for any tool that reads `CITATION.cff`; on acceptance the metadata should match exactly.
【Specific fix】Set `CITATION.cff:47` title to the exact manuscript title, or leave the placeholder clearly flagged as "in preparation" and reconcile it to the accepted title/DOI at acceptance.

---

### Issue 5 — openFDA access date is stated two ways (16 September vs 16 and 18 September)
【Problem】The disclosed extraction/access date for openFDA is inconsistent between the Methods body, the checklist, and the Acknowledgements.
【Evidence】`I_正文_IMRaD_en.md:47` "at extraction (16 September 2026)"; checklist item 5b "extraction date 16 September 2026 for both sources"; but `I_正文_IMRaD_en.md:179` (Acknowledgements) "openFDA drug/event data (… **accessed 16 and 18 September 2026**)".
【Why it matters】READUS-PV item 5b wants a single, explicit extraction date. Two dates can be read as two separate extractions and slightly undercuts the "database access date disclosed" claim the manuscript leans on. Minor, but a reviewer will ask which date is the corpus snapshot.
【Specific fix】Reconcile both §2.1 and Acknowledgements to one phrasing, e.g. "openFDA indexed corpus (20 692 687 reports) as of **16 September 2026**; the interface was queried on 16 and 18 September 2026."

---

## § Stands up (compliance confirmed, with evidence)

1. **Word limits met and verified by gate.** `_wordcount.py` asserts MAIN 3000–4000 and SUMMARY 250–300; running it returns `MAIN TEXT 3996 words (allowed 3000-4000) OK` and `SUMMARY 296 words (allowed 250-300) OK`. Manuscript `I_正文_IMRaD_en.md:13` and `:17–26` declare exactly these figures. The Summary is structured Introduction/Methods/Results/Discussion as the brief requires.
2. **Figures meet the *Anaesthesia* line-art spec.** `05_figures.py:23` sets `DPI = 600`; `clean_axes()` (lines 60–65) removes top/right spines and calls `ax.grid(False)`; the legend box is explicitly deleted (lines 169–170, 238) and no in-figure title is set. Outputs `I_fig1_rorr_forest.tif/.pdf` and `I_fig2_year_trend.tif/.pdf` exist, PIL confirms dpi (600,600) and sizes 735 KB / 418 KB (≪10 MB). The Figure 1 legend sits in the separate "Figure legends" section (`I_正文_IMRaD_en.md:725–727`), outside the artwork, and correctly explains symbols + error bars.
3. **AI disclosure is complete and correctly placed.** Full disclosure at `I_正文_IMRaD_en.md:181` (in Acknowledgements, **after** Conclusion at `:161–163`), uses (i)–(iv), states no AI as author/contributor, and states verification against archived source. `_wordcount.py` slices main text `## 1. Introduction` → `## Acknowledgements`, so the disclosure is **excluded** from the 3 996-word count. The cover letter echoes it verbatim (`I_投稿信_cover_letter.md:24`).
4. **Title is identical in 4 required locations.** Manuscript `:1` = cover letter `:10` = `README.md:9` = `CITATION.cff:3`. No mismatch in the title proper.
5. **READUS-PV checklist is present and internally complete.** `I_TableS2_READUS-PV_checklist.md` contains 32 body + 12 abstract items, each mapped to a manuscript section; formulae (A1.3), signal definition (§2.4), database access dates (§2.1), and spontaneous-reporting limitations (§4.5) are all addressed. The repository consistency gate `_check_consistency.py` returns **PASS 528 / FAIL 0**, confirming every quoted number traces to its source file — strong evidence of reporting honesty.
6. **References comply.** 33 cited; all journal articles carry a DOI (manuscript `:187` states the policy; 4 spot-checked DOIs — `10.1097/ACO.0000000000001400`, `10.1093/bja/aeu137`, `10.1007/s40264-024-01421-9`, `10.1016/j.bja.2018.09.019` — all return HTTP 302 = valid). Journal names italic, volumes bold, Vancouver order.

---

## § Questions for the authors

- Confirm against the **live** *Anaesthesia* Author Guidelines that the structured Summary headings "Introduction/Methods/Results/Discussion" are accepted (some Wiley journals expect "Background/Methods/Results/Conclusions"). The brief assumes Discussion is fine, but verify before submit.
- Why does openFDA carry **two** access dates (16 and 18 September 2026)? Which is the corpus snapshot quoted as 20 692 687 reports? (Issue 5.)
- For the `CITATION.cff` self-citation (line 47), will the title/DOI be reconciled to the accepted article at acceptance? (Issue 4.)
- Confirm the submission pack uploads the two figures as **separate** ScholarOne files (.tif/.pdf), not embedded in the manuscript DOCX, per the cover letter's "Format" paragraph.

---

## § What I actually checked

**Files read (in full or as cited):**
- `I_正文_IMRaD_en.md` (title→Conclusion, Acknowledgements, References, Figure legends; structure via heading grep)
- `I_投稿信_cover_letter.md`
- `05_figures.py`
- `_wordcount.py`
- `I_TableS2_READUS-PV_checklist.md`
- `README.md`
- `CITATION.cff`

**Commands run:**
- `python _wordcount.py` → MAIN 3996 OK, SUMMARY 296 OK (exit 0).
- `python _check_consistency.py` → `PASS 528 / FAIL 0` (exit 0).
- PIL inspection of figure files → dpi (600,600), mode RGBA, sizes 735 KB / 418 KB.
- `curl -I https://doi.org/<doi>` for 4 references → all 302 (resolve).
- `grep` for N/A / "not applicable" and for placeholder tokens (TODO/TBD/placeholder/待填/占位) in manuscript + cover letter → only the intended "two items not applicable" sentence; no leftover placeholders.

**Discrepancies found:** none that would block submission. Five minor items listed above (Issues 1–5). I did **not** read the forbidden files (`REVIEW_*.md`, `RESPONSE_*.md`, `REVISION_*.md`, `SUBMISSION_MANIFEST.md`, `GITHUB_DEPOSIT_SOP.md`, `author_verification_statement.md`, or the other three reviewers in `review_round6/`), and treated this as a first submission.
