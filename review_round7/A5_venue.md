# A5 — Venue review (Editor + reporting-standard auditor)

**Journal:** *Anaesthesia* (Wiley / Association of Anaesthetists) · Article type declared: Original Article
**Manuscript:** "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis" (git `main@80b217d`, v1.6.0)
**Review status:** First submission; I have not read any other reviewer's file. This review covers only the venue layer — reporting-checklist honesty, format hard-fails, and cover-letter/manuscript consistency.

---

## Problem 1 — READUS-PV checklist cites a section that does not exist (item 9 → "§3.9")

【Problem】 The READUS-PV checklist maps its item 9 (present all results with CIs) to four manuscript locations, the last of which is "the pseudo-signal illustration of section 3.9." The submitted manuscript has no §3.8 or §3.9; its Results sections run 3.1–3.7 only, and there is no "pseudo-signal illustration" anywhere in the text. The checklist's own preamble contradicts itself on this point.

【Evidence】
- `I_TableS2_READUS-PV_checklist.md` (item 9, Location column): "…the pseudo-signal illustration of section 3.9."
- `I_TableS2_READUS-PV_checklist.md` (intro, line re-verified 18 Sep 2026): "the seven Results sections are 3.1 to 3.7."
- `I_正文_IMRaD_en.md`: Results are §3.1–§3.7; §4 begins at "## 4. Discussion". No §3.9 exists; searching the manuscript for "pseudo-signal" returns nothing.

【Why it matters】 A reporting checklist's core promise is that each item is traceable to a real location in the manuscript. A citation to a phantom section fails that promise and undermines the credibility of the whole checklist — exactly the thing an editor checks first. It also suggests the checklist was not re-verified against the final section numbering despite the stated 18 September re-verification.

【Specific fix】 In the item‑9 row, replace "the pseudo-signal illustration of section 3.9" with the correct location (or delete it if no such illustration exists), e.g.: "…the system organ class panorama of §3.7, the Canadian rates in Table 3 and the two panels of Table S1; the proxy HYPERAESTHESIA point estimates in §3.3 are labelled as a term‑level demonstration, not a signal." Also correct the preamble's section count if any §3.8/§3.9 was intended.

---

## Problem 2 — READUS-PV item 7d/10 justification ("case-level files not accessible") is contradicted by the manuscript's own Table S9

【Problem】 Items 7d and 10 (and the Notes section) justify *not* performing case-by-case analysis on the grounds that "the case-level FDA files that individual case review would require were not accessible from our environment (§4.5)." Yet the manuscript itself presents a fully case-level table (Table S9: individual safety report identifiers, products named, received dates, country, age, sex, serious flags) extracted from the same openFDA interface. The "not accessible" reason is therefore false.

【Evidence】
- `I_TableS2_READUS-PV_checklist.md` (item 7d): "the case-level FDA files that individual case review would require were not accessible from our environment (§4.5)."
- `I_TableS2_READUS-PV_checklist.md` (Note 1): "The FDA case-level and drug-record-level files that would permit individual case review were not retrievable from our working environment."
- `I_正文_IMRaD_en.md` §2.1: openFDA `drug/event` interface returns report-level JSON that includes drug-product and reaction fields (this is how Table S9 was built).
- `I_正文_IMRaD_en.md` Table S9 (lines ~627–661): 10 individual safety report identifiers with products, dates, demographics — i.e. case-level data the author demonstrably accessed.

【Why it matters】 The honest barrier to a formal case-by-case *causality* review is not inaccessibility of case-level fields (those are available) but the absence of a patient identifier and of FDA source de-duplication in openFDA, plus the fact that no causality assessment was actually undertaken. Stating the files were inaccessible is an inaccurate justification that an alert reviewer will catch against Table S9, damaging the checklist's trustworthiness.

【Specific fix】 Rewrite the item 7d / Note 1 justification, e.g.: "Not performed. The openFDA drug/event interface returns report-level records that include case-level product and reaction fields (Table S9), but the records carry no patient identifier and openFDA omits FDA's case-level de-duplication, so series such as the one in §3.3 cannot be collapsed to individuals and a formal case-by-case causality review was not undertaken. The limitation is stated in §4.5–§4.6." Drop the "not accessible / not retrievable" wording.

---

## Problem 3 — Access date is stated two different ways across the package (duplicate-value trap)

【Problem】 The data extraction/access date is given as a single date, 16 September 2026, in the abstract, §2.1, the checklist, and the reference list (formatted 16/09/2026); but the manuscript's Data availability statement says openFDA was "accessed 16 and 18 September 2026." A reader cannot tell whether a second data pull occurred on 18 September or whether "18 September" is a slip for the analytical-plan Amendment 2 date.

【Evidence】
- `I_正文_IMRaD_en.md` §2.1: "the indexed corpus contained 20 692 687 reports at extraction (16 September 2026)."
- `I_正文_IMRaD_en.md` Acknowledgements / Data availability: "openFDA drug/event data (… accessed 16 and 18 September 2026)".
- `I_正文_IMRaD_en.md` References 18–19: "(accessed 16/09/2026)."
- `I_投稿信_cover_letter.md` (study description): "extraction date 16 September 2026 for both sources."
- (For contrast) `I_正文_IMRaD_en.md` §2.3 mentions "Amendment 2 on 18 September 2026" — a plan date, not a data-access date.

【Why it matters】 Inconsistent provenance dates are a classic reporting-integrity red flag; an editor needs one unambiguous extraction date per database. If no second pull happened, the "and 18 September 2026" is simply wrong and should be removed. If a second pull did happen, it must be stated everywhere consistently.

【Specific fix】 Use one extraction date per source. Recommended: "openFDA drug/event data (https://api.fda.gov/drug/event.json, extracted 16 September 2026)" and likewise for Canada Vigilance "accessed 16 September 2026"; delete "and 18 September 2026." If a confirmatory re-run on 18 September is material, state it explicitly as a re-run, not as a second access date, and make References 18–19 and the cover letter match.

---

## Problem 4 — CITATION.cff self-citation carries a divergent article title (duplicate-value trap)

【Problem】 The repository's `CITATION.cff` repeats the manuscript title in its `title:` field (correct), but its `references[0]` self-citation uses a different title: "…a head-to-head disproportionality study with a terminology caution," whereas the submitted manuscript title ends "…an observational head-to-head disproportionality analysis." Two different title strings for the same work appear in the submission package.

【Evidence】
- `CITATION.cff` (title): "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis" — matches manuscript.
- `CITATION.cff` (references[0].title): "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: a head-to-head disproportionality study with a terminology caution."
- `I_正文_IMRaD_en.md` (title, line 1) and `I_投稿信_cover_letter.md` (Re:, line 10): the "…an observational head-to-head disproportionality analysis" version.

【Why it matters】 A repository metadata file travels with the submission; a mismatched self-citation title invites confusion about which title is authoritative and can propagate into indexing. It is a small but real duplicate-value inconsistency.

【Specific fix】 Change `CITATION.cff` `references[0].title` to the exact submitted title: "Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases: an observational head-to-head disproportionality analysis" (or, if the citation is only a placeholder, mark it explicitly as "Manuscript in preparation; title TBC").

---

## Problem 5 — Title/abstract foreground the weakest claim (hyperalgesia "signal") while burying the strongest (terminology + reporting-setting)

【Problem】 The article is titled around "hyperalgesia reporting," and the abstract's headline result is the HYPERAESTHESIA finding — which the manuscript itself then debunks (clinical term is not a preferred term; the proxy "signal" is two patients, nine reports one man; not reproduced in Canada). The genuinely defensible, novel contributions — (a) the MedDRA terminology demonstration that a clinical-name zero is a dictionary artefact, and (b) that remifentanil's PAIN under-reporting reflects the perioperative *reporting setting*, not the drug — sit lower in the title and framing. For an Original Article at a clinical journal this over-sells the hyperalgesia angle and under-sells the actual message.

【Evidence】
- `I_正文_IMRaD_en.md` title (line 1) and Summary Results (line 23) lead with the hyperalgesia/HYPERAESTHESIA result.
- `I_正文_IMRaD_en.md` §3.3 and §4.1: the HYPERAESTHESIA signal "does not survive inspection… two patients… Canadian database… recorded none: the corrected picture is no estimable signal."
- `I_正文_IMRaD_en.md` §4.4 ("Term selection, not the data, decides the answer") and §4.3/§4.6: the substantive claim is the terminology caveat and the setting-driven PAIN deficit.
- `I_投稿信_cover_letter.md` (lines 16–18) explicitly frames the message as terminological — i.e. the author already knows the strongest claim, but the title does not reflect it.

【Why it matters】 Anaesthesia editors judge fit and headline contribution. A title that promises a hyperalgesia signal the paper retracts invites desk-rejection or a "what is the actual finding?" response, and buries the methodological contribution that justifies publication.

【Specific fix】 Retitle to foreground the actual contribution, e.g.: "Term selection, not the drug: how the chosen preferred term decides remifentanil's hyperalgesia signal in two pharmacovigilance databases" or "Hyperalgesia reporting for remifentanil is a terminology artefact, not a signal: a two-database disproportionality analysis." At minimum, the abstract's first Results sentence should state up front that the hyperalgesia signal is an artefact and that the durable finding is the reporting-setting effect.

---

## Problem 6 — Minor: READUS-PV item 5a "type/number of drugs in the database" is left effectively unaddressed

【Problem】 Item 5a asks to specify the type/number of drugs included in the database. The checklist answers only that both databases are open to all marketed products and therefore "cannot be quantified," and points to the four substance definitions instead. This is an acceptable "not applicable" stance, but the literal "number of drugs" part of the item is never addressed, which a strict READUS-PV auditor could flag.

【Evidence】 `I_TableS2_READUS-PV_checklist.md` (item 5a, Notes on items that could not be addressed #3): "FAERS and Canada Vigilance are national spontaneous reporting systems open to all marketed medicinal products; neither is restricted to a fixed drug list, so the 'type/number of drugs included' cannot be quantified."

【Why it matters】 Low severity; the response is reasonable, but the item is marked as addressed in the body table while the "number of drugs" element is explicitly declined. Consistency between the Part A table and the Notes should be airtight.

【Specific fix】 In the item 5a row, add one clause: "The number of distinct active substances in each corpus is not stated because neither database restricts the drug list; this is noted in the 'items that could not be addressed' section." (Already implied; make the cross-reference explicit so the two parts of the checklist agree.)

---

## § Stands up

1. **Word count is exactly as declared and within policy.** Re-derived directly from the manuscript text (Introduction→Conclusion for the main body; Summary for the structured abstract), the count is 3 994 main-text words and 299 Summary words — matching the declarations on the title page and in the cover letter, and within *Anaesthesia*'s 3 000–4 000 / 250–300 limits. The policy (Summary counts; references, tables and figure legends do not) is followed, since the count excludes the declarations block, references, tables and figure legends.

2. **AI disclosure is correctly placed and complete.** The disclosure sits under *Acknowledgements* (so it does not count toward the word count) and restates, with the cover letter, every required element of the Wiles et al. 2023 position statement (10.1111/anae.16071): LLM assistance used for scripting, plotting code, language editing and reference checking; no data/result/figure created or altered by AI; AI not the primary source; no AI listed as author; tools used 15–18 September 2026; no patient-identifiable data entered. The declared reference count "all 35 cited references verified by identifier" is internally consistent (manuscript, cover letter, and an actual count of 35 numbered references).

3. **Figure format meets the journal's hard rules.** The two figures are supplied as *separate* files in .tif and .pdf (not embedded in the manuscript), the .tif files report 600 ppi in their metadata (line-art resolution), and the figures contain no internal legend box, title, frame or gridline — symbol and error-bar meanings are carried entirely by the Figure legends placed in the manuscript text (Figure legends section). Axis labels inside the figures are standard and do not breach the "no in-figure legend/title/frame/gridline" rule. The legend text correctly explains the markers (filled circles = vs fentanyl, open squares = vs morphine, open triangles = vs sufentanil) and the reference line at ratio 1.

4. **Version string is consistent everywhere.** "v1.6.0" appears identically in the cover letter, the manuscript Data availability statement, `CITATION.cff`, and the git tag — no second/divergent version string was found.

---

## § Questions for the authors

1. Was the openFDA data actually pulled on a second date (18 September 2026), or is "accessed 16 and 18 September 2026" a slip for the analytical-plan Amendment 2 date? Please state one extraction date per database and make References 18–19 and the cover letter agree.
2. Table S9 demonstrates that you accessed case-level report fields (identifiers, products, demographics) via openFDA. Why, then, does the READUS-PV checklist say case-level files were "not accessible"? Should the checklist instead say a formal case-by-case *causality* review was not performed because openFDA lacks a patient identifier and source de-duplication?
3. The HYPERAESTHESIA "signal" is the headline Results item but is then retracted as two patients. Do you agree the title should foreground the terminology/reporting-setting conclusion rather than "hyperalgesia reporting"? If not, how would you defend the current title to a clinical readership?
4. Is the `CITATION.cff` self-citation title ("…a head-to-head disproportionality study with a terminology caution") intentional, or should it match the submitted manuscript title exactly?

---

## § What I actually checked

- **READUS-PV checklist (Table S2)** read in full against the manuscript: every Part A (items 1a–14d) and Part B (items 1a–4c) location claim cross-checked to the cited section/table; found the phantom "§3.9" citation (item 9) and the inaccurate "case-level files not accessible" justification (items 7d/10), plus the minor item 5a wording gap.
- **AI disclosure**: confirmed placement under Acknowledgements (excluded from word count), completeness against the Wiles et al. 2023 position statement, and consistency of the "35 references verified" claim between manuscript, cover letter and an actual reference count (35).
- **Figure format**: confirmed separate .tif/.pdf files exist, verified 600 ppi in the .tif metadata, confirmed figure legends live in the manuscript text and that the figures carry no internal legend box/title/frame/gridline; noted superseded .png renderings remain in the bundle and should be excluded from the figure submission.
- **Word count**: re-derived from the manuscript text — 3 994 main / 299 Summary — matching declarations and within limits; confirmed the exclusion policy (Summary counted; references/tables/figure legends not).
- **Article type / framing**: assessed Original Article suitability and whether the headline claim (per-drug hyperalgesia signal) is the weakest while the strongest (terminology + reporting-setting) is buried.
- **Cover letter vs manuscript**: checked journal name, title, author/affiliation/ORCID, reference count (35), and study description — all consistent; identified the `CITATION.cff` title divergence and the access-date inconsistency as the only mismatches.
- **Duplicate-value trap**: grepped the title, access date and version string across cover letter, title page, `CITATION.cff` and checklist; version is uniform, but the access date appears as both "16 September 2026" (single) and "16 and 18 September 2026," and the title appears in two forms in `CITATION.cff`.

*No checks were aborted; all seven focus areas were completed. The two figure .png files present in the directory are superseded by the .tif/.pdf set and are a housekeeping note, not a format hard-fail.*
