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
