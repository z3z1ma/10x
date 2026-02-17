from __future__ import annotations

import hashlib


def sha256_hex(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8", errors="replace")).hexdigest()
