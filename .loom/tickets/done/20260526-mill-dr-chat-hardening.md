# Design Room Chat Hardening + Delight

Status: done
Created: 2026-05-26
Updated: 2026-05-26
Depends-On: .loom/tickets/done/20260526-mill-dr-critical-fixes.md

Legacy note: Risk — low - UI polish on working chat foundation

## Summary

Make the chat panel bulletproof and delightful. Add harness configuration in the
UI (not just defaults), helpful error messages, retry on failure, test mode, and
the micro-interactions that make chatting with the AI feel native and responsive.

## Scope

### 1. Harness Configuration

In the chat header or a small config area:
- Dropdown or input to set the harness command
- Presets: "echo (test)", "opencode run", "claude -p", "codex exec"
- Custom: free-text input for any command
- Persists in localStorage
- "Test Connection" button: sends "ping" and expects "ping" back (echo mode)
- Current harness shown as small badge in chat header

### 2. Better Error Messages

When chat fails, instead of "Failed to send message", show:
- The actual error from stderr (first 200 chars)
- A suggestion: "Check that '{command}' is installed and accessible"
- If the error mentions "not found" or "ENOENT": "Command not found. Is {command} in your PATH?"
- A "Retry" button on the failed message

### 3. Retry on Failure

- Failed messages show a "↻ Retry" button
- Clicking retry re-sends the same message content + context
- The failed error message disappears and a new attempt starts
- After 3 retries, show "Check harness configuration" link

### 4. Input Enhancements

- Character count in bottom-right of input area (e.g., "142 chars")
- Cmd+Enter always sends (even if textarea doesn't have focus but chat panel does)
- Up arrow in empty input fills with last sent message (edit and resend)
- Typing indicator animation when streaming

### 5. Message Polish

- Timestamps on every message (relative: "2m ago", shown inline or on hover)
- Copy button on assistant messages (appears on hover, copies full text)
- Assistant messages render basic markdown (bold, italic, code, links, lists)
- Message grouping: consecutive same-role messages collapse spacing

### 6. Session Indicator

- Show current session info: "Session started 5m ago · 4 messages"
- "New Session" confirms before clearing: "Start fresh? Current conversation will be preserved in history."
- Previous sessions accessible via "History" button (list of past sessions by date)

## Acceptance

- ACC-001: Harness command is configurable via UI; presets offered; persists in localStorage
- ACC-002: Error messages show actual stderr content and actionable suggestions
- ACC-003: "Retry" button on failed messages re-sends the original content
- ACC-004: Cmd+Enter sends from anywhere in the chat panel
- ACC-005: Copy button appears on hover over assistant messages
- ACC-006: Timestamps show on all messages
- ACC-007: "Test Connection" with echo mode succeeds and shows confirmation

## Journal

- 2026-05-26: Created. Chat must be bulletproof for operators to trust it as
  their primary shaping interface. Error messages must be helpful, not cryptic.
