---
description: Loom Compound learning workflow (observe -> instincts -> evolve).
agent: build
subtask: false
---

You are running **Loom Compound**.

Ticket (if applicable):
$ARGUMENTS

Goals:
- Keep observations flowing into `.loom/compound/runtime/observations.jsonl`.
- Keep instincts current in `.loom/compound/instincts/local/*.md`.
- Promote stable instincts into generated artifacts when justified.

Process:
1) Ensure scaffold exists:
   - `loom compound init`
2) Capture/compile:
   - `loom compound observer run-once --json`
   - `loom compound instinct-status --json`
3) Share instincts when useful:
   - `loom compound instinct-export --out .loom/compound/instincts-export.json`
4) Optional generation:
   - `loom compound evolve --generate --json`

Required output:
- Short compound report with instincts learned/updated.
- Any generated artifact paths.
