"""
agentstateprotocol CLI — Command-line interface for inspecting agent state.

Usage:
    python -m agentstateprotocol log                    # View checkpoint history
    python -m agentstateprotocol tree                   # Visualize logic tree
    python -m agentstateprotocol branches               # List branches
    python -m agentstateprotocol diff <id1> <id2>       # Compare checkpoints
    python -m agentstateprotocol inspect <checkpoint>   # View checkpoint details
    python -m agentstateprotocol metrics                # Show agent metrics
    python -m agentstateprotocol demo                   # Run interactive demo
"""

import argparse
import json
import sys
import time
import random

from .engine import AgentStateProtocol
from .strategies import RetryWithBackoff, AlternativePathStrategy, DegradeGracefully
from .storage import FileSystemStorage


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agentstateprotocol",
        description="🧠 agentstateprotocol — Git for AI Thoughts",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Log
    log_parser = subparsers.add_parser("log", help="View checkpoint history")
    log_parser.add_argument("--branch", default=None, help="Filter by branch")
    log_parser.add_argument("--limit", type=int, default=20, help="Max entries")
    
    # Tree
    subparsers.add_parser("tree", help="Visualize logic tree")
    
    # Branches
    subparsers.add_parser("branches", help="List all branches")
    
    # Diff
    diff_parser = subparsers.add_parser("diff", help="Compare two checkpoints")
    diff_parser.add_argument("checkpoint_a", help="First checkpoint ID")
    diff_parser.add_argument("checkpoint_b", help="Second checkpoint ID")
    
    # Inspect
    inspect_parser = subparsers.add_parser("inspect", help="Inspect a checkpoint")
    inspect_parser.add_argument("checkpoint_id", help="Checkpoint ID")
    
    # Metrics
    subparsers.add_parser("metrics", help="Show agent metrics")
    
    # Demo
    subparsers.add_parser("demo", help="Run interactive demonstration")
    
    return parser


def run_demo():
    """
    Interactive demonstration of AgentStateProtocol capabilities.
    
    Simulates an AI agent that:
    1. Receives a task
    2. Tries to solve it step by step
    3. Hits an error
    4. Rolls back and tries a different approach
    5. Branches to explore alternatives
    6. Merges the best result
    """
    print("\n" + "=" * 60)
    print("🧠 AgentStateProtocol Demo — Git for AI Thoughts")
    print("=" * 60)
    
    # Initialize
    agent = AgentStateProtocol(
        "demo-agent",
        recovery_strategies=[
            RetryWithBackoff(base_delay=0.1, max_delay=1.0),
            DegradeGracefully(),
        ],
    )
    
    # Step 1: Receive task
    print("\n📋 Step 1: Agent receives a task")
    print("   Task: 'Summarize the latest quarterly earnings report'")
    
    cp1 = agent.checkpoint(
        state={
            "task": "Summarize quarterly earnings",
            "status": "received",
            "context": {"source": "user_request", "priority": "high"},
        },
        metadata={"confidence": 1.0, "tokens_used": 0},
        description="Task received",
        logic_step="task_intake",
    )
    print(f"   ✅ Checkpoint saved: {cp1.id} (hash: {cp1.hash})")
    
    # Step 2: Parse and plan
    print("\n🔍 Step 2: Agent parses the task and creates a plan")
    
    cp2 = agent.checkpoint(
        state={
            "task": "Summarize quarterly earnings",
            "plan": [
                "1. Retrieve earnings document",
                "2. Extract key financial metrics",
                "3. Identify trends vs previous quarter",
                "4. Generate executive summary",
            ],
            "current_step": 1,
        },
        metadata={"confidence": 0.9, "tokens_used": 150},
        description="Plan created",
        logic_step="planning",
    )
    print(f"   ✅ Checkpoint saved: {cp2.id}")
    print(f"   📝 Plan: 4 steps identified")
    
    # Step 3: Execute step 1 — document retrieval (FAILS!)
    print("\n⚡ Step 3: Agent tries to retrieve the document...")
    print("   💥 ERROR: Document API returned 503 (Service Unavailable)")
    
    cp3 = agent.checkpoint(
        state={
            "task": "Summarize quarterly earnings",
            "current_step": 1,
            "error": "API 503 - Service Unavailable",
        },
        metadata={"confidence": 0.3, "tokens_used": 200, "error": True},
        description="Document retrieval failed",
        logic_step="retrieve_doc:failed",
    )
    print(f"   ❌ Error checkpoint: {cp3.id}")
    
    # Step 4: Roll back!
    print("\n⏪ Step 4: Rolling back to the planning stage...")
    
    rolled_back = agent.rollback(to_checkpoint_id=cp2.id)
    print(f"   ✅ Rolled back to: {rolled_back.id}")
    print(f"   📊 State restored: plan is intact, step 1 error discarded")
    
    # Step 5: Branch to try alternative approach
    print("\n🌿 Step 5: Creating a branch for alternative approach...")
    
    agent.branch("cached-data-approach")
    print(f"   ✅ Branch 'cached-data-approach' created")
    
    cp_alt = agent.checkpoint(
        state={
            "task": "Summarize quarterly earnings",
            "approach": "Use cached data instead of live API",
            "data_source": "local_cache",
            "cached_metrics": {
                "revenue": "$12.4B",
                "net_income": "$3.1B",
                "yoy_growth": "15%",
            },
        },
        metadata={"confidence": 0.75, "tokens_used": 100},
        description="Using cached data",
        logic_step="use_cached_data",
    )
    print(f"   ✅ Alternative checkpoint: {cp_alt.id}")
    
    # Step 6: Also try main branch with retry
    print("\n🔄 Step 6: Back on main branch, retrying with backoff...")
    
    agent.switch_branch("main")
    
    cp_retry = agent.checkpoint(
        state={
            "task": "Summarize quarterly earnings",
            "current_step": 1,
            "retry_attempt": 2,
            "data": {
                "revenue": "$12.5B",
                "net_income": "$3.2B",
                "yoy_growth": "16%",
                "eps": "$2.45",
            },
        },
        metadata={"confidence": 0.95, "tokens_used": 350},
        description="Document retrieved on retry",
        logic_step="retrieve_doc:success",
    )
    print(f"   ✅ Retry succeeded! Checkpoint: {cp_retry.id}")
    
    # Step 7: Merge branches
    print("\n🔀 Step 7: Merging cached approach (as validation)...")
    
    merged = agent.merge("cached-data-approach", strategy="prefer_higher_confidence")
    print(f"   ✅ Merged! Final checkpoint: {merged.id}")
    
    # Step 8: Generate summary
    print("\n📄 Step 8: Generating final summary...")
    
    final = agent.checkpoint(
        state={
            "task": "Summarize quarterly earnings",
            "status": "completed",
            "summary": (
                "Q4 revenue reached $12.5B, up 16% YoY. "
                "Net income of $3.2B with EPS of $2.45."
            ),
        },
        metadata={"confidence": 0.95, "tokens_used": 500},
        description="Summary generated",
        logic_step="generate_summary",
    )
    print(f"   ✅ Final checkpoint: {final.id}")
    
    # Show results
    print("\n" + "=" * 60)
    print("📊 SESSION SUMMARY")
    print("=" * 60)
    
    metrics = agent.metrics
    print(f"\n   Agent: {agent.agent_name}")
    print(f"   Total Checkpoints: {metrics['total_checkpoints']}")
    print(f"   Total Rollbacks: {metrics['total_rollbacks']}")
    print(f"   Total Branches: {metrics['total_branches']}")
    print(f"   Branches: {', '.join(metrics['branches'])}")
    
    print("\n📜 HISTORY (main branch):")
    for entry in agent.history(limit=10):
        status_icon = {
            "active": "🟢", "committed": "📦",
            "rolled_back": "⏪", "recovered": "♻️",
        }.get(entry["status"], "⬜")
        print(f"   {status_icon} [{entry['id']}] {entry['status']:12s} | {entry['logic_path']}")
    
    print("\n🌳 LOGIC TREE:")
    tree_viz = agent.visualize_tree()
    for line in tree_viz.split("\n"):
        print(f"   {line}")
    
    print("\n🌿 BRANCHES:")
    for b in agent.list_branches():
        marker = " ← current" if b["is_current"] else ""
        print(f"   {'*' if b['is_current'] else ' '} {b['name']} ({b['checkpoint_count']} checkpoints){marker}")
    
    # Diff
    print(f"\n📊 DIFF between first and last checkpoint:")
    diff = agent.diff(cp1.id, final.id)
    if diff["added"]:
        for key in list(diff["added"].keys())[:3]:
            print(f"   + {key}: {str(diff['added'][key])[:60]}")
    if diff["modified"]:
        for key in list(diff["modified"].keys())[:3]:
            print(f"   ~ {key}: {str(diff['modified'][key]['before'])[:30]} → {str(diff['modified'][key]['after'])[:30]}")
    
    print("\n" + "=" * 60)
    print("✨ Demo complete! AgentStateProtocol protected the agent through:")
    print("   • 1 API failure (caught & recovered)")
    print("   • 1 rollback (restored clean state)")
    print("   • 1 branch (explored alternative path)")
    print("   • 1 merge (combined best results)")
    print("   • Full reasoning tree preserved for audit")
    print("=" * 60 + "\n")
    
    return agent


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if args.command == "demo":
        run_demo()
    elif args.command is None:
        parser.print_help()
    else:
        # For other commands, try to load from filesystem storage
        storage = FileSystemStorage()
        session = storage.load_session()
        
        if not session:
            print("No agentstateprotocol session found. Run 'agentstateprotocol demo' to create one.")
            sys.exit(1)
        
        agent = AgentStateProtocol.import_session(session)
        
        if args.command == "log":
            for entry in agent.history(branch_name=args.branch, limit=args.limit):
                print(json.dumps(entry, indent=2))
        
        elif args.command == "tree":
            print(agent.visualize_tree())
        
        elif args.command == "branches":
            for b in agent.list_branches():
                marker = "*" if b["is_current"] else " "
                print(f"  {marker} {b['name']} ({b['checkpoint_count']} checkpoints)")
        
        elif args.command == "metrics":
            print(json.dumps(agent.metrics, indent=2))
        
        elif args.command == "diff":
            diff = agent.diff(args.checkpoint_a, args.checkpoint_b)
            print(json.dumps(diff, indent=2, default=str))
        
        elif args.command == "inspect":
            for entry in agent.history():
                if entry["id"] == args.checkpoint_id:
                    print(json.dumps(entry, indent=2))
                    break
            else:
                print(f"Checkpoint {args.checkpoint_id} not found.")


if __name__ == "__main__":
    main()

