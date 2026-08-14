---
name: theatre-check
version: 1.0.0
author: ip-graph
description: >
  The verifiable-proof auditor (anti-theatre). For every kernel/docs claim, produce a VERIFIABLE PROOF
  that what is claimed is actually implemented: (1) a real test script exists, (2) it runs and passes,
  (3) it exercises REAL data (not synthetic — the theatre), and (4) the doc claim is matched to a test
  artifact. Each proof is stored with a hash so future agents can detect drift. This is "peer review
  with a verifiable outcome." Trigger when reviewing claims, before declaring something 'done', or when
  auditing the lab.
---

# THEATRE-CHECK — verifiable-proof audit

## What it does
For each kernel/claim, run a real test and store a **proof record** (test exists + passes + uses real
data + matches the doc claim + a proof hash). The proof store
(`data/references/theatre-proofs.json`) is the verifiable evidence that a claim is implemented — not
theatre.

## Why (anti-theatre)
We found 6 kernels marked VALIDATED but only tested on SYNTHETIC data (they prove the mechanism, not
integration). Theatre-check makes that visible and auditable instead of hidden.

## Usage
```
python3 scripts/theatre-check.py
# reads data/references/theatre-proofs.json for the stored proofs
```

## Verdicts
- **PROVEN** — test exists, passes, uses real data.
- **PROVEN-MECHANISM** — test exists, passes, but SYNTHETIC data (theatre risk).
- **UNPROVEN** — no passing real test for the claim.

## The rule (add to axioms)
> Before declaring a claim "done"/"validated", run `theatre-check.py` and confirm the kernel is PROVEN
> (real data). PROVEN-MECHANISM is an honest "mechanism works, not integrated" — not a claim of delivery.

---

## The 3 THEATRE MODES (the forms that slip through — learn these)

Marker/string-match checks can't catch these. This is why theatre slipped through. Audit for each:

### Mode 1 — HAND-FED PROOF FIELDS (the worst)
The test loads a real file (passes the marker) but hand-writes the object's critical fields.
```python
verse = json.load(open(".../root-verses.json"))[52]   # loads real verse
proof = TranslationProof(
    source_analysis={"segmentation": "PASS", ...},    # ← HAND-WRITTEN, never computed
    alignment={"coverage": 1.0, ...},                  # ← fabricated
)
```
**The read is decoration.** The assertion passes because the constants were typed to pass. This is
confirmation bias baked into the test. **Detect:** the object's PASS/score/status fields are literals,
never derived from the loaded data. `audit-theatre-dataflow.py` may not catch this — check by hand.

### Mode 2 — FABRICATED COMPARISON (both sides hand-written)
```python
our_reading = "nothing non-luminous can be an object"   # hand-typed
dycz_reading = "self-luminous consciousness is not perceived as an object"  # hand-typed
# agreement guaranteed because I wrote both
```
**Detect:** a "vs X" test where BOTH sides are literals, not parsed from their sources. Never do this.

### Mode 3 — HAND-CONSTRUCTED OBJECT (structure typed, not mined)
```python
essay.structure("...", [...])   # sections hand-typed
essay.mine_claim("Consciousness is self-luminous", ...)  # claim hand-typed, not mined
```
**Detect:** the AIF/claim/crux structure is literal in the test, not mined from the text.

---

## The 3-GATE RIGOROUS CHECK (run BEFORE claiming done)

```bash
# Gate 1 — does the test pass? (the old check)
python3 scripts/theatre-check.py
# Gate 2 — does it reference real data? (marker + data-flow)
python3 scripts/audit-theatre-dataflow.py   # THEATRE-flagged = 0
# Gate 3 — the MANUAL anti-theatre read (the only thing that catches Modes 1-3):
#   For each validator, ask: is the object under test DERIVED from the loaded data,
#   or hand-written next to it? If any critical field (PASS/score/status/reading)
#   is a literal and not computed from the data → it's THEATRE. Fix or mark PROVEN-MECHANISM.
```

**The hard rule:** a validator is REAL only if the object it validates is **DERIVED from the data**,
not hand-typed into the test. If the execution path (Hermes/LLM) isn't available to produce real output,
**honestly mark it PROVEN-MECHANISM** ("container test — mechanism proven, not production") — never claim
"from scratch."

## The failure that motivated this (2026-08-14)
The Tantrāloka validators looked real (they load the root file, they pass). But `translation.py` hand-fed
the proof fields, `vs-dyczkowski.py` hand-wrote both readings (fabricated agreement), and `fullstack.py`
hand-typed the claims. The marker check saw "data/" and moved on. **The fix is Gate 3 — the manual
data-flow read.** A marker is not a proof; a loaded file is not a derived object.
