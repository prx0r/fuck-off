"""
Core Engine for AgentStateProtocol — The Checkpointing & Recovery Protocol
================================================================

This is the "brain" of AgentStateProtocol. In plain English:

- A **Checkpoint** is a snapshot of what an AI agent is "thinking" at a given moment.
  Like pressing Ctrl+S on the agent's brain.

- A **Branch** is an alternative reasoning path the agent can explore.
  Like Git branches, but for thoughts instead of code.

- A **LogicTree** tracks the full decision tree — every path the agent considered,
  took, or abandoned.

- **AgentStateProtocol** ties it all together: save states, rollback on failure, branch to
  try different approaches, and recover gracefully from errors.
"""

import uuid
import time
import hashlib
import json
import copy
import logging
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional, Callable, Tuple
from enum import Enum
from datetime import datetime, timezone

logger = logging.getLogger("agentstateprotocol")


# ──────────────────────────────────────────────
#  Data Models — The "Atoms" of Agent State
# ──────────────────────────────────────────────

class CheckpointStatus(Enum):
    """Status of a checkpoint — like commit status in Git."""
    ACTIVE = "active"          # Current working state
    COMMITTED = "committed"    # Saved and finalized
    ROLLED_BACK = "rolled_back"  # Was active, but agent rolled back past it
    ABANDONED = "abandoned"    # Branch was abandoned (dead end)
    RECOVERED = "recovered"    # Restored after a failure


@dataclass
class Checkpoint:
    """
    A snapshot of an agent's "state of mind" at a specific moment.
    
    Think of it like a save point in a video game:
    - `state`: What the agent is "thinking" (any Python dict/object)
    - `logic_path`: The chain of reasoning steps that led here
    - `metadata`: Extra context (timestamps, step names, confidence scores)
    - `parent_id`: Which checkpoint came before this one (like Git parent commit)
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:12])
    timestamp: float = field(default_factory=time.time)
    state: Dict[str, Any] = field(default_factory=dict)
    logic_path: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    parent_id: Optional[str] = None
    branch_name: str = "main"
    status: CheckpointStatus = CheckpointStatus.ACTIVE
    error_context: Optional[Dict[str, Any]] = None
    hash: str = ""
    
    def __post_init__(self):
        """Auto-generate a content hash for integrity verification."""
        if not self.hash:
            content = json.dumps(self.state, sort_keys=True, default=str)
            self.hash = hashlib.sha256(content.encode()).hexdigest()[:16]
    
    @property
    def human_time(self) -> str:
        return datetime.fromtimestamp(self.timestamp, tz=timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S UTC"
        )
    
    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["status"] = self.status.value
        return d
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Checkpoint":
        data["status"] = CheckpointStatus(data["status"])
        return cls(**data)


@dataclass
class Branch:
    """
    A named reasoning path — like a Git branch but for thought processes.
    
    Example: An agent analyzing a problem might have:
    - 'main' branch: Conservative, step-by-step approach
    - 'creative' branch: Lateral thinking, unconventional solutions
    - 'fallback' branch: Safe, minimal-risk approach
    """
    name: str
    created_at: float = field(default_factory=time.time)
    parent_branch: str = "main"
    fork_checkpoint_id: Optional[str] = None
    is_active: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)
    checkpoints: List[str] = field(default_factory=list)  # checkpoint IDs
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class LogicNode:
    """A single node in the reasoning tree."""
    id: str
    description: str
    checkpoint_id: str
    children: List[str] = field(default_factory=list)
    parent: Optional[str] = None
    outcome: Optional[str] = None  # "success", "failure", "abandoned", "in_progress"
    confidence: float = 0.0
    reasoning: str = ""


class LogicTree:
    """
    The full decision tree of an agent's reasoning process.
    
    Imagine a tree where:
    - The root is the original question/task
    - Each branch is a different approach the agent tried
    - Leaves are either solutions or dead ends
    - You can trace back from any point to see "how did we get here?"
    """
    
    def __init__(self):
        self.nodes: Dict[str, LogicNode] = {}
        self.root_id: Optional[str] = None
    
    def add_node(self, node: LogicNode) -> None:
        self.nodes[node.id] = node
        if self.root_id is None:
            self.root_id = node.id
        if node.parent and node.parent in self.nodes:
            self.nodes[node.parent].children.append(node.id)
    
    def get_path_to_root(self, node_id: str) -> List[LogicNode]:
        """Trace the reasoning chain from a node back to the root."""
        path = []
        current = node_id
        visited = set()
        while current and current not in visited:
            visited.add(current)
            if current in self.nodes:
                path.append(self.nodes[current])
                current = self.nodes[current].parent
        return list(reversed(path))
    
    def get_active_paths(self) -> List[List[LogicNode]]:
        """Get all currently active (non-abandoned) reasoning paths."""
        leaves = [
            nid for nid, node in self.nodes.items()
            if not node.children and node.outcome != "abandoned"
        ]
        return [self.get_path_to_root(leaf) for leaf in leaves]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "root_id": self.root_id,
            "nodes": {nid: asdict(node) for nid, node in self.nodes.items()},
        }
    
    def visualize(self) -> str:
        """Generate a text-based tree visualization."""
        if not self.root_id:
            return "(empty tree)"
        lines = []
        self._visualize_node(self.root_id, lines, "", True)
        return "\n".join(lines)
    
    def _visualize_node(self, node_id: str, lines: list, prefix: str, is_last: bool):
        node = self.nodes.get(node_id)
        if not node:
            return
        connector = "└── " if is_last else "├── "
        status_icon = {
            "success": "✅", "failure": "❌", "abandoned": "🚫",
            "in_progress": "🔄", None: "⬜"
        }.get(node.outcome, "⬜")
        lines.append(f"{prefix}{connector}{status_icon} {node.description} [{node.id[:8]}]")
        child_prefix = prefix + ("    " if is_last else "│   ")
        for i, child_id in enumerate(node.children):
            self._visualize_node(
                child_id, lines, child_prefix, i == len(node.children) - 1
            )


# ──────────────────────────────────────────────
#  AgentStateProtocol — The Main Controller
# ──────────────────────────────────────────────

class AgentStateProtocol:
    """
    Git for AI Thoughts — The main interface.
    
    This is what agent developers interact with. It provides:
    
    1. **checkpoint()** — Save the agent's current state (like `git commit`)
    2. **rollback()** — Go back to a previous state (like `git reset`)
    3. **branch()** — Create alternative reasoning path (like `git branch`)
    4. **merge()** — Combine insights from branches (like `git merge`)
    5. **recover()** — Auto-recover from errors using strategies
    6. **history()** — View the full reasoning timeline (like `git log`)
    
    Usage:
        agent = AgentStateProtocol("my-reasoning-agent")
        
        # Save state at each step
        cp1 = agent.checkpoint(
            state={"step": "parsing", "data": parsed_result},
            metadata={"confidence": 0.95}
        )
        
        # Something went wrong? Roll back!
        agent.rollback()  # Goes to previous checkpoint
        
        # Want to try a different approach?
        agent.branch("creative-approach")
        agent.checkpoint(state={"step": "lateral_thinking", ...})
    """
    
    def __init__(
        self,
        agent_name: str,
        storage_backend=None,
        max_checkpoints: int = 1000,
        auto_checkpoint: bool = False,
        recovery_strategies: Optional[List] = None,
    ):
        self.agent_name = agent_name
        self.created_at = time.time()
        
        # Core state
        self._checkpoints: Dict[str, Checkpoint] = {}
        self._branches: Dict[str, Branch] = {}
        self._current_branch: str = "main"
        self._logic_tree = LogicTree()
        
        # Configuration
        self.max_checkpoints = max_checkpoints
        self.auto_checkpoint = auto_checkpoint
        self._recovery_strategies = recovery_strategies or []
        
        # Storage
        self._storage = storage_backend
        
        # Initialize main branch
        self._branches["main"] = Branch(name="main")
        
        # Metrics
        self._metrics = {
            "total_checkpoints": 0,
            "total_rollbacks": 0,
            "total_recoveries": 0,
            "total_branches": 1,
            "errors_caught": 0,
            "time_saved_seconds": 0.0,
        }
        
        logger.info(f"AgentStateProtocol initialized for agent: {agent_name}")
    
    # ── Checkpoint Operations ──
    
    def checkpoint(
        self,
        state: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None,
        description: str = "",
        logic_step: str = "",
    ) -> Checkpoint:
        """
        Save the agent's current "state of mind."
        
        Think of it as pressing Ctrl+S on the agent's brain.
        
        Args:
            state: The agent's current state (reasoning, data, decisions, etc.)
            metadata: Extra context (confidence scores, step names, etc.)
            description: Human-readable description of this checkpoint
            logic_step: Name of the reasoning step (for the logic tree)
        
        Returns:
            The created Checkpoint object
        
        Example:
            cp = agent.checkpoint(
                state={"reasoning": "User wants X, best approach is Y"},
                metadata={"confidence": 0.87, "tokens_used": 150},
                description="Identified user intent",
                logic_step="intent_classification"
            )
        """
        # Find parent checkpoint
        branch = self._branches[self._current_branch]
        parent_id = branch.checkpoints[-1] if branch.checkpoints else None
        
        # Build logic path
        logic_path = []
        if parent_id and parent_id in self._checkpoints:
            logic_path = list(self._checkpoints[parent_id].logic_path)
        if logic_step:
            logic_path.append(logic_step)
        
        # Create checkpoint
        cp = Checkpoint(
            state=copy.deepcopy(state),
            logic_path=logic_path,
            metadata=metadata or {},
            parent_id=parent_id,
            branch_name=self._current_branch,
            status=CheckpointStatus.ACTIVE,
        )
        
        # Store it
        self._checkpoints[cp.id] = cp
        branch.checkpoints.append(cp.id)
        
        # Update logic tree
        if logic_step or description:
            node = LogicNode(
                id=cp.id,
                description=description or logic_step,
                checkpoint_id=cp.id,
                parent=parent_id,
                outcome="in_progress",
                confidence=metadata.get("confidence", 0.0) if metadata else 0.0,
            )
            self._logic_tree.add_node(node)
        
        # Enforce max checkpoints (evict oldest)
        self._enforce_limits()
        
        # Persist if storage backend exists
        if self._storage:
            self._storage.save_checkpoint(cp)
        
        self._metrics["total_checkpoints"] += 1
        logger.info(f"Checkpoint created: {cp.id} on branch '{self._current_branch}'")
        
        return cp
    
    def rollback(self, steps: int = 1, to_checkpoint_id: Optional[str] = None) -> Optional[Checkpoint]:
        """
        Roll back to a previous state — like pressing Ctrl+Z on the agent's thinking.
        
        Args:
            steps: How many steps to go back (default: 1)
            to_checkpoint_id: Specific checkpoint ID to roll back to
        
        Returns:
            The checkpoint we rolled back to, or None if nothing to rollback
        
        Example:
            # Go back one step
            agent.rollback()
            
            # Go back 3 steps
            agent.rollback(steps=3)
            
            # Go to a specific checkpoint
            agent.rollback(to_checkpoint_id="abc123")
        """
        branch = self._branches[self._current_branch]
        
        if not branch.checkpoints:
            logger.warning("No checkpoints to rollback to.")
            return None
        
        start_time = time.time()
        
        if to_checkpoint_id:
            # Find the target checkpoint index
            try:
                target_idx = branch.checkpoints.index(to_checkpoint_id)
            except ValueError:
                logger.error(f"Checkpoint {to_checkpoint_id} not found on current branch.")
                return None
            
            # Mark rolled-back checkpoints
            for cp_id in branch.checkpoints[target_idx + 1:]:
                if cp_id in self._checkpoints:
                    self._checkpoints[cp_id].status = CheckpointStatus.ROLLED_BACK
                    if cp_id in self._logic_tree.nodes:
                        self._logic_tree.nodes[cp_id].outcome = "abandoned"
            
            branch.checkpoints = branch.checkpoints[:target_idx + 1]
        else:
            # Roll back N steps
            steps = min(steps, len(branch.checkpoints) - 1)
            if steps <= 0:
                return self._checkpoints.get(branch.checkpoints[-1])
            
            for cp_id in branch.checkpoints[-steps:]:
                if cp_id in self._checkpoints:
                    self._checkpoints[cp_id].status = CheckpointStatus.ROLLED_BACK
                    if cp_id in self._logic_tree.nodes:
                        self._logic_tree.nodes[cp_id].outcome = "abandoned"
            
            branch.checkpoints = branch.checkpoints[:-steps]
        
        # Get the checkpoint we rolled back to
        if branch.checkpoints:
            target = self._checkpoints[branch.checkpoints[-1]]
            target.status = CheckpointStatus.RECOVERED
            
            elapsed = time.time() - start_time
            self._metrics["total_rollbacks"] += 1
            self._metrics["time_saved_seconds"] += elapsed
            
            logger.info(f"Rolled back to checkpoint: {target.id}")
            return target
        
        return None
    
    def get_state(self) -> Optional[Dict[str, Any]]:
        """Get the current agent state (from the latest checkpoint)."""
        branch = self._branches[self._current_branch]
        if branch.checkpoints:
            cp = self._checkpoints[branch.checkpoints[-1]]
            return copy.deepcopy(cp.state)
        return None
    
    # ── Branch Operations ──
    
    def branch(self, name: str, from_checkpoint_id: Optional[str] = None) -> Branch:
        """
        Create a new reasoning path — like creating a Git branch.
        
        Use this when the agent wants to explore an alternative approach
        without losing its current progress.
        
        Args:
            name: Name for the new branch
            from_checkpoint_id: Start from this checkpoint (default: current HEAD)
        
        Returns:
            The new Branch object
        
        Example:
            # Try a creative approach
            agent.branch("creative-solution")
            agent.checkpoint(state={"approach": "lateral_thinking"})
            
            # Didn't work? Go back to main
            agent.switch_branch("main")
        """
        if name in self._branches:
            logger.warning(f"Branch '{name}' already exists. Switching to it.")
            self._current_branch = name
            return self._branches[name]
        
        # Determine fork point
        current_branch = self._branches[self._current_branch]
        if from_checkpoint_id:
            fork_id = from_checkpoint_id
        elif current_branch.checkpoints:
            fork_id = current_branch.checkpoints[-1]
        else:
            fork_id = None
        
        # Create branch
        new_branch = Branch(
            name=name,
            parent_branch=self._current_branch,
            fork_checkpoint_id=fork_id,
        )
        
        # Copy checkpoints up to fork point
        if fork_id and fork_id in self._checkpoints:
            try:
                idx = current_branch.checkpoints.index(fork_id)
                new_branch.checkpoints = list(current_branch.checkpoints[:idx + 1])
            except ValueError:
                new_branch.checkpoints = [fork_id]
        
        self._branches[name] = new_branch
        self._current_branch = name
        self._metrics["total_branches"] += 1
        
        logger.info(f"Branch '{name}' created from '{current_branch.name}'")
        return new_branch
    
    def switch_branch(self, name: str) -> Branch:
        """Switch to a different reasoning branch."""
        if name not in self._branches:
            raise ValueError(f"Branch '{name}' does not exist.")
        self._current_branch = name
        logger.info(f"Switched to branch: {name}")
        return self._branches[name]
    
    def merge(self, source_branch: str, strategy: str = "prefer_higher_confidence") -> Checkpoint:
        """
        Merge insights from another branch into the current one.
        
        Strategies:
        - "prefer_higher_confidence": Keep the state with higher confidence score
        - "combine": Deep-merge both states together
        - "prefer_source": Take the source branch's state
        - "prefer_target": Keep the current branch's state (just mark as merged)
        """
        if source_branch not in self._branches:
            raise ValueError(f"Source branch '{source_branch}' not found.")
        
        source = self._branches[source_branch]
        target = self._branches[self._current_branch]
        
        if not source.checkpoints:
            raise ValueError(f"Source branch '{source_branch}' has no checkpoints.")
        
        source_cp = self._checkpoints[source.checkpoints[-1]]
        target_state = self.get_state() or {}
        
        # Merge strategies
        if strategy == "prefer_higher_confidence":
            source_conf = source_cp.metadata.get("confidence", 0)
            target_cp = self._checkpoints.get(
                target.checkpoints[-1] if target.checkpoints else ""
            )
            target_conf = target_cp.metadata.get("confidence", 0) if target_cp else 0
            merged_state = copy.deepcopy(
                source_cp.state if source_conf >= target_conf else target_state
            )
        elif strategy == "combine":
            merged_state = copy.deepcopy(target_state)
            merged_state.update(copy.deepcopy(source_cp.state))
        elif strategy == "prefer_source":
            merged_state = copy.deepcopy(source_cp.state)
        else:  # prefer_target
            merged_state = copy.deepcopy(target_state)
        
        # Create merge checkpoint
        merged_cp = self.checkpoint(
            state=merged_state,
            metadata={
                "merged_from": source_branch,
                "merge_strategy": strategy,
                "source_checkpoint": source_cp.id,
            },
            description=f"Merged '{source_branch}' into '{self._current_branch}'",
            logic_step=f"merge:{source_branch}",
        )
        
        logger.info(f"Merged '{source_branch}' into '{self._current_branch}'")
        return merged_cp
    
    def list_branches(self) -> List[Dict[str, Any]]:
        """List all branches with their status."""
        result = []
        for name, branch in self._branches.items():
            result.append({
                "name": name,
                "is_current": name == self._current_branch,
                "checkpoint_count": len(branch.checkpoints),
                "parent": branch.parent_branch,
                "is_active": branch.is_active,
            })
        return result
    
    # ── Recovery Operations ──
    
    def safe_execute(
        self,
        func: Callable,
        state: Dict[str, Any],
        description: str = "",
        max_retries: int = 3,
        fallback: Optional[Callable] = None,
    ) -> Tuple[Any, Checkpoint]:
        """
        Execute a function with automatic checkpointing and recovery.
        
        This is the "safety net" — wrap any agent operation in this, and
        AgentStateProtocol will automatically:
        1. Save a checkpoint before execution
        2. Try the operation
        3. If it fails, roll back and optionally retry or use a fallback
        
        Args:
            func: The function to execute (receives state as argument)
            state: Current agent state
            description: What this step does
            max_retries: How many times to retry on failure
            fallback: Alternative function to try if all retries fail
        
        Returns:
            Tuple of (result, checkpoint)
        
        Example:
            def analyze_data(state):
                # ... risky operation that might fail ...
                return {"analysis": result}
            
            result, cp = agent.safe_execute(
                func=analyze_data,
                state=current_state,
                description="Analyzing dataset",
                max_retries=3,
                fallback=simple_analysis
            )
        """
        # Save checkpoint before attempting
        cp = self.checkpoint(
            state=state,
            metadata={"operation": description, "status": "attempting"},
            description=f"Pre-execution: {description}",
            logic_step=description,
        )
        
        last_error = None
        for attempt in range(max_retries):
            try:
                result = func(copy.deepcopy(state))
                
                # Success! Save the result
                success_cp = self.checkpoint(
                    state=result if isinstance(result, dict) else {"result": result},
                    metadata={
                        "operation": description,
                        "status": "success",
                        "attempt": attempt + 1,
                    },
                    description=f"Completed: {description}",
                    logic_step=f"{description}:success",
                )
                
                # Update logic tree
                if success_cp.id in self._logic_tree.nodes:
                    self._logic_tree.nodes[success_cp.id].outcome = "success"
                
                return result, success_cp
                
            except Exception as e:
                last_error = e
                self._metrics["errors_caught"] += 1
                logger.warning(
                    f"Attempt {attempt + 1}/{max_retries} failed for '{description}': {e}"
                )
                
                # Record the failure
                self.checkpoint(
                    state={**state, "_error": str(e), "_attempt": attempt + 1},
                    metadata={
                        "operation": description,
                        "status": "failed",
                        "error": str(e),
                        "attempt": attempt + 1,
                    },
                    description=f"Failed (attempt {attempt + 1}): {description}",
                    logic_step=f"{description}:fail:{attempt + 1}",
                )
                
                # Roll back to pre-execution state
                self.rollback(to_checkpoint_id=cp.id)
                
                # Apply recovery strategies
                for strategy in self._recovery_strategies:
                    modified_state = strategy.apply(state, e, attempt)
                    if modified_state:
                        state = modified_state
                        break
        
        # All retries exhausted — try fallback
        if fallback:
            try:
                logger.info(f"Using fallback for '{description}'")
                self.branch(f"fallback-{cp.id[:8]}")
                result = fallback(copy.deepcopy(state))
                
                fallback_cp = self.checkpoint(
                    state=result if isinstance(result, dict) else {"result": result},
                    metadata={
                        "operation": description,
                        "status": "fallback_success",
                        "original_error": str(last_error),
                    },
                    description=f"Fallback succeeded: {description}",
                    logic_step=f"{description}:fallback",
                )
                
                self._metrics["total_recoveries"] += 1
                return result, fallback_cp
                
            except Exception as fallback_error:
                logger.error(f"Fallback also failed: {fallback_error}")
                self.switch_branch("main")
        
        # Nothing worked — raise the last error with context
        raise RuntimeError(
            f"Operation '{description}' failed after {max_retries} retries. "
            f"Last error: {last_error}. "
            f"Rolled back to checkpoint: {cp.id}"
        ) from last_error
    
    # ── History & Inspection ──
    
    def history(self, branch_name: Optional[str] = None, limit: int = 50) -> List[Dict[str, Any]]:
        """
        View the reasoning timeline — like `git log`.
        
        Returns a list of checkpoints with their states, metadata, and relationships.
        """
        branch = self._branches.get(branch_name or self._current_branch)
        if not branch:
            return []
        
        result = []
        for cp_id in reversed(branch.checkpoints[-limit:]):
            if cp_id in self._checkpoints:
                cp = self._checkpoints[cp_id]
                result.append({
                    "id": cp.id,
                    "hash": cp.hash,
                    "timestamp": cp.human_time,
                    "status": cp.status.value,
                    "branch": cp.branch_name,
                    "logic_path": cp.logic_path,
                    "metadata": cp.metadata,
                    "state_keys": list(cp.state.keys()),
                    "parent_id": cp.parent_id,
                })
        return result
    
    def diff(self, checkpoint_a: str, checkpoint_b: str) -> Dict[str, Any]:
        """
        Compare two checkpoints — like `git diff`.
        
        Shows what changed in the agent's state between two points in time.
        """
        cp_a = self._checkpoints.get(checkpoint_a)
        cp_b = self._checkpoints.get(checkpoint_b)
        
        if not cp_a or not cp_b:
            raise ValueError("One or both checkpoint IDs not found.")
        
        added = {}
        removed = {}
        modified = {}
        
        all_keys = set(list(cp_a.state.keys()) + list(cp_b.state.keys()))
        
        for key in all_keys:
            a_val = cp_a.state.get(key, "__MISSING__")
            b_val = cp_b.state.get(key, "__MISSING__")
            
            if a_val == "__MISSING__":
                added[key] = b_val
            elif b_val == "__MISSING__":
                removed[key] = a_val
            elif a_val != b_val:
                modified[key] = {"before": a_val, "after": b_val}
        
        return {
            "checkpoint_a": checkpoint_a,
            "checkpoint_b": checkpoint_b,
            "added": added,
            "removed": removed,
            "modified": modified,
            "unchanged_keys": [
                k for k in all_keys 
                if k not in added and k not in removed and k not in modified
            ],
        }
    
    def get_logic_tree(self) -> LogicTree:
        """Get the full reasoning decision tree."""
        return self._logic_tree
    
    def visualize_tree(self) -> str:
        """Get a text visualization of the logic tree."""
        return self._logic_tree.visualize()
    
    @property
    def metrics(self) -> Dict[str, Any]:
        """Get performance metrics."""
        return {
            **self._metrics,
            "current_branch": self._current_branch,
            "branches": list(self._branches.keys()),
            "checkpoints_in_memory": len(self._checkpoints),
        }
    
    # ── Serialization ──
    
    def export_session(self) -> Dict[str, Any]:
        """Export the entire session state (for persistence or transfer)."""
        return {
            "agent_name": self.agent_name,
            "created_at": self.created_at,
            "current_branch": self._current_branch,
            "checkpoints": {
                cid: cp.to_dict() for cid, cp in self._checkpoints.items()
            },
            "branches": {
                name: branch.to_dict() for name, branch in self._branches.items()
            },
            "logic_tree": self._logic_tree.to_dict(),
            "metrics": self._metrics,
        }
    
    @classmethod
    def import_session(cls, data: Dict[str, Any]) -> "AgentStateProtocol":
        """Restore a session from exported data."""
        agent = cls(data["agent_name"])
        agent.created_at = data["created_at"]
        agent._current_branch = data["current_branch"]
        agent._metrics = data["metrics"]
        
        for cid, cp_data in data["checkpoints"].items():
            agent._checkpoints[cid] = Checkpoint.from_dict(cp_data)
        
        for name, branch_data in data["branches"].items():
            agent._branches[name] = Branch(**branch_data)
        
        return agent
    
    # ── Internal ──
    
    def _enforce_limits(self):
        """Remove oldest checkpoints if we exceed the max."""
        if len(self._checkpoints) > self.max_checkpoints:
            # Find oldest committed/rolled-back checkpoints to remove
            removable = sorted(
                [
                    (cid, cp) for cid, cp in self._checkpoints.items()
                    if cp.status in (CheckpointStatus.COMMITTED, CheckpointStatus.ROLLED_BACK)
                ],
                key=lambda x: x[1].timestamp,
            )
            
            to_remove = len(self._checkpoints) - self.max_checkpoints
            for cid, _ in removable[:to_remove]:
                del self._checkpoints[cid]
    
    def __repr__(self) -> str:
        branch = self._branches[self._current_branch]
        return (
            f"AgentStateProtocol('{self.agent_name}', "
            f"branch='{self._current_branch}', "
            f"checkpoints={len(branch.checkpoints)}, "
            f"branches={len(self._branches)})"
        )



