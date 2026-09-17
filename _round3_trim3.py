# -*- coding: utf-8 -*-
p = 'I_正文_IMRaD_en.md'
s = open(p, encoding='utf-8').read()
reps = [
    # L149 tighten
    ("HYPERALGESIA, the term the clinical literature uses, is not a preferred term in either dictionary, so a search on it returns nothing \u2014 a zero ordinarily read as no signal. The preferred term carrying the concept, HYPERAESTHESIA, is present in both corpora and meets the signal criterion for all four opioids including remifentanil (4.73, 2.54\u20138.80), though eight of the nine dated remifentanil reports fall in 2024 (\u00a73.8).",
     "HYPERALGESIA, the clinical term, is not a preferred term in either dictionary, so a search on it returns a zero ordinarily read as no signal. HYPERAESTHESIA, the preferred term carrying the concept, meets the signal criterion for all four opioids, remifentanil included (4.73, 2.54\u20138.80); eight of the nine dated remifentanil reports fall in 2024 (\u00a73.8)."),
    # L137 tighten
    ("remifentanil contributed no report in eight of the ten years; of the ten, eight are dated to 2024 and one has no usable receivedate (so the year table holds nine), and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06\u20135.90; 3.495, 1.52\u20138.05).",
     "remifentanil contributed no report in eight of the ten years; eight are dated to 2024 and one has no usable receivedate (so the year table holds nine), and in 2024 both ratios exceed one with intervals that exclude it (2.495, 1.06\u20135.90; 3.495, 1.52\u20138.05)."),
    # L366 tighten
    ("nine reports carry a usable receivedate in 2015\u20132024 (eight in 2024); the tenth has none and is omitted, so the table holds nine rows. In 2024 both head-to-head ratios exceed one with intervals that exclude it.",
     "nine reports carry a usable receivedate in 2015\u20132024 (eight in 2024; the tenth omitted), so the table holds nine rows. In 2024 both head-to-head ratios exceed one with intervals that exclude it."),
]
for a, b in reps:
    c = s.count(a)
    assert c == 1, "EXPECTED 1 got %d: %s" % (c, a[:60])
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("trim3 applied, %d edits" % len(reps))
