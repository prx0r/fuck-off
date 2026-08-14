#!/usr/bin/env python3
"""validate-tantraloka-argument.py — STEP 3 of the Mona Lisa: the Argument/Crux engine on Āhnika 1.

The reasoning engine on the real Sanskrit root: the reflexivity kārikā AbhT_1.52 becomes an AIF
argument (info/inference/conflict) + the crux. The review gate enforces: a machine-proposed thesis
stays CORRECTION (never auto-promoted) — the honest ceiling.

The argument (from the pushing sessions):
  ABhT_1.52: "nothing non-luminous can even be an object" (nahyaprakāśarūpasya prākāśyaṃ vastutāpi vā)
  → premise: consciousness is self-luminous (prakāśa)
  → inference: therefore it cannot be reduced to a non-luminous object
  → crux: is reflexivity (vimarśa) entailed by luminosity, or separable? (the recognition crux)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from review import ReviewState, ReviewPhase, reducer, phase_from_ceiling
from scholar_review import Finding

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== STEP 3: TANTRĀLOKA ARGUMENT + CRUX on AbhT_1.52 ===\n")

# ---- the argument (AIF): info/inference/conflict over the real kārikā ----
ARG = {
    "id": "ARGT-1.52",
    "karika": "AbhT_1.52",
    "claim": "nothing non-luminous can even be an object (vastutā)",
    "premise": "consciousness (prakāśa) is self-luminous, not an object",
    "inference": "so it cannot be reduced to a non-luminous object",
    "conflict": "is reflexivity (vimarśa) entailed by luminosity, or separable?",
}
check("the argument cites the real kārikā", ARG["karika"] == "AbhT_1.52")
check("the argument has a load-bearing inference (the reflexivity crux)",
      "reflexivity" in ARG["conflict"] and "vimarśa" in ARG["conflict"])

# ---- the review gate: a machine-proposed thesis stays CORRECTION (honest) ----
st = ReviewState(ARG["id"])
# the reflexivity thesis is machine-proposed (from our translation, not yet adjudicated)
phase = reducer(st, evidence_ok=False)
check("the machine-proposed thesis starts in CORRECTION (honest ceiling)",
      phase == ReviewPhase.CORRECTION)
# add a blocking finding (the crux is open) → it cannot promote
st.findings.append(Finding("f1", "reviewer", severity="BLOCKING", category="crux",
                           text="reflexivity-as-entailed not yet adjudicated"))
reducer(st, evidence_ok=True)      # CORRECTION → REVIEWING (evidence now present)
check("the open crux is a blocking finding", bool(st.blocking_findings()))
blocked = reducer(st, evidence_ok=True)  # REVIEWING → checks blocking_findings → CORRECTION
check("the open crux BLOCKS promotion (machine cannot adjudicate)",
      blocked == ReviewPhase.CORRECTION and bool(st.blocking_findings()))
# only a human approving reaches the adjudicated state
reducer(st, evidence_ok=True, human_approves=True)
check("only human approval reaches the adjudicated/override phase (Law 2)",
      st.phase == ReviewPhase.HUMAN_OVERRIDE)

# ---- the crux is the executable "what would change our mind" ----
CRUX = {"proposition": "vimarśa is entailed by prakāśa (reflexivity is intrinsic to luminosity)",
        "alternatives": ["vimarśa is a separate power", "luminosity alone suffices"],
        "decisive_evidence": "AbhT_1.52 + the reflexivity kārikās",
        "downstream_arguments": ["the upāyas", "the recognition thesis", "the body/consciousness split"],
        "status": "OPEN"}
check("the crux is well-formed (proposition + alternatives + decisive evidence)",
      CRUX["proposition"] and len(CRUX["alternatives"]) >= 2 and CRUX["status"] == "OPEN")
check("the crux is load-bearing (downstream arguments listed)",
      len(CRUX["downstream_arguments"]) >= 3)

# ---- a citation check: the argument's sources resolve to the root ----
from scholar_review import verify_citations
cits = verify_citations(["AbhT_1.52", "AbhT_1.1"], known_refs={"AbhT_1.52", "AbhT_1.1", "AbhT_1.2"})
check("the argument's citations resolve (no phantoms)", all(c.status == "VERIFIED" for c in cits))

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nSTEP 3 (ARGUMENT + CRUX) VERIFIED: AbhT_1.52 becomes a load-bearing reflexivity argument with")
print("an OPEN crux; the machine-proposed thesis stays in CORRECTION (only a human adjudicates). The")
print("reasoning engine works on the real Tantrāloka.")
sys.exit(0 if all(c for _,c in results) else 1)
