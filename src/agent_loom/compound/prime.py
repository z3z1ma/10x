from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class PrimeResult:
    ok: bool
    wrote: List[str]
    warnings: List[str]


def _prime_markdown_by_subsystem() -> Tuple[Dict[str, str], List[str]]:
    warnings: List[str] = []
    out: Dict[str, str] = {}

    from agent_loom.memory.core import prime as memory_prime
    from agent_loom.team.prime import prime as team_prime
    from agent_loom.ticket.core import prime as ticket_prime
    from agent_loom.workspace.prime import prime as workspace_prime

    subsystems = [
        ("memory", memory_prime),
        ("team", team_prime),
        ("ticket", ticket_prime),
        ("workspace", workspace_prime),
    ]

    for name, fn in subsystems:
        try:
            res = fn()
        except Exception as e:
            warnings.append(f"prime: failed for {name}: {e}")
            out[name] = ""
            continue

        md = ""
        payload = getattr(res, "payload", None)
        if isinstance(payload, dict):
            md = str((payload or {}).get("markdown") or "")
        else:
            md = str(getattr(res, "markdown", "") or "")
        if not md.strip():
            warnings.append(f"prime: empty markdown for {name}")
        out[name] = md

    return out, warnings


def prime_rules(*, root: Path) -> PrimeResult:
    md_by_subsystem, warns = _prime_markdown_by_subsystem()
    rules_dir = root / ".opencode" / "rules"
    wrote: List[str] = []

    try:
        rules_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return PrimeResult(
            ok=False,
            wrote=[],
            warnings=sorted({*warns, f"prime: failed to create {rules_dir}: {e}"}),
        )

    for subsystem in sorted(md_by_subsystem.keys()):
        text = str(md_by_subsystem.get(subsystem) or "")
        p = rules_dir / f"{subsystem}.md"
        try:
            p.write_text(text.rstrip() + "\n", encoding="utf-8")
            wrote.append(f".opencode/rules/{subsystem}.md")
        except Exception as e:
            warns.append(f"prime: failed to write .opencode/rules/{subsystem}.md: {e}")

    return PrimeResult(
        ok=len(wrote) > 0, wrote=sorted(wrote), warnings=sorted({w for w in warns if w})
    )
