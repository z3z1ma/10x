# Design Room Editor File Sync

Status: done
Created: 2026-05-26
Updated: 2026-05-26

Legacy note: Risk — medium - introduces file watching for arbitrary paths beyond .loom; must handle race conditions, conflict detection, and content hashing without corrupting editor state

## Summary

The Design Room editor does not pick up external file changes. When a chat
subprocess (or any external process) modifies the currently-open file on disk,
the editor content stays stale until the user manually navigates away and back.

This is a critical gap because the primary Design Room workflow is:
1. Open a record in the editor
2. Chat with a harness subprocess about it
3. The subprocess modifies the file
4. Editor should reflect changes immediately

Current partial support: The backend `LoomWatcher` watches `.loom/` and emits
`RecordChanged` events. The editor `$effect` at line 63-75 of `DocumentEditor.svelte`
refetches content on `RecordChanged` if the editor is clean. This works for `.loom`
files when metadata actually changes.

Gaps:
1. Watcher only covers `.loom/` - files outside (e.g., source code) are invisible
2. Content changes that don't alter parsed record metadata don't trigger `RecordChanged`
3. No content-hash comparison - refetch happens on every `RecordChanged` even if content is identical
4. Conflict detection is boolean (`modified = true`) with no resolution UI
5. After chat subprocess runs, there's a race: watcher might not fire before user navigates away

The fix: Add content-hash-based live sync that:
- Watches the currently-open file specifically (not all workspace files)
- Compares content hashes to detect real changes
- Auto-updates the editor when clean (no local edits)
- Shows conflict UI when dirty (local edits exist and file changed externally)
- Provides "Accept external" and "Keep mine" conflict resolution

Closure claim: Files modified externally (by chat subprocess, other editors, or
git operations) are reflected in the Design Room editor within ~1 second, with
conflict handling when local edits exist.

## Related Records

- `.loom/tickets/20260526-mill-factory-data-integrity.md` - parent plan
- `loom-mill/src/loom_mill/watcher/watcher.py:12-97` - existing `.loom` file watcher
- `loom-mill/src/loom_mill/api/design.py:97-132` - record update endpoint (atomic write)
- `loom-mill/frontend/src/lib/design/DocumentEditor.svelte:52-75` - current load/sync logic
- `loom-mill/frontend/src/lib/ws.svelte.ts:147-157` - RecordChanged handling
- `loom-mill/src/loom_mill/chat/harness.py` - chat subprocess that modifies files
- `loom-mill/src/loom_mill/state/store.py:90-97` - event publication

## Scope

Write:
- `loom-mill/src/loom_mill/watcher/watcher.py` - extend to watch individual open files, not just `.loom/`
  OR add a dedicated file-content watcher for the Design Room
- `loom-mill/src/loom_mill/api/design.py` - add endpoint to subscribe to file changes
  OR add a new WebSocket event for file content changes
- `loom-mill/src/loom_mill/state/models.py` - add FileContentChanged event type
- `loom-mill/frontend/src/lib/design/DocumentEditor.svelte` - enhanced sync logic with
  content hashing, auto-update, and conflict resolution UI
- `loom-mill/frontend/src/lib/ws.svelte.ts` - handle new file content change events

Read:
- `loom-mill/src/loom_mill/app.py:47-65` - lifespan watcher setup
- `loom-mill/src/loom_mill/api/ws.py` - WebSocket event serialization

Non-goals:
- Do NOT implement OT (operational transform) or CRDT for concurrent editing
- Do NOT watch the entire workspace (only the currently-open file)
- Do NOT add multi-user collaboration features
- Do NOT change the save mechanism (Mod-S explicit save is fine)
- Do NOT add automatic saving on external change detection

### Detailed Design

**Backend: File content change detection**

Option chosen: Extend the existing `LoomWatcher` to accept "additional watch paths"
registered by the frontend when a document is opened. Simpler than a separate watcher.

```python
# In watcher.py - add methods:
class LoomWatcher:
    def __init__(self, ...):
        ...
        self._watched_files: set[Path] = set()
    
    def watch_file(self, path: Path) -> None:
        """Register an additional file path to watch for content changes."""
        self._watched_files.add(path.resolve())
    
    def unwatch_file(self, path: Path) -> None:
        """Stop watching a specific file."""
        self._watched_files.discard(path.resolve())
```

OR (simpler approach): Use polling for the open file since only one file is open at
a time. A lightweight `asyncio.Task` that checks file mtime + content hash every 500ms.

**Chosen approach: Polling with content hash**

Add a new API concept: when the frontend opens a document, it tells the backend
"I'm watching this file" via a new endpoint or WebSocket message. The backend starts
a lightweight poll loop for that file and emits `file_content_changed` events.

Actually, simplest approach: **frontend-driven polling**. The frontend periodically
fetches `GET /records/{id}/content` and compares the content hash. This avoids
backend complexity and uses existing infrastructure.

```
Frontend polling approach:
1. When document opens, start a 1-second interval timer
2. Each tick: fetch GET /records/{id}/content with If-None-Match (content hash)
3. Backend returns 304 if unchanged, 200 with new content if changed
4. On 200: compare with editor content
   - If editor is clean: auto-update editor content
   - If editor is dirty: show conflict banner
5. When document closes or changes, stop timer
```

**Backend: Add ETag/hash support to GET /records/{id}/content:**

```python
async def get_record_content(request: Request) -> Response:
    # ... existing logic ...
    content = path.read_text()
    content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
    
    # Support conditional requests
    if_none_match = request.headers.get("if-none-match")
    if if_none_match and if_none_match.strip('"') == content_hash:
        return Response(status_code=304)
    
    return JSONResponse(
        {"content": content, "hash": content_hash},
        headers={"ETag": f'"{content_hash}"'}
    )
```

**Frontend: DocumentEditor sync enhancement:**

```svelte
// Replace the store.state.records $effect with polling:
let pollInterval: ReturnType<typeof setInterval>;
let lastKnownHash = '';

$effect(() => {
  if (documentPath) {
    // Start polling
    clearInterval(pollInterval);
    pollInterval = setInterval(pollForChanges, 1000);
  } else {
    clearInterval(pollInterval);
  }
  return () => clearInterval(pollInterval);
});

async function pollForChanges() {
  if (!documentPath || loading) return;
  const res = await fetch(apiUrl(`/records/${encodeURIComponent(documentPath)}/content`), {
    headers: lastKnownHash ? { 'If-None-Match': `"${lastKnownHash}"` } : {}
  });
  if (res.status === 304) return; // No change
  if (!res.ok) return;
  
  const data = await res.json();
  lastKnownHash = data.hash;
  
  if (data.content === lastSavedContent) return; // Same as what we saved
  
  if (!modified) {
    // Clean editor: auto-update
    setContent(data.content);
    lastSavedContent = data.content;
  } else {
    // Dirty editor: show conflict
    conflict = true;
    conflictContent = data.content;
  }
}
```

**Conflict resolution UI:**

When `conflict = true`, show a banner at the top of the editor:

```
┌────────────────────────────────────────────────────────────────┐
│ ⚠ File changed externally. You have unsaved local edits.       │
│ [Accept external changes]  [Keep my version]  [View diff]      │
└────────────────────────────────────────────────────────────────┘
```

- "Accept external changes": replaces editor content with disk version, clears modified
- "Keep my version": dismisses banner, keeps local content, user can Mod-S to overwrite
- "View diff": shows a simple inline diff of external vs local (optional, nice-to-have)

## Acceptance

- ACC-001: When a chat subprocess modifies the currently-open file and the editor
  has no local changes, the editor content updates within 2 seconds.
  - Evidence: Open file in editor, trigger chat that modifies it, observe auto-update.
  - Audit: Verify no flicker, scroll position preserved if possible.

- ACC-002: When a file changes externally and the editor HAS unsaved local changes,
  a conflict banner appears with resolution options.
  - Evidence: Modify in editor (don't save), externally change file, observe conflict banner.
  - Audit: Verify neither version is lost; both options work correctly.

- ACC-003: Polling does not cause performance issues (no excessive network requests,
  no editor jank).
  - Evidence: Open editor, verify network tab shows ~1 req/sec, verify editor remains responsive.
  - Audit: Verify 304 responses are lightweight. Verify polling stops when document is closed.

- ACC-004: `npm --prefix loom-mill/frontend run build` passes.
  - Evidence: Build output.

- ACC-005: Backend tests pass (`pytest loom-mill/tests/`).
  - Evidence: Test output.

## Current State

Implementation is complete for the narrowed frontend polling design. Backend
`GET /records/{id}/content` now returns `hash` and `ETag` and supports `304` for
matching `If-None-Match`. `DocumentEditor.svelte` now polls the open document once
per second, auto-updates clean editor state while preserving scroll position, and
shows a conflict banner with "Accept external" and "Keep mine" controls when the
editor has unsaved changes.

Automated evidence is recorded in
`.loom/evidence/20260526-mill-editor-file-sync-validation.md`. Manual browser verification
for ACC-001 through ACC-003 and any audit decision remain the next honest review
steps before closure.

## Journal

- 2026-05-26: Created ticket. Source: operator noticed editor doesn't reflect
  external file changes during chat-driven editing workflow.
- 2026-05-26: Started implementation using the narrowed frontend polling with
  content hash design. Scope follows the later ticket design decision and avoids
  websocket/file-watcher expansion.
- 2026-05-26: Implemented backend content hash/ETag support, frontend polling,
  clean auto-update, dirty conflict banner resolution, and records API test
  coverage for hash/304 behavior. Automated checks passed; moved to review for
  manual browser acceptance and audit posture.
