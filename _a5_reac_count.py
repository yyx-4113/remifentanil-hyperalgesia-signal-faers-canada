import csv, os
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cv", "cvponline_extract_20241130")
n = blank = 0
vers = {}
with open(os.path.join(DATA, "reactions.txt"), encoding="utf-8", errors="replace", newline="") as fh:
    for row in csv.reader(fh, delimiter="$", quotechar='"'):
        n += 1
        if len(row) >= 10:
            v = row[9].strip()
            if not v: blank += 1
            else: vers[v] = vers.get(v, 0) + 1
print("reaction rows:", n, "blank version:", blank, "versions:", vers)
