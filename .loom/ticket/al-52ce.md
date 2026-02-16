---
"id": "al-52ce"
"status": "open"
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
