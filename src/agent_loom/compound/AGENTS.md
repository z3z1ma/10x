# Loom Compound subsystem (agent guide)

Scope: `src/agent_loom/compound/**`

## What this module owns

Compound is Loom's learning loop:

- Ingest runtime observations from adapters/hooks.
- Derive/update instincts from observations.
- Evolve instincts into reusable assets (skills/commands/agents).
- Sync scaffold/runtime state under `.loom/compound`.

## Entry points

- CLI: `src/agent_loom/compound/cli.py` (`loom compound ...`)
- Learning pipeline: `src/agent_loom/compound/engine.py`
- Observer loop: `src/agent_loom/compound/observer.py`
- Hook ingestion adapters: `src/agent_loom/compound/hooks.py`
- Instinct parsing/storage: `src/agent_loom/compound/instincts.py`
- Evolved artifact generation: `src/agent_loom/compound/evolve.py`
- Path/state contracts: `paths.py`, `state.py`, `observations.py`

## Command/control flow

Hook path (`claude-hook`, `opencode-hook`, `omp-hook`):

1. CLI delegates to `hooks.py` adapter entrypoint.
2. Payload is normalized/sanitized.
3. Observation appended to runtime observation log.
4. Observer nudge is emitted.

Learning path (`instincts-update` / observer loop):

1. Load compound state cursor (`state.py`).
2. Ingest new observations since last cursor (`observations.py`).
3. Run derivation command template from config.
4. Parse/apply instincts and write markdown artifacts.
5. Update state cursor and regenerate indexes/summary artifacts.

Evolution path (`evolve`):

1. Read active instincts.
2. Cluster/select candidates.
3. Emit evolved skills/commands/agents under `.loom/compound/evolved/`.

## Internal module map

- `cli.py`: command surface and routing.
- `engine.py`: core instincts update orchestrator.
- `observer.py`: background event loop and cooldown behavior.
- `hooks.py`: adapter-specific event normalization and logging.
- `observations.py`: observation read/ingest/offset/hash mechanics.
- `instincts.py`: instinct model parse/save/merge/render.
- `evolve.py`: clustering and artifact generation.
- `install.py`, `sync.py`, `import_export.py`: setup/sync/transport workflows.
- `paths.py`, `state.py`: canonical filesystem/state contracts.

## Storage contract

Canonical root: `.loom/compound/`

- `runtime/observations.jsonl`
- `runtime/observer.{pid,log,nudge}`
- `instincts/local/*.md`
- `instincts/inherited/*.md`
- `INSTINCTS.md`
- `state.json`
- `config.json`
- `evolved/{skills,commands,agents}/`

Observation log is append-oriented; state cursor tracks processed offsets.

## Where to change code

- New CLI subcommand: `cli.py` + dedicated module.
- Learning/update semantics: `engine.py`, `instincts.py`, `state.py`.
- Hook adapter behavior: `hooks.py`.
- Observer scheduling/cooldown: `observer.py`.
- Filesystem contract changes: `paths.py` (+ migration-safe updates in write paths/tests).
- Evolved output format: `evolve.py`.

## Guardrails

- Keep observation ingestion sanitized and robust against malformed payloads.
- Preserve state cursor invariants (offset/hash/timestamp correctness).
- Keep instincts canonicalized (stable IDs/slugs, deterministic writes).
- Do not bypass `paths.py` contracts with ad-hoc path construction.
- Treat observer as idempotent/eventual: avoid duplicate destructive writes.

## Fast tests for compound changes

- `uv run pytest tests/test_compound_adapter_hooks_cli.py`
- `uv run pytest tests/test_compound_learning_v2.py`
- `uv run pytest tests/test_compound_install.py`
- `uv run pytest tests/test_compound_run.py`
