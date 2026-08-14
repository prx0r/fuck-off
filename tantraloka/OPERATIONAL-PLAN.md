# TANTRĀLOKA — OPERATIONAL PLAN (the autonomous live-system sequence)

*2026-08-14. The executable order + what to build/run at each step, mapped to the actual scripts and
kernels. See `README.md` in this folder for the full hypotheses + why. This is the sequence an autonomous
agent follows, one layer at a time, gated.*

---

## STEP 0 — PREFLIGHT (verify the machinery + sources)

```bash
# 1. the sources are ingested and resolvable
python3 scripts/ingest-tantraloka-root.py          # 5,860 kārikās → data/tantraloka/
# 2. the whole kernel suite passes (the organism is real)
python3 scripts/run-tests.py                       # must be 76/76
# 3. the read plane builds
python3 scripts/build-static-site.py               # concept + corpus pages
```

---

## STEP 1 — THE ATLAS (WHAT it is): bibliography → tagging → condition → timeline

**Goal:** Tantrāloka registers as a canonical WORK with tradition/school/time, rights-resolved.

| Task | Build/Run | Gate |
|---|---|---|
| A1 Bibliography | register the work + 2 etexts in `source_registry` | all source_refs resolve, rights ok |
| A2 Tagging | tag tradition=Trika, school=Pratyabhijñā, genre=treatise, author=Abhinavagupta | term-senses map to Trika via semantic-shift atlas |
| A3 Condition | separate kārikā (PRIMARY) vs Jayaratha Viveka (SECONDARY) | `integrity_gate` primary-source gate |
| A4 Timeline | place at c.975-1025, lineage Utpaladeva→Abhinavagupta→Jayaratha | temporal edges valid_at/invalid_at |

**Test to write:** `validate-tantraloka-atlas.py` — assert the work resolves, tags correct, kārikā vs
Viveka separated (primary vs secondary), timeline placed.

---

## STEP 2 — THE REFINERY (the translation spine): ingest → L0 → TranslationProof → Commentary

**Goal:** Āhnika 1 (333 kārikās) tokenized + proof-carrying translated FROM THE SANSKRIT (not Dyczkowski).

| Task | Build/Run | Gate |
|---|---|---|
| B1 INGEST | each kārikā → SOURCE object (sha256) | content-addressed, dedupe |
| B2 L0 | `vidyut_l0` SLP1 tokenize each verse | position-anchored, deterministic |
| B3 TranslationProof | translate from root → 11-dim vector | gate BLOCKED until human adjudication |
| B4 Commentary | Jayaratha + our note per kārikā, KORAL-separated | primary vs secondary kept apart |

**Test to write:** `validate-tantraloka-translation.py` — the flagship `AbhT_1.52` through L0 + Proof.

---

## STEP 3 — THE REASONING ENGINE: argument → crux → synthesis

**Goal:** the pushing sessions become crux nodes over the actual kārikās.

| Task | Build/Run | Gate |
|---|---|---|
| C1 Argument | claims → AIF (info/inference/conflict) | citecheck, no phantoms |
| C1 Crux | the reflexivity crux on AbhT_1.52 + upāyas cruxes | crux-compiler minimal divergence |
| C2 Synthesis | converged Āhnika-1 position, adjudicated inputs | derivation-complete, immune-gated |

**Test to write:** `validate-tantraloka-argument.py` — reflexivity crux resolves to AbhT_1.52.

---

## STEP 4 — THE REPRODUCTIVE + SENSORY: essay → education → products

**Goal:** the organism's outputs become touchable products.

| Task | Build/Run | Gate |
|---|---|---|
| D1 Essay | reactive essay, every sentence cites a kārikā | mutate → prose stale |
| D2 Education | LearningClaims + wrong-answer→neighbor on upāyas | each answer derivable |
| D3 Products | compile → bundles → Astro → MCP | 0-JS, JSON-LD, canonical |

---

## STEP 5 — THE VALIDATION vs DYCZKOWSKI (the payoff) + the flywheel

**Goal:** where we agree = hard core, where we differ = the interpretation-space.

| Task | Build/Run | Gate |
|---|---|---|
| E1 Three-version | `translation_variant` our Āhnika-1 vs Dyczkowski | agreement core + divergence surfaced |
| E2 Feedback | divergences → cruxes → re-prioritize (Q + R up) | `next_action` reorders the queue |

**Test to write:** `validate-tantraloka-vs-dyczkowski.py` — per-kārikā agreement; load-bearing terms
agree, contested readings diverge (matching the pushing sessions' flags).

---

## THE HYPOTHESES (testable, falsifiable)

1. **The atlas is real:** Tantrāloka resolves to 1 work / 2 etexts with Trika tagging + a timeline node.
2. **The spine holds:** 5,860 kārikās tokenize; TranslationProof gates BLOCKED until human (honest).
3. **The crux is real:** `AbhT_1.52` (reflexivity) is the load-bearing crux — retracting it collapses the
   Āhnika-1 argument.
4. **Reactive works:** editing a kārikā recompiles its essay + education (staleness blast-radius).
5. **The validation is meaningful:** our from-scratch translation AGREES with Dyczkowski on the technical
   core (prakāśa/vimarśa/upāya) and DIVERGES on the cruxes the pushing sessions flagged — proving the
   organism independently reconstructs the scholarship.

---

## ORDERING RULE (why this order)

Bottom-up, each step's output feeds the next. **The atlas (Step 1) must precede translation (Step 2)**
because the term-senses + rights + primary/secondary split are prerequisites. **TranslationProof (B3) must
precede Argument (Step 3)** because arguments cite proven claims, not drafts. **Validation (Step 5) is last**
because it needs the full from-scratch output to compare. Each step is gated: nothing proceeds until its
layer passes the invariant + primary-source gate + honest ceilings.

---

*This is the operational plan. README.md in this folder has the full hypotheses + the "what we expect and
why." Start at STEP 0 (preflight), then STEP 1. Each step's test script makes it verifiable.*
