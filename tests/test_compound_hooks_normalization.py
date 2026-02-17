from __future__ import annotations

from agent_loom.compound import hooks


def test_normalize_opencode_payload_uses_fallback_tool_extractors() -> None:
    event, normalized = hooks._normalize_opencode_payload(
        {
            "type": "tool.execute.after",
            "sessionID": "sess-1",
            "input": {"name": "bash", "args": {"command": "git status --porcelain"}},
            "output": {"stderr": "", "args": {"command": "echo ignored"}},
            "error": "failed",
        },
        event_override="",
    )
    assert event == "tool.execute.after"
    assert normalized["hook_event_name"] == "tool.execute.after"
    assert normalized["session_id"] == "sess-1"
    assert normalized["tool_name"] == "bash"
    assert normalized["tool_input"] == {"command": "echo ignored"}
    assert normalized["tool_response"] == {
        "stderr": "",
        "args": {"command": "echo ignored"},
    }
    assert normalized["reason"] == "failed"


def test_normalize_omp_payload_inverts_is_error() -> None:
    event, normalized = hooks._normalize_omp_payload(
        {
            "event_name": "tool_result",
            "session": {"id": "sess-omp"},
            "tool": "bash",
            "input": {"command": "git status"},
            "output": {"exit_code": 1},
            "ok": True,
            "is_error": True,
        },
        event_override="",
    )
    assert event == "tool_result"
    assert normalized["hook_event_name"] == "tool_result"
    assert normalized["session_id"] == "sess-omp"
    assert normalized["tool_name"] == "bash"
    assert normalized["tool_input"] == {"command": "git status"}
    assert normalized["tool_response"] == {"exit_code": 1}
    # Explicit is_error should override explicit ok.
    assert normalized["ok"] is False
