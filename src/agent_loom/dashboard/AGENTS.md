# Loom Dashboard subsystem (agent guide)

Scope: `src/agent_loom/dashboard/**`

## What this module owns

Dashboard provides a Flask-backed SPA and JSON API that aggregates subsystem state (ticket/team/workspace/memory/compound). It is primarily a read surface, with optional guarded writes.

## Entry points

- CLI: `src/agent_loom/dashboard/cli.py` (`loom dashboard start`)
- Flask app wiring: `src/agent_loom/dashboard/app.py`
- Auth helpers: `src/agent_loom/dashboard/auth.py`
- Response envelopes: `src/agent_loom/dashboard/http.py`
- Workspace read helpers: `src/agent_loom/dashboard/workspace_read.py`
- Compound filesystem adapters: `src/agent_loom/dashboard/compound_fs.py`
- Introspection route support: `src/agent_loom/dashboard/introspect.py`
- UI template: `src/agent_loom/dashboard/templates/dashboard.html`

## Request/control flow

1. `cli.py` builds `ServerConfig` (host/port/workspace mode/write controls/auth token).
2. `app.create_app` registers routes and error handlers.
3. Routes delegate to subsystem APIs or local read helpers.
4. All responses go through `http.ok` / `http.err`.
5. Write routes must pass `_ensure_writes_enabled` and `_require_auth`.

## Internal boundaries

- Keep route handlers thin in `app.py`.
- Put reusable domain logic in helper modules (`workspace_read.py`, `compound_fs.py`, etc.).
- Keep auth policy centralized in `auth.py`.
- Keep JSON response shape centralized in `http.py`.

## Data dependencies

Dashboard reads subsystem storage contracts, including:

- `.loom/ticket/`
- `.loom/team/runs/`
- `.loom/memory/`
- `.loom/workspace/` and `.loom/workspaces/`
- `.loom/compound/` and `.opencode/`

It should not create hidden side-channel state outside explicit write endpoints.

## Where to change code

- New API endpoint: add route in `app.py`; extract reusable logic if non-trivial.
- Workspace endpoint behavior: `workspace_read.py`.
- Auth/token behavior: `auth.py`.
- Envelope/serialization behavior: `http.py`.
- UI-only updates: `templates/dashboard.html`.

## Guardrails

- Writes are opt-in and auth-gated; preserve this default.
- Keep endpoint payloads stable and machine-readable.
- Validate path/mode inputs before diff or file reads.
- Avoid unbounded reads for logs/captures; keep size limits.
- Keep exceptions mapped to explicit JSON error responses.

## Fast tests for dashboard changes

- `uv run pytest tests/test_server_api_contract.py`
- `uv run pytest tests/test_server_auth.py`
