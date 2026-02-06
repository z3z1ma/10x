from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


@dataclass(frozen=True)
class ObservationCount:
    count: int
    tail_sha256: str


def _sha256(text: str) -> str:
    import hashlib

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_observations_tail(file_path: Path, *, max_lines: int) -> List[Dict[str, Any]]:
    if max_lines <= 0:
        return []
    if not file_path.exists():
        return []
    raw = file_path.read_text(encoding="utf-8")
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    tail = lines[max(0, len(lines) - max_lines) :]
    out: List[Dict[str, Any]] = []
    for ln in tail:
        try:
            obj = json.loads(ln)
        except Exception:
            continue
        if isinstance(obj, dict):
            out.append(obj)
    return out


def count_observations(file_path: Path) -> ObservationCount:
    if not file_path.exists():
        return ObservationCount(count=0, tail_sha256="")
    raw = file_path.read_text(encoding="utf-8")
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    tail = "\n".join(lines[max(0, len(lines) - 200) :])
    return ObservationCount(count=len(lines), tail_sha256=_sha256(tail) if tail else "")
