from __future__ import annotations

from agent_loom.core.errors import LoomError


class MemoryError(LoomError):
    def __init__(
        self,
        message: str,
        *,
        code: str = "ERROR",
        exit_code: int = 1,
        hint: str = "",
        suggestions: list[str] | None = None,
        details: dict | None = None,
    ) -> None:
        super().__init__(
            message,
            code=code,
            hint=hint,
            details=details,
            suggestions=list(suggestions or []),
            exit_code=exit_code,
            http_status=400 if str(code).startswith("ARG") else 500,
        )


__all__ = ["MemoryError"]
