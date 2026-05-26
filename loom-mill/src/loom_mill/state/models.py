from __future__ import annotations

from dataclasses import dataclass, field

from loom_mill.parser import LoomRecord
from loom_mill.processes.backpressure import BackpressureSignal
from loom_mill.workstation.models import OutputEvent, WorkstationState


@dataclass(frozen=True)
class GitState:
    current_branch: str | None = None
    recent_commits: tuple[str, ...] = ()
    dirty: bool = False


@dataclass(frozen=True)
class MillState:
    records: tuple[LoomRecord, ...] = ()
    git: GitState = field(default_factory=GitState)
    workstations: dict[str, WorkstationState] = field(default_factory=dict)
    backpressure_signals: dict[str, tuple[BackpressureSignal, ...]] = field(default_factory=dict)


@dataclass(frozen=True)
class RecordAdded:
    path: str
    record: LoomRecord


@dataclass(frozen=True)
class RecordChanged:
    path: str
    record: LoomRecord
    previous: LoomRecord


@dataclass(frozen=True)
class RecordRemoved:
    path: str
    previous: LoomRecord


@dataclass(frozen=True)
class GitStateChanged:
    git: GitState
    previous: GitState


@dataclass(frozen=True)
class WorkstationStateChanged:
    workstation_id: str
    workstation: WorkstationState


@dataclass(frozen=True)
class WorkstationOutput:
    workstation_id: str
    output: OutputEvent


MillEvent = RecordAdded | RecordChanged | RecordRemoved | GitStateChanged | WorkstationStateChanged | WorkstationOutput
