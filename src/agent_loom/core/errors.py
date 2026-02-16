from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class LoomWarning:
    code: str
    message: str
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "code": str(self.code),
            "message": str(self.message),
        }
        if self.details:
            payload["details"] = dict(self.details)
        return payload


class LoomError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        code: str = "ERROR",
        hint: str = "",
        details: Mapping[str, Any] | None = None,
        suggestions: Sequence[str] | None = None,
        http_status: int = 500,
        exit_code: int = 1,
    ) -> None:
        super().__init__(str(message))
        self.code = str(code or "ERROR")
        self.hint = str(hint or "")
        self.details = dict(details or {})
        self.suggestions = [str(s) for s in (suggestions or []) if str(s).strip()]
        self.http_status = int(http_status)
        self.exit_code = int(exit_code)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {"code": self.code, "message": str(self)}
        if self.hint:
            payload["hint"] = self.hint
        if self.suggestions:
            payload["suggestions"] = list(self.suggestions)
        if self.details:
            payload["details"] = dict(self.details)
        return payload


def coerce_loom_error(
    exc: BaseException,
    *,
    default_code: str = "ERROR",
    default_message: str = "internal error",
    default_http_status: int = 500,
    default_exit_code: int = 1,
    expose_message: bool = False,
    error_id: str = "",
) -> LoomError:
    if isinstance(exc, LoomError):
        if error_id and "error_id" not in exc.details:
            details = dict(exc.details)
            details["error_id"] = str(error_id)
            return LoomError(
                str(exc),
                code=exc.code,
                hint=exc.hint,
                details=details,
                suggestions=exc.suggestions,
                http_status=exc.http_status,
                exit_code=exc.exit_code,
            )
        return exc

    code = str(getattr(exc, "code", default_code) or default_code)
    hint = str(getattr(exc, "hint", "") or "")
    details_obj = getattr(exc, "details", None)
    details = (
        dict(details_obj)
        if isinstance(details_obj, Mapping)
        else ({"details": details_obj} if details_obj is not None else {})
    )
    if error_id:
        details.setdefault("error_id", str(error_id))
    suggestions_obj = getattr(exc, "suggestions", None)
    suggestions = (
        [str(s) for s in suggestions_obj if str(s).strip()]
        if isinstance(suggestions_obj, Sequence) and not isinstance(suggestions_obj, str)
        else []
    )

    http_status = int(getattr(exc, "http_status", default_http_status) or default_http_status)
    exit_code = int(getattr(exc, "exit_code", default_exit_code) or default_exit_code)
    message = str(exc) if expose_message else str(default_message)
    return LoomError(
        message,
        code=code,
        hint=hint,
        details=details,
        suggestions=suggestions,
        http_status=http_status,
        exit_code=exit_code,
    )


__all__ = ["LoomError", "LoomWarning", "coerce_loom_error"]
