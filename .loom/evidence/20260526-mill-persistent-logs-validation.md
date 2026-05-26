# Mill Persistent Logs Validation

ID: evidence:20260526-mill-persistent-logs-validation
Type: Evidence Dossier
Status: recorded
Created: 2026-05-26
Updated: 2026-05-26
Observed: 2026-05-26

## Summary

Validation observations for `ticket:20260526-mill-persistent-logs` after adding backend disk log fallback and frontend empty-buffer log hydration.

## Observations

- Observation: Frontend production build completed successfully.
  - Procedure/source: Ran `npm --prefix loom-mill/frontend run build` from the repository root.
  - Actual result: Vite completed with `built in 1.82s`; existing Svelte warnings were emitted from `src/lib/design/ChatPanel.svelte`, `src/lib/design/ChatMessage.svelte`, and `src/lib/design/ChatInput.svelte`.
- Observation: The requested backend test command could not run in the ambient Python environment.
  - Procedure/source: Ran `python -m pytest tests/ -x` from `loom-mill`.
  - Actual result: Failed before collection with `/run/current-system/sw/bin/python: No module named pytest`.
- Observation: Backend tests run through project dev dependencies stopped on an iteration diff assertion unrelated to the log endpoint.
  - Procedure/source: Ran `uv run --extra dev python -m pytest tests/ -x` from `loom-mill`.
  - Actual result: 15 tests passed, then `tests/test_iterations.py::test_exit_boundary_records_uncommitted_working_tree_diff_and_auto_commit` failed because `records[0].lines_removed` was `0`, expected `1`.
- Observation: The existing log REST endpoint test passed after the change.
  - Procedure/source: Ran `uv run --extra dev python -m pytest tests/test_multi_workstation.py::test_logs_persist_and_rest_endpoint_returns_tail -q` from `loom-mill`.
  - Actual result: `1 passed in 1.02s`.

## Artifacts

- Command outputs are preserved in the session transcript; no separate raw artifact files were created.

## What This Shows

- `ticket:20260526-mill-persistent-logs#ACC-004` - supports - the frontend build passed.
- `ticket:20260526-mill-persistent-logs#ACC-005` - partially supports - the log-specific backend endpoint test passed, but the full backend suite did not pass cleanly.

## What This Does Not Show

- This does not prove the browser end-to-end behavior after an actual page refresh; no manual browser reproduction was run.
- This does not prove live WebSocket streaming beyond the frontend build preserving type and bundle validity.
- The full backend suite result is limited by an unrelated failing iteration test and should be rechecked after that failure is resolved or understood.

## Related Records

- `ticket:20260526-mill-persistent-logs` - implementation ticket under validation.
