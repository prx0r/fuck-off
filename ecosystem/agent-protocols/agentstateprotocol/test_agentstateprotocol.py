"""
Test Suite for AgentStateProtocol
========================
Comprehensive tests covering all core functionality.
"""

import pytest
import time
import json
import tempfile
import shutil
from pathlib import Path

# Add parent to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from agentstateprotocol.engine import AgentStateProtocol, Checkpoint, Branch, LogicTree, CheckpointStatus
from agentstateprotocol.strategies import (
    RetryWithBackoff, AlternativePathStrategy, 
    DegradeGracefully, CompositeStrategy,
)
from agentstateprotocol.serializers import JSONSerializer, PickleSerializer, CompressedSerializer
from agentstateprotocol.storage import FileSystemStorage, SQLiteStorage, InMemoryStorage
from agentstateprotocol.decorators import agentstateprotocol_step, get_agent, register_agent


# ── Fixtures ──

@pytest.fixture
def agent():
    return AgentStateProtocol("test-agent")


@pytest.fixture
def agent_with_checkpoints(agent):
    agent.checkpoint(
        state={"step": "init", "data": "hello"},
        metadata={"confidence": 0.5},
        description="Initialization",
        logic_step="init",
    )
    agent.checkpoint(
        state={"step": "process", "data": "world"},
        metadata={"confidence": 0.8},
        description="Processing",
        logic_step="process",
    )
    agent.checkpoint(
        state={"step": "analyze", "data": "result"},
        metadata={"confidence": 0.95},
        description="Analysis",
        logic_step="analyze",
    )
    return agent


@pytest.fixture
def tmp_dir():
    d = tempfile.mkdtemp()
    yield d
    shutil.rmtree(d, ignore_errors=True)


# ── Core Engine Tests ──

class TestCheckpoint:
    def test_create_checkpoint(self, agent):
        cp = agent.checkpoint(state={"key": "value"})
        assert cp.id is not None
        assert cp.hash != ""
        assert cp.state == {"key": "value"}
        assert cp.branch_name == "main"
    
    def test_checkpoint_hash_consistency(self, agent):
        cp1 = agent.checkpoint(state={"a": 1, "b": 2})
        cp2 = agent.checkpoint(state={"a": 1, "b": 2})
        assert cp1.hash == cp2.hash  # Same content = same hash
    
    def test_checkpoint_with_metadata(self, agent):
        cp = agent.checkpoint(
            state={"reasoning": "analyzing"},
            metadata={"confidence": 0.87, "step": "analysis"},
        )
        assert cp.metadata["confidence"] == 0.87
    
    def test_checkpoint_logic_path(self, agent):
        agent.checkpoint(state={}, logic_step="step1")
        cp2 = agent.checkpoint(state={}, logic_step="step2")
        assert cp2.logic_path == ["step1", "step2"]
    
    def test_checkpoint_serialization(self):
        cp = Checkpoint(
            state={"test": True},
            metadata={"score": 0.5},
            status=CheckpointStatus.ACTIVE,
        )
        d = cp.to_dict()
        restored = Checkpoint.from_dict(d)
        assert restored.state == cp.state
        assert restored.status == cp.status


class TestRollback:
    def test_rollback_one_step(self, agent_with_checkpoints):
        agent = agent_with_checkpoints
        rolled = agent.rollback()
        assert rolled is not None
        state = agent.get_state()
        assert state["step"] == "process"
    
    def test_rollback_multiple_steps(self, agent_with_checkpoints):
        agent = agent_with_checkpoints
        rolled = agent.rollback(steps=2)
        state = agent.get_state()
        assert state["step"] == "init"
    
    def test_rollback_to_specific_checkpoint(self, agent):
        cp1 = agent.checkpoint(state={"version": 1})
        cp2 = agent.checkpoint(state={"version": 2})
        cp3 = agent.checkpoint(state={"version": 3})
        
        agent.rollback(to_checkpoint_id=cp1.id)
        state = agent.get_state()
        assert state["version"] == 1
    
    def test_rollback_empty_branch(self, agent):
        result = agent.rollback()
        assert result is None
    
    def test_rollback_updates_metrics(self, agent_with_checkpoints):
        agent = agent_with_checkpoints
        agent.rollback()
        assert agent.metrics["total_rollbacks"] == 1


class TestBranching:
    def test_create_branch(self, agent_with_checkpoints):
        agent = agent_with_checkpoints
        branch = agent.branch("experiment")
        assert branch.name == "experiment"
        assert branch.parent_branch == "main"
    
    def test_switch_branch(self, agent):
        agent.checkpoint(state={"main": True})
        agent.branch("alt")
        agent.checkpoint(state={"alt": True})
        
        agent.switch_branch("main")
        state = agent.get_state()
        assert "main" in state
    
    def test_branch_isolation(self, agent):
        agent.checkpoint(state={"shared": True})
        
        # Create branch from current point
        agent.branch("isolated")
        agent.checkpoint(state={"isolated": True, "shared": True})
        
        # Switch back to main
        agent.switch_branch("main")
        cp_main = agent.checkpoint(state={"main_only": True, "shared": True})
        
        # Main branch should not have isolated data
        state = agent.get_state()
        assert "isolated" not in state
    
    def test_list_branches(self, agent_with_checkpoints):
        agent = agent_with_checkpoints
        agent.branch("feature-1")
        agent.branch("feature-2")
        
        branches = agent.list_branches()
        names = [b["name"] for b in branches]
        assert "main" in names
        assert "feature-1" in names
        assert "feature-2" in names
    
    def test_invalid_branch_switch(self, agent):
        with pytest.raises(ValueError):
            agent.switch_branch("nonexistent")


class TestMerge:
    def test_merge_prefer_higher_confidence(self, agent):
        agent.checkpoint(
            state={"answer": "A"},
            metadata={"confidence": 0.6},
        )
        
        agent.branch("better")
        agent.checkpoint(
            state={"answer": "B"},
            metadata={"confidence": 0.9},
        )
        
        agent.switch_branch("main")
        merged = agent.merge("better", strategy="prefer_higher_confidence")
        state = agent.get_state()
        assert state["answer"] == "B"
    
    def test_merge_combine(self, agent):
        agent.checkpoint(state={"key1": "val1"})
        
        agent.branch("extra")
        agent.checkpoint(state={"key2": "val2"})
        
        agent.switch_branch("main")
        agent.merge("extra", strategy="combine")
        state = agent.get_state()
        assert "key1" in state
        assert "key2" in state


class TestSafeExecute:
    def test_successful_execution(self, agent):
        def good_func(state):
            return {"result": state["input"] * 2}
        
        result, cp = agent.safe_execute(
            func=good_func,
            state={"input": 5},
            description="double_input",
        )
        assert result["result"] == 10
    
    def test_retry_on_failure(self, agent):
        call_count = 0
        
        def flaky_func(state):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("Not ready yet")
            return {"success": True}
        
        result, cp = agent.safe_execute(
            func=flaky_func,
            state={},
            description="flaky_operation",
            max_retries=3,
        )
        assert result["success"] is True
        assert call_count == 3
    
    def test_fallback_execution(self, agent):
        def always_fails(state):
            raise RuntimeError("Nope")
        
        def fallback(state):
            return {"fallback": True}
        
        result, cp = agent.safe_execute(
            func=always_fails,
            state={},
            description="failing_op",
            max_retries=2,
            fallback=fallback,
        )
        assert result["fallback"] is True
    
    def test_all_retries_exhausted(self, agent):
        def always_fails(state):
            raise RuntimeError("Always fails")
        
        with pytest.raises(RuntimeError, match="failed after"):
            agent.safe_execute(
                func=always_fails,
                state={},
                description="doomed",
                max_retries=2,
            )


# ── Logic Tree Tests ──

class TestLogicTree:
    def test_tree_building(self, agent_with_checkpoints):
        tree = agent_with_checkpoints.get_logic_tree()
        assert tree.root_id is not None
        assert len(tree.nodes) == 3
    
    def test_tree_visualization(self, agent_with_checkpoints):
        viz = agent_with_checkpoints.visualize_tree()
        assert "init" in viz.lower() or len(viz) > 0
    
    def test_path_to_root(self, agent_with_checkpoints):
        tree = agent_with_checkpoints.get_logic_tree()
        # Get the last node
        last_node_id = list(tree.nodes.keys())[-1]
        path = tree.get_path_to_root(last_node_id)
        assert len(path) >= 1


# ── History & Diff Tests ──

class TestHistoryAndDiff:
    def test_history(self, agent_with_checkpoints):
        history = agent_with_checkpoints.history()
        assert len(history) == 3
        # History is reverse chronological
        assert history[0]["logic_path"][-1] == "analyze"
    
    def test_diff(self, agent):
        cp1 = agent.checkpoint(state={"a": 1, "b": 2})
        cp2 = agent.checkpoint(state={"a": 1, "b": 3, "c": 4})
        
        diff = agent.diff(cp1.id, cp2.id)
        assert "c" in diff["added"]
        assert "b" in diff["modified"]
        assert diff["modified"]["b"]["before"] == 2
        assert diff["modified"]["b"]["after"] == 3


# ── Serializer Tests ──

class TestSerializers:
    def test_json_serializer(self):
        s = JSONSerializer()
        state = {"key": "value", "nested": {"a": [1, 2, 3]}}
        data = s.serialize(state)
        restored = s.deserialize(data)
        assert restored == state
    
    def test_pickle_serializer(self):
        s = PickleSerializer()
        state = {"key": "value", "set_data": {1, 2, 3}}
        data = s.serialize(state)
        restored = s.deserialize(data)
        assert restored["set_data"] == {1, 2, 3}
    
    def test_compressed_serializer(self):
        s = CompressedSerializer()
        state = {"big_data": "x" * 10000}
        data = s.serialize(state)
        assert len(data) < 10000  # Should be compressed
        restored = s.deserialize(data)
        assert restored == state
    
    def test_hash_consistency(self):
        s = JSONSerializer()
        state = {"a": 1, "b": 2}
        h1 = s.get_hash(state)
        h2 = s.get_hash(state)
        assert h1 == h2


# ── Storage Backend Tests ──

class TestFileSystemStorage:
    def test_save_and_load(self, tmp_dir):
        storage = FileSystemStorage(base_path=f"{tmp_dir}/.agentstateprotocol")
        agent = AgentStateProtocol("test", storage_backend=storage)
        
        cp = agent.checkpoint(state={"saved": True})
        loaded = storage.load_checkpoint(cp.id)
        assert loaded is not None
        assert loaded.state["saved"] is True
    
    def test_list_checkpoints(self, tmp_dir):
        storage = FileSystemStorage(base_path=f"{tmp_dir}/.agentstateprotocol")
        agent = AgentStateProtocol("test", storage_backend=storage)
        
        agent.checkpoint(state={"v": 1})
        agent.checkpoint(state={"v": 2})
        
        listed = storage.list_checkpoints()
        assert len(listed) == 2


class TestSQLiteStorage:
    def test_save_and_load(self, tmp_dir):
        storage = SQLiteStorage(db_path=f"{tmp_dir}/test.db")
        agent = AgentStateProtocol("test", storage_backend=storage)
        
        cp = agent.checkpoint(state={"stored": True})
        loaded = storage.load_checkpoint(cp.id)
        assert loaded is not None
        assert loaded.state["stored"] is True
    
    def test_query_by_branch(self, tmp_dir):
        storage = SQLiteStorage(db_path=f"{tmp_dir}/test.db")
        agent = AgentStateProtocol("test", storage_backend=storage)
        
        agent.checkpoint(state={"branch": "main"})
        agent.branch("feature")
        agent.checkpoint(state={"branch": "feature"})
        
        main_cps = storage.list_checkpoints(branch="main")
        feature_cps = storage.list_checkpoints(branch="feature")
        assert len(main_cps) >= 1


# ── Recovery Strategy Tests ──

class TestStrategies:
    def test_retry_with_backoff(self):
        strategy = RetryWithBackoff(base_delay=0.01, max_delay=0.1)
        assert strategy.can_handle(TimeoutError())
        assert not strategy.can_handle(ValueError())
        
        result = strategy.apply({"key": "val"}, TimeoutError(), attempt=0)
        assert result is not None
        assert "_retry_metadata" in result
    
    def test_alternative_path(self):
        def modifier(state, error):
            state["approach"] = "alternative"
            return state
        
        strategy = AlternativePathStrategy(alternatives=[modifier])
        result = strategy.apply({"key": "val"}, RuntimeError(), attempt=0)
        assert result["approach"] == "alternative"
    
    def test_degrade_gracefully(self):
        strategy = DegradeGracefully()
        result = strategy.apply({"key": "val"}, MemoryError(), attempt=0)
        assert result["_quality"] == "reduced"
    
    def test_composite_strategy(self):
        composite = CompositeStrategy([
            RetryWithBackoff(base_delay=0.01),
            DegradeGracefully(),
        ])
        assert composite.can_handle(TimeoutError())
        assert composite.can_handle(MemoryError())


# ── Session Export/Import Tests ──

class TestSessionPersistence:
    def test_export_import(self, agent_with_checkpoints):
        agent = agent_with_checkpoints
        
        exported = agent.export_session()
        restored = AgentStateProtocol.import_session(exported)
        
        assert restored.agent_name == agent.agent_name
        assert len(restored.history()) == len(agent.history())


# ── Decorator Tests ──

class TestDecorators:
    def test_agentstateprotocol_step_decorator(self):
        register_agent("test-dec", AgentStateProtocol("test-dec"))
        
        @agentstateprotocol_step("my_step", agent_name="test-dec")
        def my_func(state):
            return {"output": state.get("input", 0) + 1}
        
        result = my_func({"input": 5})
        assert result["output"] == 6
        
        agent = get_agent("test-dec")
        assert agent.metrics["total_checkpoints"] >= 2


# ── Metrics Tests ──

class TestMetrics:
    def test_metrics_tracking(self, agent):
        agent.checkpoint(state={"v": 1})
        agent.checkpoint(state={"v": 2})
        agent.rollback()
        agent.branch("test")
        
        m = agent.metrics
        assert m["total_checkpoints"] == 2
        assert m["total_rollbacks"] == 1
        assert m["total_branches"] == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])


