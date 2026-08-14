# Contributing to AgentStateProtocol

Thanks for your interest in contributing to AgentStateProtocol.

## Development Setup

1. Fork and clone the repository.
2. Create and activate a virtual environment.
3. Install dev dependencies:

```bash
pip install -e .[dev]
```

## Project Structure

- `agentstateprotocol/engine.py`: core checkpointing and recovery logic
- `agentstateprotocol/decorators.py`: decorators and middleware helpers
- `agentstateprotocol/storage.py`: storage backend implementations
- `agentstateprotocol/strategies.py`: recovery strategy implementations
- `agentstateprotocol/serializers.py`: serialization utilities
- `agentstateprotocol/cli.py`: command-line interface
- `test_agentstateprotocol.py`: automated tests

## Testing

```bash
pytest
```

## Pull Requests

Before opening a PR:

1. Ensure tests pass locally.
2. Include tests for behavior changes.
3. Update docs when changing user-facing behavior.
