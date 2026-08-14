# retrieval/ — graph-retrieval architectures

GraphRAG retrieval references. See `../../docs/ECOSYSTEM-INDEX.md` §3.

| Repo | Why we cloned |
|------|---------------|
| SubgraphRAG (Graph-COM/SubgraphRAG) | retrieve smallest useful graph (validates us) |
| PathRAG (BUPT-GAMMA/PathRAG) | retrieve reasoning paths, bounded token |
| HippoRAG (OSU-NLP-Group/HippoRAG) | PPR associative retrieval |
| nano-graphrag (gusye1234/nano-graphrag) | ~1100-line reference implementation |
| LightRAG (HKUDS/LightRAG) | dual-level retrieval |

| gusye1234/nano-graphrag | **CLONED (tracked, 3.3M)** — 1100-line reference; stable-LCC + GraphML determinism tested |

| BUPT-GAMMA/PathRAG | **CLONED** (2.1M) — the paper code; our lib/retrieval.py mirrors its flow-pruning + keyword→entity→context flow |

| microsoft/graphrag | **CLONED local-only** (32M) — the canonical GraphRAG (reference) |
| OpenSPG/KAG | **CLONED local-only** (238M) — logical-form reasoning (reference) |
| OSU-NLP-Group/HippoRAG | **CLONED local-only** (114M) — PPR retrieval (we implemented its core) |
