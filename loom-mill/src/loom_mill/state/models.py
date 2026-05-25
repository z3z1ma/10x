from __future__ import annotations

from dataclasses import dataclass, field

from loom_mill.parser import LoomRecord


@dataclass(frozen=True)
class GitState:
    current_branch: str | None = None
    recent_commits: tuple[str, ...] = ()
    dirty: bool = False


@dataclass(frozen=True)
class MillState:
    records: tuple[LoomRecord, ...] = ()
    git: GitState = field(default_factory=GitState)


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


MillEvent = RecordAdded | RecordChanged | RecordRemoved | GitStateChanged
