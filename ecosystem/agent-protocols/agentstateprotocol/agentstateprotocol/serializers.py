"""
Serializers for agentstateprotocol
=========================

Serializers convert agent state (Python objects) into formats that can be
saved to disk, sent over a network, or stored in a database.

Think of them as "translators" between the agent's brain and storage:

- JSONSerializer: Human-readable, great for debugging (like saving a diary)
- PickleSerializer: Compact binary, preserves complex Python objects (like a brain scan)
- CompressedSerializer: Adds compression for large states (like zipping a file)
"""

import json
import gzip
import pickle
import hashlib
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from datetime import datetime

logger = logging.getLogger("agentstateprotocol.serializers")


class StateSerializer(ABC):
    """Base class for state serializers."""
    
    @abstractmethod
    def serialize(self, state: Dict[str, Any]) -> bytes:
        """Convert state dict to bytes."""
        pass
    
    @abstractmethod
    def deserialize(self, data: bytes) -> Dict[str, Any]:
        """Convert bytes back to state dict."""
        pass
    
    def get_hash(self, state: Dict[str, Any]) -> str:
        """Generate a content hash for integrity verification."""
        serialized = self.serialize(state)
        return hashlib.sha256(serialized).hexdigest()[:16]


class JSONSerializer(StateSerializer):
    """
    Human-readable JSON serialization.
    
    Pros: Easy to inspect, debug, and version control
    Cons: Larger file size, can't handle all Python types
    
    Best for: Development, debugging, small-to-medium states
    """
    
    def __init__(self, indent: int = 2, sort_keys: bool = True):
        self.indent = indent
        self.sort_keys = sort_keys
    
    def serialize(self, state: Dict[str, Any]) -> bytes:
        try:
            return json.dumps(
                state,
                indent=self.indent,
                sort_keys=self.sort_keys,
                default=self._default_handler,
            ).encode("utf-8")
        except (TypeError, ValueError) as e:
            logger.error(f"JSON serialization failed: {e}")
            # Fallback: convert non-serializable values to strings
            safe_state = self._make_json_safe(state)
            return json.dumps(safe_state, indent=self.indent).encode("utf-8")
    
    def deserialize(self, data: bytes) -> Dict[str, Any]:
        return json.loads(data.decode("utf-8"))
    
    def _default_handler(self, obj):
        """Handle non-JSON-serializable types."""
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, bytes):
            return obj.hex()
        if isinstance(obj, set):
            return list(obj)
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return str(obj)
    
    def _make_json_safe(self, obj, depth=0):
        """Recursively convert non-serializable values to strings."""
        if depth > 50:
            return str(obj)
        if isinstance(obj, dict):
            return {str(k): self._make_json_safe(v, depth + 1) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [self._make_json_safe(item, depth + 1) for item in obj]
        if isinstance(obj, (str, int, float, bool, type(None))):
            return obj
        return str(obj)


class PickleSerializer(StateSerializer):
    """
    Binary Python serialization using pickle.
    
    Pros: Handles ANY Python object, compact format
    Cons: Not human-readable, Python-version sensitive, security risk with untrusted data
    
    Best for: Production, complex states with custom objects
    
    ⚠️ WARNING: Only use with trusted data. Pickle can execute arbitrary code.
    """
    
    def __init__(self, protocol: int = pickle.HIGHEST_PROTOCOL):
        self.protocol = protocol
    
    def serialize(self, state: Dict[str, Any]) -> bytes:
        return pickle.dumps(state, protocol=self.protocol)
    
    def deserialize(self, data: bytes) -> Dict[str, Any]:
        return pickle.loads(data)


class CompressedSerializer(StateSerializer):
    """
    Compression wrapper — adds gzip compression to any serializer.
    
    Reduces storage size by 60-90% for typical agent states.
    
    Best for: Large states, resource-constrained environments
    """
    
    def __init__(
        self,
        inner_serializer: Optional[StateSerializer] = None,
        compression_level: int = 6,
    ):
        self.inner = inner_serializer or JSONSerializer(indent=0)
        self.level = compression_level
    
    def serialize(self, state: Dict[str, Any]) -> bytes:
        raw = self.inner.serialize(state)
        return gzip.compress(raw, compresslevel=self.level)
    
    def deserialize(self, data: bytes) -> Dict[str, Any]:
        raw = gzip.decompress(data)
        return self.inner.deserialize(raw)
