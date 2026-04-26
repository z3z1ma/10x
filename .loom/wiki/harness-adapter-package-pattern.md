---
id: wiki:harness-adapter-package-pattern
kind: wiki
page_type: workflow
status: active
created_at: 2026-04-25T22:14:57Z
updated_at: 2026-04-26T01:04:44Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:install-experience-harness-adapters
  spec:
    - spec:opencode-plugin-install-contract
  ticket:
    - ticket:6uy1rx20
    - ticket:q7h1d05q
    - ticket:cldrel01
  evidence:
    - evidence:open-loom-smoke
    - evidence:claude-plugin-hybrid
  critique:
    - critique:open-loom-config-hook-review
    - critique:claude-plugin-integration-review
  research:
    - research:loom-install-distribution-methods
---

# Summary

Adapter packages are harness-native packaging surfaces that make Loom easier to
install without becoming owners of Loom semantics.

`open-loom@0.1.0` is the first accepted example in this repository: an OpenCode
npm plugin that exposes bundled Loom rules, skills, and optional command wrappers
through OpenCode config surfaces.

Claude Code is the first accepted hybrid example: a Claude plugin exposes skills
and command wrappers, while a plugin hook generates one static `loom.md` file into
Claude's documented rule surface and blocks the first unsafe prompt until a new
session loads that rule file.

# When To Use It

Use this pattern when a harness has a first-class package, plugin, or extension
mechanism that can expose Loom's required surfaces more cleanly than direct
user-config mutation.

Do not use this pattern when the harness package system cannot express ordered
always-on rules, skill discovery, or command wrappers without a separate fallback.
In that case, use a hybrid install and document the split.

Use the hybrid form when the harness package can carry some Loom surfaces but not
all of them. The package should still improve installation, but the missing
surface must be synchronized into a documented harness-owned surface, not hidden
inside hook stdout or a custom agent prompt.

# Inputs

- canonical top-level `rules/`, `skills/`, and optional `commands/`
- the harness's official package/plugin/extension docs
- a ticket that owns one bounded harness install slice
- evidence for package structure, install behavior, and surface discovery
- critique for operator clarity and release-packaging risk

# Procedure

1. Start from the canonical Loom surfaces. Do not copy dogfooding `.loom/` or
   `.opencode/` state into the package.
2. Choose the smallest harness-native registration path that exposes rules,
   skills, and commands.
3. Keep generated files derivative and source-marked when generation is required.
4. Declare compatibility metadata when the package manager or harness supports it.
5. Validate package layout before publication or release.
6. Validate harness loading through the harness's own debug, install, link, or
   discovery commands when available.
7. Record install caveats as evidence and either accept them explicitly or create
   follow-up tickets.
8. Update install docs only after evidence supports the recommendation.

# Hybrid Adapter Procedure

Use this procedure when a harness plugin/package cannot own every Loom surface.

1. Name which Loom surfaces the package can natively expose and which it cannot.
2. Route the missing surface to a documented static harness surface.
3. Keep generated outputs derivative from canonical `rules/`, `skills/`, and
   optional `commands/`.
4. Prefer one generated ordered rule file when the harness does not document
   ordering across multiple rule files.
5. Treat hooks as installers or guards, not as the static knowledge channel.
6. Fail closed when a bootstrap sync changes instructions after the session has
   already loaded context.
7. Validate both manifest shape and real install/load behavior; schema validation
   alone is not enough.
8. Keep disable/uninstall cleanup explicit when the harness provides no lifecycle
   hook.

# Claude Hybrid Example

The accepted Claude prototype uses this split:

- `.claude-plugin/plugin.json` exposes canonical `skills/` and optional
  `commands/`.
- `.claude-plugin/marketplace.json` exposes local marketplace `agent-loom` with
  plugin `loom` sourced from `./` for local/prototype installs.
- Claude auto-loads the standard plugin `hooks/hooks.json`; the manifest should
  not duplicate that standard hook path.
- `SessionStart` runs `scripts/claude-sync-rules.sh`, which generates one managed
  `loom.md` from canonical `rules/*.md` into user or project
  `.claude/rules/loom/`.
- Project-local sync requires an explicit project settings `enabledPlugins` entry
  for Loom; `.claude/` directory existence alone is not a project install signal.
- `UserPromptSubmit` runs `scripts/claude-loom-restart-guard.sh`, which blocks
  prompts when sync failed, sync is pending, or rules were just installed after
  Claude loaded instructions.
- `scripts/claude-clean-rules.sh` is the explicit cleanup path because Claude docs
  do not describe an uninstall lifecycle hook.

The important accepted limitation is the two-session bootstrap: the first
plugin-enabled session can install `loom.md`, but Claude loads it on the next
session. The guard prevents the first prompt from reaching the model when the
session just installed or updated Loom rules.

# Outputs

- package or adapter entrypoint files
- package metadata and compatibility range
- install docs and adapter fixture notes
- evidence record for package contents and harness loading
- critique record or disposition for release-packaging risk
- ticket acceptance decision with residual risks or linked follow-ups

# Failure Modes

- treating package files as the new canonical Loom source
- recommending a plugin path before the harness actually loads the package
- hiding a required fallback step behind plugin-first marketing
- publishing docs that point at files omitted from the package
- claiming cold-cache or first-run behavior works when only warm-cache behavior
  was observed
- overgeneralizing one harness's plugin behavior to other harnesses
- assuming plugin schema validation proves installed plugin behavior
- declaring a standard auto-loaded hook file in the plugin manifest and causing a
  duplicate hook-load error
- treating `${CLAUDE_PLUGIN_ROOT}` as the user's or project's `.claude` directory
- selecting project-local install scope because `.claude/` exists instead of
  because the plugin is explicitly enabled for that project
- relying on hook stdout or a custom agent prompt as the always-on rule layer
- proceeding after a bootstrap sync even though the harness loaded instructions
  before generated rules existed

# Sources

- `spec:opencode-plugin-install-contract`
- `ticket:6uy1rx20`
- `ticket:us1brnsv`
- `ticket:q7h1d05q`
- `ticket:cldrel01`
- `evidence:open-loom-smoke`
- `evidence:claude-plugin-hybrid`
- `critique:open-loom-config-hook-review`
- `critique:claude-plugin-integration-review`
- `research:loom-install-distribution-methods`
- `plan:install-experience-harness-adapters`
- `initiative:loom-install-experience`

# Related Pages

Future Cursor, Gemini, and Codex package work should link here only after their
harness-specific evidence is recorded. Claude and OpenCode are accepted examples
with linked ticket, evidence, and critique records.
