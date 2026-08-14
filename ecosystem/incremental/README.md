# incremental/ — Salsa-style incremental computation (performance speedup)

| Repo | Why |
|------|-----|
| salsa-rs/salsa | **CLONED** (5.4M) — memoized tracked queries, dependency tracking, reuse-on-change |

Validated: `experiment-salsa-incremental.py` — unchanged reads reuse (0 recompute), single change = O(1) update.
