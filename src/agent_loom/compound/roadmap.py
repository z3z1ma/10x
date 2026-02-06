from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from agent_loom.compound.blocks import (
    block_markers,
    upsert_managed_block,
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _one_line(text: str, max_len: int = 400) -> str:
    t = " ".join(str(text or "").split())
    return t if len(t) <= max_len else t[:max_len] + "..."


def is_trivial_changelog_note(note: str) -> bool:
    t = _one_line(str(note or "").lower(), 400)
    if not t:
        return True
    trivial = {
        "no changes",
        "no change",
        "noop",
        "no-op",
        "none",
        "n/a",
        "nothing",
        "(none)",
        "no updates",
        "no significant changes",
    }
    if t in trivial:
        return True
    if re.search(
        r"(^|\b)(no changes|no change|no updates|no significant changes)(\b|$)", t
    ):
        return True
    return False


def strip_changelog_timestamp(entry_line: str) -> str:
    line = _one_line(entry_line, 800)
    return re.sub(r"^\-\s+\d{4}-\d{2}-\d{2}T[^\s]+\s+", "", line).strip()


def append_changelog(
    *,
    roadmap_path: Path,
    note: str,
    max_entries: int = 120,
    dedupe_window: int = 20,
) -> bool:
    n = _one_line(str(note or ""), 400)
    if is_trivial_changelog_note(n):
        return False

    doc = roadmap_path.read_text(encoding="utf-8")
    begin, end = block_markers("changelog-entries")
    b = doc.find(begin)
    e = doc.find(end)

    entry = f"- {_now_iso()} {n}"
    if b != -1 and e != -1 and e > b:
        inside = doc[b + len(begin) : e].strip()
        lines = [ln for ln in inside.splitlines() if ln.strip()]
        new_sig = strip_changelog_timestamp(entry).lower()
        recent = [
            strip_changelog_timestamp(ln).lower()
            for ln in lines[: max(0, dedupe_window)]
            if ln.strip()
        ]
        if new_sig in recent:
            return False
        lines.insert(0, entry)
        inner = "\n".join(lines[: max(1, max_entries)])
        updated = upsert_managed_block(doc, "changelog-entries", inner)
    else:
        updated = upsert_managed_block(doc, "changelog-entries", entry)

    roadmap_path.write_text(updated, encoding="utf-8")
    return True


def default_roadmap_compass() -> str:
    return "\n".join(
        [
            "## Compass",
            "",
            "- Direction: _(fill in)_",
            "- Themes: _(fill in)_",
            "- Next focus (1-3): _(fill in)_",
            "- Guardrails: keep memory changes meaningful; avoid churn; prefer compounding.",
        ]
    )


def render_roadmap_backlog() -> str:
    # Best-effort: render from ticket index without invoking a subprocess.
    try:
        from agent_loom.ticket.core import list_tickets

        res = list_tickets(limit=50)
    except Exception:
        return "- _(loom ticket not available or repo not initialized)_"

    if not res.tickets:
        return "- _(no tickets)_"

    lines: List[str] = []
    for t in res.tickets[:60]:
        pr = f"p{t.priority}" if isinstance(t.priority, int) else "p?"
        status = str(t.status or "").strip() or "unknown"
        title = _one_line(str(t.title or ""), 160)
        lines.append(f"- {t.id} [{status}] ({pr}) {title}")
    return "\n".join(lines)
