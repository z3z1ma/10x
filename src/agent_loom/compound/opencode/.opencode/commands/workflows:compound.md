---
description: Compound -> extract reusable patterns into skills + memory, update docs and changelog.
agent: build
subtask: false
---

You are running the **Compound** phase.

Ticket (if applicable):
$ARGUMENTS

This is where we convert “we learned a thing” into **procedural memory**.

Goals:
- Store recallable memory notes (loom memory) so future planning retrieves them automatically.
- Create/update skills under `.opencode/skills/` (and mirror to `.claude/skills/`).
- Update AI-managed blocks in AGENTS + LOOM docs.
- Append an agent-optimized entry to LOOM_ROADMAP.

Process:
1) Ensure compound scaffolding exists:
   - Run via bash: `loom compound init --dest .`
2) Gather context:
   - Run via bash: `git status --porcelain` and `git diff --stat`
   - If a ticket ID was provided, `loom ticket show $ARGUMENTS`
3) Write 1-5 memory notes using Loom directly:
   - Run via bash: `loom memory add --title ... --body ... --tag ... --scope command:workflows:plan`
4) Create/update skills using Loom:
   - Run via bash: `loom compound skill upsert <name> --description ... --body "..."` (or pipe stdin)
5) Create/update instincts using Loom (only if the heuristic is durable):
   - Run via bash: `loom compound instinct upsert create|update <id> ...`
6) Update allowed doc blocks using Loom:
   - Run via bash: `loom compound docblock upsert --file AGENTS.md --id loom-core-context --content "..."`
   - Run via bash: `loom compound docblock upsert --file LOOM_ROADMAP.md --id roadmap-ai-notes --content "..."`
7) Append a short changelog entry using Loom:
   - Run via bash: `loom compound changelog append --note "..."`
8) Finish by refreshing derived compound docs:
   - Run via bash: `loom compound refresh`

Required output:
- A short “Compound report” section (what we learned).
- A short list of changes applied (skills/instincts/docs/memos).
