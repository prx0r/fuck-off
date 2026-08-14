#!/usr/bin/env python3
"""build-arxiv-index.py — generate the canonical arXiv reference catalog.

Reads all arXiv ids + titles from the survey specs, adds category + status + note, and writes:
  data/references/arxiv.json        (machine-readable catalog)
  docs/ARXIV-INDEX.md               (readable, agent-navigable catalog)
Organized for quick agent retrieval.
"""
import json, os, re

SPECS = ["/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-08-GRAPH-REASONING-SURVEY.md",
         "/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-09-AGENT-ORCHESTRATION-SURVEY.md",
         "/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-10-FRONTIER-AGENT-SURVEY.md",
         "/mnt/HC_Volume_106427611/ip-graph/specs/SPEC-07-ECOSYSTEM-SURVEY.md"]

# id -> (category, status, note)
CATALOG = {
  # ---- graph reasoning (SPEC-08) ----
  "2307.07697": ("graph-reasoning", "REFERENCE", "Think-on-Graph: graph exploration as an agent action"),
  "2407.10805": ("graph-reasoning", "GAP", "ToG-2: alternating text<->graph search (trace/investigate)"),
  "2407.04363": ("graph-reasoning", "GAP", "AriGraph: semantic + episodic memory + world model"),
  "2509.24276": ("graph-reasoning", "GAP", "G-reasoner (GFM-RAG): graph foundation model for RAG"),
  "2502.14902": ("graph-reasoning", "GAP", "PathRAG: retrieve reasoning paths, bounded token context"),
  "2605.25480": ("graph-reasoning", "VALIDATES", "LLM-Wiki: retrieval as reasoning, self-evolving agent-native retrieval"),
  "2602.10246": ("graph-reasoning", "GAP", "KORAL: knowledge-graph-guided LLM reasoning"),
  "2606.01613": ("graph-reasoning", "GAP", "TechGraphRAG: evidence-sufficiency gate"),
  "2605.26874": ("graph-reasoning", "GAP", "KGs as the missing data layer for LLM ops"),
  "2607.22652": ("graph-reasoning", "BET", "KG2Code: executable graph queries (path/filter)"),
  "2505.07291": ("graph-reasoning", "REFERENCE", "graph reasoning (survey context)"),
  # ---- agent memory (SPEC-09/10) ----
  "2605.12061": ("agent-memory", "GAP", "SAGE: self-evolving agentic graph-memory engine"),
  "2607.03726": ("agent-memory", "GAP", "SelfMem: self-optimizing memory for AI agents"),
  "2310.08560": ("agent-memory", "REFERENCE", "MemGPT: LLMs as operating systems"),
  "2608.11224": ("agent-memory", "GAP", "agent memory for lifelong AI partners"),
  # ---- agent orchestration (SPEC-09) ----
  "2606.01416": ("agent-orchestration", "GAP", "Self-healing agentic orchestrators"),
  "2607.11138": ("agent-orchestration", "GAP", "formal hierarchical architecture for agentic orchestration"),
  "2608.04458": ("agent-orchestration", "GAP", "architectural implications of agentic AI workflows"),
  # ---- agent RL / training (SPEC-10) ----
  "2504.15466": ("agent-rl", "GAP", "learning adaptive parallel reasoning"),
  "2412.21139": ("agent-rl", "GAP", "SWE-Gym: training SE agents and verifiers"),
  "2512.16144": ("agent-rl", "GAP", "INTELLECT-3: technical report (Prime Intellect)"),
  "2505.22954": ("agent-rl", "GAP", "Darwin Godel Machine: open-ended evolution of self-improving agents"),
  "2608.03392": ("agent-rl", "GAP", "Self-evolving coding agents"),
  "2606.21228": ("agent-rl", "GAP", "Sakana Fugu technical report"),
  # ---- agent evaluation (SPEC-10) ----
  "2406.12045": ("agent-eval", "REFERENCE", "tau-bench: tool-agent-user interaction benchmark"),
  "2512.11147": ("agent-eval", "GAP", "MiniScope: least-privilege tool-calling authorization"),
  "2607.13411": ("agent-eval", "GAP", "frontier AI agents as clinical security auditors"),
  "2502.14297": ("agent-eval", "GAP", "evaluating Sakana's AI Scientist"),
  # ---- agent frameworks (SPEC-10) ----
  "2511.03690": ("agent-frameworks", "REFERENCE", "OpenHands Software Agent SDK"),
  "2512.23760": ("agent-frameworks", "GAP", "audited skill-graph self-improvement"),
  # ---- skills / datasets (SPEC-09) ----
  "2608.10906": ("skills-datasets", "GAP", "GitSkills: a dataset of agent skills on GitHub"),
  "2603.19461": ("skills-datasets", "REFERENCE", "skills/dataset reference"),
}

# titles from the survey footnotes
TITLES = {
  "2307.07697": "Think-on-Graph: Deep and Responsible Reasoning of LLM on Knowledge Graph",
  "2407.10805": "ToG-2: Alternating Graph and Document Reasoning",
  "2407.04363": "AriGraph: Learning to Generate Knowledge Graphs from Text",
  "2509.24276": "G-reasoner: Graph Foundation Model for Retrieval-Augmented Generation",
  "2502.14902": "PathRAG: Pruning Graph-based Retrieval Augmented Generation with Relational Paths",
  "2605.25480": "Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki",
  "2602.10246": "KORAL: Knowledge Graph Guided LLM Reasoning for SSD Operational Analysis",
  "2606.01613": "TechGraphRAG: An Agentic Graph-Augmented RAG Framework for Technical Literature Reasoning",
  "2605.26874": "Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations",
  "2607.22652": "KG2Code: Bridging Knowledge Graphs and LLMs via Executable Code for Question Answering",
  "2605.12061": "SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory",
  "2607.03726": "SelfMem: Self-Optimizing Memory for AI Agents",
  "2310.08560": "MemGPT: Towards LLMs as Operating Systems",
  "2608.11224": "Harnessing agent memory to build lifelong AI partners for materials scientists",
  "2606.01416": "Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Models",
  "2607.11138": "A Formal Hierarchical Architecture for Agentic Orchestration with Stackelberg Games",
  "2608.04458": "Architectural Implications of Agentic AI Workflows",
  "2504.15466": "Learning Adaptive Parallel Reasoning with Language Models",
  "2412.21139": "Training Software Engineering Agents and Verifiers with SWE-Gym",
  "2512.16144": "INTELLECT-3: Technical Report",
  "2505.22954": "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents",
  "2608.03392": "Self-Evolving Coding Agents",
  "2606.21228": "Sakana Fugu Technical Report",
  "2406.12045": "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains",
  "2512.11147": "MiniScope: A Least Privilege Framework for Authorizing Tool Calling Agents",
  "2607.13411": "Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors",
  "2502.14297": "Evaluating Sakana's AI Scientist for Autonomous Research",
  "2511.03690": "The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents",
  "2512.23760": "Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards",
  "2608.10906": "GitSkills: A Dataset of Agent Skills on GitHub",
}

entries = []
for aid, (cat, status, note) in CATALOG.items():
    entries.append({
        "arxiv_id": aid, "url": f"https://arxiv.org/abs/{aid}",
        "title": TITLES.get(aid, ""), "category": cat, "status": status, "note": note,
    })

# build the json
os.makedirs("/mnt/HC_Volume_106427611/ip-graph/data/references", exist_ok=True)
json.dump({"count": len(entries), "entries": entries}, open("/mnt/HC_Volume_106427611/ip-graph/data/references/arxiv.json", "w"), indent=1)

# build the readable md
cats = {}
for e in entries: cats.setdefault(e["category"], []).append(e)
lines = ["# ARXIV INDEX — canonical arXiv reference catalog", "",
         f"*2026-08-14. {len(entries)} papers, organized by category for agent retrieval. Machine form: `data/references/arxiv.json`.*", "",
         "Status legend: GAP (to adopt) · BET (frontier) · VALIDATES (confirms us) · REFERENCE (study)",
         ""]
for cat in sorted(cats):
    lines.append(f"## {cat} ({len(cats[cat])})")
    lines.append("")
    for e in sorted(cats[cat], key=lambda x: x["arxiv_id"]):
        lines.append(f"- **{e['title']}** — [{e['arxiv_id']}]({e['url']}) · `{e['status']}` · {e['note']}")
    lines.append("")
open("/mnt/HC_Volume_106427611/ip-graph/docs/ARXIV-INDEX.md", "w").write("\n".join(lines))

print(f"=== ARXIV INDEX ===")
print(f"total: {len(entries)} papers")
for cat in sorted(cats):
    print(f"  {cat:20s} {len(cats[cat])}")
print(f"\nwrote data/references/arxiv.json + docs/ARXIV-INDEX.md")
