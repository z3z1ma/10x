from __future__ import annotations

from typing import Any, Mapping, Sequence

from agent_loom.core.errors import LoomError


class WorkspaceError(LoomError):
    def __init__(
        self,
        message: str,
        *,
        code: str = "ERROR",
        hint: str = "",
        details: Mapping[str, Any] | None = None,
        suggestions: Sequence[str] | None = None,
        exit_code: int = 2,
        http_status: int = 400,
    ) -> None:
        super().__init__(
            message,
            code=code,
            hint=hint,
            details=details,
            suggestions=suggestions,
            exit_code=exit_code,
            http_status=http_status,
        )


__all__ = ["WorkspaceError"]
