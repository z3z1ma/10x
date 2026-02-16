---
"id": "al-aec3"
"status": "review"
"deps": []
"links": []
"created": "2026-02-15T23:26:49Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"parent": "al-d38a"
"tags":
- "sprint:YAML-Sprint-Foundations"
"external": {}
---
# Define YAML team composition schema

Objective alignment:
We need a single declarative contract before wiring behavior into Team runtime. A strict schema is the foundation for modularity and prevents more logic from accumulating inside ad hoc branches in `team/core.py`.

## Scope
- Define a versioned YAML schema for team composition.
- Implement parsing + validation in a dedicated domain module.
- Provide deterministic normalization output that downstream runtime logic can consume.

## Non-goals
- No runtime behavior changes to `start`, `spawn`, or `send` yet.
- No CLI UX changes besides what is required for parser test harnesses.

## Implementation plan
1. Add a new module for composition schema and parsing, for example:
   - `src/agent_loom/team/composition.py`
   - optional supporting dataclasses/types in `src/agent_loom/team/models.py`
2. Define schema version and top-level sections, covering at minimum:
   - metadata/version
   - member definitions (always-on vs ephemeral)
   - worktree mapping patterns
   - communication and escalation policy
   - BYO agent references
3. Implement strict validation rules:
   - unknown keys rejected
   - required keys enforced
   - invalid enum values rejected
   - overlapping or ambiguous mapping patterns detected
4. Return a normalized internal representation with deterministic ordering.
5. Add focused tests:
   - `tests/test_team_composition_schema.py`
   - valid config fixtures and invalid config fixtures
   - explicit assertions on error messages/hints for malformed YAML

## Verification
- `uv run pytest tests/test_team_composition_schema.py`
- `uv run ruff check .`
- `uv run basedpyright`

## Acceptance criteria
- A versioned YAML schema exists with explicit required/optional fields and defaults.
- Invalid configs fail fast with actionable error messages.
- Normalized parser output is stable and suitable for runtime consumption.
- Parser behavior is covered by dedicated unit tests.

## Risks and edge cases
- Risk: schema overreach creates unnecessary complexity.
  - Detection: parser requires many optional fields to operate.
  - Mitigation: default-minimal schema with additive optional sections.
- Risk: pattern matching semantics are ambiguous.
  - Detection: two mappings can claim the same worktree/ticket.
  - Mitigation: deterministic precedence or hard validation failure.

## Notes

**2026-02-15T23:37:22Z**

Started work. Acked inbox and beginning schema/parser implementation. First milestone ETA ~35m: composition domain models + strict loader + initial passing tests for valid/invalid fixtures.

**2026-02-15T23:40:19Z**

Milestone 1 complete: added src/agent_loom/team/composition.py with strict versioned schema parser/validator + deterministic normalization, including unknown-key rejection, enum validation, BYO reference checks, and ambiguous worktree pattern overlap detection. Added focused fixture-backed tests in tests/test_team_composition_schema.py (unknown key, invalid enum, overlap, BYO reference). Running verification now.

**2026-02-15T23:47:48Z**

First milestone committed (6778745). Delivered strict versioned YAML composition schema parser in src/agent_loom/team/composition.py with dedicated TeamCompositionError, required/optional/defaulted fields, unknown-key rejection, enum validation, BYO agent reference validation, and ambiguous worktree mapping overlap detection. Added deterministic normalization ordering and fixture-backed tests in tests/test_team_composition_schema.py plus tests/fixtures/team_composition/*.yaml covering valid minimal/unsorted and invalid unknown key/enum/overlap cases. Verification run: uv run pytest tests/test_team_composition_schema.py (6 passed), uv run ruff check . (pass), uv run basedpyright (0 errors, 1 existing warning in src/agent_loom/team/core.py:1065 reportUnusedParameter).

**2026-02-15T23:50:54Z**

Finalized schema acceptance coverage with two additional tests in tests/test_team_composition_schema.py: malformed YAML parse errors include source context, and invalid mapping wildcard patterns are rejected with actionable hint. Added follow-up commit b3ee48b (in addition to 6778745). Verification rerun complete: uv run pytest tests/test_team_composition_schema.py (8 passed), uv run ruff check . (pass), uv run basedpyright (0 errors, 1 pre-existing warning at src/agent_loom/team/core.py:1065), env -u TEAM_* uv run pytest (261 passed, 6 failed unrelated to this ticket in architecture guardrails/compound adapter hooks/loom init CLI tests). No runtime behavior wiring changes made.

**2026-02-15T23:55:41Z**

Merged into team/merge-queue-44953bb8 via queue item 2a2bb71263. Validation on merge-queue: ruff passed; basedpyright returned 0 errors (1 existing warning in src/agent_loom/team/core.py:1065 unused parameter session_path); pytest run in neutral env (TEAM_* unset) had 261 passed / 6 failed (fails in architecture guardrail + compound adapter hooks + loom init CLI tests).
