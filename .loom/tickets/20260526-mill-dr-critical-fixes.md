# Design Room Critical Bug Fixes

ID: ticket:20260526-mill-dr-critical-fixes
Type: Ticket
Status: open
Created: 2026-05-26
Updated: 2026-05-26
Risk: medium - harness subprocess invocation is the root cause of the chat failure

Priority: high - chat is completely broken, undo doesn't work

## Summary

Three critical bugs make the Design Room unusable in its current state:
1. Chat fails with "Failed to send message" because `harness.py` uses `-m` flag
   that doesn't exist for `opencode run`.
2. Ctrl+Z doesn't undo because `history()` extension is missing from CodeMirror.
3. Text selection on a single line has invisible/low-contrast background.
4. Long lines scroll horizontally (no word wrap).

## Scope

### Backend Fix (`loom-mill/src/loom_mill/chat/harness.py`)

The current code does:
```python
if "opencode" in args[0]:
    args.extend(["-m", prompt])
```

This is wrong. `opencode run` doesn't have `-m`. The fix:
- For any harness: pipe the prompt to stdin by default.
- The subprocess should receive the full prompt on stdin and produce output on stdout.
- Add an "echo" test mode: if harness_command is "echo", just echo the prompt back
  (useful for testing without a real AI).
- Add better error reporting: capture stderr and include it in the error response.

```python
async def run_harness(command, prompt, session_id, broadcast_fn):
    args = shlex.split(command)
    
    # Special test mode
    if args[0] == "echo":
        await broadcast_fn({"event": "chat_stream", "data": {"session_id": session_id, "delta": prompt, "done": False}})
        await broadcast_fn({"event": "chat_complete", "data": {"session_id": session_id, "message": {"role": "assistant", "content": prompt}}})
        return prompt
    
    proc = await asyncio.create_subprocess_exec(
        *args,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=os.getcwd(),
    )
    
    # Write prompt to stdin
    proc.stdin.write(prompt.encode("utf-8"))
    await proc.stdin.drain()
    proc.stdin.close()
    
    # Stream stdout...
```

### Frontend Fix (`DocumentEditor.svelte`)

Add missing CodeMirror extensions:
```typescript
import { history, historyKeymap } from '@codemirror/commands';

// In extensions array:
history(),
keymap.of([...defaultKeymap, ...historyKeymap, ...searchKeymap, indentWithTab]),
EditorView.lineWrapping,  // word wrap
```

### Theme Fix (`editor-theme.ts`)

Fix selection background for single-line:
```typescript
'.cm-selectionBackground': { 
  backgroundColor: 'rgba(99, 102, 241, 0.25) !important'  // more visible
},
'&.cm-focused .cm-selectionBackground': {
  backgroundColor: 'rgba(99, 102, 241, 0.3) !important'
},
```

## Acceptance

- ACC-001: Sending "hello" in chat with harness_command="echo" returns "hello" as response
- ACC-002: Ctrl+Z undoes the last edit in the editor
- ACC-003: Selecting text on a single line shows visible background highlight
- ACC-004: Long lines wrap instead of scrolling horizontally
- ACC-005: Backend tests pass

## Current State

Ready to start. The fixes are small and targeted.

## Journal

- 2026-05-26: Created. Chat failure root cause: invalid `-m` flag on opencode.
  Editor issues: missing history() extension and lineWrapping.
