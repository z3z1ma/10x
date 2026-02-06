from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agent_loom.compound.blocks import upsert_managed_block
from agent_loom.compound.scaffold import require_scaffold_installed


DOC_BLOCK_MAX_CHARS = 5000


@dataclass(frozen=True)
class DocblockResult:
    ok: bool
    changed: bool


def docblock_upsert(
    *, root: Path, file: str, block_id: str, content: str
) -> DocblockResult:
    require_scaffold_installed(root)

    f = str(file or "").strip().replace("\\", "/")
    bid = str(block_id or "").strip()
    c = str(content or "").replace("\r\n", "\n").strip()
    if not f or not bid or not c:
        raise ValueError("file, id, and content are required")

    allowed: dict[str, set[str]] = {
        "AGENTS.md": {"loom-core-context"},
        "LOOM_ROADMAP.md": {"roadmap-ai-notes"},
    }
    if f not in allowed or bid not in allowed[f]:
        raise ValueError(f"doc block not allowed: {f}#{bid}")

    if f.startswith("/") or ".." in f.split("/"):
        raise ValueError("file must be repo-relative")

    if len(c) > DOC_BLOCK_MAX_CHARS:
        c = c[:DOC_BLOCK_MAX_CHARS].rstrip() + "\n"

    abs_path = (root / f).resolve()
    try:
        abs_path.relative_to(root.resolve())
    except Exception as e:
        raise ValueError("file escapes repo root") from e

    existing = abs_path.read_text(encoding="utf-8") if abs_path.exists() else ""
    updated = upsert_managed_block(existing, bid, c)
    if updated != existing:
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_text(updated, encoding="utf-8")
        return DocblockResult(ok=True, changed=True)
    return DocblockResult(ok=True, changed=False)
