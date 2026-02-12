from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agent_loom.pack.core import install_pack, update_pack
from agent_loom.pack.lock import index_packs, load_lock

COMPOUND_PACK_ID = "loom-compound-core"


@dataclass(frozen=True)
class CompoundInstallResult:
    dest: str
    dry_run: bool
    wrote: list[str]
    skipped: list[str]
    warnings: list[str]


def _pack_installed(repo_root: Path, *, pack_id: str) -> bool:
    try:
        lock = load_lock(repo_root)
    except Exception:
        return False
    return pack_id in index_packs(lock)


def install_opencode(
    *, dest: Path, dry_run: bool, force: bool = False
) -> CompoundInstallResult:
    repo_root = dest.expanduser().resolve()

    if _pack_installed(repo_root, pack_id=COMPOUND_PACK_ID):
        pr = update_pack(
            repo_root=repo_root,
            pack_id=COMPOUND_PACK_ID,
            dry_run=bool(dry_run),
            force=bool(force),
        )
    else:
        pr = install_pack(
            repo_root=repo_root,
            pack_id=COMPOUND_PACK_ID,
            dry_run=bool(dry_run),
            force=bool(force),
        )

    return CompoundInstallResult(
        dest=str(repo_root),
        dry_run=bool(dry_run),
        wrote=sorted(set(list(pr.wrote or []))),
        skipped=sorted(set(list(pr.skipped or []))),
        warnings=sorted(set(list(pr.warnings or []))),
    )


__all__ = [
    "COMPOUND_PACK_ID",
    "install_opencode",
]
