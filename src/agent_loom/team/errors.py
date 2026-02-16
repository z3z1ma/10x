from __future__ import annotations

from agent_loom.core.errors import LoomError


class TeamError(LoomError):
    def __init__(
        self,
        message: str,
        *,
        code: str = "ERROR",
        exit_code: int = 1,
        data: dict | None = None,
        hint: str = "",
        suggestions: list[str] | None = None,
    ) -> None:
        details = {"data": data} if data is not None else None
        super().__init__(
            message,
            code=code,
            hint=hint,
            details=details,
            suggestions=list(suggestions or []),
            exit_code=exit_code,
            http_status=400 if str(code) in {"ARG", "ARGPARSE"} else 500,
        )
        self.data = data


__all__ = ["TeamError"]
