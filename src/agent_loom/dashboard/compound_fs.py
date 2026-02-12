from __future__ import annotations

from pathlib import Path


def list_skills(repo_root: Path) -> list[dict[str, str]]:
    base = repo_root / ".opencode" / "skills"
    if not base.exists() or not base.is_dir():
        return []

    out: list[dict[str, str]] = []
    for d in sorted([p for p in base.iterdir() if p.is_dir()], key=lambda p: p.name):
        skill_md = d / "SKILL.md"
        out.append(
            {
                "name": d.name,
                "path": str(d.relative_to(repo_root).as_posix()),
                "skill_md": str(skill_md.relative_to(repo_root).as_posix())
                if skill_md.exists()
                else "",
            }
        )
    return out


def read_skill(repo_root: Path, *, name: str) -> dict[str, str]:
    base = repo_root / ".opencode" / "skills" / name
    p = base / "SKILL.md"
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(f"Skill not found: {name}")
    return {
        "name": name,
        "path": str(base.relative_to(repo_root).as_posix()),
        "text": p.read_text(encoding="utf-8", errors="replace"),
    }


def read_instincts(repo_root: Path) -> dict:
    from agent_loom.compound.instincts import load_instincts

    store = load_instincts(repo_root / ".loom" / "compound" / "instincts.json")
    return {
        "version": int(store.version),
        "instincts": [
            {
                "id": i.id,
                "title": i.title,
                "trigger": i.trigger,
                "action": i.action,
                "domain": i.domain,
                "source": i.source,
                "tags": list(i.tags or []),
                "confidence": float(i.confidence or 0.0),
                "status": i.status,
                "notes": i.notes,
                "created_at": i.created_at,
                "updated_at": i.updated_at,
                "evidence": list(i.evidence or []),
            }
            for i in list(store.instincts or [])
        ],
    }
