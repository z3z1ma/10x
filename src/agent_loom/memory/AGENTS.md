# Loom Memory subsystem (agent guide)

Scope: `src/agent_loom/memory/**`

## What this module owns

Memory is Loom's markdown-first associative memory system:

- Notes in markdown with structured frontmatter.
- Derived SQLite index for recall/search/link graph.
- Scoped retrieval (file/folder/command/tag/filetype) and wikilink hydration.

Source of truth is note files; sqlite is derived/rebuildable.

## Entry points

- CLI: `src/agent_loom/memory/cli.py` (`loom memory ...`)
- Orchestration: `src/agent_loom/memory/core.py`
- Storage/file operations: `src/agent_loom/memory/vault.py`
- Recall/search/ranking: `src/agent_loom/memory/recall.py`
- SQLite index: `src/agent_loom/memory/index.py`
- Wikilink hydration/stub creation: `src/agent_loom/memory/hydrate.py`

## Command flow

Typical write flow (`add`, `edit`, `append`, `forget`):

1. CLI parses and normalizes arguments.
2. `core.py` validates/normalizes frontmatter and scopes.
3. Hydration resolves wikilinks/stubs when needed.
4. `vault.py` writes/rewrites note files.
5. Index operations synchronize derived sqlite/link state.

Typical read flow (`recall`, `list`, `around`, `timeline`, `grep`):

1. CLI delegates to `core.py`.
2. `recall.py` executes query/filter/ranking logic.
3. `index.py` provides indexed metadata/FTS/link graph.
4. Structured output is emitted according to requested format.

## Internal module map

- `core.py`: command-level orchestrator.
- `vault.py`: vault path resolution and note file IO.
- `index.py`: sqlite schema/index sync/link diagnostics.
- `recall.py`: retrieval, ranking, context-pack composition.
- `hydrate.py`: wikilink parse/resolve/scaffold.
- `frontmatter.py`: note frontmatter parsing/serialization.
- `scopes.py`: scope parsing/matching/validation.
- `models.py`, `constants.py`, `errors.py`, `utils.py`: domain contracts.

## Storage contract

Default vault root: `.loom/memory/`

- `notes/` (shared tracked notes)
- `personal/notes/` (private)
- `personal/ephemeral/notes/` (ephemeral)
- `meta.json`
- `index.sqlite3` (derived cache)

Keep note IDs, filename stems, and frontmatter consistent.

## Where to change code

- New CLI command/flags: `cli.py` + `core.py` handler path.
- New write behavior/metadata semantics: `core.py` + `vault.py` + `frontmatter.py`.
- New retrieval/ranking behavior: `recall.py` (+ `index.py` when schema/query changes).
- New scope semantics: `scopes.py` and relevant core/recall integrations.
- Link/hydration behavior: `hydrate.py` + `index.py` diagnostics.

## Guardrails

- Notes are canonical; never treat sqlite as source of truth.
- Preserve deterministic rebuild semantics for reindexing.
- Do not rewrite fenced code or inline code spans during hydration.
- Keep scope/tag/link normalization stable for automation.
- Keep CLI behavior backwards-consistent unless explicitly changing UX.

## Fast tests for memory changes

- `uv run pytest tests/test_memory_cli_ux.py`
- `uv run pytest tests/test_memory_notes.py`
- `uv run pytest tests/test_memory_recall_notes.py`
- `uv run pytest tests/test_memory_link_hydration.py`
- `uv run pytest tests/test_memory_scope_glob.py`

For broader regressions:

- `uv run pytest tests/test_memory_notes_merge.py tests/test_memory_notes_golden.py`
