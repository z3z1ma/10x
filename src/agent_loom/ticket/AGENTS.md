# Loom Ticket subsystem (agent guide)

Scope: `src/agent_loom/ticket/**`

## What this module owns

Loom Ticket is the canonical issue/state tracker for Loom. It stores tickets as markdown files with YAML frontmatter in `.loom/ticket/`, enforces ticket semantics (status/priority/type/deps/claims), and provides both human CLI and machine-readable JSON flows.

## Entry points

- CLI: `src/agent_loom/ticket/cli.py` (`loom ticket ...`)
- Business logic: `src/agent_loom/ticket/core.py`
- Persistence + locking + audit: `src/agent_loom/ticket/store.py`
- Read API for dashboard: `src/agent_loom/ticket/api.py`

## Command flow

Typical flow for any command:

1. `cli.py` parses args and dispatches to `_handle_*`.
2. Handler calls `core.py` functions (`create`, `update`, `list_tickets`, `dep`, `claim`, `sync`, etc.).
3. `core.py` applies validation/normalization and delegates storage to `TicketStore`.
4. `store.py` performs frontmatter read/write, lock/lease updates, audit logging, and filesystem operations.
5. CLI emits text or JSON via shared output helpers.

## Internal module map

- `core.py`: all ticket operations and orchestration.
- `store.py`: filesystem source of truth, locking, claims, audit, cache.
- `models.py`: typed ticket/result models.
- `frontmatter.py`: markdown frontmatter parse/format utilities.
- `normalize.py`: status/priority/type/tag normalization helpers.
- `graph.py`: dependency graph and cycle logic.
- `adapters.py`: external sync adapters for `sync-external` paths.
- `constants.py` / `errors.py`: contracts and domain errors.

## Storage contract

Canonical location is `.loom/ticket/`:

- `<id>.md` active tickets
- `closed/<id>.md` closed tickets
- `.locks/` claim/lease/lock files
- `.audit/` audit trail
- `.cache/` derived cache artifacts
- `config.yaml` ticket module config/sprint defaults

Tickets are markdown + YAML frontmatter. Keep key names and enum values normalized.

## Where to change code

- Add new CLI command: `cli.py` parser + `_dispatch` + `_handle_*`.
- Add/modify behavior: `core.py`.
- Change persistence semantics or file layout: `store.py` (+ related models/normalizers/tests).
- Change dependency visualization/logic: `graph.py`.
- Change dashboard read behavior: `api.py`.

## Guardrails

- Keep CLI thin: parsing/dispatch only; no heavy business logic.
- Keep write semantics centralized in `core.py` + `store.py`.
- Preserve claim/lease + audit semantics when touching write commands.
- Preserve JSON output contract for automation.
- Validate dependency changes against cycle detection behavior.

## Fast tests for ticket changes

- `uv run pytest tests/test_ticket_ux.py`
- `uv run pytest tests/test_ticket_sprint_context.py`
- `uv run pytest tests/test_ticket_sync.py`

If dashboard-facing read APIs changed, also run:

- `uv run pytest tests/test_server_api_contract.py`
- `uv run pytest tests/test_server_auth.py`
