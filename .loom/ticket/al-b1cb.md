---
"id": "al-b1cb"
"status": "open"
"deps": []
"links": []
"created": "2026-02-16T05:15:12Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"parent": "al-445a"
"tags":
- "sprint:YAML-Sprint-Foundations"
- "ticket"
- "sprint"
- "ux"
"external": {}
---
# Ticket module: first-class sprint workflow hardening

Objective alignment:
The charter requires first-class sprint support in the ticket module. Current sprint context exists; this ticket hardens workflow edges so sprint planning/execution is deterministic for team automation.

Scope:
- Audit and tighten sprint context behavior in `src/agent_loom/ticket/core.py` and `src/agent_loom/ticket/cli.py`.
- Ensure create/list/update interactions with sprint tag defaults are explicit and tested (including override/opt-out behavior).
- Verify parent/dependency workflows used by sprint prep remain robust under sprint-tag filtering.
- Expand tests in `tests/test_ticket_sprint_context.py` and `tests/test_ticket_ux.py` for edge cases.

Non-goals:
- No team/tmux orchestration changes.
- No external issue tracker integration work.
- No bulk redesign of ticket model beyond sprint semantics.

Implementation plan:
1) Enumerate sprint-context invariants (priority of stored sprint vs TEAM_SPRINT_TAG env vs explicit CLI flags).
2) Implement code adjustments where behavior is implicit/ambiguous.
3) Add regression tests for listing/filtering with and without sprint context, plus explicit tag override precedence.
4) Validate parent/dependency operations still behave correctly under sprint-constrained list/readiness views.

Verification:
- uv run pytest tests/test_ticket_sprint_context.py tests/test_ticket_ux.py tests/test_team_sprint.py
- uv run ruff check .
- uv run basedpyright

Risks/edge cases:
- Hidden precedence rules can silently drop tickets from sprint views.
- Environment-provided sprint tags can cause accidental cross-sprint contamination if override order is wrong.
- Parent/dependency graph operations must remain global-correct even when views are sprint-filtered.

## Acceptance Criteria

- Sprint context precedence is explicitly codified and covered by tests.
- Ticket create/list behavior with sprint defaults, explicit tags, and --no-sprint-tag is deterministic and documented in tests.
- Parent/dependency workflows continue to function correctly with sprint-focused planning usage.
