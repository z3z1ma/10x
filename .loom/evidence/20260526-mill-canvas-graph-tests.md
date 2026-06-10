# Mill Canvas Graph Backend Tests

Status: recorded
Created: 2026-05-26
Updated: 2026-05-26
Observed: 2026-05-26

## Summary

Observed the Loom Mill pytest suite after replacing the shaping backend flat block
model with graph nodes and edges.

## Observation

Procedure: ran `uv run pytest tests/ -v` from `loom-mill/` after implementation.

Observed result: pytest collected 111 tests and reported `111 passed, 1 warning in
36.11s`.

Additional check: ran `git diff --check` from the repository root. It produced no
output, indicating no whitespace errors in the current diff.

Additional scan: searched `loom-mill/src` for `InteractionBlock`, `BlockType`,
`state.blocks`, `add_block`, and `block_added`. No files were found.

## Artifacts

- Command output excerpt: `111 passed, 1 warning in 36.11s` from `uv run pytest tests/ -v`.
- Warning observed in `tests/test_watcher.py::test_git_state_updates_from_git_operations`: pytest reported an ignored asyncio subprocess transport cleanup exception after tests passed.
- Command output excerpt: `git diff --check` returned no output.
- Scan output excerpt: old block-model grep over `loom-mill/src` returned `No files found`.

## What This Shows

- `.loom/tickets/done/20260526-mill-canvas-graph-model.md#ACC-001` - supports - model construction and serialization round-trip tests passed.
- `.loom/tickets/done/20260526-mill-canvas-graph-model.md#ACC-002` - supports - session graph save/load tests passed.
- `.loom/tickets/done/20260526-mill-canvas-graph-model.md#ACC-003` - supports - REST graph response tests passed.
- `.loom/tickets/done/20260526-mill-canvas-graph-model.md#ACC-004` - supports - WebSocket graph event payload tests passed.
- `.loom/tickets/done/20260526-mill-canvas-graph-model.md#ACC-005` - supports - no old block model references were found under `loom-mill/src`.
- `.loom/tickets/done/20260526-mill-canvas-graph-model.md#ACC-006` - supports - full pytest suite passed.

## What This Does Not Show

This evidence does not prove frontend canvas rendering, visual layout quality,
operator interaction behavior in a browser, or audit acceptance. The pytest warning
should be rechecked if asyncio subprocess cleanup becomes relevant to this ticket's
runtime behavior.

## Related Records

- `.loom/tickets/done/20260526-mill-canvas-graph-model.md` - implementation ticket supported by this evidence.
- `.loom/specs/mill-shaping-canvas.md` - graph behavior specification that defines downstream expectations.
