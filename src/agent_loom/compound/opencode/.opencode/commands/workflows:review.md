---
description: Review -> multi-angle code review before merge, update tickets with findings.
agent: build
subtask: false
---

You are running the **Review** phase.

Ticket:
$ARGUMENTS

Goals:
- Review changes for correctness, security, performance, and docs.
- Record required follow-ups back into the ticket.

Process:
1) Ensure compound scaffolding exists:
   - Run via bash: `loom compound init --dest .`
2) Gather context:
   - `loom ticket show $ARGUMENTS`
   - Run via bash: `git status --porcelain` and `git diff --stat`
3) If the OpenCode `task` tool is available, run three subreviews (subagents):
   - agent: `review-quality`
   - agent: `review-security`
   - agent: `review-docs`
   Provide them the diff summary + ticket details.
   If `task` is not available, do a single-agent review with those lenses.
4) Synthesize findings into:
   - must-fix
   - should-fix
   - nice-to-have
5) Update the ticket:
   - add notes
   - create new tickets if issues are substantial
6) Finish by refreshing derived compound docs:
   - Run via bash: `loom compound refresh`

Output:
- Review summary.
- Concrete, prioritized findings.
- Ticket updates performed.
