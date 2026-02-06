from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _clamp(n: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, n))


def _validate_kebab(ident: str, *, label: str) -> None:
    import re

    if not isinstance(ident, str):
        raise ValueError(f"{label} must be a string")
    ident = ident.strip()
    if len(ident) < 1 or len(ident) > 64:
        raise ValueError(f"{label} must be 1-64 chars")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", ident):
        raise ValueError(f"{label} must be kebab-case")


InstinctStatus = Literal["active", "deprecated"]


@dataclass
class Instinct:
    id: str
    title: str
    trigger: str
    action: str
    tags: List[str]
    confidence: float
    status: InstinctStatus
    skill: Optional[str]
    notes: Optional[str]
    created_at: str
    updated_at: str
    evidence: List[Dict[str, Any]]


@dataclass
class InstinctStore:
    version: int
    instincts: List[Instinct]


def load_instincts(file_path: Path) -> InstinctStore:
    if not file_path.exists():
        return InstinctStore(version=1, instincts=[])
    try:
        raw = file_path.read_text(encoding="utf-8")
        parsed = json.loads(raw)
    except Exception:
        return InstinctStore(version=1, instincts=[])
    if not isinstance(parsed, dict) or parsed.get("version") != 1:
        return InstinctStore(version=1, instincts=[])
    items = parsed.get("instincts")
    if not isinstance(items, list):
        return InstinctStore(version=1, instincts=[])
    out: List[Instinct] = []
    for it in items:
        if not isinstance(it, dict):
            continue

        st_raw = str(it.get("status") or "active").strip().lower()
        status: InstinctStatus = "deprecated" if st_raw == "deprecated" else "active"
        out.append(
            Instinct(
                id=str(it.get("id") or ""),
                title=str(it.get("title") or ""),
                trigger=str(it.get("trigger") or ""),
                action=str(it.get("action") or ""),
                tags=list(it.get("tags") or []),
                confidence=float(it.get("confidence") or 0.0),
                status=status,
                skill=(str(it.get("skill")) if it.get("skill") is not None else None),
                notes=(str(it.get("notes")) if it.get("notes") is not None else None),
                created_at=str(it.get("created_at") or ""),
                updated_at=str(it.get("updated_at") or ""),
                evidence=list(it.get("evidence") or []),
            )
        )
    return InstinctStore(version=1, instincts=out)


def save_instincts(file_path: Path, store: InstinctStore) -> None:
    payload = {
        "version": 1,
        "instincts": [
            {
                "id": i.id,
                "title": i.title,
                "trigger": i.trigger,
                "action": i.action,
                "tags": i.tags,
                "confidence": i.confidence,
                "status": i.status,
                **({"skill": i.skill} if i.skill is not None else {}),
                **({"notes": i.notes} if i.notes is not None else {}),
                "created_at": i.created_at,
                "updated_at": i.updated_at,
                "evidence": i.evidence,
            }
            for i in store.instincts
        ],
    }
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def render_instincts_index(instincts: List[Instinct], *, max_items: int = 25) -> str:
    active = [i for i in instincts if i.status == "active"]
    active.sort(key=lambda x: float(x.confidence or 0.0), reverse=True)
    active = active[: max(0, int(max_items))]
    if not active:
        return "- _(none)_"

    def one_line(s: str, limit: int = 200) -> str:
        t = " ".join(str(s or "").split())
        return t if len(t) <= limit else t[:limit] + "..."

    lines: List[str] = []
    for i in active:
        tags = f" [{', '.join(i.tags)}]" if i.tags else ""
        skill = f" -> skill: `{i.skill}`" if i.skill else ""
        pct = int(round(float(i.confidence or 0.0) * 100))
        lines.append(
            "\n".join(
                [
                    f"- **{i.id}** ({pct}%){tags}{skill}",
                    f"  - Trigger: {one_line(i.trigger)}",
                    f"  - Action: {one_line(i.action)}",
                ]
            )
        )
    return "\n".join(lines)


@dataclass(frozen=True)
class InstinctDelta:
    created: int
    updated: int


def instinct_upsert(
    store: InstinctStore,
    *,
    operation: Literal["create", "update"],
    ident: str,
    title: Optional[str] = None,
    trigger: Optional[str] = None,
    action: Optional[str] = None,
    confidence: Optional[float] = None,
    confidence_delta: Optional[float] = None,
    evidence_note: Optional[str] = None,
    session_id: Optional[str] = None,
) -> InstinctDelta:
    _validate_kebab(ident, label="instinct.id")
    by_id: Dict[str, Instinct] = {i.id: i for i in store.instincts}

    if operation == "create":
        if ident in by_id:
            return InstinctDelta(created=0, updated=0)
        if not (title and trigger and action):
            raise ValueError("create requires title, trigger, action")
        if confidence is None:
            raise ValueError("create requires confidence")
        ts = _now_iso()
        inst = Instinct(
            id=ident,
            title=str(title).strip() or ident,
            trigger=str(trigger).strip(),
            action=str(action).strip(),
            tags=[],
            confidence=_clamp(float(confidence), 0.0, 1.0),
            status="active",
            skill=None,
            notes=None,
            created_at=ts,
            updated_at=ts,
            evidence=[{"ts": ts, "sessionID": session_id, "note": evidence_note}]
            if (evidence_note or session_id)
            else [{"ts": ts, "sessionID": session_id}],
        )
        store.instincts.append(inst)
        return InstinctDelta(created=1, updated=0)

    inst = by_id.get(ident)
    if inst is None:
        return InstinctDelta(created=0, updated=0)

    changed = False
    if confidence_delta is not None:
        inst.confidence = _clamp(
            float(inst.confidence or 0.0) + float(confidence_delta), 0.0, 1.0
        )
        changed = True
    if confidence is not None:
        inst.confidence = _clamp(float(confidence), 0.0, 1.0)
        changed = True

    if isinstance(title, str):
        inst.title = title
        changed = True
    if isinstance(trigger, str):
        inst.trigger = trigger
        changed = True
    if isinstance(action, str):
        inst.action = action
        changed = True

    if evidence_note:
        inst.evidence.append(
            {"ts": _now_iso(), "sessionID": session_id, "note": evidence_note}
        )
        changed = True

    if changed:
        inst.updated_at = _now_iso()
        return InstinctDelta(created=0, updated=1)
    return InstinctDelta(created=0, updated=0)
