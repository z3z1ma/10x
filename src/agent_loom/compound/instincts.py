from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Literal, Optional, Tuple

InstinctStatus = Literal["active", "deprecated"]

_EVIDENCE_RE = re.compile(
    r"^\-\s+ts=(?P<ts>\S+)\s+source_id=(?P<source_id>\S+)\s+source_hash=(?P<source_hash>\S+)\s*$"
)


@dataclass
class Instinct:
    id: str
    title: str
    trigger: str
    action: str
    tags: List[str]
    confidence: float
    status: InstinctStatus
    domain: str
    source: str
    notes: Optional[str]
    created_at: str
    updated_at: str
    evidence: List[Dict[str, Any]]


@dataclass
class InstinctStore:
    version: int
    instincts: List[Instinct]


@dataclass(frozen=True)
class InstinctCandidate:
    id: str
    title: str
    trigger: str
    action: str
    confidence: float
    tags: List[str]
    notes: str
    domain: str = ""


def _instincts_dirs(instincts_file: Path) -> tuple[Path, Path]:
    base = instincts_file.parent / "instincts"
    return base / "personal", base / "inherited"


def _clamp(n: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, n))


def _one_line(text: str) -> str:
    return " ".join(str(text or "").split()).strip()


def _slug(text: str) -> str:
    value = str(text or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "general"


def _domain_for(tags: list[str], explicit: str = "") -> str:
    if str(explicit or "").strip():
        return _slug(explicit)
    if tags:
        return _slug(tags[0])
    return "general"


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    src = str(text or "")
    if not src.startswith("---\n"):
        return {}, src
    end = src.find("\n---\n", 4)
    if end < 0:
        return {}, src

    front = src[4:end]
    body = src[end + 5 :]
    out: dict[str, str] = {}
    for line in front.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[str(key).strip()] = str(value).strip()
    return out, body


def _extract_section(body: str, heading: str) -> str:
    lines = str(body or "").splitlines()
    marker = f"## {heading}"
    start = -1
    for idx, line in enumerate(lines):
        if line.strip() == marker:
            start = idx + 1
            break
    if start < 0:
        return ""

    collected: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        collected.append(line)
    return "\n".join(collected).strip()


def _parse_evidence_block(body: str) -> list[dict[str, Any]]:
    evidence_text = _extract_section(body, "Evidence")
    if not evidence_text:
        return []

    out: list[dict[str, Any]] = []
    for line in evidence_text.splitlines():
        m = _EVIDENCE_RE.match(line.strip())
        if not m:
            continue
        out.append(
            {
                "ts": str(m.group("ts") or ""),
                "source_id": str(m.group("source_id") or ""),
                "source_hash": str(m.group("source_hash") or ""),
            }
        )
    return out


def _parse_instinct_markdown(path: Path, *, default_source: str) -> Instinct | None:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None

    fm, body = _parse_frontmatter(text)
    instinct_id = _slug(str(fm.get("id") or path.stem))
    if not instinct_id:
        return None

    tags = [
        _slug(t)
        for t in [x.strip() for x in str(fm.get("tags") or "").split(",") if x.strip()]
    ]
    source = _slug(str(fm.get("source") or default_source))
    action = _extract_section(body, "Action") or str(fm.get("action") or "")

    status_raw = str(fm.get("status") or "active").strip().lower()
    status: InstinctStatus = "deprecated" if status_raw == "deprecated" else "active"

    confidence = _clamp(float(str(fm.get("confidence") or "0") or 0.0), 0.0, 1.0)
    domain = _domain_for(tags, str(fm.get("domain") or ""))
    notes = _extract_section(body, "Notes") or str(fm.get("notes") or "")

    return Instinct(
        id=instinct_id,
        title=_one_line(str(fm.get("title") or "")),
        trigger=_one_line(str(fm.get("trigger") or "")),
        action=_one_line(action),
        tags=tags,
        confidence=confidence,
        status=status,
        domain=domain,
        source=source,
        notes=notes or None,
        created_at=str(fm.get("created_at") or ""),
        updated_at=str(fm.get("updated_at") or ""),
        evidence=_parse_evidence_block(body),
    )


def _load_legacy_json(file_path: Path) -> list[Instinct]:
    if not file_path.exists():
        return []
    try:
        parsed = json.loads(file_path.read_text(encoding="utf-8"))
    except Exception:
        return []

    if not isinstance(parsed, dict) or parsed.get("version") != 1:
        return []

    items = parsed.get("instincts")
    if not isinstance(items, list):
        return []

    out: list[Instinct] = []
    for it in items:
        if not isinstance(it, dict):
            continue
        tags = [_slug(str(t)) for t in list(it.get("tags") or []) if str(t).strip()]
        status_raw = str(it.get("status") or "active").strip().lower()
        status: InstinctStatus = "deprecated" if status_raw == "deprecated" else "active"
        out.append(
            Instinct(
                id=_slug(str(it.get("id") or "")),
                title=_one_line(str(it.get("title") or "")),
                trigger=_one_line(str(it.get("trigger") or "")),
                action=_one_line(str(it.get("action") or "")),
                tags=tags,
                confidence=_clamp(float(it.get("confidence") or 0.0), 0.0, 1.0),
                status=status,
                domain=_domain_for(tags),
                source="personal",
                notes=(str(it.get("notes")) if it.get("notes") is not None else None),
                created_at=str(it.get("created_at") or ""),
                updated_at=str(it.get("updated_at") or ""),
                evidence=list(it.get("evidence") or []),
            )
        )
    return [i for i in out if i.id]


def load_instincts(file_path: Path) -> InstinctStore:
    personal_dir, inherited_dir = _instincts_dirs(file_path)
    instincts: list[Instinct] = []

    for directory, source in [(personal_dir, "personal"), (inherited_dir, "inherited")]:
        if not directory.exists() or not directory.is_dir():
            continue
        for md in sorted(directory.glob("*.md"), key=lambda p: p.name):
            parsed = _parse_instinct_markdown(md, default_source=source)
            if parsed is not None and parsed.id:
                instincts.append(parsed)

    if not instincts:
        instincts = _load_legacy_json(file_path)

    instincts.sort(key=lambda x: x.id)
    return InstinctStore(version=2, instincts=instincts)


def _render_instinct_markdown(inst: Instinct) -> str:
    tags = ", ".join(_slug(t) for t in list(inst.tags or []) if str(t).strip())
    notes_text = _one_line(str(inst.notes or ""))
    lines: list[str] = [
        "---",
        f"id: {inst.id}",
        f"title: {inst.title}",
        f"trigger: {inst.trigger}",
        f"confidence: {float(inst.confidence):.4f}",
        f"status: {inst.status}",
        f"domain: {inst.domain}",
        f"source: {inst.source}",
        f"created_at: {inst.created_at}",
        f"updated_at: {inst.updated_at}",
        f"tags: {tags}",
        f"notes: {notes_text}",
        "---",
        "",
        "## Action",
        inst.action,
        "",
        "## Evidence",
    ]
    if inst.evidence:
        for ev in inst.evidence:
            lines.append(
                "- "
                + f"ts={str(ev.get('ts') or '')} "
                + f"source_id={str(ev.get('source_id') or '')} "
                + f"source_hash={str(ev.get('source_hash') or '')}"
            )
    else:
        lines.append("- _(none)_")

    lines.extend(["", "## Notes", notes_text or "- _(none)_", ""])
    return "\n".join(lines)


def save_instincts(file_path: Path, store: InstinctStore) -> None:
    personal_dir, _ = _instincts_dirs(file_path)
    personal_dir.mkdir(parents=True, exist_ok=True)

    personal = [i for i in list(store.instincts or []) if str(i.source or "") != "inherited"]
    expected_files: set[str] = set()

    for inst in sorted(personal, key=lambda x: x.id):
        filename = f"{_slug(inst.id)}.md"
        expected_files.add(filename)
        path = personal_dir / filename
        path.write_text(_render_instinct_markdown(inst), encoding="utf-8")

    for md in sorted(personal_dir.glob("*.md"), key=lambda p: p.name):
        if md.name not in expected_files:
            md.unlink(missing_ok=True)

    if file_path.exists():
        file_path.unlink(missing_ok=True)


def render_instincts_index(instincts: List[Instinct], *, max_items: int = 40) -> str:
    active = [i for i in instincts if i.status == "active"]
    active.sort(key=lambda x: (str(x.domain or ""), -float(x.confidence or 0.0), x.id))
    active = active[: max(0, int(max_items))]
    if not active:
        return "- _(none)_"

    grouped: dict[str, list[Instinct]] = {}
    for inst in active:
        grouped.setdefault(_slug(inst.domain), []).append(inst)

    lines: list[str] = []
    for domain in sorted(grouped.keys()):
        lines.append(f"### {domain}")
        lines.append("")
        for inst in grouped[domain]:
            pct = int(round(float(inst.confidence or 0.0) * 100))
            tags = f" [{', '.join(inst.tags)}]" if inst.tags else ""
            lines.append(f"- **{inst.id}** ({pct}%){tags}")
            lines.append(f"  - Trigger: {_one_line(inst.trigger)}")
            lines.append(f"  - Action: {_one_line(inst.action)}")
            lines.append(f"  - Source: {_one_line(inst.source)}")
        lines.append("")

    return "\n".join(lines).strip()


def sync_instincts_markdown(*, root: Path, store: InstinctStore) -> None:
    md_path = root / ".loom" / "compound" / "INSTINCTS.md"
    lines = [
        "# INSTINCTS",
        "",
        "## Active instincts (grouped by domain)",
        "",
        render_instincts_index(store.instincts, max_items=200),
        "",
        "## Notes",
        "",
        "- Instincts are the pre-skill layer: small, repeatable heuristics.",
        "- Promote stable instincts into harness-native skills and commands when warranted.",
        "",
    ]
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(lines), encoding="utf-8")


def _source_already_in_evidence(inst: Instinct, source_id: str) -> bool:
    for ev in inst.evidence:
        try:
            if str(ev.get("source_id") or "") == source_id:
                return True
        except Exception:
            continue
    return False


def apply_instinct_candidates(
    *,
    store: InstinctStore,
    candidates: Iterable[InstinctCandidate],
    source_id: str,
    source_ts: str,
    source_hash: str,
) -> Tuple[int, int]:
    by_id: Dict[str, Instinct] = {i.id: i for i in store.instincts}
    created = 0
    updated = 0

    for c in candidates:
        candidate_id = _slug(c.id)
        if not candidate_id:
            continue

        tags = [_slug(t) for t in list(c.tags or []) if str(t).strip()]
        domain = _domain_for(tags, explicit=str(c.domain or ""))

        existing = by_id.get(candidate_id)
        if existing is None:
            inst = Instinct(
                id=candidate_id,
                title=_one_line(c.title),
                trigger=_one_line(c.trigger),
                action=_one_line(c.action),
                tags=tags,
                confidence=_clamp(float(c.confidence), 0.0, 1.0),
                status="active",
                domain=domain,
                source="personal",
                notes=(str(c.notes).strip() or None),
                created_at=source_ts,
                updated_at=source_ts,
                evidence=[
                    {
                        "ts": source_ts,
                        "source_id": source_id,
                        "source_hash": source_hash,
                    }
                ],
            )
            store.instincts.append(inst)
            by_id[inst.id] = inst
            created += 1
            continue

        if _source_already_in_evidence(existing, source_id):
            continue

        changed = False
        if existing.title != _one_line(c.title):
            existing.title = _one_line(c.title)
            changed = True
        if existing.trigger != _one_line(c.trigger):
            existing.trigger = _one_line(c.trigger)
            changed = True
        if existing.action != _one_line(c.action):
            existing.action = _one_line(c.action)
            changed = True
        if list(existing.tags) != tags:
            existing.tags = tags
            changed = True
        if float(existing.confidence or 0.0) != float(c.confidence):
            existing.confidence = _clamp(float(c.confidence), 0.0, 1.0)
            changed = True
        if existing.domain != domain:
            existing.domain = domain
            changed = True
        if c.notes and (existing.notes or "") != str(c.notes):
            existing.notes = str(c.notes)
            changed = True

        existing.evidence.append(
            {
                "ts": source_ts,
                "source_id": source_id,
                "source_hash": source_hash,
            }
        )
        changed = True

        if changed:
            existing.updated_at = source_ts
            updated += 1

    store.instincts.sort(key=lambda x: x.id)
    return created, updated


__all__ = [
    "Instinct",
    "InstinctStore",
    "InstinctCandidate",
    "load_instincts",
    "save_instincts",
    "render_instincts_index",
    "sync_instincts_markdown",
    "apply_instinct_candidates",
]
