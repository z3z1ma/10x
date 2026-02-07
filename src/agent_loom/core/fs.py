from __future__ import annotations

from pathlib import Path
from urllib.parse import quote, unquote


FS_SAFE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.@+"


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def fs_escape(name: str, *, safe: str = FS_SAFE) -> str:
    """Reversible encoding for filesystem path segments."""

    return quote(str(name), safe=safe)


def fs_unescape(seg: str) -> str:
    return unquote(str(seg))
