# Loom Core shared utilities (agent guide)

Scope: `src/agent_loom/core/**`

## What this module owns

`agent_loom.core` is shared infrastructure consumed by all subsystems:

- CLI output contracts
- CLI arg normalization helpers
- git/fs/io/path/time/runtime/exec primitives
- lightweight concurrency helpers

It is intentionally dependency-light and reusable.

## Module map

- `cli_output.py`: shared JSON envelope/output primitives used by all CLIs.
- `cli_args.py`: argv rewrite/splitting helpers.
- `git.py`: git root/worktree/status/commit utilities.
- `exec.py`: subprocess execution wrappers and errors.
- `fs.py`: filesystem helpers and escape/unescape utilities.
- `io.py`: atomic text/json read/write helpers.
- `paths.py`: canonical path normalization helpers.
- `time.py`: ISO timestamps and duration parsing.
- `concurrent.py`: threadpool-based `parallel_map` helper.
- `env.py`, `runtime.py`: environment and cwd context helpers.

## Control-flow role in the system

Subsystem CLIs and domain modules import these helpers instead of reimplementing shared behavior. Most critical contract is `cli_output.py`; output helpers must remain centralized there.

## Where to change code

- New shared CLI output behavior: `cli_output.py` (and then update consumers/tests).
- New git operations needed by multiple modules: `git.py`.
- New safe subprocess behavior: `exec.py`.
- Shared atomic file semantics: `io.py`.
- Shared time/duration parsing: `time.py`.

Do not add subsystem-specific business logic here.

## Guardrails

- Keep APIs generic and cross-subsystem.
- Avoid importing subsystem modules from core.
- Preserve atomic IO semantics for state/lockfile safety.
- Preserve deterministic/stable JSON envelope behavior.
- Prefer explicit errors over silent fallthrough.

Architecture guardrails are enforced in `tests/test_architecture_guardrails.py`.

## Fast tests for core changes

- `uv run pytest tests/test_core_helpers.py`
- `uv run pytest tests/test_architecture_guardrails.py`

Then run affected subsystem tests that consume changed helper behavior.
