---
name: ticket-cli-ux-tests
description: Procedure for adding stable, low-noise UX tests for loom ticket CLI behavior (stdout/stderr + exit codes).
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-09T04:37:26.148941Z"
  source_episode_ids: "9ab03e71ade631a0d3bf8b48dc47183684f6ab3d335e96c44ec1d9307d0171b7"
  source_instinct_ids: "cli-ux-change-requires-ux-test,keep-core-and-cli-error-contract-aligned,stabilize-cli-output-contract"
  tags: "cli,loom-ticket,testing,ux-contract"
  updated_at: "2026-02-09T04:37:26.148941Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
# Skill: Ticket CLI UX Tests

## When to use
- You changed `src/agent_loom/ticket/cli.py` output, flags, or error handling.
- You touched ticket core behavior that is surfaced in the CLI and want to lock the user-facing contract.

## Procedure
1. Identify the user-visible contract you changed:
- Exit code (0 vs non-zero)
- Which stream (stdout vs stderr)
- 1-5 key lines/phrases users rely on

2. Add/extend a focused UX test file:
- Prefer `tests/test_ticket_ux.py` for CLI contract tests.
- Name tests after behavior, not implementation (e.g., `test_ticket_show_missing_ticket_prints_helpful_error`).

3. Invoke the CLI through the narrowest boundary you have:
- Use the project’s existing CLI test harness (runner/subprocess helper) if present.
- Capture `exit_code`, `stdout`, `stderr`.

4. Assert minimally but meaningfully:
- Assert exact exit code.
- Assert that critical, stable lines appear in the right stream.
- Avoid asserting whole multi-line blocks unless they are intentionally part of the contract.
- Avoid volatile content (timestamps, absolute paths, machine-specific formatting) in assertions.

5. Lock error-path UX:
- For validation/missing-resource paths, assert the error headline + a single actionable hint.
- Ensure the CLI maps core errors to consistent user messages.

6. Run gates locally:
- `uv run ruff check .`
- `uv run basedpyright`
- `uv run pytest`

## Done criteria
- Tests fail if the user-visible output/exit code contract regresses.
- Refactors that keep the contract intact do not require rewriting assertions.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
