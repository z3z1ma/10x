# INSTINCTS

This is the *fast index* of the current instinct set.
The source of truth is `.opencode/memory/instincts.json`.

<!-- BEGIN:compound:instincts-md -->
## Active instincts (top confidence)

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
  - Action: Put workflow guidance in `.opencode/commands/workflow-*.md` (command-discoverable docs) and avoid duplicating full skill content inside the compound template unless required; keep skills procedural an...

## Notes

- Instincts are the pre-skill layer: small, repeatable heuristics.
- When an instinct proves useful across sessions, promote it into a Skill.
<!-- END:compound:instincts-md -->
