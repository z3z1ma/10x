## Module architecture

### Responsibility boundaries

**CLI layer** (`team/cli.py`):
- Parser construction and argument validation only
- Dispatches to command handler modules
- Must NOT contain business logic or state manipulation
- Uses shared output helpers from `core/cli_output.py`

**Command handlers** (`team/commands/*.py`):
- Grouped by domain: lifecycle, workers, objective, inbox, merge, utils
- Each module owns command implementation for its domain
- Delegates to `team/core.py` for run state and tmux orchestration
- Uses `team/output.py` for JSON/text emission via shared primitives

**Core orchestration** (`team/core.py`):
- Run state management (start/pause/resume/disband)
- Worker lifecycle and worktree coordination
- Inbox and messaging
- Merge queue
- Sprint and objective state
- tmux session/window/pane management
- **Critical:** This file is a known hotspot (~6500 LOC) undergoing decomposition

**Domain modules**:
- `team/permissions.py`: role guards and environment checks
- `team/utilities.py`: shared helpers (parsing, git, pathing)
- `team/inbox.py`: inbox storage backend
- `team/merge_queue.py`: merge queue storage
- `team/models.py`: run state and message dataclasses
- `team/start_state.py`: typed run-state normalization/mutation for `start` create/update paths
- `team/tmux.py`: tmux subprocess wrappers

**Output contract** (`team/output.py`):
- Wraps `core/cli_output.py` shared primitives
- Adds team-specific JSON envelope metadata if needed
- All CLI commands MUST use these helpers, not local duplicates

### Guardrails

1. **No duplicate output helpers**: All CLI serialization/emission uses `core/cli_output.py` primitives via `team/output.py`. Local helper duplication is a regression.
2. **Command handlers stay thin**: Business logic belongs in `team/core.py` or domain modules, not in `team/commands/*.py`.
3. **Hotspot size control**: `team/core.py` is monitored for growth. New functionality should extract to domain modules when feasible.
4. **Import direction**: Domain modules may NOT import from `team/commands/*`. Command handlers import from domain modules and core.

## Architecture (continued)

- `core.py` orchestrates run lifecycle, tmux spawning, messaging, and merge queue flows.
- `commands/` contains thin CLI handlers that delegate to `core.py`.
- `composition.py` parses/validates Team YAML roster schema.
- `composition_runtime.py` resolves runtime member profiles from roster state.
- `targets.py` expands/validates send/capture targets and broadcast groups.
- `prompts.py` renders manager/worker/architect/integrator runtime prompts.
- `run_state.py` is the source of truth for run path resolution and persisted run state IO.
- `start_state.py` owns reusable start-path state mutation helpers (merge/model/default/session normalization).

### Module boundaries and guardrails

- `commands/` must remain orchestration wrappers; business logic belongs in core/domain modules.
- Runtime state is read/written through `run_state.py`; do not bypass it from command handlers.
- Roster parsing/validation stays in `composition.py`; runtime resolution stays in `composition_runtime.py`.
- Target expansion/routing behavior stays in `targets.py`; `core.py` enforces policy and delivery.
- CLI handlers must use shared output helpers from `agent_loom.core.cli_output` for JSON envelopes and payload normalization.

## Roster YAML (version 3)

Roster is an optional, repo-committable artifact loaded with `loom team start --roster <path>`.

Built-ins are fixed and always present under `builtins`: `manager`, `architect`, `worker`, `integrator`.
Each built-in only supports `{harness, agent, model}`.

Optional sections:
- `mounts` for persisted worktree mounts (same syntax as `loom team start --mount SRC[:DEST]`).
- `members` for additional custom personas (custom roles only). `always_on: true` auto-spawns; `always_on: false` is spawned on-demand via `loom team spawn-persona`.
- `communication` for policy extensions (custom-role routes/broadcast groups only; built-in routes remain fixed in code).

Built-in operating model remains immutable:
- manager + architect live in repo root
- workers are ticket-scoped in per-ticket worktrees
- integrator is persistent in the merge-queue worktree
