#!/usr/bin/env python3
"""Build the Loom CLI into a self-contained executable zipapp."""

from __future__ import annotations

import shutil
import tempfile
import zipapp
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOOM_PKG = ROOT / "loom"
OUTPUT = ROOT / "skills" / "loom"


def main() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        # Copy the loom package into the staging area
        shutil.copytree(LOOM_PKG, tmp / "loom")
        # Write root __main__.py that bootstraps the CLI
        (tmp / "__main__.py").write_text(
            "from loom.__main__ import main\nraise SystemExit(main())\n"
        )
        # Build the zipapp
        zipapp.create_archive(
            str(tmp),
            str(OUTPUT),
            interpreter="/usr/bin/env python3",
        )
    OUTPUT.chmod(0o755)
    print(f"Built: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
