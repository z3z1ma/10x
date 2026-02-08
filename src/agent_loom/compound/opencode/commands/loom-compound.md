---
description: Loom Compound -> capture durable learnings (memos + skills) from recent work.
agent: build
subtask: false
---

You are running **Loom Compound**.

Ticket (if applicable):
$ARGUMENTS

This is where we convert "we learned a thing" into durable, replayable memory.

Goals:
- Package evidence into an Episode under `.loom/compound/episodes/...`.
- Compile/update instincts in `.loom/compound/instincts.json`.
- Compile/update skills under `.opencode/skills/` (optional mirror to `.claude/skills/`).
- Store a few Loom Memory notes when the learning is contextual or narrative.

Process:
1) If compound scaffolding isn't installed yet, install it once:
   - Run via bash: `loom compound init`
2) Gather context:
   - Run via bash: `git status --porcelain` and `git diff --stat`
   - If a ticket ID was provided: `loom ticket show $ARGUMENTS`
3) Decide what to persist:
   - If the learning is contextual ("why" / history), store a memo:
     - `loom memory add --title "..." --body "..." --tag compound --scope repo:.`
   - If the learning is procedural ("how" / repeatable), propose a Skill and apply via `learn`.
   - If there's nothing durable, stop. Don't force churn.
4) Apply procedural learnings (optional, deterministic):
   - Prepare a JSON object with:
     - `instinct_candidates`: `{id,title,trigger,action,confidence,tags}`
     - `skill_candidates`: `{name,description,body,tags,source_instinct_ids}`
   - Run via bash: `loom compound learn --proposals '<json>'`

Optional:
- `loom compound refresh` (refresh derived docs)

Required output:
- A short "Compound report" section (what we learned).
- A short list of changes applied (episode/instincts/skills/memos).
