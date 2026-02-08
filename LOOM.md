<!-- BEGIN:compound:agents-ai-behavior -->
# Compound Engineering Baseline

This block is maintained by the compound system.

**Core loop:** Plan -> Work -> Review -> Compound -> Repeat.

**Memory model:**
- **Observations** are logged automatically from tool calls and session events.
- **Instincts** are small heuristics extracted from observations.
- **Skills** are durable procedural memory (directory + SKILL.md) and are the primary compounding mechanism.
- **Episodes** are immutable evidence capsules. If a patch is too large to inline, the full patch is stored as a blob.
- **Decisions** are append-only records of normalized ops applied to instincts/skills (governance; replayable).

**Non-negotiables:**
- Keep skills small, specific, and triggerable from the `description`.
- Prefer updating an existing skill over creating a near-duplicate.
- Never put secrets into skills, memos, or observations.

**Where things live:**
- Boundary: `.loom/**` is Loom-owned durable evidence + compiled state; `.opencode/**` is OpenCode integration + runtime artifacts (including skills).
- Skills: `.opencode/skills/<name>/SKILL.md`
- Instincts: `.loom/compound/instincts.json` (index at `.loom/compound/INSTINCTS.md`)
- Observations: `.opencode/memory/observations.jsonl` (gitignored by default)
- Episodes: `.loom/compound/episodes/YYYY/MM/<episode_id>.json` (committed evidence)
- Blobs: `.loom/compound/blobs/<sha256>.<ext>` (full patches, raw proposals, prompt snapshots)
- Decisions: `.loom/compound/decisions/YYYY/MM/<decision_id>.json` (append-only ops log)

**Core docs:**
- `AGENTS.md` (stable human-owned overview)
- `LOOM.md` (derived always-on context + instincts summary)
- `.loom/compound/ROADMAP.md` (direction + backlog + changelog)
<!-- END:compound:agents-ai-behavior -->

<!-- BEGIN:compound:loom-commands -->
- `/loom-plan` - Create tickets + plan (uses `loom memory recall`)
- `/loom-work` - Work in a worktree and implement
- `/loom-review` - Review changes before merge
- `/loom-compound` - Capture durable learnings (memos + skills)
<!-- END:compound:loom-commands -->

<!-- BEGIN:compound:loom-core-context -->
# Loom always-on context (second-order compression)

This block is Loom's AI-managed "operating manual": short, sticky, and updated only when a principle proves durable.

- First-order: observations -> instincts -> skills.
- Second-order: compress patterns into a few fundamentals that are always-on.
- Prefer agent-native primitives: ticket, memory, workspace, team.
- Governance loop: Plan -> Work -> Review -> Compound -> Repeat.
- When the system learns something structural, it should update this manual (not just add a memo).

@.loom/compound/ROADMAP.md
<!-- END:compound:loom-core-context -->

<!-- BEGIN:compound:instincts-index -->
- **avoid-tooling-artifacts-in-templates** (90%) [compound, hygiene, templates]
  - Trigger: When adding or reviewing files under template trees like src/agent_loom/compound/opencode/ (or other scaffolded outputs).
  - Action: Exclude tool-specific project files (e.g., `.serena/*`, local IDE metadata, assistant-runner configs) from templates and committed scaffolds unless they are a deliberate product feature; prefer removi...
- **compound-template-determinism-first** (82%) [compound, determinism, templates, tests]
  - Trigger: When changing compound scaffold/template contents or compound install logic (e.g., src/agent_loom/compound/scaffold.py, src/agent_loom/compound/paths.py, src/agent_loom/compound/docs.py, compound open...
  - Action: Treat the installed `.opencode/` (and any `.loom/compound/` docs) as a contract: preserve stable paths, stable file ordering, stable newline formatting, and stable rendered content; immediately update...
- **template-docs-use-root-relative-paths** (78%) [compound, docs, portability]
  - Trigger: When editing README/docs content that will be scaffolded into a repo (e.g., src/agent_loom/compound/opencode/README.md, src/agent_loom/compound/opencode/.loom/compound/README.md, `.opencode/commands/*...
  - Action: Write links and references using repo-root-relative paths (no absolute machine paths, no editor URIs) and avoid references to removed/retired template files (e.g., AGENTS.md copies) to keep docs porta...
- **prefer-command-docs-over-embedded-skill-copies** (74%) [commands, compound, docs, skills]
  - Trigger: When documenting workflows for end-users inside compound-installed `.opencode/` trees.
  - Action: Put loom command guidance in `.opencode/commands/loom-*.md` (command-discoverable docs) and avoid duplicating full skill content inside the compound template unless required; keep skills procedural an...
<!-- END:compound:instincts-index -->
