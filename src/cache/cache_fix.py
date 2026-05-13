"""QA cache bugfix â€” cache branch."""
import time

_STORE = {}


def get(key: str):
    entry = _STORE.get(key)
    if entry and entry["expires"] > time.time():
        return entry["value"]
    _STORE.pop(key, None)
    return None


def set_value(key: str, value, ttl: int = 60) -> None:
    _STORE[key] = {"value": value, "expires": time.time() + ttl}


def invalidate(key: str) -> None:
    _STORE.pop(key, None)
