# Loom Cohesion + Simplification Plan (Quick Wins + Staged Deep Refactors)

Date: 2026-02-16
Owner ticket: `al-8543`

## Requirements Summary

1. Improve cohesion by making module boundaries explicit and reducing cross-layer imports.
2. Simplify duplicated CLI behaviors (JSON envelope emission, argv normalization, command-name rendering).
3. Sequence work in low-risk quick wins first, then staged deep refactors for `workspace` and `team`.
4. Preserve intentional user-facing semantics while reducing maintenance overhead.

### Codebase Evidence (current pain points)

- `team/core.py` is a 6,646-line monolith that mixes run-state migration, filesystem lifecycle setup, roster parsing, and tmux/session orchestration in one place (`src/agent_loom/team/core.py:2359-2905`, file length from `wc -l`).
- `workspace/cli.py` is 1,772 lines and combines parser construction plus a large `_render_text` type-dispatch renderer (`src/agent_loom/workspace/cli.py:238-520`, `1496-1720`).
- Workspace command modules import presentation behavior from CLI internals (`src/agent_loom/workspace/commands/core.py:89-96`, `src/agent_loom/workspace/commands/harness.py:31-34`, `src/agent_loom/workspace/commands/worktree.py:25-28`).
- Workspace docs explicitly define harness and repo modes as orthogonal (`src/agent_loom/workspace/core.py:3-12`), but one combined CLI currently wires both (`src/agent_loom/workspace/cli.py:1496-1720`) and all command modules alias `workspace_root = harness_root` (`src/agent_loom/workspace/commands/core.py:26`, `harness.py:28`, `worktree.py:22`).
- Team command modules duplicate JSON envelope helpers (`src/agent_loom/team/commands/lifecycle.py:43-51`, `inbox.py:14-16`, `workers.py:19-27`, `merge.py:14-16`, `objective.py:20-22`, `utils.py:26-28`) instead of sharing one output helper (`src/agent_loom/team/output.py:14-16`).
- CLI argv normalization/error plumbing is repeated per subsystem (`src/agent_loom/ticket/cli.py:71-77,171-204`; `src/agent_loom/memory/cli.py:55-61,76-197`; `src/agent_loom/team/cli.py:75-82,94-220`).

## Acceptance Criteria (testable)

1. **Team JSON output cohesion**: No module in `src/agent_loom/team/commands/` defines `emit_json_result`; all team command handlers use a shared helper.
2. **Workspace presentation boundary**: `workspace/commands/*` no longer imports `_render_text` or `emit_result` from `workspace/cli.py`.
3. **CLI normalization cohesion**: Shared normalization/error primitives exist in `agent_loom/core` and are used by ticket/memory/team CLIs for common alias/equals rewrites.
4. **Workspace mode separation**: Parser/build logic is split so repo-mode and harness-mode wiring have separate builder modules with a thin composition layer.
5. **Team orchestration decomposition**: `team/core.py` `start()` responsibilities are extracted into dedicated helpers/modules (bootstrap/state/session spawn) with unchanged external behavior.
6. **Quality gates pass**: `uv run ruff check .`, `uv run basedpyright`, and `uv run pytest` all pass.

## Implementation Steps

### Phase 0 — Guardrails + Baseline (small, required)

1. Add characterization tests around:
   - team JSON output envelope shape for representative commands (lifecycle + inbox).
   - workspace text rendering for representative result types.
   - CLI argv normalization behavior for existing aliases in ticket/memory/team.
2. Record baseline snapshots for:
   - `loom workspace --help` and `loom workspace harness --help`.
   - one representative team command `--json` output.


### Phase 1 — Quick Wins (low risk, high cohesion)

1. **Centralize team JSON envelope emission**
   - Create one canonical helper in `src/agent_loom/team/output.py` and consume it from all command modules.
   - Replace per-file `emit_json_result` functions in:
     - `src/agent_loom/team/commands/lifecycle.py`
     - `src/agent_loom/team/commands/inbox.py`
     - `src/agent_loom/team/commands/workers.py`
     - `src/agent_loom/team/commands/merge.py`
     - `src/agent_loom/team/commands/objective.py`
     - `src/agent_loom/team/commands/utils.py`

2. **Decouple workspace presentation from CLI module**
   - Extract `_render_text` and supporting render helpers from `src/agent_loom/workspace/cli.py:238-520` into a dedicated renderer module (e.g., `workspace/render.py`).
   - Update `workspace/commands/core.py`, `workspace/commands/harness.py`, and `workspace/commands/worktree.py` to depend on renderer/output module(s), not CLI internals.
   - Keep CLI as composition + argument wiring.

3. **Extract shared argv normalization utilities**
   - Add core helpers for common operations (`--flag=value` remapping, alias rewrite pass, simple positional rewrite scaffolding).
   - Refactor repeated patterns in `ticket/cli.py`, `memory/cli.py`, and `team/cli.py` to use shared primitives while preserving subsystem-specific behavior.

### Phase 2 — Workspace Cohesion Refactor (staged)

1. Split workspace parser/build responsibilities:
   - `workspace/cli_repo.py` for single-repo commands (`status/init/worktree/merge/cleanup/sandbox/snapshot`).
   - `workspace/cli_harness.py` for harness control plane commands.
   - retain `workspace/cli.py` as thin entrypoint + global concerns (`--json anywhere`, top-level dispatch/error envelope).
2. Deduplicate `_cmd_name` logic currently duplicated between
   - `src/agent_loom/workspace/cli.py:145-182`
   - `src/agent_loom/workspace/commands/core.py:29-66`
3. Clarify root-resolution contracts:
   - Make repo-mode root resolution explicit (repo root function) and harness-mode explicit (harness root function), replacing broad `workspace_root = harness_root` aliases where they obscure mode intent.

### Phase 3 — Team Core Decomposition (staged deep refactor)

1. Extract `start()` preflight/bootstrap logic from `src/agent_loom/team/core.py:2359-2905` into focused modules:
   - run-state loading/migration/normalization
   - run path initialization + lock-scoped persistence
   - manager session/tmux bootstrap
2. Keep `start()` as orchestration glue with strict step ordering and explicit return contracts.
3. Move reusable run-state mutation logic into typed helper functions to reduce ad-hoc dict mutation blocks.
4. Add focused tests for each extracted unit (state normalization, model override merge, mount precedence, session adoption).

## Risks and Mitigations

1. **Risk:** Behavioral regressions in CLI UX due to normalization changes.
   - **Mitigation:** Characterization tests before refactor + golden cases for known aliases.
2. **Risk:** Output-format drift while unifying JSON/text emitters.
   - **Mitigation:** Snapshot tests for JSON envelopes and key text outputs.
3. **Risk:** Deep split of `team/core.py` introduces orchestration order bugs.
   - **Mitigation:** Preserve existing call order in staged helper extraction; no semantic changes in same PR as structural split.
4. **Risk:** Workspace mode split confuses entrypoint behavior.
   - **Mitigation:** Keep one public command surface (`loom workspace ...`) with compatibility parser in thin top-level module.

## Verification Steps

1. Run targeted tests introduced in Phases 0-1.
2. Run subsystem suites impacted by refactor:
   - `uv run pytest tests/team tests/workspace tests/ticket tests/memory`
3. Run project gates:
   - `uv run ruff check .`
   - `uv run basedpyright`
   - `uv run pytest`
4. Manual smoke checks:
   - `uv run loom workspace --help`
   - `uv run loom workspace harness --help`
   - representative `loom team ... --json` command(s)

## Deliverable Sequencing

- **PR A (Quick Wins):** Phase 1 (+ Phase 0 tests)
- **PR B (Workspace staged refactor):** Phase 2
- **PR C (Team staged refactor):** Phase 3

This sequencing keeps risk controlled while delivering immediate cohesion improvements early.
