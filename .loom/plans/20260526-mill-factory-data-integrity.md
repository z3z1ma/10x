# Factory Floor Data Integrity & Design Room Live Sync

ID: plan:20260526-mill-factory-data-integrity
Type: Plan
Status: completed
Created: 2026-05-26
Updated: 2026-05-26
Risk: medium - touches core data pipelines for logs, diffs, and file sync; regression risk if workstation lifecycle events break

## Summary

First genuine workstation run exposed critical data-flow gaps in the Factory Floor
and a missing sync primitive in the Design Room. The workstation completed
successfully (3m 2s, exit 0) but:

1. Logs disappeared after completion ("Waiting for output..." forever)
2. Iterations tab entries are not interactive/clickable
3. Playback shows "No changes" despite the subprocess modifying files
4. Design Room editor doesn't pick up external file mutations (broken for chat-driven workflows)
5. Chat subprocess exit has no visible indicator in the UI

Root causes identified through deep triage:

- **Logs**: Frontend only holds a 500-line WebSocket buffer. On completion/refresh,
  logs vanish. Backend persists full stdout/stderr to disk and has a `GET /workstations/{id}/logs`
  endpoint, but the frontend never calls it as a fallback.
- **Playback**: Iteration diffs compare `previous_sha..HEAD` (commit-to-commit only).
  Many harness subprocesses (opencode, codex, etc.) modify files without creating
  git commits. Working-tree changes are invisible to the current diff logic.
- **Iterations**: Tab is read-only with no click handlers. No link between iteration
  entries and their diffs in playback.
- **File sync**: Editor refetches on `RecordChanged` events from the `.loom` watcher,
  but this only works for `.loom` files and only when record metadata actually changes.
  Chat subprocesses modify files in the workspace root, outside the watched path.
- **Chat exit**: `chat_complete` event arrives but frontend only stops the streaming
  indicator. No explicit "process finished" badge with exit code.

## Related Records

- `spec:mill-factory-floor` - Factory Floor behavior contract; workstation lifecycle
- `loom-mill/src/loom_mill/workstation/engine.py` - subprocess lifecycle, log capture, iteration recording
- `loom-mill/src/loom_mill/workstation/manager.py` - event pumping to WebSocket
- `loom-mill/src/loom_mill/api/workstation.py` - REST endpoints including existing GET /logs
- `loom-mill/frontend/src/lib/ws.svelte.ts` - WebSocket store and log buffer
- `loom-mill/frontend/src/lib/LogViewer.svelte` - "Waiting for output..." empty state
- `loom-mill/frontend/src/lib/Playback.svelte` - diff-based playback viewer
- `loom-mill/frontend/src/lib/IterationsTab.svelte` - read-only iteration list
- `loom-mill/frontend/src/lib/design/DocumentEditor.svelte` - editor with partial sync
- `loom-mill/src/loom_mill/watcher/watcher.py` - file watcher (currently `.loom` only)
- `loom-mill/src/loom_mill/chat/harness.py` - chat subprocess lifecycle

## Strategy

Execute in dependency order: logs first (unblocks operator visibility), then
playback (unblocks iteration review), then iterations interactivity (links the two),
then file sync (unblocks Design Room chat workflow), then chat exit indicator (polish).

Tickets 1-3 fix the Factory Floor data pipeline. Ticket 4 fixes the Design Room
foundation for chat-driven editing. Ticket 5 is polish that completes the chat UX.

Split: generalist handles backend-heavy tickets (1, 2, 4) where correctness and
data-flow logic matter most. Frontend-expert handles UI-heavy tickets (3, 5) where
visual design and interaction quality matter most. Ticket 4 is split between both:
generalist for backend file-watching, frontend-expert for editor conflict UI.

Recovery: Each ticket is independently valuable. If playback diff detection proves
too complex for uncommitted changes, fall back to "last commit" mode with a warning.

## Execution Units

### Unit: Persistent Log Retrieval

Ticket: ticket:20260526-mill-persistent-logs

Fix "Waiting for output..." by fetching persisted logs from disk when the
WebSocket live buffer is empty. The frontend should call `GET /workstations/{id}/logs`
as a hydration source on initial load, reconnect, and when the workstation has
completed but output buffer is empty. Backend already has the endpoint and persists
full logs to `.mill/workstations/{id}/logs/stdout.log`.

Closure claim: Logs are always visible for any workstation that has run, regardless
of when the user opened the detail panel or whether the page was refreshed.

### Unit: Playback Working-Tree Diff Detection

Ticket: ticket:20260526-mill-playback-worktree-diff

Fix playback showing "No changes" when the subprocess modifies files without
committing. The iteration boundary recording should detect uncommitted working-tree
changes (staged + unstaged) and include them in the diff, not just commit-to-commit
diffs.

Closure claim: Playback correctly shows all file changes made during a workstation
run, whether committed or left as working-tree modifications.

### Unit: Iterations Tab Interactivity

Ticket: ticket:20260526-mill-iterations-interactive

Make iteration entries clickable, navigating to their diff in the playback view.
Add visual affordances showing each iteration's file count and line delta. Connect
the Iterations tab and Playback tab as complementary views of the same data.

Closure claim: Clicking an iteration entry shows its diff, either inline or by
switching to the Playback tab with that iteration selected.

### Unit: Design Room File Sync

Ticket: ticket:20260526-mill-editor-file-sync

Add bi-directional live file sync to the Design Room editor. When external
processes (including chat subprocesses) modify the open file on disk, the editor
should pick up changes in near-real-time. Handle conflict when the editor has
unsaved local changes and the file changes underneath.

Closure claim: Files modified externally (by chat subprocess, other editors, or
git operations) are reflected in the Design Room editor within ~1 second, with
conflict handling when local edits exist.

### Unit: Chat Subprocess Exit Indicator

Ticket: ticket:20260526-mill-chat-exit-indicator

Add a visible indicator in the chat UI when the subprocess exits, showing exit code
and duration. Currently the streaming indicator just disappears and the response
message appears with no explicit boundary marker.

Closure claim: Users can clearly see when the chat subprocess has finished, what
exit code it returned, and how long it took.

## Milestones

### Milestone: Factory Floor Visibility

Child tickets: ticket:20260526-mill-persistent-logs, ticket:20260526-mill-playback-worktree-diff, ticket:20260526-mill-iterations-interactive

True when: An operator can run a workstation, close/reopen the app, and still see
full logs, correct file diffs in playback, and clickable iteration entries linking
to their diffs.

### Milestone: Design Room Live Editing

Child tickets: ticket:20260526-mill-editor-file-sync, ticket:20260526-mill-chat-exit-indicator

True when: A chat subprocess can modify a `.loom` record, and the editor reflects
the change automatically. The chat shows clear exit status.

## Current State

All five child tickets implemented and in review. Backend tests (59 passed) and
frontend build both pass. Awaiting operator verification in the running app.

## Journal

- 2026-05-26: Created plan with Status `open`. Source: operator's first genuine
  workstation run exposed all five issues simultaneously. Deep triage identified
  root causes in backend data flow and frontend hydration logic.
- 2026-05-26: All five tickets implemented. 59 backend tests pass, frontend builds
  clean. All tickets moved to `review`. Plan moved to `review` pending operator
  verification in the running app.
