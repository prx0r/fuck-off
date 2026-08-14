"""
Recovery Strategies for agentstateprotocol
=================================

When an agent hits an error, these strategies determine HOW to recover.

Think of them as "playbooks" for different types of failures:

- RetryWithBackoff: "Wait a bit, then try again" (good for API timeouts)
- AlternativePathStrategy: "Try a completely different approach" (good for logic errors)
- DegradeGracefully: "Give a simpler answer" (good for resource limits)
"""

import time
import random
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

logger = logging.getLogger("agentstateprotocol.strategies")


class RecoveryStrategy(ABC):
    """
    Base class for recovery strategies.
    
    Each strategy answers: "Given this error, how should the agent modify
    its state before trying again?"
    """
    
    @abstractmethod
    def apply(
        self,
        state: Dict[str, Any],
        error: Exception,
        attempt: int,
    ) -> Optional[Dict[str, Any]]:
        """
        Apply the recovery strategy.
        
        Args:
            state: The agent's state when the error occurred
            error: The exception that was raised
            attempt: Which retry attempt this is (0-indexed)
        
        Returns:
            Modified state to retry with, or None if this strategy doesn't apply
        """
        pass
    
    @abstractmethod
    def can_handle(self, error: Exception) -> bool:
        """Check if this strategy can handle the given error type."""
        pass


class RetryWithBackoff(RecoveryStrategy):
    """
    "Wait a bit, then try again" — with exponential backoff.
    
    Perfect for transient errors like:
    - API rate limits (429 errors)
    - Network timeouts
    - Temporary service outages
    
    How it works:
    - 1st retry: wait 1 second
    - 2nd retry: wait 2 seconds
    - 3rd retry: wait 4 seconds
    - ... and so on, up to a maximum wait time
    
    Plus a random "jitter" so multiple agents don't all retry at the same moment.
    """
    
    def __init__(
        self,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        jitter: bool = True,
        error_types: Optional[tuple] = None,
    ):
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.jitter = jitter
        self.error_types = error_types or (
            TimeoutError, ConnectionError, OSError,
        )
    
    def can_handle(self, error: Exception) -> bool:
        return isinstance(error, self.error_types)
    
    def apply(
        self,
        state: Dict[str, Any],
        error: Exception,
        attempt: int,
    ) -> Optional[Dict[str, Any]]:
        if not self.can_handle(error):
            return None
        
        delay = min(self.base_delay * (2 ** attempt), self.max_delay)
        if self.jitter:
            delay *= (0.5 + random.random())
        
        logger.info(f"RetryWithBackoff: waiting {delay:.1f}s before retry #{attempt + 1}")
        time.sleep(delay)
        
        # Return state with retry metadata
        state["_retry_metadata"] = {
            "strategy": "backoff",
            "attempt": attempt + 1,
            "delay_applied": delay,
        }
        return state


class AlternativePathStrategy(RecoveryStrategy):
    """
    "Try a different approach" — when the current logic path hits a dead end.
    
    This is like a chess player who realizes a move doesn't work and
    switches to a completely different strategy.
    
    You provide alternative approaches as functions, and this strategy
    will cycle through them on each retry.
    """
    
    def __init__(
        self,
        alternatives: Optional[list] = None,
        state_modifiers: Optional[Dict[str, Any]] = None,
    ):
        """
        Args:
            alternatives: List of callables that modify state for alternative paths
            state_modifiers: Dict of key-value pairs to inject into state on retry
        """
        self.alternatives = alternatives or []
        self.state_modifiers = state_modifiers or {}
    
    def can_handle(self, error: Exception) -> bool:
        return True  # Can always try an alternative
    
    def apply(
        self,
        state: Dict[str, Any],
        error: Exception,
        attempt: int,
    ) -> Optional[Dict[str, Any]]:
        # Apply state modifiers
        for key, value in self.state_modifiers.items():
            state[key] = value
        
        # Try alternative functions
        if self.alternatives and attempt < len(self.alternatives):
            try:
                modified = self.alternatives[attempt](state, error)
                if modified:
                    return modified
            except Exception as e:
                logger.warning(f"Alternative path {attempt} failed: {e}")
        
        state["_alternative_path"] = {
            "attempt": attempt + 1,
            "original_error": str(error),
        }
        return state


class DegradeGracefully(RecoveryStrategy):
    """
    "Give a simpler answer" — reduce complexity when resources are limited.
    
    Like a website that drops from HD video to SD when bandwidth is low.
    
    Configuration:
    - degradation_levels: List of state modifications, from least to most degraded
    """
    
    def __init__(
        self,
        degradation_levels: Optional[list] = None,
        error_types: Optional[tuple] = None,
    ):
        self.degradation_levels = degradation_levels or [
            {"_quality": "reduced", "_max_tokens": 500},
            {"_quality": "minimal", "_max_tokens": 100},
            {"_quality": "fallback", "_use_cache": True},
        ]
        self.error_types = error_types or (
            MemoryError, TimeoutError, RuntimeError,
        )
    
    def can_handle(self, error: Exception) -> bool:
        return isinstance(error, self.error_types)
    
    def apply(
        self,
        state: Dict[str, Any],
        error: Exception,
        attempt: int,
    ) -> Optional[Dict[str, Any]]:
        if not self.can_handle(error):
            return None
        
        level = min(attempt, len(self.degradation_levels) - 1)
        degradation = self.degradation_levels[level]
        
        logger.info(f"Degrading to level {level}: {degradation}")
        state.update(degradation)
        state["_degradation_metadata"] = {
            "level": level,
            "reason": str(error),
        }
        return state


class CompositeStrategy(RecoveryStrategy):
    """
    Combine multiple strategies — try them in order until one works.
    
    Like a doctor trying treatments from most specific to most general.
    """
    
    def __init__(self, strategies: list):
        self.strategies = strategies
    
    def can_handle(self, error: Exception) -> bool:
        return any(s.can_handle(error) for s in self.strategies)
    
    def apply(
        self,
        state: Dict[str, Any],
        error: Exception,
        attempt: int,
    ) -> Optional[Dict[str, Any]]:
        for strategy in self.strategies:
            if strategy.can_handle(error):
                result = strategy.apply(state, error, attempt)
                if result is not None:
                    return result
        return None
