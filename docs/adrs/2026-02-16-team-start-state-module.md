# Introduce `team/start_state.py` for start-path run state mutations

Date: 2026-02-16

## Status

Accepted

## Context

`team/core.py` had a large `start()` pathway that mixed lock orchestration with
ad-hoc run-state normalization and mutation logic (merge config updates, model
overrides, defaults/base-ref handling, worker role migration, and session
adoption). The mutation logic was duplicated across create/update branches and
hard to test in isolation.

## Decision

Create `src/agent_loom/team/start_state.py` as a focused domain module for
start-path run-state mutations. The module owns typed helpers and dataclasses:

- `StartMergeOptions`
- `StartModelOverrides`
- normalization/mutation helpers for harness config, merge/default config,
  session adoption, and legacy role migration.

`team/core.py` retains orchestration ordering and side-effect boundaries
(locking, file persistence, tmux bootstrap), and delegates state mutation logic
to `start_state.py`.

## Consequences

- Easier to add focused unit tests for start-state behavior without tmux/file
  orchestration.
- Clearer separation between orchestration flow (`core.py`) and state mutation
  semantics (`start_state.py`).
- `team/core.py` remains a hotspot, but future decomposition can now build on a
  dedicated start-state boundary instead of editing inlined dict-mutation
  blocks.
