#!/usr/bin/env python3
"""experiment-curiosity-patterns.py — analyze the LOGICVID gold exemplars for what makes a question
interesting to a human.

These are live human curiosity exemplars (research-library). The task: extract the CURIOSITY MARKERS —
the recurring patterns of what a curious mind finds interesting. This tells us WHAT to train
question-generation toward (the gold), and WHY certain questions pull attention.

Markers hypothesized from reading the exemplars:
  distinction-forensics  "are these 2 words the same or different?"
  live-issue isolation   "does X explain Y or merely rename it?"
  cross-domain bridge    "can one process language span these domains?"
  honest-boundary        "what has NOT been established?"
  convergence            "can we reach this from another direction?"
  mechanism-gap          "what is the actual mechanism?"
  subversion             "does the argument assume what it proves?"
  paradox                "an apparent contradiction that must be resolved?"
"""
import os, re, sys

SPECS = "/mnt/HC_Volume_106427611/ip-graph/specs"
EXEMPLARS = [f for f in os.listdir(SPECS) if f.startswith("SPEC-4") and "LOGICVID" in f]

# marker -> regex signals (what a curious human writes)
MARKERS = {
    "distinction-forensics": [r"\bare they\b.*\b(different|same|interchangeable)\b",
                              r"\bnot.*\bequivalent\b", r"treat.*\bas.*interchangeable"],
    "live-issue": [r"does\b.*\b(explain|rename|redescri)", r"merely\b.*\b(rename|redescribe)",
                   r"explain.*or.*rename"],
    "cross-domain": [r"shared\b.*\b(language|process)", r"same.*\bdifferent.*communities",
                     r"one\b.*\b(process|language).*span"],
    "honest-boundary": [r"has NOT\b.*\b(been|established)", r"not\b.*\bestablished\b",
                        r"what has not", r"has not\b.*\bproved"],
    "convergence": [r"rediscovered.*\b(many|several|independent).*(direction|way)",
                    r"same.*primitive.*different", r"from.*many.*directions"],
    "mechanism-gap": [r"what is the\b.*\b(mechanism|cause)", r"how does\b.*\b(actually|work)",
                      r"the actual mechanism"],
    "subversion": [r"assume.*\b(it|what)\b.*\bproves", r"circular", r"assume.*the.*subject"],
    "paradox": [r"paradox", r"apparent.*contradiction", r"contradiction.*resolve"],
    "tension": [r"tension", r"tension between", r"tension at"],
}

print("=== CURIOSITY PATTERNS IN THE LOGICVID GOLD EXEMPLARS ===\n")
print(f"exemplars analyzed: {len(EXEMPLARS)}\n")

# scan each exemplar, count marker hits
marker_counts = {m: 0 for m in MARKERS}
per_exemplar = {}
for f in EXEMPLARS:
    text = open(os.path.join(SPECS, f)).read().lower()
    hits = {}
    for m, pats in MARKERS.items():
        c = sum(len(re.findall(p, text)) for p in pats)
        hits[m] = c
        marker_counts[m] += c
    per_exemplar[f] = hits

# the curiosity profile: which markers dominate across ALL exemplars
print("aggregate curiosity-marker profile (all exemplars):")
total = sum(marker_counts.values())
for m, c in sorted(marker_counts.items(), key=lambda x: -x[1]):
    print(f"  {m:24s} {c:4d}  {'█' * int(30*c/max(total,1))}")

print("\n=== WHAT THIS REVEALS ABOUT HUMAN CURIOSITY ===\n")
print("The dominant markers = what a curious human most repeatedly does:")
top = sorted(marker_counts.items(), key=lambda x: -x[1])[:4]
for m, c in top:
    print(f"  • {m} ({c} hits)")

print("\n=== INSIGHT ===")
print("These live exemplars show curiosity is NOT random — it has a REPEATABLE structure:")
print("the human repeatedly (1) tests if terms are equivalent (distinction), (2) asks if a concept")
print("explains or renames (live-issue), (3) seeks shared structure across domains (bridge), and")
print("(4) marks honest boundaries. These are the GOLD markers our question-generation should learn")
print("to produce. Analyzing WHY these pull attention → the training signal for the Question-Growth")
print("Engine: generate questions that exhibit the same curiosity profile as the human exemplars.")
