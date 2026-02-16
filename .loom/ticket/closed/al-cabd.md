---
"id": "al-cabd"
"status": "closed"
"deps": []
"links": []
"created": "2026-02-16T16:42:16Z"
"type": "task"
"priority": 2
"assignee": "z3z1ma"
"tags":
- "docs"
- "agents"
- "architecture"
"external": {}
---
# Author subsystem AGENTS.md architecture guides

Create or update AGENTS.md in each major src/agent_loom subsystem so agents can understand responsibilities, control flow, data stores, and test coverage without reading entire modules.

## Notes

**2026-02-16T16:42:27Z**

Scoping module-level AGENTS.md docs for ticket/workspace/team/memory/compound/pack/dashboard/core.

**2026-02-16T16:50:11Z**

Implemented subsystem-level AGENTS.md docs for ticket, workspace, team, memory, compound, pack, dashboard, and core. Each guide now documents boundaries, entrypoints, control flow, storage contracts, guardrails, and module-targeted test guidance. Added changie fragment Changed-20260216-094903.yaml.

**2026-02-16T16:50:15Z**

Validation gates passed: uv run ruff check . ; uv run basedpyright ; uv run pytest (316 passed).
