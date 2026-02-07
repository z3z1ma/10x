from __future__ import annotations

import time
from typing import Any, Optional

from agent_loom.core.time import parse_iso_z


def meta_last_used_at_epoch(meta: dict[str, Any]) -> Optional[float]:
    ts = meta.get("last_used_at") or meta.get("updated_at") or meta.get("created_at")
    dt = parse_iso_z(str(ts or ""))
    if dt is None:
        return None
    return float(dt.timestamp())


def meta_ttl_seconds(meta: dict[str, Any]) -> Optional[int]:
    ttl = meta.get("ttl_seconds")
    if ttl is None:
        return None
    try:
        ttl_s = int(ttl)
    except Exception:
        return None
    if ttl_s <= 0:
        return None
    return ttl_s


def meta_is_expired(meta: dict[str, Any], *, now: Optional[float] = None) -> bool:
    ttl_s = meta_ttl_seconds(meta)
    if ttl_s is None:
        return False
    used = meta_last_used_at_epoch(meta)
    if used is None:
        return False
    n = float(time.time() if now is None else now)
    return (used + ttl_s) <= n
