from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agent_loom.compound.paths import required_scaffold_paths


@dataclass(frozen=True)
class ScaffoldCheck:
    ok: bool
    missing: list[str]


def check_scaffold_installed(root: Path) -> ScaffoldCheck:
    missing: list[str] = []
    for rel in required_scaffold_paths():
        p = root / Path(rel)
        if not p.exists():
            missing.append(rel)
    missing = sorted(missing)
    return ScaffoldCheck(ok=(len(missing) == 0), missing=missing)


def require_scaffold_installed(root: Path) -> None:
    st = check_scaffold_installed(root)
    if st.ok:
        return
    lines = "\n".join([f"- {p}" for p in st.missing])
    raise ValueError(
        "compound scaffolding is not installed (missing required files):\n"
        + lines
        + "\n\nRun: loom compound init --dest .\n"
    )
