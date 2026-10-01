# Submission field guide — *Pharmacoepidemiology and Drug Safety* (PDS)

> Companion to `SUBMISSION_MANIFEST.md` (the authoritative "what to upload" manifest).
> This file maps the Wiley **Research Exchange** submission fields to the local build
> artefacts produced by `python _build_submission.py` (output in `_upload/`).
> Journal: *Pharmacoepidemiology and Drug Safety* (Wiley / ISPE). EIC: **Brian L. Strom**.
> Manuscript version cited throughout: **v1.9.5**.

## Research Exchange field → local file

| Research Exchange field | Local file (`_upload/`) | Notes |
|---|---|---|
| Article type | — | Select **Original Report** |
| Title | (from `I_正文_IMRaD_en.md`, line 1) | "Term selection, not the drug: how the chosen preferred term decides remifentanil hyperalgesia reporting in two national pharmacovigilance databases" |
| Abstract | (from `I_正文_IMRaD_en.md`, `## Summary`) | Structured: **Objective / Methods / Results / Conclusions**; 299 words |
| Keywords | (from title page) | remifentanil; opioid-induced hyperalgesia; pharmacovigilance; disproportionality analysis; spontaneous reporting |
| Cover letter | `Cover_Letter.docx` (also `Cover_Letter_PDS.docx`) | Addressed to Prof. Brian L. Strom; restates the AI disclosure and data-availability statement |
| Manuscript file (Main Document) | `Manuscript.docx` | Title page → Summary → body → Acknowledgements → References → Tables 1–6 → figure legends |
| Figures | `I_fig1_rorr_forest.tif` / `.pdf`, `I_fig2_year_trend.tif` / `.pdf` | Line art, 600 ppi, 180 mm wide; no title/border/grid/legend box inside the image |
| Supplementary Material | `Supporting_Information.docx` | Tables S1 (panels A & B) and S3–S9, plus Appendix S1 |
| Supplementary Material (checklist) | `READUS-PV_checklist.docx` | Completed READUS-PV checklist promised in §4.6 / Table S2 |
| Author disclosure / COI | PDS COI form (completed in the system) | No competing interests; no funding. State the single-author status. |
| Funding statement | (manuscript Declarations) | "The research did not receive any specific grant…" |
| Data availability | (manuscript Declarations) | Repository URL + `v1.9.5` release; raw FAERS / Canada Vigilance not redistributed |
| AI-use disclosure | (manuscript *Acknowledgements* → Use of generative AI) | Restated in the cover letter and the Author Verification Statement |

## PDS-specific points to confirm at submission

1. **Body-word cap.** Original Reports "typically do not exceed" 3 000 words of body text
   (Introduction to Conclusion, headings included). The manuscript is **3 974 words** — inside
   the 3 000–4 000 gate window but 974 words above PDS's typical 3 000-word soft cap; the gap is
   the cost of preserving every gate-locked number and phrase. No further non-numeric slack
   remains before a scientific figure would need to move.
2. **Structured abstract** uses Objective/Methods/Results/Conclusions (PDS house style).
3. **Transparency statement** after the READUS-PV line cites Wang & Pottegård 2024 (ref 40).
4. **AI policy** — the manuscript cites Wiley's Generative-AI policy; the disclosure lives in
   the Declarations, not in the abstract or competing-interests section.
5. **COI form** — Wiley requires the journal's own COI form in addition to the manuscript
   statement; complete it in Research Exchange (no conflicts to declare here).
6. **Repository URL** must resolve in a browser immediately before submitting:
   <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.9.5>
