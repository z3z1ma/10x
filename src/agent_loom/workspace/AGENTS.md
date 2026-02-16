# Loom Workspace subsystem (agent guide)

Scope: `src/agent_loom/workspace/**`

## What this module owns

Workspace manages git worktree lifecycle in two modes:

- Repo mode: single-repo worktree operations and metadata.
- Harness mode: multi-repo control plane under `.loom/workspaces/`.

It is the isolation/lifecycle layer used by Team and by manual workflows.

## Entry points

- CLI entry: `src/agent_loom/workspace/cli.py` (`loom workspace ...`)
- Parser composition:
  - Repo mode parser wiring: `cli_repo.py`
  - Harness mode parser wiring: `cli_harness.py`
- Command handlers: `workspace/commands/*.py`
- Domain orchestration:
  - Shared/repo logic: `workspace/core.py`, `workspace/repo/*.py`
  - Harness logic: `workspace/harness/*.py`

## Command flow

Typical flow:

1. `cli.py` builds parser and resolves command function.
2. A thin command handler (`commands/*.py`) parses args into domain calls.
3. Business logic executes in `core.py`, `repo/*.py`, or `harness/*.py`.
4. State + metadata modules persist changes.
5. Output is rendered/emitted by `workspace/output.py` via shared CLI output primitives.

## Internal module map

- `commands/`: thin CLI adapters only.
- `core.py`: shared workspace orchestration helpers.
- `repo/core.py`, `repo/cleanup.py`, `repo/sandbox.py`: repo-mode lifecycle.
- `harness/core.py` + `harness/*.py`: multi-repo harness lifecycle (deps, exec, leases, cleanup, components, impact, sandbox).
- `state.py`: persistent workspace state read/write.
- `worktree_meta.py`: worktree metadata schema and storage.
- `guards.py`: repo-mode vs harness-mode guardrails.
- `git/core.py`, `git/diff.py`: git plumbing and diff helpers.
- `models.py`, `render.py`, `output.py`, `utils.py`: DTOs and presentation/utilities.

## Storage contract

Repo mode (`.loom/workspace/`):

- `worktrees/`
- `meta/worktrees/` (annotations/metadata)

Harness mode (`.loom/workspaces/`):

- `workspace.json`
- `repos/`
- `worktrees/`
- `states/`
- `meta/groups/`
- `components/`
- `leases/`

Do not introduce storage writes outside these contracts unless you are deliberately evolving the architecture.

## Where to change code

- Add a new command: parser in `cli_repo.py` or `cli_harness.py`, handler in `commands/`.
- Add business behavior: `core.py`, `repo/*.py`, or `harness/*.py`.
- Change persistence/schema: `state.py` and/or `worktree_meta.py`.
- Change output formatting/JSON envelope usage: `output.py` and `render.py`.

## Guardrails

- Command modules stay thin; domain logic belongs in core/repo/harness modules.
- Domain modules must not import from `workspace/commands/*`.
- Respect mode separation enforced by `guards.py`.
- Use shared `agent_loom.core.cli_output` paths for JSON output.
- Preserve lease/TTL/cleanup semantics across repo and harness flows.

## Fast tests for workspace changes

- `uv run pytest tests/test_workspace_cli_ux.py`
- `uv run pytest tests/test_workspace_init.py`
- `uv run pytest tests/test_workspace_worktree_diff.py`
- `uv run pytest tests/test_workspace_meta_storage.py`
- `uv run pytest tests/test_workspace_harness_cleanup_ttl.py`
- `uv run pytest tests/test_workspace_leases_gc.py`

If dashboard workspace endpoints changed, also run server API/auth tests.
