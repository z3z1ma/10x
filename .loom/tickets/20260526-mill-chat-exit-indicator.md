# Chat Subprocess Exit Indicator

ID: ticket:20260526-mill-chat-exit-indicator
Type: Ticket
Status: closed
Created: 2026-05-26
Updated: 2026-05-26
Risk: low - small backend event payload addition plus frontend UI state/rendering

## Summary

When a Design Room chat subprocess finishes, there's no visible indicator that it
exited. The streaming indicator just disappears and the response message appears.
The operator knows the subprocess exited (exit code 0) but the UI doesn't reflect
this boundary.

Current flow:
1. User sends message → "Generating response..." indicator
2. Streaming content appears character by character
3. `chat_complete` event arrives → streaming stops, final message renders
4. No explicit "Done" / "Exit: 0" / boundary marker

The fix: Add a subtle system message or badge after the assistant's response that
shows the subprocess exit status. This provides clear closure for each chat turn.

Closure claim: Users can clearly see when the chat subprocess has finished, what
exit code it returned, and optionally how long it took.

## Related Records

- `plan:20260526-mill-factory-data-integrity` - parent plan
- `loom-mill/src/loom_mill/chat/harness.py:36-83` - emits chat_complete with exit status
- `loom-mill/src/loom_mill/api/design.py:205-239` - chat message endpoint
- `loom-mill/frontend/src/lib/ws.svelte.ts:164-190` - chat_complete/chat_error handling
- `loom-mill/frontend/src/lib/design/ChatPanel.svelte` - chat UI
- `loom-mill/frontend/src/lib/design/ChatMessage.svelte` - message rendering

## Scope

Write:
- `loom-mill/frontend/src/lib/design/ChatPanel.svelte` - add exit indicator after assistant response
- `loom-mill/frontend/src/lib/design/ChatMessage.svelte` - optionally add exit badge to last message
- `loom-mill/frontend/src/lib/ws.svelte.ts` - store exit_code from chat_complete event
- `loom-mill/src/loom_mill/chat/harness.py` - ensure exit_code is included in chat_complete payload
- `loom-mill/src/loom_mill/api/design.py` - pass exit_code through to chat event

Non-goals:
- Do NOT change the streaming behavior
- Do NOT add subprocess duration tracking (nice-to-have for a future pass)
- Do NOT change the echo mode response behavior; echo completions report exit code 0
- Do NOT add a "restart subprocess" button (future work)

### Detailed Design

**Backend: Include exit_code in chat_complete event**

Check if `chat_complete` already includes exit_code. From `harness.py:72-79`:
```python
yield {"event": "chat_complete", "data": {
    "session_id": session_id,
    "message": {"role": "assistant", "content": full_output, "timestamp": ...}
}}
```

Need to add `exit_code` to the data payload:
```python
yield {"event": "chat_complete", "data": {
    "session_id": session_id,
    "exit_code": proc.returncode,
    "message": {"role": "assistant", "content": full_output, "timestamp": ...}
}}
```

**Frontend: Store and display exit info**

In `ws.svelte.ts`, when handling `chat_complete`:
```typescript
case 'chat_complete':
  if (data.session_id === this.chatSession.id) {
    this.chatSession = {
      ...this.chatSession,
      streaming: false,
      lastExitCode: data.exit_code ?? null,  // NEW
      messages: [...this.chatSession.messages, data.message],
      streamingContent: ''
    };
  }
  break;
```

**UI: Exit indicator in ChatPanel**

After the last assistant message, when `streaming === false` and `lastExitCode !== null`,
show a subtle divider/badge:

```
─── Session completed · Exit: 0 ───
```

Design:
- Centered text with thin horizontal lines on each side
- Text: "Session completed · Exit: 0" (green for 0, red for non-zero)
- Font: 10px, text-tertiary color
- Appears below the assistant's response
- Disappears when the user sends a new message (resets for next turn)

For errors (non-zero exit), the existing `chat_error` handler already shows an error.
But we can enhance it:
```
─── Session failed · Exit: 1 ───
```

**Alternative simpler design**: Instead of a separate element, add a small badge
to the bottom-right of the assistant message bubble itself:

```
┌─────────────────────────────────────┐
│ Here's the updated file with the    │
│ changes you requested...            │
│                          ✓ Exit: 0  │
└─────────────────────────────────────┘
```

Recommend: the divider approach since it's clearer as a session boundary.

## Acceptance

- ACC-001: After a chat subprocess completes with exit 0, a "Session completed" indicator
  with the exit code appears below the assistant's response.
  - Evidence: Send a chat message, wait for completion, observe exit indicator.
  - Audit: Verify exit code value matches the actual subprocess exit code.

- ACC-002: After a chat subprocess fails with non-zero exit, the error indicator
  clearly shows the exit code.
  - Evidence: Trigger a failing subprocess, observe error indicator with exit code.
  - Audit: Verify it's visually distinct from success (red vs green).

- ACC-003: The exit indicator does not appear during streaming and does appear for the echo harness with exit code 0.
  - Evidence: Send a message in echo mode, verify exit indicator after completion. Start streaming, verify no premature exit indicator.
  - Audit: Verify echo mode is handled cleanly.

- ACC-004: `npm --prefix loom-mill/frontend run build` passes.
  - Evidence: Build output.

## Current State

Implementation complete and awaiting any desired final review. Backend `chat_complete` now includes `exit_code` for echo and successful subprocess completions. Frontend stores `lastExitCode`, clears it when a new message is sent or a new session starts, and renders the subtle divider only after a completed assistant message. Frontend build passed; backend pytest could not run because `pytest` is not installed for the active Python interpreter.

Evidence: `evidence:20260526-mill-chat-exit-indicator-validation`

## Journal

- 2026-05-26: Created ticket. Source: operator observed subprocess exiting with
  exit code 0 but no clear UI indicator of completion.
- 2026-05-26: Started implementation. Operator clarified echo mode should also report `Exit: 0`; updated acceptance and non-goal accordingly.
- 2026-05-26: Implemented exit code payload, frontend state reset/storage, and completion divider. Verified frontend build and `git diff --check`; backend pytest is blocked by missing `pytest` module in the active Python environment. Recorded validation in `evidence:20260526-mill-chat-exit-indicator-validation`.
