---
"id": "al-89cc"
"status": "open"
"deps":
- "al-aec3"
"links": []
"created": "2026-02-15T23:27:04Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"parent": "al-d38a"
"tags":
- "sprint:YAML-Sprint-Foundations"
"external": {}
---
# Integrate YAML composition into team start/run state

Objective alignment:
After schema definition, Team must ingest YAML composition as first-class run configuration. This moves configuration ownership out of hardcoded defaults and into a declarative source of truth.

## Scope
- Add Team CLI entry points for YAML composition input.
- Parse and validate YAML during `loom team start`.
- Persist normalized composition in run state for downstream commands.
- Surface composition metadata in status/charter where relevant.

## Non-goals
- No broadcast enforcement yet.
- No worker lifecycle automation yet beyond persisting config.

## Implementation plan
1. Extend CLI/start command surface:
   - `src/agent_loom/team/cli.py`
   - `src/agent_loom/team/commands/lifecycle.py`
   - add config flag(s), for example `--composition <path>`.
2. In `src/agent_loom/team/core.py::start`, call composition parser and persist normalized result into `run.json`.
3. Define precedence explicitly:
   - CLI explicit overrides
   - YAML composition values
   - existing defaults
4. Ensure persisted composition survives resume and appears in status output where useful.
5. Add tests:
   - `tests/test_team_start_yaml_composition.py`
   - cases for missing file, invalid yaml, invalid schema, and valid persistence.

## Verification
- `uv run pytest tests/test_team_start_yaml_composition.py`
- `uv run ruff check .`
- `uv run basedpyright`

## Acceptance criteria
- `loom team start` accepts YAML composition input and fails fast on invalid config.
- Valid composition is normalized and persisted in run state.
- Restart/resume preserves composition without recomputing nondeterministically.
- Test coverage exists for valid and invalid start-time composition loading.

## Risks and edge cases
- Risk: precedence confusion between CLI and YAML.
  - Detection: unexpected run config values in tests.
  - Mitigation: table-driven precedence tests.
- Risk: run-state migration regressions for existing runs without composition.
  - Detection: start/resume tests fail for legacy run payloads.
  - Mitigation: backward-safe defaults when `composition` key is absent.
