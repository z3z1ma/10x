from __future__ import annotations

import subprocess
from pathlib import Path
from typing import List, Optional

from agent_loom.core.exec import ExecError
from agent_loom.core.exec import run as core_run
from agent_loom.workspace.errors import WorkspaceError


def run(
    cmd: List[str], cwd: Optional[Path] = None, check: bool = True
) -> subprocess.CompletedProcess[str]:
    try:
        return core_run(cmd, cwd=cwd, check=check)
    except ExecError as e:
        raise WorkspaceError(str(e)) from e


def short(s: str, n: int = 10) -> str:
    return s[:n]
