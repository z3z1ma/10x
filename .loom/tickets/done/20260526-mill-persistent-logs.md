# Persistent Log Retrieval

Status: done
Created: 2026-05-26
Updated: 2026-05-26

Legacy note: Risk — low - uses existing backend endpoint and disk persistence; change is additive frontend hydration logic

## Summary

After a workstation completes (or on page refresh/reconnect), the Logs tab shows
"Waiting for output..." forever despite full stdout/stderr being persisted to disk
at `.mill/workstations/{id}/logs/stdout.log`.

Root cause: The frontend `LogViewer` renders from `workstation.output[]` which is
populated exclusively by live WebSocket `log` events buffered in the client. The
initial `snapshot` message includes workstation state but NOT log history. The
backend already has `GET /workstations/{id}/logs?stream=stdout&tail=N` (line 304-326
of `api/workstation.py`) that reads from disk, but the frontend never calls it.

The fix: Frontend should hydrate logs from the REST endpoint when:
1. A workstation is selected and its `output[]` is empty
2. On WebSocket reconnect (snapshot received)
3. When workstation status transitions to completed/stopped and live buffer might be incomplete

Closure claim: Logs are always visible for any workstation that has run, regardless
of when the user opened the panel or whether the page was refreshed.

## Related Records

- `.loom/tickets/20260526-mill-factory-data-integrity.md` - parent plan
- `loom-mill/src/loom_mill/api/workstation.py:304-326` - existing GET /logs endpoint
- `loom-mill/src/loom_mill/workstation/engine.py:191-210` - log capture to disk
- `loom-mill/src/loom_mill/workstation/engine.py:364-366` - log dir path
- `loom-mill/frontend/src/lib/ws.svelte.ts:105-113` - WebSocket log buffer (500 cap)
- `loom-mill/frontend/src/lib/LogViewer.svelte:40-47` - "Waiting for output..." display
- `loom-mill/frontend/src/lib/DetailPanel.svelte:226-227` - passes `workstation.output` to LogViewer
- `.loom/evidence/20260526-mill-persistent-logs-validation.md` - build and backend test observations

## Scope

Write:
- `loom-mill/frontend/src/lib/DetailPanel.svelte` - add log hydration fetch when output is empty
- `loom-mill/frontend/src/lib/LogViewer.svelte` - add "loaded from disk" indicator, differentiate live vs historical
- `loom-mill/frontend/src/lib/ws.svelte.ts` - optionally add a method to hydrate logs from REST into the store
- `loom-mill/src/loom_mill/api/workstation.py` - enhance GET /logs to also return stderr interleaved, add combined stream option

Read:
- `loom-mill/src/loom_mill/workstation/engine.py` - understand log path and format
- `loom-mill/frontend/src/lib/types.ts` - OutputEvent type shape

Non-goals:
- Do NOT change how live WebSocket log streaming works (that's working fine)
- Do NOT add server-side log pagination with offset/limit (tail is sufficient)
- Do NOT change the 500-line live buffer cap
- Do NOT add log search/filter (future work)

### Detailed Design

**Backend enhancement to GET /logs:**
- Add `stream=combined` option that returns both stdout and stderr interleaved by timestamp
- Each line should include: `{ stream: "stdout"|"stderr", line: string, timestamp: string }`
- Use the existing log files; parse line-by-line, timestamp from file write order
- Default tail=500 to match the live buffer size

**Frontend hydration logic in DetailPanel:**
```
When a workstation is selected AND workstation.output is empty or undefined:
  1. Call GET /workstations/{id}/logs?stream=combined&tail=500
  2. Set workstation.output = response.lines (formatted as OutputEvent[])
  3. Show a subtle "(loaded from history)" badge in the LogViewer header
```

**Trigger points:**
1. `DetailPanel` mounts with a selected workstation that has empty output
2. After WebSocket snapshot (reconnect) - workstations have state but no output
3. When user clicks on a completed workstation in the list

**LogViewer enhancement:**
- When logs are loaded from disk, show a subtle indicator in the header:
  "Logs (historical)" vs "Logs (live)"
- If workstation is running but output is empty (race condition), show
  "Connecting to live output..." instead of "Waiting for output..."
- If workstation is completed and no log files exist on disk either, show
  "No logs available for this run."

## Acceptance

- ACC-001: After a workstation completes, switching to the Logs tab shows the full
  log output from disk, not "Waiting for output...".
  - Evidence: Start workstation, wait for completion, verify logs visible. Refresh page, verify logs still visible.
  - Audit: Verify disk fetch is called exactly once, not on every re-render.

- ACC-002: On page refresh with a completed workstation selected, logs load from
  disk within 500ms.
  - Evidence: Measure time from page load to logs visible in the panel.
  - Audit: Verify no infinite loop or repeated fetches.

- ACC-003: Live-streaming logs during an active workstation still work as before
  (no regression).
  - Evidence: Start a workstation, verify live log streaming works in real-time.
  - Audit: Verify WebSocket log events still populate output[].

- ACC-004: `npm --prefix loom-mill/frontend run build` passes.
  - Evidence: Build output.

- ACC-005: Backend tests pass (`pytest loom-mill/tests/`).
  - Evidence: Test output.

## Current State

Implementation is complete and awaiting review/audit. Backend `GET /logs` now falls
back to persisted disk logs when the in-memory engine is missing and accepts
`stream=combined` by reading persisted stdout and stderr files into the same string
line response. Frontend store hydration fetches stdout history once for an empty
non-running selected workstation, and `LogViewer` now distinguishes live connection,
history loading, and no-output empty states.

Verification is mixed: frontend build passed and the existing log endpoint test
passed through `uv run --extra dev`, but the requested ambient `python -m pytest`
command could not run because `pytest` is not installed, and the full suite through
`uv run --extra dev` stopped on an unrelated iteration diff assertion.

## Journal

- 2026-05-26: Created ticket. Source: operator observed "Waiting for output..." on
  completed workstation after first genuine Factory Floor run.
- 2026-05-26: Started bounded implementation run for backend disk log fallback and
  frontend empty-buffer hydration.
- 2026-05-26: Implemented backend disk fallback and frontend hydration. Recorded
  validation in `.loom/evidence/20260526-mill-persistent-logs-validation.md`; moved to review
  because full backend suite did not pass cleanly.
