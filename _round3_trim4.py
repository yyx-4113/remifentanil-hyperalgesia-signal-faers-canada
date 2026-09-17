# -*- coding: utf-8 -*-
p = 'I_正文_IMRaD_en.md'
s = open(p, encoding='utf-8').read()
old = "HYPERAESTHESIA, the preferred term carrying the concept, meets the signal criterion for all four opioids, remifentanil included (4.73, 2.54\u20138.80); eight of the nine dated remifentanil reports fall in 2024 (\u00a73.8)."
new = "HYPERAESTHESIA, the preferred term carrying the concept, meets the signal criterion for all four opioids (4.73, 2.54\u20138.80); eight of the ten reports fall in 2024 (\u00a73.8)."
c = s.count(old)
assert c == 1, "got %d" % c
s = s.replace(old, new)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("trim4 applied")
