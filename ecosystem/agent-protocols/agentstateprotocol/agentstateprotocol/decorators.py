"""
Decorators and framework integrations for AgentStateProtocol.
"""

import functools
import logging
import time
from typing import Callable, Dict

from .engine import AgentStateProtocol

logger = logging.getLogger("agentstateprotocol.decorators")

_agent_registry: Dict[str, AgentStateProtocol] = {}


def get_agent(name: str = "default") -> AgentStateProtocol:
    """Get or create a named AgentStateProtocol instance."""
    if name not in _agent_registry:
        _agent_registry[name] = AgentStateProtocol(name)
    return _agent_registry[name]


def register_agent(name: str, agent: AgentStateProtocol) -> None:
    """Register an AgentStateProtocol instance for use with decorators."""
    _agent_registry[name] = agent


def agentstateprotocol_step(
    step_name: str,
    agent_name: str = "default",
    auto_rollback: bool = True,
    max_retries: int = 1,
):
    """Decorator that wraps a function with automatic checkpointing."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            agent = get_agent(agent_name)

            state = {}
            if args and isinstance(args[0], dict):
                state = args[0]
            elif "state" in kwargs:
                state = kwargs["state"]

            pre_cp = agent.checkpoint(
                state=state,
                metadata={"step": step_name, "phase": "pre_execution"},
                description=f"Before: {step_name}",
                logic_step=step_name,
            )

            last_error = None
            for attempt in range(max_retries):
                try:
                    start = time.time()
                    result = func(*args, **kwargs)
                    elapsed = time.time() - start

                    result_state = result if isinstance(result, dict) else {"result": result}
                    agent.checkpoint(
                        state=result_state,
                        metadata={
                            "step": step_name,
                            "phase": "post_execution",
                            "duration_ms": round(elapsed * 1000, 2),
                            "attempt": attempt + 1,
                        },
                        description=f"After: {step_name}",
                        logic_step=f"{step_name}:done",
                    )
                    return result
                except Exception as exc:
                    last_error = exc
                    logger.warning(
                        "Step '%s' failed (attempt %s): %s",
                        step_name,
                        attempt + 1,
                        exc,
                    )
                    if auto_rollback:
                        agent.rollback(to_checkpoint_id=pre_cp.id)

            raise last_error

        return wrapper

    return decorator


def checkpoint_context(agent_name: str = "default", description: str = ""):
    """Context manager for checkpointing a block of code."""

    class CheckpointContext:
        def __init__(self):
            self.agent = get_agent(agent_name)
            self.state = {}
            self._pre_cp = None

        def __enter__(self):
            self._pre_cp = self.agent.checkpoint(
                state={},
                description=f"Context start: {description}",
                logic_step=description,
            )
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                logger.warning("Context '%s' failed: %s", description, exc_val)
                self.agent.rollback(to_checkpoint_id=self._pre_cp.id)
                return False

            if self.state:
                self.agent.checkpoint(
                    state=self.state,
                    description=f"Context complete: {description}",
                    logic_step=f"{description}:done",
                )
            return False

    return CheckpointContext()


class AgentStateProtocolMiddleware:
    """Middleware wrapper for frameworks like LangChain, CrewAI, and AutoGen."""

    def __init__(self, agent_name: str, **kwargs):
        self.agent = AgentStateProtocol(agent_name, **kwargs)
        register_agent(agent_name, self.agent)

    def wrap(self, func: Callable, step_name: str = "") -> Callable:
        """Wrap a function with checkpointing."""
        name = step_name or getattr(func, "__name__", "unnamed_step")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            state = {}
            if args and isinstance(args[0], dict):
                state = args[0]

            result, _cp = self.agent.safe_execute(
                func=lambda s: func(*args, **kwargs),
                state=state,
                description=name,
            )
            return result

        return wrapper

    def get_history(self) -> list:
        return self.agent.history()

    def get_tree(self) -> str:
        return self.agent.visualize_tree()
