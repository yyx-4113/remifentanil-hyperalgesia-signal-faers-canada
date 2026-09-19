# -*- coding: utf-8 -*-
"""
Round-9 audit fixes (apply F1/F2/F3 + version bump to v1.9.1).

Findings from the comprehensive manuscript check:
  F1  (content error, §3.7): "rests on 532 anaphylactic-shock reports — 9.9% of the
      remifentanil cohort against 0.28% for fentanyl" is wrong. 532 is the MORPHINE
      Cardiac-disorders count (Table S1 Panel A line 397); the immune-disorders class
      cited (ROR 2.363 / RORR 1.792) is remifentanil = 9 reports (8.1%) in Canada
      Panel A, fentanyl = 229 (4.7%). Fix to the correct Panel A figures.
  F2  (version drift): manuscript Data availability (line 181) and README (line 4)
      still say release v1.8.0; the current published version is v1.9.1 (CITATION.cff).
      Bump both to v1.9.1 (self-consistent with the new release).
  F3  (typo, line 121): stray colon "p = 0.10), : the rise is real" -> remove ":".

Idempotent: each substitution only fires if the OLD string is present; if neither old
nor new is found it errors; if new is already present it is a no-op.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


def write(p, s):
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f:
        f.write(s)


DONE = []


def sub(text, old, new, label, path):
    if old in text:
        text = text.replace(old, new, 1)
        DONE.append(label)
        return text
    if new in text:
        return text  # already applied -> idempotent no-op
    raise SystemExit(f"[{label}] ERROR: neither old nor new found in {path}")


# ---- 1) manuscript ----
p = "I_正文_IMRaD_en.md"
t = read(p)

# F1: §3.7 immune-disorders sentence
t = sub(
    t,
    "rests on 532 anaphylactic-shock reports \u2014 9.9% of the remifentanil cohort against 0.28% for fentanyl",
    "rests on 9 reports (8.1% of the remifentanil cohort) against 4.7% for fentanyl",
    "F1",
    p,
)

# F2: Data availability release name + URL
t = sub(
    t,
    "release `v1.8.0` (`https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.8.0`)",
    "release `v1.9.1` (`https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.9.1`)",
    "F2-ms",
    p,
)

# F3: stray colon in §3.7 year-trend sentence
t = sub(t, "p = 0.10), : the rise is real", "p = 0.10), the rise is real", "F3", p)

write(p, t)

# ---- 2) README ----
p = "README.md"
r = read(p)
r = sub(
    r,
    "**Current release:** <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.8.0>",
    "**Current release:** <https://github.com/yyx-4113/remifentanil-hyperalgesia-signal-faers-canada/releases/tag/v1.9.1>",
    "F2-readme-link",
    p,
)
r = sub(
    r,
    "python _check_consistency.py       # must print FAIL 0 and exit 0 (618 assertions at v1.8.0)",
    "python _check_consistency.py       # must print FAIL 0 and exit 0 (619 assertions at v1.9.1)",
    "F2-readme-gate1",
    p,
)
r = sub(
    r,
    "python _verify_docx.py             # must print FAIL 0 and exit 0 (110 assertions at v1.8.0)",
    "python _verify_docx.py             # must print FAIL 0 and exit 0 (109 assertions at v1.9.1)",
    "F2-readme-gate2",
    p,
)
write(p, r)

# ---- 3) CITATION.cff ----
p = "CITATION.cff"
c = read(p)
c = sub(c, 'version: "1.9.0"', 'version: "1.9.1"', "F2-cff", p)
write(p, c)

print("Applied:", DONE if DONE else "(no-op: already applied)")
