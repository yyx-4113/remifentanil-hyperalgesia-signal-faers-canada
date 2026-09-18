# Independent peer review — A1 (anaesthesiology / perioperative medicine / OIH & pain medicine)

**Manuscript:** *Remifentanil and hyperalgesia reporting in two national pharmacovigilance databases*
**Journal targeted:** *Anaesthesia* (Original Article)
**Reviewer role:** Domain expert in anaesthesiology, perioperative medicine, opioid-induced hyperalgesia and pain medicine.
**Reading basis:** `I_正文_IMRaD_en.md` read whole (Summary → Conclusion → Tables 1–S9 → Appendix S1 → figure legends) and `ANALYSIS_PLAN.md`. No prior reviews, responses, manifests, or the other three reviewers' files were opened. Treated as a first submission.

---

## Issue 1 — The "ultrashort half-life makes true tolerance and withdrawal uncommon" claim is pharmacologically inverted and contradicts the paper's own citation

【Problem】 The statement that remifentanil's "ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal uncommon" misrepresents the pharmacology of remifentanil and directly contradicts reference 5, which the manuscript itself cites for the opposite phenomenon.

【Evidence】 `I_正文_IMRaD_en.md:139` ("For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME part of the deficit is probably physiological: remifentanil's ultrashort half-life and lack of oral or transdermal formulation make true tolerance and withdrawal uncommon"). Reference 5 (Guignard et al., *Anesthesiology* 2000, line 33/194) is cited in the Introduction as the very paper that demonstrated **acute intra-operative opioid tolerance**: "intraoperative remifentanil increases postoperative pain and morphine requirement." The OIH literature implicates the *rapid offset* of remifentanil (context-insensitive half-time 3–4 min, line 31) as the trigger that unmasks the sensitised state, not as a protective feature.

【Why it matters】 This sentence is the one place the manuscript draws a mechanistic, drug-level conclusion about tolerance/withdrawal, and it is backwards. A *Anaesthesia* clinician-reviewer will read it as exonerating remifentanil on tolerance, when the canonical teaching (and the manuscript's own ref 5, plus refs 6, 14) is that remifentanil is the *prototypical* acute-tolerance/OIH opioid precisely because of its pharmacokinetics. It also creates an internal inconsistency: the same drug is said elsewhere to cause hyperalgesia (line 31) yet here to seldom show tolerance. This undermines the credibility of the "setting, not drug" interpretation in §4.3.

【Specific fix】 Replace with a version that separates acute from chronic:
> "For DRUG TOLERANCE and DRUG WITHDRAWAL SYNDROME the deficit may in part reflect pharmacology: remifentanil is given intravenously for short, supervised perioperative intervals and has no outpatient oral or transdermal formulation, so the *chronic* physical dependence and withdrawal captured in the fentanyl/morphine chronic-pain cohorts are uncommon for it. This does not speak to *acute* intra-operative tolerance, which is well documented with remifentanil (Guignard et al., 2000; Joly et al., 2005) and is mechanistically linked to its rapid offset."

---

## Issue 2 — The DRUG INEFFECTIVE specificity-probe "reversal" does not argue against a uniform artefact; the simpler explanation is the same indication/setting confounding

【Problem】 The manuscript uses the DRUG INEFFECTIVE direction reversal between databases as evidence "against a uniform global reporting artefact," but the reversal is fully explained by the very indication/setting difference the manuscript invokes to explain PAIN, so the probe is logically circular and does not do the work claimed.

【Evidence】 `I_正文_IMRaD_en.md:105` ("A global artefact would have pushed this term in the same direction; it did not") and `:281` ("The reversal for DRUG INEFFECTIVE … argues against a uniform global reporting artefact"). In FAERS remifentanil under-reports DRUG INEFFECTIVE (RORR 0.568 vs fentanyl, 0.470 vs morphine; Table 2), but in Canada it over-reports (1.277 vs fentanyl, 1.703 vs morphine; Table 3). The manuscript itself notes the term is ~3× commoner in the Canadian corpus (208 365 counts / 1 154 017 reports vs 1 299 278 / 20 692 687, line 105) and that the Canadian fentanyl/morphine cohorts are dominated by chronic-pain/transdermal/outpatient use (§3.6, Table S3: 23.6% consumer reports for morphine vs 5.4% for remifentanil). "DRUG INEFFECTIVE" (treatment failure) is a natural report in a chronic-pain cohort and an unnatural one for a short perioperative infusion — the same setting axis that explains PAIN.

【Why it matters】 The probe is presented as the concrete proof that the under-reporting pattern is *not* a database-invariant instrument artefact (line 139, "The specificity probe makes the argument concrete … but narrows rather than settles it"). But because the comparator cohorts differ in indication between the two databases, the reversal is exactly what the setting hypothesis predicts; it simultaneously "argues against" and is "explained by" the same confounder. A reviewer will see the contradiction. The probe cannot distinguish "uniform artefact absent" from "cohorts differ in indication," which is the more parsimonious reading.

【Specific fix】 Either drop the causal claim or restate it honestly:
> "The DRUG INEFFECTIVE direction reversed between databases (under-reported in FAERS, over-reported in Canada). This is most parsimoniously explained by the same indication difference that drives PAIN: in Canada the fentanyl and morphine cohorts are dominated by chronic-pain treatment where 'drug ineffective' is a meaningful report, whereas remifentanil is a short perioperative infusion for which treatment failure is not a natural concept. The reversal therefore shows the under-reporting pattern is not invariant across databases, but it cannot be used as evidence against a reporting artefact, because the comparator cohorts are not indication-matched between the two corpora."

---

## Issue 3 — "Under-reporting reflects the perioperative setting, not the drug" is over-stated; the matched-setting stratum still points below 1 and the unity claim rides on a 4-report stratum

【Problem】 The conclusion that holding indication and reporting depth constant removes the PAIN deficit is stronger than the data support; in the only adequately populated matched stratum the point estimate is still below 1, and the apparent "reversal to unity" comes from a stratum with only four remifentanil reports.

【Evidence】 `I_正文_IMRaD_en.md:113` and `:137` and §4.3. Table 5: in the **perioperative anaesthesia** stratum (remifentanil n = 84, the only well-populated matched stratum) PAIN RORR vs fentanyl is **0.399** (0.048–3.295) — below 1, the wide interval merely reflecting small numbers. The claim that "once both cohorts are drawn from the same setting the deficit is no longer distinguishable from unity" rests on the **pain-indication** stratum where remifentanil n = 4 (a = 1), giving 1.791 (0.184–17.397). Table 6 Mantel–Haenszel: PAIN vs morphine adjusted 0.978 but with CI **0.042–22.751** — a near-vacuous interval that "includes 1" only because of negligible precision. The depth-adjusted point estimates move toward 1 but the manuscript's own wording ("the movement of the point estimate, not the interval, is what the table is for," Table 6 note) concedes the intervals are uninformative.

【Why it matters】 This is the manuscript's central interpretation (headline finding #2). Stating it as "setting, not drug" invites a clinician to conclude remifentanil bears no analgesic-liability signal, when the matched-setting evidence is at best "attenuated and statistically unresolved." The discrepancy between the strong narrative and the thin (n = 4; CI 0.04–22.8)支撑 data is exactly what a methods-minded *Anaesthesia* reviewer will press.

【Specific fix】 Soften to "attenuated, not eliminated":
> "Holding indication and reporting depth constant attenuates but does not abolish the deficit. In the perioperative-anaesthesia stratum (remifentanil n = 84) the PAIN ratio against fentanyl was 0.399 (0.05–3.30), still below 1; the point estimate reaches unity only in the pain-indication stratum, which contained four remifentanil reports, and in the depth-adjusted analysis the confidence intervals are too wide to distinguish the ratio from 1 or from a substantial deficit. The pattern is therefore consistent with a setting effect, but the data cannot establish that the drug contributes nothing."

---

## Issue 4 — The MedDRA premise (HYPERALGESIA is not a PT and HYPERAESTHESIA is "the only term that carries the concept") must be demonstrated from the licensed v27.1 browser, and must rule out a distinct "Hyperalgesia" PT

【Problem】 The headline finding #1 rests on HYPERALGESIA being a lowest-level term with no preferred-term status, mapping to HYPERAESTHESIA (10020568); the manuscript further calls HYPERAESTHESIA "the only term in the dictionary that carries the concept." Standard pharmacovigilance references routinely list "Hyperalgesia" as its own preferred term, so this premise must be shown explicitly, not asserted, and the possibility of a second PT must be excluded.

【Evidence】 `I_正文_IMRaD_en.md:63` ("HYPERALGESIA, a lowest level term mapping to the preferred term HYPERAESTHESIA"), `:93` (zero by construction), Table S6 ("the only term in the dictionary that carries the concept"), ref 22 (MedDRA v27.1). The empirical zero is strong and internally consistent (0 reports in 20 692 687 FAERS and 1 154 017 Canadian; adjacent-token search also 0; Table S4). A public MedDRA-linked source (bio-add ADR Ontology) defines **HYPERAESTHESIA (10020568)** with the hyperalgesia definition ("increased sensation of pain … due to damage to soft tissue containing nociceptors"), which lends plausibility to the manuscript's mapping. However, many coding references present "Hyperalgesia" as a standalone PT distinct from HYPERAESTHESIA, and I could not confirm from public sources whether PT "Hyperalgesia" (commonly 10020566) exists in v27.1. If it does, the concept is carried by two PTs, the "only term" claim is false, and the primary analysis should have queried PT "Hyperalgesia" as the natural term.

【Why it matters】 This is the load-bearing fact for the entire "artefact, not safety" conclusion. If a distinct "Hyperalgesia" PT exists in v27.1 and the authors simply failed to query it (because they assumed the clinical word is not a PT), the premise — and the contrast with the HYPERAESTHESIA proxy — is incomplete rather than demonstrative. A reviewer will check this against the MedDRA browser; the manuscript must pre-empt that check.

【Specific fix】 Add to the supplement (Table S4/S6 or a new panel) the verbatim MedDRA v27.1 browser output showing, for the string "Hyperalgesia": (i) whether a PT "Hyperalgesia" exists and its code; (ii) the LLT→PT mapping. Then state explicitly: "We confirmed in MedDRA v27.1 that 'HYPERALGESIA' is not a current PT and that the LLT maps to PT HYPERAESTHESIA (10020568); no separate 'Hyperalgesia' PT exists in this release, so HYPERAESTHESIA is the correct primary term." If a separate PT is found, add it to the 18-term set and report it on the same footing as HYPERAESTHESIA.

---

## Issue 5 — The dynorphin / descending-facilitation mechanism is asserted from two reviews; a primary mechanistic citation is missing and expected by an *Anaesthesia* reviewer

【Problem】 The OIH mechanism sentence ("N-methyl-D-aspartate receptor hyperactivation, descending facilitation and increased dynorphin release," line 31) is cited only to a 2024 current-state review (ref 1) and a 2006 qualitative review (ref 2); the foundational preclinical demonstrations of spinal dynorphin and RVM descending facilitation are absent.

【Evidence】 `I_正文_IMRaD_en.md:31` cites [1,2] only. The mechanism is established by the Porreca/Vanderah/Ossipov group: Vanderah et al., *J Neurosci* 2001, "Tonic descending facilitation from the rostral ventromedial medulla mediates opioid-induced abnormal pain and antinociceptive tolerance"; Gardell et al., *J Neurosci* 2001, "Sustained morphine exposure induces a spinal dynorphin-dependent enhancement of excitatory transmitter release"; Vanderah et al., *J Neurosci* 2000, "Dynorphin promotes abnormal pain and spinal opioid antinociceptive tolerance." These are the primary sources for the descending-facilitation / dynorphin limb the manuscript names.

【Why it matters】 For an Original Article in *Anaesthesia* on OIH, the mechanism paragraph should cite the primary mechanistic literature, not only narrative reviews. It signals the author is fluent in the OIH field and prevents the mechanism claim from looking second-hand. Low effort, high credibility payoff.

【Specific fix】 Add after [2] in line 31, e.g.: "… increased dynorphin release [1, 2], the latter demonstrated preclinically as spinal dynorphin-dependent descending facilitation from the rostral ventromedial medulla [Vanderah et al., *J Neurosci* 2001; Gardell et al., *J Neurosci* 2001]." (Full entries to be added to References.)

---

## Issue 6 — The comparator-term under-reporting is attributed wholly to "setting"; the pharmacological exposure difference (short intra-operative use vs chronic use) is a plausible contributor the manuscript does not acknowledge

【Problem】 The manuscript reads remifentanil's under-reporting of nausea, vomiting, pruritus and constipation as purely a reporting-setting effect, but these are dose- and exposure-dependent adverse effects for which remifentanil's brief intra-operative exposure genuinely yields fewer events than chronic morphine/fentanyl use.

【Evidence】 `I_正文_IMRaD_en.md:103` (11/12 comparator-term ratios < 1) and §4.3 ("the comparators' PAIN proportions rise for setting, not pharmacology"). Nausea/vomiting/pruritus/constipation are classic opioid adverse effects whose incidence scales with cumulative exposure and outpatient/chronic use. Remifentanil is used intravenously for hours; morphine/fentanyl cohorts include long-term outpatient and transdermal use (Table S3, line 113). The manuscript is correct that "analgesic superiority cannot be inferred" (line 137), but it over-reaches in attributing the comparator-term deficit *entirely* to setting.

【Why it matters】 Conflating "reporting setting" with "shorter drug exposure" weakens the otherwise careful interpretation. A reviewer may read the all-encompassing "setting, not drug" as special pleading, since part of the lower AE frequency is a real pharmacological/concentration-time consequence of how remifentanil is used.

【Specific fix】 In §4.3, after "not pharmacology," add a qualifying sentence:
> "We attribute the comparator-term deficit chiefly to the perioperative reporting setting, but acknowledge that remifentanil's brief intra-operative exposure also yields genuinely fewer nausea, vomiting, pruritus and constipation events than the chronic morphine and transdermal fentanyl use that dominate the comparator cohorts; the two are not fully separable here."

---

## Issue 7 — "A zero from the clinical name alone is an artefact of terminology, not evidence of safety" is clinically responsible, but its incidence caveat must stay visible in the Abstract/Conclusion

【Problem】 The conclusion is sound and responsibly hedged in the Limitations, but the Abstract/Conclusion phrasing could be read by a clinician as "remifentanil OIH is not a concern," which the manuscript does not intend.

【Evidence】 `I_正文_IMRaD_en.md:163` (Conclusion: "a zero obtained from the clinical name alone is an artefact of terminology, not evidence of safety"); correctly paired with §4.5 ("Disproportionality cannot quantify a pharmacological effect," line 147) and §4.2 ("spontaneous reports show a concept was coded, not its incidence," line 133). The incidence caveat is present but sits in §4.5, not in the Abstract or Conclusion.

【Why it matters】 The single most mis-quotable sentence in the paper is the Conclusion line. Because the study is hypothesis-generating and makes no clinical safety claim (line 37), the incidence caveat should travel with the conclusion so the take-home is not "terminology artefact ⇒ no safety issue."

【Specific fix】 Append to the Conclusion sentence:
> "… not evidence of safety, and equally not evidence of harm: spontaneous reporting cannot address OIH incidence in either direction, which remains a question for prospective quantitative sensory testing."

---

## Issue 8 — The "all four opioids meet the signal criterion" headline is itself contaminated by the same duplicated case series and should be framed accordingly up front

【Problem】 The Summary and §4.1 lead with "HYPERAESTHESIA meets the signal criterion for all four opioids (including remifentanil)," with the one-patient contamination revealed afterwards; the same patient also inflates the fentanyl and sufentanil 2024 signals, so "all four" is partly the same artefact.

【Evidence】 `I_正文_IMRaD_en.md:97, 129` and `:121`. The manuscript states (§3.3) that "all seven of the 2024 sufentanil HYPERAESTHESIA reports and five of the 17 2024 fentanyl reports come from" the same 76-year-old man (Table S9), and §3.7 repeats this. So the apparent signal in three of four cohorts is driven by one duplicated reporter.

【Why it matters】 A reader stopping at the Abstract/§4.1 takeaway ("signal for all four opioids") is misled; the manuscript's own later text shows the signal is not drug-specific but reporter-specific. The ordering (headline first, caveat second) undercuts the honest "no estimable signal" message.

【Specific fix】 In the Summary and §4.1, subordinate the "all four" statement:
> "HYPERAESTHESIA meets the signal criterion for all four opioids in the uncorrected counts, but the 2024 elevation in three of the four cohorts is supplied by a single duplicated reporter (§3.3, §3.7); once identified, no drug-specific signal remains."

---

## Issue 9 — PAIN as a "pragmatic proxy" for hyperalgesia is clinically weak (it usually records the treated indication, not OIH); the manuscript acknowledges this but the framing in the Introduction under-states it

【Problem】 PAIN is used both as a pragmatic proxy for the hyperalgesia concept (§2.3) and as the instrument probe; clinically, a spontaneous "PAIN" report almost always denotes the treated condition or an unrelated event, not opioid-induced sensitisation, so its value as any OIH proxy is limited.

【Evidence】 `I_正文_IMRaD_en.md:61` ("PAIN therefore carries no information about hyperalgesia … the syndrome's defining measurement has no preferred term in either dictionary") — the manuscript does say this. But §2.3 still lists PAIN "as a pragmatic proxy [20]" before qualifying it, and the Abstract (line 23) foregrounds "Remifentanil reported pain least" as a finding without the caveat that "PAIN" is not OIH.

【Why it matters】 Minor, because the manuscript is internally consistent and the INADEQUATE ANALGESIA sensitivity (Table S5 note, line 143/527) correctly shows the answer flips with term choice. But the Abstract reader should not infer a pain/OIH signal from PAIN. The distinction between analgesia (pain relief) and hyperalgesia (paradoxical sensitisation) is otherwise handled well (line 143).

【Specific fix】 In the Abstract (line 23) and §2.3, label PAIN explicitly as "a general reporting-burden probe, not an OIH proxy," so the two roles are not conflated.

---

## Issue 10 — Minor: the Fletcher & Martinez magnitude is numerically correct but the scale wording should match the source

【Problem】 The 9.4 mm figure is accurate in magnitude but the manuscript writes "9.4 mm on a 100 mm scale" whereas Fletcher & Martinez report "9.4 cm on a 100 cm visual analogue scale"; the proportion is identical but the units should be stated consistently.

【Evidence】 `I_正文_IMRaD_en.md:33` ("9.4 mm on a 100 mm scale at 1 h"); Fletcher & Martinez *Br J Anaesth* 2014 (ref 7, verified): "MD: 9.4 cm; 95% CI: 4.4, 14.5 at 1 h … on a 100 cm visual analogue scale." 9.4 cm / 100 cm = 9.4 mm / 100 mm, so the value is correct; only the unit label differs from the source.

【Why it matters】 Trivial, but an *Anaesthesia* copy editor will flag the mismatch with the cited source; stating "9.4 mm on a 100 mm VAS (reported as 9.4 cm on a 100 cm VAS by Fletcher & Martinez)" removes any ambiguity.

【Specific fix】 Reword line 33 to: "attributed to remifentanil a rise in postoperative pain of 9.4 mm (on a 100 mm VAS; 9.4 cm on the 100 cm scale reported) at 1 h, 7.1 mm at 4 h and 3.0 mm at 24 h …"

---

## § Stands up — things I suspected were wrong but found correct

1. **The Fletcher & Martinez 2014 meta-analytic figures are exactly as cited.** I expected the "9.4 mm at 1 h" to be rounded or mis-attributed; verification against the source (27 RCTs, 1 494 patients; MD 9.4 cm at 1 h, 7.1 at 4 h, 3.0 at 24 h; SMD 0.70 for 24-h morphine) confirms the manuscript's numbers and the "mainly remifentanil" attribution (lines 33, 195). No discrepancy.
2. **The Rivosecchi 2014 "16 supporting / 6 refuting" count is accurate.** I suspected the categories might be mutually exclusive and not sum to 35; they overlap (22 were prevention-focused, 16+6 = 22 of 35, the remainder neutral/mixed), and the manuscript's "16 supporting and 6 refuting … real but too small to warrant prevention" matches the source's expert opinion (lines 33, 196; PubMed PMID 24669819).
3. **Kim 2015 and Huang 2024 are correctly represented.** Kim (ref 9) indeed concluded "no sufficient evidence to support or refute OIH in humans" (lines 33, 197; Am J Ther 2015;22:e62–74) — the manuscript's "evidence insufficient" is fair. Huang 2024 (ref 10) is a 31-study meta-analysis (2 019 patients) reporting a dose–pain correlation (P = 0.03) — the manuscript's "meta-analysis of 31 trials … dose–response relation" is accurate (lines 33, 198; BMC Anesthesiol 2024;24:25).
4. **HYPERAESTHESIA (10020568) does carry the hyperalgesia concept, supporting the proxy choice.** The public MedDRA-linked ontology defines HYPERAESTHESIA (10020568) with the hyperalgesia definition, and the empirical zero for the string HYPERALGESIA across 20 692 687 + 1 154 017 reports is internally consistent (Tables S4, §3.2). The proxy strategy is defensible; my initial suspicion that the zero was a query error is not supported by the data as presented.
5. **The one-patient / ten-report disclosure is handled with commendable honesty.** §3.3, §3.7, Table S9 and the covariance/leave-2024-out corrections (Appendix S1 A1.5, A1.8) show the authors did not hide the duplicated case series; the "no estimable remifentanil signal" conclusion is the correct reading.

---

## § Questions for the authors — what I need to know (not guessing)

1. In MedDRA **v27.1** (the exact release of the Canadian extract, ref 22), does a preferred term **"Hyperalgesia"** (distinct from HYPERAESTHESIA, 10020568) exist, and if so what is its PT code? Please show the browser LLT→PT mapping for the string "Hyperalgesia." This determines whether the primary analysis should have included a second PT.
2. For the **pain-indication stratum** in Table 5 (remifentanil n = 4, a = 1, PAIN RORR 1.791), what are the actual indication free-text strings that qualified those four reports, and were they truly "pain" as an analgesic indication rather than, e.g., "pain anaesthesia" or post-operative pain? The entire "reversal to unity" rests on these four.
3. The DRUG INEFFECTIVE Canadian over-reporting (1.703 vs morphine) — is this driven by the chronic-pain indication stratum specifically? A stratified breakdown (as in Table 5) for DRUG INEFFECTIVE by indication would show whether the reversal is the setting effect I hypothesise (Issue 2).
4. Reference 5 (Guignard 2000) is cited for acute tolerance/hyperalgesia in the Introduction but the Discussion (line 139) implies tolerance is "uncommon" for remifentanil. Do the authors intend "acute intra-operative tolerance" (common) or "chronic physical dependence" (uncommon)? The revision in Issue 1 needs this clarified.
5. Were the 33 references all resolved by identifier as stated (line 181)? I spot-checked refs 1, 2, 5, 6, 7, 8, 9, 10, 14 and they are accurate; I did not re-verify 11–13, 15–33, so confirmation that each DOI resolves is requested.

---

## § What I actually checked

**Files read (whole):**
- `D:\2026.9\极速交付9月会员日优惠套路\06_FAERS单药物SOC分类安全性评估\瑞芬太尼\I_正文_IMRaD_en.md` — Summary, Introduction, Methods (§2.1–2.6), Results (§3.1–3.7), Discussion (§4.1–4.6), Conclusion, Acknowledgements, all 33 References, Tables 1–S9, Appendix S1 (A1.1–A1.9), both figure legends.
- `D:\2026.9\极速交付9月会员日优惠套路\06_FAERS单药物SOC分类安全性评估\瑞芬太尼\ANALYSIS_PLAN.md` — read as the methods plan (Amendments 1–2).

**Not opened (per independence instruction):** REVIEW_*.md, RESPONSE_*.md, REVISION_*.md, SUBMISSION_MANIFEST.md, GITHUB_DEPOSIT_SOP.md, author_verification_statement.md, and `review_round6/` files other than this one.

**External verification (web searches, this session):**
- Fletcher & Martinez 2014 (*Br J Anaesth* 112:991–1004): confirmed 27 RCTs / 1 494 patients; MD 9.4 cm (4.4–14.5) at 1 h, 7.1 at 4 h, 3.0 at 24 h on 100 cm VAS; SMD 0.70 for 24-h morphine; "mainly associated with remifentanil." → manuscript numbers correct.
- Rivosecchi 2014 (*Expert Opin Drug Saf* 13:587–603, PMID 24669819): confirmed 35 articles, 16 support, 6 refute, 22 prevention; expert opinion "real but does not reach clinical significance requiring prevention." → manuscript correct.
- Kim 2015 (*Am J Ther* 22:e62–74, PMID 25830866): confirmed conclusion "no sufficient evidence to support or refute OIH in humans." → manuscript correct.
- Huang 2024 (*BMC Anesthesiol* 24:25, PMID 38218762): confirmed 31 studies / 2 019 patients; dose–pain correlation P = 0.03. → manuscript correct.
- MedDRA: HYPERAESTHESIA = PT 10020568, defined (bio-add ADR Ontology) with the hyperalgesia meaning; supports the proxy. Could **not** confirm from public sources whether a separate "Hyperalgesia" PT exists in v27.1 — flagged as author verification (Issue 4 / Q1).
- Dynorphin/descending-facilitation mechanism: confirmed primary sources Vanderah et al. *J Neurosci* 2001 (RVM descending facilitation), Gardell et al. *J Neurosci* 2001 (spinal dynorphin), Vanderah et al. *J Neurosci* 2000 (dynorphin promotes abnormal pain/tolerance) — absent from the manuscript's citations; recommended as must-cite (Issue 5).

**Values recomputed / cross-checked against the manuscript (no discrepancy found unless stated):**
- PAIN RORR vs fentanyl 0.066 and vs morphine 0.046 (Table 2) = Abstract line 23 and Table 3 Canada 0.235/0.146 — consistent.
- HYPERAESTHESIA rate "1 in 538 remifentanil, 1 in 216 morphine" (Abstract line 23) = 5 375/10 ≈ 538 and 56 501/262 ≈ 216 (Table 2 note) — consistent.
- DRUG INEFFECTIVE Canadian prevalence "3× commoner": 208 365 / 1 154 017 = 18.1% vs 1 299 278 / 20 692 687 = 6.3%; ratio 2.87 ≈ 3 — consistent with line 105.
- DRUG INEFFECTIVE FAERS RORR 0.568/0.470 (Table 2) vs Canada 1.277/1.703 (Table 3) — consistent with the reversal described in lines 105/281.
- Table 5 perioperative stratum PAIN vs fentanyl 0.399 (n = 84) and pain stratum 1.791 (n = 4) — consistent with the over-statement flagged in Issue 3.
- Table 6 MH-adjusted PAIN vs morphine 0.978 (0.042–22.751) — consistent; flagged as near-vacuous in Issue 3.

**Discrepancy stated:** None in the recomputed numbers. The only substantive uncertainties are (a) the MedDRA "Hyperalgesia" PT existence in v27.1 (Issue 4, requires author verification) and (b) the pharmacological-vs-setting contribution to comparator-term under-reporting (Issue 6, interpretive). Both are flagged above with specific fixes.
