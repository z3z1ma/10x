from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence


@dataclass(frozen=True)
class ExecError(RuntimeError):
    cmd: Sequence[str]
    cwd: Optional[Path]
    returncode: int
    stdout: str
    stderr: str

    def __str__(self) -> str:
        cwd = self.cwd or Path.cwd()
        return (
            f"Command failed: {' '.join(self.cmd)}\n"
            f"cwd: {cwd}\n"
            f"stdout:\n{self.stdout}\n"
            f"stderr:\n{self.stderr}"
        )


def which(exe: str) -> Optional[str]:
    return shutil.which(exe)


def run(
    cmd: Sequence[str],
    *,
    cwd: Optional[Path] = None,
    check: bool = True,
    env: Optional[dict[str, str]] = None,
    timeout: Optional[float] = None,
) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(
        list(cmd),
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=env,
        timeout=timeout,
    )
    if check and p.returncode != 0:
        raise ExecError(
            cmd=cmd,
            cwd=cwd,
            returncode=int(p.returncode),
            stdout=str(p.stdout or ""),
            stderr=str(p.stderr or ""),
        )
    return p
