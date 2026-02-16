---
"id": "al-f6e4"
"status": "review"
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

## Notes

**2026-02-16T00:38:48Z**

Implemented core draft for broadcast/comms boundaries: added grouped target resolution in team.targets, began send-path policy enforcement + escalation handling in team.core, and added draft tests (test_team_send_broadcast.py, test_team_comms_policy.py). Currently validating/fixing type+lint issues before first commit.

**2026-02-16T00:39:42Z**

Milestone complete: implemented broadcast target groups (, , , , and ), send fan-out with per-recipient delivery reports + dedupe, communication route enforcement, and escalation route resolution constraints in team.core/targets/composition. Added tests  and , plus target group coverage in . Verification run: ============================= test session starts ==============================
platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/alexanderbutler/code_projects/personal/agent-loom/.loom/team/runs/MiyagiDo/worktrees/al-f6e4
configfile: pyproject.toml
collected 21 items

tests/test_team_targets.py .........                                     [ 42%]
tests/test_team_send_broadcast.py .                                      [ 47%]
tests/test_team_comms_policy.py ...                                      [ 61%]
tests/test_team_composition_schema.py ........                           [100%]

============================== 21 passed in 0.21s ==============================, All checks passed!, 0 errors, 0 warnings, 0 notes.

**2026-02-16T00:40:01Z**

Validation passed for current implementation. Commands: uv run pytest tests/test_team_targets.py tests/test_team_send_broadcast.py tests/test_team_comms_policy.py tests/test_team_composition_schema.py ; uv run ruff check . ; uv run basedpyright. Preparing commit now.

**2026-02-16T00:40:33Z**

First milestone commit landed: b0ae7f0 (feat(team): enforce broadcast targets and comms policy routes). Delivered in this commit: broadcast target resolution with builtin/policy groups, send fan-out with dedupe and per-recipient delivery report, route-based communication policy enforcement, escalation resolution constraints, and new tests covering broadcast and policy rejection paths. Verification after commit: uv run pytest tests/test_team_send_broadcast.py tests/test_team_comms_policy.py ; uv run ruff check . ; uv run basedpyright. Remaining before READY_FOR_REVIEW: assemble final review summary + risks (implementation work complete).,cwd:/Users/alexanderbutler/code_projects/personal/agent-loom/.loom/team/runs/MiyagiDo/worktrees/al-f6e4}

**2026-02-16T00:40:46Z**

Completion candidate moved to review. Verification commands run: uv run pytest tests/test_team_send_broadcast.py tests/test_team_comms_policy.py ; uv run ruff check . ; uv run basedpyright. Key behavior verified: broadcast fan-out deduplicates recipients and reports partial delivery deterministically; forbidden routes fail with PERMISSION errors; escalation alias resolves only for worker/investigator senders and enforces configured escalation target role resolution. Risks: route token matching is intentionally string-based (role/group/worker/ticket tokens); future schema hardening may tighten allowed route token vocabulary to avoid policy misconfiguration typos.

**2026-02-16T00:43:17Z**

Merged into team/merge-queue-44953bb8 via queue item 9a9219c35f. Validation on merge-queue: ruff passed; basedpyright passed with 0 errors and 0 warnings; pytest in neutral env (TEAM_* unset) had 275 passed / 7 failed. Failures: tests/test_architecture_guardrails.py::{TestHotspotSizeControl::test_hotspot_files_within_size_threshold,TestModuleBoundaryDocumentation::test_readmes_contain_architecture_sections}, tests/test_compound_adapter_hooks_cli.py::{test_hook_adapters_log_observation_json,test_init_instincts_sync_json_smoke,test_omp_hook_reads_stdin_payload_with_event}, tests/test_loom_init_cli_ux.py::{test_init_yes_json_in_git_repo_initializes_everything,test_init_yes_json_outside_git_skips_team}.
