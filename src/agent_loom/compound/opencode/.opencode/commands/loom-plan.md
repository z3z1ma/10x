---
description: Loom Plan -> create tickets and an implementation plan (use memory recall).
agent: plan
subtask: false
---

You are running **Loom Plan**.

User idea / request:
$ARGUMENTS

Goals:
- Turn the idea into ticketed intent plus an executable plan.
- Pull in relevant prior learnings (memory/skills) so we don't relearn basics.
- Do not implement code in this phase.

Process:
1) If compound scaffolding isn't installed yet, install it once:
   - Run via bash: `loom compound init`
2) Recall memory notes relevant to this request:
   - `loom memory recall "$ARGUMENTS" --command loom-plan --format prompt`
3) Inspect current ticket backlog:
   - `loom ticket list`
4) Create tickets:
   - 1 epic ticket (outcome + acceptance criteria)
   - N task tickets (small, sequential)
   - add deps if sequencing matters
5) Write the plan:
   - ticket IDs + titles
   - sequencing
   - checks/tests
   - risks + rollback

Optional:
- `loom compound refresh` (refresh derived docs)

Output:
- A concise plan document.
- A list of created/updated ticket IDs.
