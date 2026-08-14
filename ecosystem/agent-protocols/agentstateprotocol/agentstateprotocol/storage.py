"""
Storage Backends for agentstateprotocol
==============================

Storage backends handle WHERE and HOW agent checkpoints are persisted.

Think of them as different "filing cabinets" for the agent's memories:

- FileSystemStorage: Saves checkpoints as files on disk (simple, like folders)
- SQLiteStorage: Uses a database (fast queries, great for history search)
- InMemoryStorage: RAM only, no persistence (fast, for testing)
"""

import os
import json
import sqlite3
import logging
import shutil
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pathlib import Path

logger = logging.getLogger("agentstateprotocol.storage")


class StorageBackend(ABC):
    """Base class for storage backends."""
    
    @abstractmethod
    def save_checkpoint(self, checkpoint) -> None:
        """Persist a checkpoint."""
        pass
    
    @abstractmethod
    def load_checkpoint(self, checkpoint_id: str):
        """Load a checkpoint by ID."""
        pass
    
    @abstractmethod
    def list_checkpoints(
        self, branch: Optional[str] = None, limit: int = 100
    ) -> List[Dict[str, Any]]:
        """List stored checkpoints."""
        pass
    
    @abstractmethod
    def delete_checkpoint(self, checkpoint_id: str) -> bool:
        """Delete a checkpoint."""
        pass
    
    @abstractmethod
    def save_session(self, session_data: Dict[str, Any]) -> None:
        """Save full session state."""
        pass
    
    @abstractmethod
    def load_session(self) -> Optional[Dict[str, Any]]:
        """Load full session state."""
        pass


class FileSystemStorage(StorageBackend):
    """
    File-based storage — each checkpoint is a JSON file.
    
    Directory structure:
        .agentstateprotocol/
        ├── session.json          # Full session metadata
        ├── checkpoints/
        │   ├── abc123.json       # Individual checkpoint files
        │   ├── def456.json
        │   └── ...
        └── branches/
            ├── main.json
            └── creative.json
    
    Best for: Development, debugging (you can inspect files directly)
    """
    
    def __init__(self, base_path: str = ".agentstateprotocol"):
        self.base_path = Path(base_path)
        self.checkpoints_dir = self.base_path / "checkpoints"
        self.branches_dir = self.base_path / "branches"
        
        # Create directories
        self.checkpoints_dir.mkdir(parents=True, exist_ok=True)
        self.branches_dir.mkdir(parents=True, exist_ok=True)
    
    def save_checkpoint(self, checkpoint) -> None:
        filepath = self.checkpoints_dir / f"{checkpoint.id}.json"
        with open(filepath, "w") as f:
            json.dump(checkpoint.to_dict(), f, indent=2, default=str)
        logger.debug(f"Checkpoint saved: {filepath}")
    
    def load_checkpoint(self, checkpoint_id: str):
        from .engine import Checkpoint
        filepath = self.checkpoints_dir / f"{checkpoint_id}.json"
        if not filepath.exists():
            return None
        with open(filepath) as f:
            data = json.load(f)
        return Checkpoint.from_dict(data)
    
    def list_checkpoints(
        self, branch: Optional[str] = None, limit: int = 100
    ) -> List[Dict[str, Any]]:
        checkpoints = []
        for filepath in sorted(
            self.checkpoints_dir.glob("*.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )[:limit]:
            with open(filepath) as f:
                data = json.load(f)
            if branch is None or data.get("branch_name") == branch:
                checkpoints.append(data)
        return checkpoints
    
    def delete_checkpoint(self, checkpoint_id: str) -> bool:
        filepath = self.checkpoints_dir / f"{checkpoint_id}.json"
        if filepath.exists():
            filepath.unlink()
            return True
        return False
    
    def save_session(self, session_data: Dict[str, Any]) -> None:
        filepath = self.base_path / "session.json"
        with open(filepath, "w") as f:
            json.dump(session_data, f, indent=2, default=str)
    
    def load_session(self) -> Optional[Dict[str, Any]]:
        filepath = self.base_path / "session.json"
        if filepath.exists():
            with open(filepath) as f:
                return json.load(f)
        return None
    
    def clear(self) -> None:
        """Delete all stored data."""
        if self.base_path.exists():
            shutil.rmtree(self.base_path)
        self.checkpoints_dir.mkdir(parents=True, exist_ok=True)
        self.branches_dir.mkdir(parents=True, exist_ok=True)


class SQLiteStorage(StorageBackend):
    """
    SQLite-based storage — fast queries, great for searching history.
    
    Uses a single .db file with tables for checkpoints, branches, and sessions.
    
    Best for: Production, large numbers of checkpoints, complex queries
    """
    
    def __init__(self, db_path: str = ".agentstateprotocol/agentstateprotocol.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
        self._init_db()
    
    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS checkpoints (
                    id TEXT PRIMARY KEY,
                    timestamp REAL,
                    branch_name TEXT,
                    parent_id TEXT,
                    status TEXT,
                    hash TEXT,
                    state_json TEXT,
                    metadata_json TEXT,
                    logic_path_json TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_data TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_cp_branch 
                ON checkpoints(branch_name)
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_cp_timestamp 
                ON checkpoints(timestamp DESC)
            """)
    
    def save_checkpoint(self, checkpoint) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO checkpoints 
                (id, timestamp, branch_name, parent_id, status, hash,
                 state_json, metadata_json, logic_path_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    checkpoint.id,
                    checkpoint.timestamp,
                    checkpoint.branch_name,
                    checkpoint.parent_id,
                    checkpoint.status.value,
                    checkpoint.hash,
                    json.dumps(checkpoint.state, default=str),
                    json.dumps(checkpoint.metadata, default=str),
                    json.dumps(checkpoint.logic_path),
                ),
            )
    
    def load_checkpoint(self, checkpoint_id: str):
        from .engine import Checkpoint, CheckpointStatus
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM checkpoints WHERE id = ?", (checkpoint_id,)
            ).fetchone()
        
        if not row:
            return None
        
        return Checkpoint(
            id=row["id"],
            timestamp=row["timestamp"],
            branch_name=row["branch_name"],
            parent_id=row["parent_id"],
            status=CheckpointStatus(row["status"]),
            hash=row["hash"],
            state=json.loads(row["state_json"]),
            metadata=json.loads(row["metadata_json"]),
            logic_path=json.loads(row["logic_path_json"]),
        )
    
    def list_checkpoints(
        self, branch: Optional[str] = None, limit: int = 100
    ) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            if branch:
                rows = conn.execute(
                    "SELECT * FROM checkpoints WHERE branch_name = ? "
                    "ORDER BY timestamp DESC LIMIT ?",
                    (branch, limit),
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM checkpoints ORDER BY timestamp DESC LIMIT ?",
                    (limit,),
                ).fetchall()
        
        return [
            {
                "id": row["id"],
                "timestamp": row["timestamp"],
                "branch": row["branch_name"],
                "status": row["status"],
                "hash": row["hash"],
                "state_keys": list(json.loads(row["state_json"]).keys()),
                "metadata": json.loads(row["metadata_json"]),
            }
            for row in rows
        ]
    
    def delete_checkpoint(self, checkpoint_id: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "DELETE FROM checkpoints WHERE id = ?", (checkpoint_id,)
            )
            return cursor.rowcount > 0
    
    def save_session(self, session_data: Dict[str, Any]) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO sessions (session_data) VALUES (?)",
                (json.dumps(session_data, default=str),),
            )
    
    def load_session(self) -> Optional[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT session_data FROM sessions ORDER BY id DESC LIMIT 1"
            ).fetchone()
        if row:
            return json.loads(row[0])
        return None


class InMemoryStorage(StorageBackend):
    """
    RAM-only storage — no persistence, used for testing.
    
    Data is lost when the process ends. Fast but ephemeral.
    """
    
    def __init__(self):
        self._checkpoints: Dict[str, Any] = {}
        self._session: Optional[Dict[str, Any]] = None
    
    def save_checkpoint(self, checkpoint) -> None:
        self._checkpoints[checkpoint.id] = checkpoint.to_dict()
    
    def load_checkpoint(self, checkpoint_id: str):
        from .engine import Checkpoint
        data = self._checkpoints.get(checkpoint_id)
        if data:
            return Checkpoint.from_dict(data)
        return None
    
    def list_checkpoints(
        self, branch: Optional[str] = None, limit: int = 100
    ) -> List[Dict[str, Any]]:
        cps = list(self._checkpoints.values())
        if branch:
            cps = [cp for cp in cps if cp.get("branch_name") == branch]
        return sorted(cps, key=lambda x: x.get("timestamp", 0), reverse=True)[:limit]
    
    def delete_checkpoint(self, checkpoint_id: str) -> bool:
        return self._checkpoints.pop(checkpoint_id, None) is not None
    
    def save_session(self, session_data: Dict[str, Any]) -> None:
        self._session = session_data
    
    def load_session(self) -> Optional[Dict[str, Any]]:
        return self._session
