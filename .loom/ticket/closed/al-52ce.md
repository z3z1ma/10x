---
"id": "al-52ce"
"status": "closed"
"deps": []
"links":
- "al-2bfa"
"created": "2026-02-16T06:43:32Z"
"type": "bug"
"priority": 2
"assignee": "z3z1ma"
"tags":
- "sprint:Modular-refinement"
- "team"
- "tests"
- "modularity"
"external": {}
---
# Harden team test suite against TEAM_* env leakage in worker panes

Running team tests inside an active worker pane inherits TEAM_ROLE/TEAM_WORKER_ID and triggers permission-gated command failures. Add shared test harness/env fixture to clear TEAM_* vars by default so tests are environment-stable.

## Notes

**2026-02-16T06:45:12Z**

2026-02-16: Started work. Reproducing and patching tests to clear TEAM_* env vars by default in shared harness. No blockers.

**2026-02-16T06:45:52Z**

2026-02-16: Added tests/conftest.py autouse fixture to clear TEAM_* env vars via monkeypatch for test isolation. Next: run ruff, basedpyright, and targeted/full pytest; then commit and move to review if green.

**2026-02-16T06:48:00Z**

2026-02-16 verification: uv run ruff check . ✅; uv run basedpyright ✅; targeted suite uv run pytest tests/test_team_* tests/test_ticket_sprint_context.py tests/test_ticket_ux.py ✅ (163 passed). Full uv run pytest currently has pre-existing non-team failures in compound/init tests tied to TICKET_DIR env leakage in worker pane (outside this ticket scope).

**2026-02-16T06:48:11Z**

Ready for review. Change: added tests/conftest.py autouse fixture that removes all TEAM_* env vars per test via monkeypatch, preventing worker-pane TEAM_ROLE/TEAM_WORKER_ID leakage into tests. Verification commands: uv run ruff check . ; uv run basedpyright ; uv run pytest tests/test_team_* tests/test_ticket_sprint_context.py tests/test_ticket_ux.py (163 passed). Risk: full uv run pytest still shows unrelated failures in compound/init tests due non-TEAM env leakage (TICKET_DIR), not modified in this ticket.
