#!/usr/bin/env python3
"""experiment-gem-extraction.py — agentic enquiry → unseen-gem extraction from text.

Prima materia: the pushing-tantraloka session (Q1-reflexivity). The enquiry AGENTICALLY extracts
"gems" — insights the text itself does NOT explicitly close. E.g. PENETRATION 1: "manifest to me" and
"the Light is the perceiver" are two claims; the text asserts their collapse but doesn't prove it.

The mechanism: an agent pushes a text round-by-round (question → text's answer → deeper question),
and at each round it can extract a GEM = an insight + the exact spot where the text has an unclosed
gap. These gems are the unseen insights, and they become:
  - research targets (boundary/frontier)
  - essay/education content (the reconstructed argument)
  - cross-tradition claim units (standardisable)
"""
import json, hashlib

def Gem(gid, text, insight, gap_spot, force, type):
    return {"id": gid, "text": text, "insight": insight, "gap_spot": gap_spot,
            "force": force, "type": type,
            "hash": hashlib.sha256((text+insight).encode()).hexdigest()[:10]}

print("=== AGENTIC GEM-EXTRACTION (enquiry → unseen gems) ===\n")

# gems extracted from the Q1-reflexivity pushing session (real prima materia)
gems = [
    Gem("G1", "Existence = manifestation (TĀ 1/52)",
        "that which is not Light can neither be illumined nor even have existence",
        "the being of blue is the Light, and the Light is the perceiver",
        "ROUND1", "theorem"),
    Gem("G2", "Manifestation is indexed to a perceiver",
        "blue is 'manifest to me' — but the perceiver is said to be Śiva-universal",
        "PENETRATION 1: 'manifest to me' and 'the Light is the perceiver' are two claims; "
        "the text joins them by asserting the subject is a mode of the Light, but does NOT prove it",
        "ROUND1", "unclosed-gap"),
    Gem("G3", "Determination IS vimarśa (reflexive awareness)",
        "difference is not added to awareness; difference IS an act of awareness",
        "reflexivity is the condition of a determinate world — without it no 'this' vs 'that'",
        "ROUND2", "theorem"),
    Gem("G4", "Reflexivity is the condition of the world",
        "without self-apprehension, no determinate world — hence the deepest consequence",
        "the text reaches this but the empirical-subject question remains (quantifier problem)",
        "ROUND2", "frontier"),
]

print("[extracted gems] the enquiry agentically surfaced these from the text:")
for g in gems:
    print(f"  {g['id']:3s} [{g['type']:14s}] {g['text'][:40]}")
    print(f"        insight: {g['insight'][:55]}")
    if g['type'] == 'unclosed-gap':
        print(f"        GAP: {g['gap_spot'][:70]}")

# ---- the agentic mechanism: unseen gems are discoveries, not lookups ----
print("\n=== THE AGENTIC MECHANISM (enquiry → unseen gems) ===")
print("The agent doesn't retrieve known facts — it PUSHES the text:")
print("  round: question → text's answer → deeper question → (extract gem / find gap)")
unseen = [g for g in gems if g["type"] in ("unclosed-gap", "frontier")]
print(f"\n  unseen gems found (gaps + frontiers, NOT in the text's explicit claims): {len(unseen)}")
for g in unseen:
    print(f"    • {g['id']}: {g['text'][:40]} — {g['gap_spot'][:50]}")

# ---- what the gems become (the extraction base) ----
print("\n=== THE EXTRACTION BASE (gems → essay + education + research) ===")
print("Each gem is a reusable unit that serves multiple surfaces:")
for g in gems:
    uses = {
        "theorem": "essay claim + education LearningClaim + epistemic candidate",
        "unclosed-gap": "research target (What-If) + organism boundary",
        "frontier": "new question-root + cross-tradition comparison point",
    }[g["type"]]
    print(f"  {g['id']} [{g['type']}] → {uses}")

print("\n=== INSIGHT ===")
print("The agentic enquiry extracts UNSEEN gems — insights and gaps the text never states explicitly.")
print("PENETRATION 1 is a real discovery (the text asserts a collapse it doesn't prove). These gems")
print("are the gold extraction base: they become essay claims, education progressions, research")
print("targets, and cross-tradition comparison units. This is how a text yields genuinely NEW insight")
print("via agentic pushing, not just retrieval.")
