# pyright: reportMissingImports=false

import json
import os
from datetime import UTC, datetime
from typing import Any

_HEARTBEAT_KEY = "study-record:celery-beat:heartbeats"
_in_memory_heartbeats: list[dict[str, str]] = []


def _state_url() -> str:
    return os.getenv("APP_STATE_REDIS_URL", "redis://localhost:6379/2")


def _env_flag(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def use_memory_store() -> bool:
    return _env_flag("APP_STATE_USE_MEMORY", default=False)


def state_backend_name() -> str:
    return "memory" if use_memory_store() else _state_url()


def _redis_client() -> Any:
    import redis

    return redis.Redis.from_url(_state_url(), decode_responses=True)


def append_heartbeat(source: str) -> dict[str, str]:
    entry = {
        "source": source,
        "recorded_at": datetime.now(UTC).isoformat(),
    }
    if use_memory_store():
        _in_memory_heartbeats.append(entry)
        return entry

    _redis_client().rpush(_HEARTBEAT_KEY, json.dumps(entry))
    return entry


def list_heartbeats() -> list[dict[str, str]]:
    if use_memory_store():
        return list(_in_memory_heartbeats)

    values = _redis_client().lrange(_HEARTBEAT_KEY, 0, -1)
    items: list[dict[str, str]] = []
    for value in values:
        payload = json.loads(value)
        items.append({"source": str(payload["source"]), "recorded_at": str(payload["recorded_at"])})
    return items


def clear_heartbeats() -> int:
    if use_memory_store():
        cleared = len(_in_memory_heartbeats)
        _in_memory_heartbeats.clear()
        return cleared

    client = _redis_client()
    cleared = client.llen(_HEARTBEAT_KEY)
    client.delete(_HEARTBEAT_KEY)
    return int(cleared)
