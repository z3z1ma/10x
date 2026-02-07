from __future__ import annotations

from typing import List


def _one_line(text: str, max_len: int = 400) -> str:
    t = " ".join(str(text or "").split())
    return t if len(t) <= max_len else t[:max_len] + "..."


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
