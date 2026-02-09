from __future__ import annotations

from dataclasses import dataclass
from difflib import unified_diff
from pathlib import Path
from typing import Dict, Iterable, Optional

from agent_loom.pack.packs import iter_pack_files


@dataclass(frozen=True)
class PackDiff:
    relpath: str
    diff: str


def _is_likely_text_path(relpath: str) -> bool:
    rp = str(relpath or "").strip().lower()
    if not rp:
        return False
    if rp.endswith(".gitignore"):
        return True
    for suf in (
        ".md",
        ".txt",
        ".yaml",
        ".yml",
        ".json",
        ".toml",
        ".py",
        ".ts",
        ".tsx",
        ".js",
        ".jsx",
        ".d.ts",
        ".css",
        ".html",
        ".xml",
    ):
        if rp.endswith(suf):
            return True
    return False


def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def diff_text(
    *,
    a_text: str,
    b_text: str,
    fromfile: str,
    tofile: str,
    max_lines: int = 400,
) -> str:
    if a_text == b_text:
        return ""

    diff_lines = list(
        unified_diff(
            a_text.splitlines(keepends=True),
            b_text.splitlines(keepends=True),
            fromfile=fromfile,
            tofile=tofile,
        )
    )
    if max_lines > 0 and len(diff_lines) > max_lines:
        diff_lines = diff_lines[:max_lines]
        diff_lines.append("(diff truncated)\n")
    return "".join(diff_lines)


def pack_file_index(pack_id: str) -> Dict[str, Path]:
    return {rel: p for rel, p in iter_pack_files(pack_id)}


def diff_pack_file(
    *,
    repo_root: Path,
    pack_id: str,
    relpath: str,
    max_lines: int = 400,
) -> Optional[PackDiff]:
    rel = str(relpath or "").strip().lstrip("/")
    if not rel:
        return None
    if not _is_likely_text_path(rel):
        return None

    files = pack_file_index(pack_id)
    src_p = files.get(rel)
    if src_p is None:
        return None

    dst_p = (repo_root / rel).resolve()
    if not dst_p.exists():
        return None

    src_txt = _read_text(src_p)
    dst_txt = _read_text(dst_p)
    if src_txt == dst_txt:
        return None

    diff = diff_text(
        a_text=src_txt,
        b_text=dst_txt,
        fromfile=f"pack:{pack_id}/{rel}",
        tofile=str(dst_p),
        max_lines=max_lines,
    )
    return PackDiff(relpath=rel, diff=diff)


def diff_pack_files(
    *,
    repo_root: Path,
    pack_id: str,
    relpaths: Iterable[str],
    max_lines: int = 400,
) -> list[PackDiff]:
    out: list[PackDiff] = []
    for rel in relpaths:
        d = diff_pack_file(
            repo_root=repo_root,
            pack_id=pack_id,
            relpath=rel,
            max_lines=max_lines,
        )
        if d is not None and d.diff.strip():
            out.append(d)
    return out


def any_pack_diffs(
    *,
    repo_root: Path,
    pack_id: str,
    relpaths: Iterable[str],
) -> bool:
    for rel in relpaths:
        if (
            diff_pack_file(repo_root=repo_root, pack_id=pack_id, relpath=rel)
            is not None
        ):
            return True
    return False


__all__ = [
    "PackDiff",
    "any_pack_diffs",
    "diff_pack_file",
    "diff_pack_files",
    "diff_text",
    "pack_file_index",
]
