from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


Heading = tuple[int, str]


@dataclass(frozen=True)
class RecordMetadata:
    id: str | None = None
    type: str | None = None
    status: str | None = None
    created: date | None = None
    updated: date | None = None
    risk: str | None = None
    priority: str | None = None
    depends_on: tuple[str, ...] = ()


@dataclass(frozen=True)
class LoomRecord:
    path: str
    surface: str | None
    metadata: RecordMetadata = field(default_factory=RecordMetadata)
    headings: tuple[Heading, ...] = ()
    references: tuple[str, ...] = ()
    labeled_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class LoomGraph:
    root: str
    records: tuple[LoomRecord, ...] = ()
