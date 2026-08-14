# LAYER 00 — CORE ENGINE

*Part of the `VISION-CHUNK-LAYER-MAP.md` spine (Chunk 1). The domain-agnostic epistemic kernel that
every other layer builds on.*

## 1. What it is
The shared object envelope + epistemic status ladder that makes every object in every domain carry the
same provenance-aware structure. This is the "general engine" — domain-agnostic by design.

## 2. Purpose
One envelope everywhere: `id · layer · derived_from · source_refs · epistemic_ceiling · review_state ·
authority`. Plus the 4-axis authority and the invariant `authority(projection) <= authority(parent)`.

## 3. Data
- The epistemic ladder: MACHINE_PROPOSED → ENGINEERING_VALIDATED → SCHOLARLY_CORROBORATED →
  INDEPENDENT_REVIEWED → ADJUDICATED
- 4-axis Authority: generation · evidence · review · publication

## 4. Processes
```
any object → wrap in envelope → assign epistemic_ceiling + authority → enforce invariant
```

## 5. Implementations
- Spec: `specs/SPEC-02-epistemic-envelope.md`
- (to build) `lib/epistemic.py`

## 6. Docs
- `specs/SPEC-02-epistemic-envelope.md`
- `docs/vision/VISION.md` (the engine/domain separation)

## 7. Current state
`NOT_STARTED` (see `STATE.yaml`). No envelope on graph objects yet.
