#!/usr/bin/env python3
"""build-github-index.py — generate the canonical GitHub reference catalog.

Extracts repo owner/name + inline descriptions from the survey specs, assigns category + tier + note,
and writes:
  data/references/github.json   (machine-readable catalog with tags/metadata)
  docs/GITHUB-INDEX.md          (readable, agent-navigable)
"""
import json, os, re

SPECS = [
    "/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-07-ECOSYSTEM-SURVEY.md",
    "/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-08-GRAPH-REASONING-SURVEY.md",
    "/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-09-AGENT-ORCHESTRATION-SURVEY.md",
    "/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-10-FRONTIER-AGENT-SURVEY.md",
    "/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-11-AGENT-MEMORY-SURVEY.md",
]

# owner/repo -> (category, tier, note)
# tier: 0=clone-first, 1=ingest, 2=architecture, ref=reference, 3=watch
CATALOG = {
  # ---- epistemic / knowledge graph (SPEC-07) ----
  "infinitywings/rka": ("epistemic", 0, "research-workflow-as-state; supersession/staleness propagation"),
  "aaronsb/knowledge-graph-system": ("epistemic", 0, "Kappa Graph: supporting vs contradicting evidence, grounding"),
  "vouchdev/vouch": ("epistemic", 0, "git-native write/review gate (don't rebuild)"),
  "eigenius/eigenius": ("epistemic", 0, "typed knowledge classes (Declared/Observed/Derived/Verified)"),
  "Detective-XH/DocGraph": ("epistemic", 0, "SQLite KG + drift audits (staleness)"),
  "xoai/sage-wiki": ("compilers", 0, "graph as compile output"),
  "rhanka/graphify": ("compilers", 0, "extract->canonicalize->reconcile->typed graph"),
  "obra/knowledge-graph": ("compilers", 0, "query a vault as a KG; agent interface"),
  # ---- argumentation / datasets ----
  "arg-tech/aif-arg-datasets": ("argumentation", 1, "xAIF argument graphs (QT30) - the moat dataset"),
  "allenai/scifact": ("datasets", 1, "scientific claim<->evidence gold"),
  "jiho283/FactKG": ("datasets", 1, "108k claims with reasoning structures"),
  "swarnaHub/ExplaGraphs": ("datasets", 1, "argument->explanation graph"),
  "kixlab/suggestbot_dataset": ("datasets", 1, "verifiable claims + supporting/refuting info"),
  "lamps-lab/msvec": ("datasets", 1, "multi-domain scientific claims"),
  "westlake-autolab/BioKGBench": ("datasets", 1, "agents checking claims against a KG"),
  "altuncu/FACTors": ("datasets", 1, "118k fact-check claims"),
  "romain-girardi-eng/EleutherIA": ("philosophy", 1, "free-will philosophy KG (~19k nodes/69k passages)"),
  "bhaskatripathi/graphGita": ("philosophy", 2, "Gita->KG with MCTS interpretation"),
  # ---- science corpus infra ----
  "allenai/s2orc": ("science-infra", 2, "S2ORC: scholarly open research corpus"),
  "allenai/s2orc-doc2json": ("science-infra", 1, "paper parsing (PDF2JSON/TEX2JSON/JATS2JSON)"),
  "ourresearch/OpenAlex": ("science-infra", 2, "open catalog of scholarship"),
  "allenai/peS2o": ("science-infra", 2, "pretraining efficiently on S2ORC"),
  # ---- graph reasoning (SPEC-08) ----
  "RManLuo/gfm-rag": ("graph-reasoning", 0, "G-reasoner: graph foundation model for RAG"),
  "RManLuo/reasoning-on-graphs": ("graph-reasoning", 0, "graph-valid plan before answering"),
  "DataArcTech/ToG-2": ("graph-reasoning", 0, "alternating text<->graph search"),
  "IDEA-FinAI/ToG": ("graph-reasoning", 2, "original Think-on-Graph"),
  "BUPT-GAMMA/PathRAG": ("graph-reasoning", 0, "retrieve reasoning paths, bounded token"),
  "Graph-COM/SubgraphRAG": ("graph-reasoning", 0, "retrieve smallest useful graph"),
  "OSU-NLP-Group/HippoRAG": ("graph-reasoning", 0, "PPR associative retrieval"),
  "LHRLAB/HyperGraphRAG": ("graph-reasoning", 2, "hypergraph representation (BET)"),
  "gusye1234/nano-graphrag": ("graph-reasoning", 2, "~1100-line reference GraphRAG"),
  "circlemind-ai/fast-graphrag": ("graph-reasoning", 2, "production-minded HippoRAG-like"),
  "HKUDS/LightRAG": ("graph-reasoning", 2, "dual-level retrieval"),
  "OpenSPG/KAG": ("graph-reasoning", 2, "ontology + logic + retrieval"),
  "getzep/graphiti": ("graph-reasoning", 0, "epistemic graph vs temporal events"),
  "airi-institute/arigraph": ("graph-reasoning", 0, "semantic + episodic memory"),
  "microsoft/graphrag": ("graph-reasoning", 2, "reference GraphRAG (not foundation)"),
  "GraphRAG-Bench/GraphRAG-Benchmark": ("graph-reasoning", 2, "GraphRAG benchmark"),
  "JayLZhou/GraphRAG": ("graph-reasoning", 2, "in-depth graphrag study"),
  "lyndonkl/graphragmcp": ("graph-reasoning", 2, "GraphRAG MCP research server"),
  "ngl567/KGR-Survey": ("graph-reasoning", 2, "task-oriented KG reasoning survey"),
  # ---- agent orchestration (SPEC-09) ----
  "restatedev/restate": ("agent-runtime", 3, "distributed stateful actors + durable calls"),
  "temporalio/temporal": ("agent-runtime", 3, "mature durable execution (we already run it)"),
  "dbos-inc/dbos-transact-py": ("agent-runtime", 3, "durable execution on Postgres"),
  "ghuntley/loom": ("agent-runtime", 3, "Huntley's Rust AI coding agent (PROPRIETARY — reference only)"),
  "XiaoConstantine/herdr-workflow": ("agent-runtime", 0, "composable event-sourced multi-agent workflow; agents propose immutable evidence, reducers own lifecycle"),
  "broomva/arcan": ("agent-runtime", 0, "tiny agent kernel; event sourcing done correctly"),
  "valkor-ai/loom": ("agent-runtime", 3, "loop engineering (Apache-2.0 open; local-only)"),
  "ReinaMacCredy/maestro": ("agent-runtime", 3, "agent harness w/ verdict ledger (local-only, sqlite sk- strings)"),
  "hatchet-dev/hatchet": ("agent-runtime", 3, "queue/scheduling ergonomics"),
  "pydantic/pydantic-ai": ("agent-runtime", 2, "Python agent shell"),
  "microsoft/autogen": ("agent-runtime", 2, "agent framework (LangGraph-alt)"),
  "dapr/dapr-agents": ("agent-runtime", 3, "Dapr Agents (distributed)"),
  "langchain-ai/langgraph": ("agent-runtime", 2, "benchmark target, not foundation"),
  # ---- agent memory / self-evolving (SPEC-11) ----
  "EvoScientist/EvoScientist": ("agent-memory", 0, "self-evolving AI scientists (study deepest)"),
  "neomjs/neo": ("agent-memory", 0, "Neo.mjs agent OS / software organism"),
  "neo4j-labs/meta-knowledge-graph": ("agent-memory", 0, "self-improving memory layer, lifecycle hooks"),
  "neo4j-labs/agent-memory": ("agent-memory", 0, "graph-native agent memory"),
  "MemTensor/MemOS": ("agent-memory", 0, "self-evolving memory OS + Hermes integration"),
  "MemTensor/MemRL": ("agent-memory", 2, "runtime RL on episodic memory"),
  "Memento-Teams/Memento-Skills": ("agent-memory", 2, "agents design their own skills"),
  "Zhang-Henry/CoEvoSkills": ("agent-memory", 2, "skill + verifier co-evolution"),
  "ViktorAxelsen/MemSkill": ("agent-memory", 2, "memory policy learns how to remember"),
  "aiming-lab/SkillRL": ("agent-memory", 2, "trajectories -> hierarchical skills -> RL"),
  "Qwen-Applications/skill-self-play": ("agent-memory", 2, "skill self-play (Alibaba/Qwen)"),
  "EvolvingAgentsLabs/evolving-memory": ("agent-memory", 2, "evolving memory / cognitive trajectory"),
  "EvoMap/evolver-claude-code-plugin": ("agent-memory", 2, "GEP-powered self-evolution"),
  "RangeKing/self-evolving-agent": ("agent-memory", 2, "correct governance model"),
  "191341025/Self-Evolving-Skill": ("agent-memory", 2, "five-gate knowledge governance"),
  "DiaaAj/a-mem-mcp": ("agent-memory", 2, "self-evolving graph memory MCP"),
  "memory-graph/memory-graph": ("agent-memory", 2, "temporal graph memory MCP"),
  "ipiton/agent-memory-mcp": ("agent-memory", 2, "agent persistent memory MCP"),
  "LuckyGirl-XU/Awesome-Agent-Dynamic-Graphs": ("agent-memory", 3, "research-index: agent dynamic graphs"),
  "DataArcTech/Awesome-Agent-Skill-Papers": ("agent-memory", 3, "research-index: agent skill papers"),
  # ---- MCP / protocols (SPEC-09) ----
  "modelcontextprotocol/servers": ("protocols", 2, "MCP reference servers"),
  "agentic-community/mcp-gateway": ("protocols", 2, "MCP gateway (tool explosion)"),
  "agentic-community/mcp-gateway-registry": ("protocols", 2, "MCP gateway registry (control plane)"),
  "a2aproject/A2A": ("protocols", 2, "A2A agent-to-agent protocol"),
  "GoogleCloudPlatform/knowledge-catalog": ("protocols", 2, "Open Knowledge Format (OKF)"),
  "BerriAI/self-improving-agent": ("agent-memory", 2, "self-improvement as PR (minimal diff, human approves)"),
  "EverMind-AI/EverOS": ("agent-runtime", 2, "local-first memory runtime (Markdown+SQLite+LanceDB)"),
  "EvolvingAgentsLabs/evolving-memory": ("agent-memory", 2, "dream-cycle consolidation -> procedural memory"),
  "alecnielsen/adversarial-review": ("agent-runtime", 1, "4-phase adversarial debate loop"),
  "Ahren09/AgentReview": ("agent-runtime", 1, "peer-review process simulation (37.1% reviewer bias)"),
  "eigenius/eigenius": ("epistemic", 0, "grade model (declared<observed<derived<verified)"),
  "allenai/scifact": ("datasets", 1, "claim<->evidence gold (SUPPORT/CONTRADICT)"),
  "xoai/sage-wiki": ("compilers", 2, "graph-as-compile-output"),

  "yoheinakajima/instagraph": ("compilers", 0, "text->graph; our graph.json uses its schema"),
  "iwe-org/seventeen-centuries": ("compilers", 0, "philosophy markdown-graph (fragments+concepts)"),
  "BUPT-GAMMA/PathRAG": ("retrieval", 0, "the PathRAG paper code (flow-pruning)"),
  "getzep/graphiti": ("agent-memory", 0, "temporal edges (valid_at/invalid_at/episodes)"),

  "mntlra/knowledgeProvenance": ("epistemic", 1, "PROV-K nanopubs: multi-source assertions + trust networks"),
  "prometheus-eval/cmu-paper-reviewer": ("agent-runtime", 1, "CMU paper reviewer (5 critical issues)"),
  "gallantlab/literature-review-toolkit": ("science-infra", 1, "topic-agnostic literature review agent"),
  "wan-huiyan/agent-review-panel": ("agent-runtime", 1, "16-phase adversarial review panel (claim/severity verify + judge)"),

}

def main():
    entries = []
    for repo, (cat, tier, note) in CATALOG.items():
        owner, name = repo.split("/", 1)
        entries.append({"owner": owner, "name": name, "repo": repo,
                        "url": f"https://github.com/{repo}", "category": cat, "tier": tier,
                        "tier_label": {0:"clone-first",1:"ingest",2:"architecture",3:"watch"}[tier],
                        "note": note})
    os.makedirs("/mnt/HC_Volume_106427611/ip-graph/data/references", exist_ok=True)
    json.dump({"count": len(entries), "entries": entries},
              open("/mnt/HC_Volume_106427611/ip-graph/data/references/github.json", "w"), indent=1)
    # readable md
    cats = {}
    for e in entries: cats.setdefault(e["category"], []).append(e)
    L = ["# GITHUB INDEX — canonical GitHub reference catalog", "",
         f"*2026-08-14. {len(entries)} repos, organized by category + tier for agent retrieval. Machine form: `data/references/github.json`.*", "",
         "Tier: 0=clone-first · 1=ingest · 2=architecture · 3=watch", ""]
    for cat in sorted(cats):
        L.append(f"## {cat} ({len(cats[cat])})"); L.append("")
        for e in sorted(cats[cat], key=lambda x: x["tier"]):
            L.append(f"- **{e['owner']}/{e['name']}** — `T{e['tier']}` · {e['note']} · <{e['url']}>")
        L.append("")
    open("/mnt/HC_Volume_106427611/ip-graph/docs/GITHUB-INDEX.md", "w").write("\n".join(L))
    print(f"=== GITHUB INDEX ===")
    print(f"total: {len(entries)} repos")
    for cat in sorted(cats): print(f"  {cat:22s} {len(cats[cat])}")
    print(f"\nwrote data/references/github.json + docs/GITHUB-INDEX.md")

main()
