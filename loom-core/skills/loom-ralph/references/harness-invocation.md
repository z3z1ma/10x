# Harness Invocation

Loom does not prescribe one launch mechanism.

## Acceptable transports

- a harness-native subagent system
- a headless CLI invocation
- a manual fresh-context handoff
- another documented transport stored in `.loom/harness.md`

## What must stay constant

Regardless of transport, preserve:

- the packet file
- the packet's authority as the bounded contract
- the fresh-context nature of the worker
- the explicit output contract

## Prompt guidance

Keep the wrapper prompt short.

Examples:

- "Execute the attached Ralph packet. Stay inside scope and write scope. Return outcome, changed files, evidence, blockers, and next recommendation."
- "Run the attached critique packet. Focus on unsupported claims, hidden risk, and missing follow-through."

Let the packet do the heavy lifting.
