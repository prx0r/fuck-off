# WORKING NOTES — PER-LAYER GOLD VALIDATION (anti-theatre measurement)

*2026-08-15 · agentgraph. The honest record of testing each translation layer against HUMAN GOLD. This
is the anti-theatre doctrine applied: a layer is real only when its committed output scores against a gold
with a metric. Findings are honest — including the gaps.*

---

## 1. WHAT GOLD EXISTS (per layer)
| Layer | Gold source | Count |
|---|---|---|
| T1 / L0 / ARGMAP / L2 | `patala/data/published/ipvv/*.json` — published passages carrying `source`(dict) + `l0` + `argmap` + `l2`/`l2_text` | **55 passages** |
| L200 / C1 | `patala/translations/_stack/ipvv/l200/` + `c1/` (the frozen specs + gold-proofs) + the `ingest-ipvv-gold-proofs.py` audit | ~63 gold-proof passages (currently `gate=BLOCKED`) |
| ARGUMENT | `patala/data/evaluation/recovery-gold-v1.json` (ARGUMENT-RECOVERY-BENCH-v1: propositions/inferences/attacks/cruxes) | **51 cases** |
| L2 (Tantrāloka) | Dyczkowski vol1 (gold register) | on disk |

## 2. THE EVAL HARNESS (built, deterministic, no model)
`ip-graph/scripts/eval-layer-gold.py` — loads the published IPVV golds, scores committed registry output
vs gold by content-token recall.

## 3. THE HONEST RESULT (run it: `python3 scripts/eval-layer-gold.py --all`)
```
T1:      scored 0/49 gold   (committed 597)   — no clean match to gold
L0:      scored 49/49, mean_recall 0.0        — committed L0 doesn't overlap gold
ARGMAP:  scored 0/49        (committed 50)
L2:      scored 49/49, mean_recall 0.0        — committed L2 (3) doesn't cover gold
```
**The committed factory output scores ~0 recall against the published IPVV golds.** The causes:
1. **The published IPVV "golds" are CHUNK / COMMENTARY-level, not kārikā-level.** A published chunk is a
   long commentarial passage (e.g. `source.text` 48,976 chars spanning offsets 6300-7200), while the
   factory produces **kārikā-level** objects (an 85-char verse like `ipvv:V2O:k1`). These are DIFFERENT
   TASKS — a kārikā cannot be scored against a 49k-char commentary chunk. So the published IPVV chunks
   are the gold for the UPPER layers (commentary/essay), NOT for the factory's kārikā-level T1/L2.
2. **ipvv has only 1 committed T1** (of the gold corpus) — the factory has barely produced kārikā-level
   output for ipvv, so there's nothing to score even if the gold were aligned.
3. **Passage-id / granularity mismatch** (chunk vs kārikā) + **empty verse** in the L0/SOURCE payload.

## 4. THE CORRECT GOLD PER LAYER (what the eval must use)
| Layer | Correct gold | Why |
|---|---|---|
| T1 (kārikā gloss) | **kārikā-level** gold — Dyczkowski for Tantrāloka, or a kārikā-level IPVV gold | the factory produces kārikā-level T1 |
| L2 (kārikā prose) | **kārikā-level** gold — Dyczkowski (Tantrāloka) | same granularity as the factory |
| L200 / C1 | the IPVV gold-proofs + the frozen specs | already passage-level |
| ARGUMENT | `recovery-gold-v1.json` (51 cases) | not chunk-bound — evaluable now |
| Commentary / Essay | the published IPVV chunk passages | they ARE commentary/essay-level gold |

**The eval is only meaningful when the gold is at the SAME granularity as the factory's output.** The
published IPVV chunks validate the upper layers, not the kārikā spine. The next step is to validate T1/L2
against a kārikā-level gold (Dyczkowski), and ARGUMENT against its 51-case bench — which IS directly
evaluable now.

---

*This is a working note in the validation lane. It documents the per-layer gold sources, the eval harness,
and the honest finding (recall not measurable until the id-mapping + verse-recovery are closed).*
