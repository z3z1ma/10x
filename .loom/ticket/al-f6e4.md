---
"id": "al-f6e4"
"status": "open"
"deps":
- "al-89cc"
"links": []
"created": "2026-02-15T23:27:31Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"parent": "al-d38a"
"tags":
- "sprint:YAML-Sprint-Foundations"
"external": {}
---
# Add broadcast messaging + communication and escalation boundaries

Objective alignment:
YAML composition must govern who can talk to whom, and how escalations happen, otherwise multi-agent runs remain fragile and noisy. This ticket adds explicit policy enforcement to messaging.

## Scope
- Extend send target model to support broadcast groups.
- Enforce communication boundaries from composition policy.
- Enforce escalation routes and failure behavior.
- Return actionable errors for forbidden or ambiguous communication.

## Non-goals
- No new worker spawning behavior beyond what is required for target resolution.
- No changes to merge queue semantics.

## Implementation plan
1. Extend target resolution in `src/agent_loom/team/targets.py` for group targets (for example: `all`, `workers`, policy-defined groups).
2. Extend `src/agent_loom/team/core.py::send` and inbox nudge flow to fan out safely with durable message records.
3. Add policy checks that validate sender role, recipient set, and escalation permissions before dispatch.
4. Implement explicit escalation helper behavior (for example worker to manager escalation constraints).
5. Add tests:
   - `tests/test_team_send_broadcast.py`
   - `tests/test_team_comms_policy.py`
   - include forbidden-route, unknown-group, and partial-delivery failure cases.

## Verification
- `uv run pytest tests/test_team_send_broadcast.py tests/test_team_comms_policy.py`
- `uv run ruff check .`
- `uv run basedpyright`

## Acceptance criteria
- Broadcast send reaches all eligible recipients exactly once.
- Communication policy forbids invalid routes and returns deterministic errors.
- Escalation routes are explicit and enforced.
- Tests cover positive fan-out and policy rejection paths.

## Risks and edge cases
- Risk: noisy or duplicated broadcast deliveries.
  - Detection: duplicated inbox ids or repeated pane sends in tests.
  - Mitigation: deduplicate recipient set before delivery.
- Risk: partial delivery leaves unclear operator state.
  - Detection: some recipients get message while command reports success.
  - Mitigation: return per-recipient delivery report and explicit failure reason.
