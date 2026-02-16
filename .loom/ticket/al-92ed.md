---
"id": "al-92ed"
"status": "open"
"deps":
- "al-2510"
- "al-b1cb"
"links": []
"created": "2026-02-16T05:15:21Z"
"type": "task"
"priority": 2
"assignee": "z3z1ma"
"parent": "al-445a"
"tags":
- "sprint:YAML-Sprint-Foundations"
- "team"
- "ticket"
- "sprint"
- "e2e"
"external": {}
---
# Sprint prep E2E: architect fanout + dependency plan contract

Objective alignment:
This sprint depends on lower-quality worker execution with minimal ambiguity. We need an end-to-end contract test proving sprint prep creates actionable, dependency-ordered tickets under active sprint context.

Scope:
- Add/expand tests around sprint prep workflow in team module (`prep-sprint`, architect handoff metadata, ticket creation conventions).
- Validate created ticket metadata includes sprint tag, parent linkage, and dependency wiring primitives expected by manager/architect loop.
- Cover durable notification semantics needed for completion protocol (`loom team send`, inbox acknowledgment expectations).

Non-goals:
- No tmux runtime integration tests.
- No broad agent prompt rewriting.
- No dashboard/API-level planning UI work.

Implementation plan:
1) Define E2E fixture run state for sprint prep path with roster + sprint context.
2) Extend `tests/test_team_sprint.py` and related prompt/flow tests to assert ticket payload contracts and notification strings.
3) Add assertions that created tickets are parented/tagged and dependency commands can be applied predictably.
4) Ensure failure cases (missing sprint context, malformed prep payload) surface actionable errors.

Verification:
- uv run pytest tests/test_team_sprint.py tests/test_team_prompts.py tests/test_ticket_sprint_context.py
- uv run ruff check .
- uv run basedpyright

Risks/edge cases:
- Over-mocking can hide integration breakage between team and ticket modules.
- Prompt text assertions can be brittle; assert contractual clauses, not incidental whitespace.
- Dependency plan assertions must tolerate id variability while enforcing structure.

## Acceptance Criteria

- Sprint prep tests prove architect handoff artifacts contain required sprint metadata and planning fields.
- Ticket creation path in prep flow is parented/tagged correctly and supports dependency encoding.
- Failure modes return explicit errors without partial inconsistent state.
