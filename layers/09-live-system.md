# LAYER 09 — LIVE SYSTEM
*Spine (Chunk 10). State, staleness, docs-in-sync, orchestration.*

## 1. What it is
The meta-layer that keeps the whole project in sync: this vision→chunk→layer map, STATE.yaml, the
specs (draft → live), and staleness tracking. It's how the vision actually gets executed by agents.

## 2. Purpose
Make the project self-describing: an agent reads VISION → CHUNK-LAYER-MAP → a layer doc → its state →
advances it. The docs never go stale (redirect stubs instead).

## 3. Data
- `VISION-CHUNK-LAYER-MAP.md` — the top-down decomposition
- `VISION-CHUNKS.json` — the machine-resolvable form
- `STATE.yaml` — the live per-layer tracker
- `specs/` (draft) → `docs/` (live) workflow

## 4. Processes
```
agent: pick chunk → layer doc → read state → advance → update STATE.yaml → update doc if implemented
```

## 5. Implementations
- `VISION-CHUNK-LAYER-MAP.md` · `VISION-CHUNKS.json` · `STATE.yaml` · `specs/README.md`

## 6. Docs
- `docs/vision/VISION.md` · `NAVIGATION.md` · `AGENTS.md`

## 7. Current state
`IN_PROGRESS` — the map + STATE + specs are built; the loop (agent execution) is next.
