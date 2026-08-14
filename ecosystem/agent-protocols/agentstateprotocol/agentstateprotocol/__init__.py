"""
AgentStateProtocol package.

Checkpointing and recovery protocol for AI agents.
"""

__version__ = "0.1.0"
__author__ = "AgentStateProtocol Contributors"

from .engine import AgentStateProtocol, Checkpoint, Branch, LogicTree
from .strategies import RecoveryStrategy, RetryWithBackoff, AlternativePathStrategy
from .serializers import StateSerializer, JSONSerializer, PickleSerializer
from .storage import StorageBackend, FileSystemStorage, SQLiteStorage

__all__ = [
    "AgentStateProtocol",
    "Checkpoint",
    "Branch",
    "LogicTree",
    "RecoveryStrategy",
    "RetryWithBackoff",
    "AlternativePathStrategy",
    "StateSerializer",
    "JSONSerializer",
    "PickleSerializer",
    "StorageBackend",
    "FileSystemStorage",
    "SQLiteStorage",
]
