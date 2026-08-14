# LAYER 05 — REVIEW & GATE
*Spine (Chunk 6). Review events + authority + adjudication.*

## 1. What it is
The epistemic honesty layer: review events that are EVIDENCE ABOUT a target (never mutating it), plus
the 4-axis authority ladder.

## 2. Purpose
Mark every claim honestly (MACHINE_PROPOSED vs SCHOLARLY_CORROBORATED) and let only humans raise the
review axis. Physics edges may be corroborated; the free-will thesis stays machine-proposed.

## 3. Data
- ReviewEvent / Adjudication / PromotionEvent records (patala pattern)

## 4. Processes
```
ReviewProposal → Adjudication → new version → PromotionEvent  (never mutates in place)
```

## 5. Implementations
- Spec: `specs/SPEC-02-epistemic-envelope.md`

## 6. Docs
- `specs/SPEC-02-epistemic-envelope.md`

## 7. Current state
`NOT_STARTED`.
