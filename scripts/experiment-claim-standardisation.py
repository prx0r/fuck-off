#!/usr/bin/env python3
"""experiment-claim-standardisation.py — standardising tough claims ACROSS traditions.

From SPEC-35 (comparative pushing) + the enquiry gems: ask every tradition the same question-shapes,
then standardise the claims so they're COMPARABLE. The standardised form separates WHAT IS CLAIMED from
the tradition-specific vocabulary, so "vimarśa" and "self-reflexivity" and "reflective awareness" can be
compared as the same structural claim — without collapsing their differences.

The standardisation unit: a ClaimUnit = {question_shape, structural_claim, tradition, evidence, strength}.
This is how a gem (e.g. G3: determination is reflexive awareness) becomes comparable across traditions.
"""
import json, hashlib

def ClaimUnit(shape, structural_claim, tradition, vocab, evidence, strength, boundary):
    return {"question_shape": shape, "structural_claim": structural_claim, "tradition": tradition,
            "tradition_vocab": vocab, "evidence": evidence, "strength": strength, "boundary": boundary}

print("=== CROSS-TRADITION CLAIM STANDARDISATION ===\n")

# the same structural question asked across traditions → standardisable claims
# question_shape: "does determination require self-reference?"  (from the vimarśa enquiry)
claims = [
    ClaimUnit("REFLEXIVITY", "determination/difference requires self-reference",
        "Trika/Śaiva", {"vimarśa", "tādātmya"}, "TĀ 1/52-55", "WELL_SUPPORTED",
        "empirical-subject collapse unproved"),
    ClaimUnit("REFLEXIVITY", "determination/difference requires self-reference",
        "Buddhist epistemology", {"svasaṃvedana", "reflexive awareness"}, "Dignāga/Dharmakīrti",
        "PROVED", "scope: awareness, not a subject"),
    ClaimUnit("REFLEXIVITY", "determination/difference requires self-reference",
        "Phenomenology", {"self-presence", "intentionality"}, "Husserl",
        "PLAUSIBLE", "no regress; presence-of"),
    ClaimUnit("REFLEXIVITY", "determination/difference requires self-reference",
        "Cognitive science", {"self-model", "metacognition"}, "Solms/Levin",
        "WELL_SUPPORTED", "top-down control"),
]

print("[standardised] the same structural claim, 4 traditions, different vocabulary:")
print(f"{'tradition':18s} {'structural claim':38s} {'strength':14s} boundary")
for c in claims:
    print(f"{c['tradition']:18s} {c['structural_claim'][:36]:38s} {c['strength']:14s} {c['boundary'][:30]}")
    print(f"  vocab: {c['tradition_vocab']}")

print("\n=== THE STANDARDISATION (what's comparable vs what's not) ===")
print("The standardised form separates:")
print("  STRUCTURAL CLAIM  (what is claimed)  → comparable across traditions")
print("  TRADITION VOCAB   (vimarśa / svasaṃvedana / self-presence / metacognition) → the local names")
print("  BOUNDARY          (what each tradition did NOT establish) → the honest differences")

print("\n[the power] now we can compare HONESTLY:")
for a in range(len(claims)):
    for b in range(a+1, len(claims)):
        same = claims[a]["structural_claim"] == claims[b]["structural_claim"]
        # same structural claim, different strength/boundary = a genuine comparative datum
        print(f"  {claims[a]['tradition']} vs {claims[b]['tradition']}: "
              f"same structural claim ({same}), "
              f"strengths {claims[a]['strength']}/{claims[b]['strength']}, "
              f"boundaries differ ({claims[a]['boundary'][:20]} | {claims[b]['boundary'][:20]})")

print("\n=== INSIGHT ===")
print("Standardisation lets us compare 'tough claims' across traditions WITHOUT collapsing them:")
print("the structural claim is the comparable core; the vocabulary and boundary preserve each tradition's")
print("specifics. 'vimarśa' and 'metacognition' can be compared as the SAME structural move while keeping")
print("their honest differences. This is the cross-tradition comparison engine — the 'analogy ≠ identity'")
print("discipline made technical, and it feeds essays/education (compare readings) + research (where do")
print("traditions diverge? = a crux).")
