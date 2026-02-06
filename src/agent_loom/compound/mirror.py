from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MirrorResult:
    synced: int


def sync_claude_skills_mirror(*, root: Path, enabled: bool) -> MirrorResult:
    if not enabled:
        return MirrorResult(synced=0)

    src = root / ".opencode" / "skills"
    dst = root / ".claude" / "skills"
    if not src.exists() or not src.is_dir():
        return MirrorResult(synced=0)

    synced = 0
    for skill_dir in sorted([p for p in src.iterdir() if p.is_dir()]):
        src_md = skill_dir / "SKILL.md"
        if not src_md.exists():
            continue
        name = skill_dir.name
        raw = src_md.read_text(encoding="utf-8")
        dst_md = dst / name / "SKILL.md"
        existing = ""
        if dst_md.exists():
            existing = dst_md.read_text(encoding="utf-8")
        if existing == raw:
            continue
        dst_md.parent.mkdir(parents=True, exist_ok=True)
        dst_md.write_text(raw, encoding="utf-8")
        synced += 1
    return MirrorResult(synced=synced)
