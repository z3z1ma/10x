# Design Room: Chat Experience Overhaul

Status: done
Created: 2026-05-26
Updated: 2026-05-26

Legacy note: Risk — low - backend echo fix is trivial; frontend is UI polish

Priority: high - chat is the primary interaction model and currently feels broken

## Summary

The chat experience has three problems that make it feel broken and unprofessional:

1. **Echo mode dumps the entire internal prompt** including system instructions,
   conversation history, and document content. This is jarring and useless for
   testing. Echo should mirror ONLY the user's message.

2. **No streaming/subprocess indicator.** When you send a message, there's nothing
   showing that work is happening. The response just appears after a delay (or the
   error appears). There must be a visible "Thinking..." indicator while the
   subprocess runs.

3. **Response appears truncated.** The echo code has `prompt[:500]` which cuts off
   long prompts arbitrarily. The full response should be shown.

4. **Harness config is too prominent.** The harness selector takes a full row above
   the chat, stealing vertical space from messages. It should be more compact.

## Scope

### Backend Fix (`loom-mill/src/loom_mill/chat/harness.py`)

Change the echo mode to return ONLY the user's message, not the full prompt:

```python
# Current (broken):
response = f"[echo] {prompt[:500]}"

# Fix: Accept user_message as separate parameter for echo mode
async def run_harness(command, prompt, session_id, broadcast_fn, *, user_message=None):
    args = shlex.split(command)
    
    if args[0] == "echo":
        # Echo mode: just mirror the user's message, useful for testing the pipeline
        echo_text = user_message or prompt
        await broadcast_fn({"event": "chat_stream", "data": {"session_id": session_id, "delta": echo_text, "done": False}})
        await broadcast_fn({"event": "chat_complete", "data": {"session_id": session_id, "message": {"role": "assistant", "content": echo_text}}})
        return echo_text
    # ... rest unchanged
```

Update the caller in `design.py` to pass `user_message=content` alongside the full prompt.

### Frontend: Streaming Indicator (`ChatPanel.svelte`)

When `store.chatSession.streaming` is true (after send, before complete/error):
- Show a "thinking" indicator in the message area:
  ```svelte
  {#if store.chatSession.streaming && !store.chatSession.streamingContent}
    <div class="flex items-center gap-2 px-4 py-3 text-[11px] text-text-tertiary">
      <span class="flex gap-0.5">
        <span class="w-1.5 h-1.5 rounded-full bg-accent-primary animate-bounce" style="animation-delay: 0ms"></span>
        <span class="w-1.5 h-1.5 rounded-full bg-accent-primary animate-bounce" style="animation-delay: 150ms"></span>
        <span class="w-1.5 h-1.5 rounded-full bg-accent-primary animate-bounce" style="animation-delay: 300ms"></span>
      </span>
      <span>Generating response...</span>
    </div>
  {/if}
  ```

- Also add a subtle "streaming" state to the input area: disable the textarea and
  show the send button as a stop button (■ square icon) that could cancel the stream.

### Frontend: Compact Harness Config

Move the harness selector INTO the chat header row instead of a separate full-width row:

```svelte
<!-- Before: separate row -->
<!-- After: inline in header -->
<div class="flex items-center h-8 px-3 border-b border-border-default text-[11px]">
  <span class="font-medium text-text-secondary">Chat</span>
  <span class="ml-2 text-text-quaternary">·</span>
  <select bind:value={harnessCommand} class="ml-1 bg-transparent text-[10px] text-text-tertiary border-none focus:outline-none">
    <option value="echo">echo</option>
    <option value="opencode run">opencode</option>
    <option value="claude -p">claude</option>
  </select>
  <span class="ml-auto text-[10px] text-text-quaternary">
    {store.chatSession.messages.length} msgs
  </span>
  <button class="ml-2 text-[10px] text-text-tertiary hover:text-accent-primary">New</button>
</div>
```

This saves ~32px of vertical space for actual messages.

## Acceptance

- ACC-001: Echo mode returns ONLY the user's message text (no system prompt, no history, no document content)
  - Evidence: Send "hello" in echo mode → response is exactly "hello"
  - Audit: Verify harness.py echo path uses user_message parameter

- ACC-002: Animated "Generating..." indicator shows while waiting for response
  - Evidence: Send message → 3 bouncing dots + "Generating response..." appears immediately
  - Audit: Verify indicator disappears when chat_complete or chat_error arrives

- ACC-003: No response truncation - full content displayed regardless of length
  - Evidence: Send a 1000-char message in echo mode → full text returned
  - Audit: Verify no [:500] or similar slicing

- ACC-004: Harness selector is inline in header row (not a separate full-width row)
  - Evidence: Playwright screenshot showing compact header with inline selector
  - Audit: Verify vertical space saved (~32px)

- ACC-005: Backend tests pass
  - Evidence: pytest output
  - Audit: No regressions

## Journal

- 2026-05-26: Created. The echo dumping the full prompt is the most jarring issue -
  makes it look like the system is broken when it's actually working correctly
  but showing internals.
