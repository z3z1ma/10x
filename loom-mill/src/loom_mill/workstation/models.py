from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path


class WorkstationStatus(StrEnum):
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"
    COMPLETED = "completed"


@dataclass(frozen=True)
class OutputEvent:
    stream: str
    data: str


@dataclass
class WorkstationState:
    status: WorkstationStatus = WorkstationStatus.IDLE
    worktree_path: Path | None = None
    process_id: int | None = None
    exit_code: int | None = None
    output: list[OutputEvent] = field(default_factory=list)
