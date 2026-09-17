# -*- coding: utf-8 -*-
p = 'I_正文_IMRaD_en.md'
s = open(p, encoding='utf-8').read()
reps = [
    # L149 tighten opener + drop trailing duplicate specificity-probe clause
    ("Three findings stand out; the first qualifies the others. ",
     "Three findings stand out, the first qualifying the others. "),
    ("; a specificity probe behaved inconsistently, arguing against a uniform global artefact.",
     "."),
    # L155 tighten
    ("The two literatures address different things. Quantitative sensory testing detects a change in pain threshold but not how often that change reaches clinical recognition and reporting [24]; reporting data show that a concept was recognised and coded, not how often it occurs. Under the correct preferred term the reporting data do contain the concept and code it disproportionately for every opioid examined; what they do not show is an excess specific to remifentanil, and the stronger database contributed no remifentanil report of it. The two sources are compatible: a real but modest phenomenon, coded rarely.",
     "Quantitative sensory testing detects a threshold change but not its clinical recognition or reporting [24]; reporting data show a concept was coded, not its incidence. Under the correct preferred term the data contain the concept and code it disproportionately for every opioid; they show no remifentanil-specific excess, and the stronger database contributed no remifentanil report. The two sources are compatible: a real but modest phenomenon, coded rarely."),
    # L131 tighten opener
    ("This comparison is exploratory: no multiplicity correction was applied, and it describes the remifentanil reporting profile rather than claiming class-specific signals.",
     "This comparison is exploratory, with no multiplicity correction, and describes the remifentanil profile rather than claiming class-specific signals."),
    # L141 tighten
    ("Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by ANAPHYLACTIC SHOCK (532 events) and ANAPHYLACTIC REACTION (367), and the same excess appeared in Canada (2.363). The pipeline therefore detects signals when present, supporting \u2014 but not proving \u2014 that its failure to detect a hyperalgesia signal reflects the data, not the method.",
     "Remifentanil showed a strong immune-class signal (10.951; 8.613 versus fentanyl), driven by anaphylactic shock (532 events) and reaction (367), and the same excess appeared in Canada (2.363). It therefore detects signals, supporting \u2014 not proving \u2014 that the absent hyperalgesia signal reflects the data, not the method."),
    # L167 tighten
    ("That zero is not a fact about remifentanil, or about reporting, or about the syndrome; it is a fact about the dictionary, because the concept is carried by a preferred term no clinician would type: HYPERAESTHESIA. A reader who stops at the first query reports a structural absence; one who checks the dictionary finds a signal, though not necessarily the one he set out to find, because",
     "That zero is not about remifentanil, reporting or the syndrome; it is about the dictionary, because the concept is carried by a preferred term no clinician would type: HYPERAESTHESIA. A reader who stops at the first query reports a structural absence; one who checks finds a signal that may not be the one intended, because"),
]
for a, b in reps:
    c = s.count(a)
    assert c == 1, "EXPECTED 1 got %d: %s" % (c, a[:60])
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("trim2 applied, %d edits" % len(reps))
