from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class HarnessConfig:
    command: str
    args: list[str] = field(default_factory=list)
    env: dict[str, str] | None = None
    cwd: str | None = None

    def command_line(self, ticket_path: Path) -> list[str]:
        rendered_ticket_path = str(ticket_path)
        return [
            self.command,
            *[arg.replace("{ticket_path}", rendered_ticket_path) for arg in self.args],
        ]
