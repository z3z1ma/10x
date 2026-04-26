---
id: evidence:claude-plugin-hybrid
kind: evidence
status: recorded
created_at: 2026-04-25T22:48:07Z
updated_at: 2026-04-26T00:59:31Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:q7h1d05q
  plan:
    - plan:install-experience-harness-adapters
  research:
    - research:loom-install-distribution-methods
  critique:
    - critique:claude-plugin-integration-review
external_refs:
  claude_code_docs:
    - https://code.claude.com/docs/en/plugins
    - https://code.claude.com/docs/en/plugins-reference
    - https://code.claude.com/docs/en/settings
    - https://code.claude.com/docs/en/memory
    - https://code.claude.com/docs/en/skills
    - https://code.claude.com/docs/en/hooks
    - https://code.claude.com/docs/en/plugin-marketplaces
---

# Summary

Structural evidence for the automated Claude Code hybrid plugin prototype.

The observed shape is: `.claude-plugin/plugin.json` exposes Loom's canonical
`skills/` and optional `commands/` directories as Claude plugin components.
`.claude-plugin/marketplace.json` exposes the repository as a local marketplace
named `agent-loom`. A plugin `SessionStart` hook runs
`scripts/claude-sync-rules.sh` to generate `loom.md` from bundled canonical
`rules/*.md` under `${CLAUDE_PLUGIN_ROOT}/rules` into a Claude-loaded rule
surface: project/local `.claude/rules/loom/` when the current project's Claude
settings enable the `loom` plugin, otherwise user-level `~/.claude/rules/loom/`.
When that sync changes files for the current session, a `UserPromptSubmit` hook
runs `scripts/claude-loom-restart-guard.sh` to block prompts until the user starts
a new session where the rules are loaded.

# Procedure

- Re-checked current Claude Code docs for plugins, plugin reference, settings,
  memory, skills, and hooks.
- Added `.claude-plugin/plugin.json` pointing `skills` at `./skills/` and
  `commands` at `./commands/`. Claude loads standard plugin `hooks/hooks.json`
  automatically, so the manifest does not repeat that path.
- Added `.claude-plugin/marketplace.json` with marketplace `agent-loom` and plugin
  `loom` sourced from `./`.
- Added `hooks/hooks.json` with a `SessionStart` command hook for
  `${CLAUDE_PLUGIN_ROOT}/scripts/claude-sync-rules.sh`.
- Added `hooks/hooks.json` with a `UserPromptSubmit` command hook for
  `${CLAUDE_PLUGIN_ROOT}/scripts/claude-loom-restart-guard.sh`.
- Added `scripts/claude-sync-rules.sh`, which generates one managed `loom.md`
  from canonical `rules/*.md`, writes it into a scope-appropriate Claude rule
  directory, writes a managed manifest for stale-file cleanup, and fails closed
  through guard-readable markers for unsafe or failed sync states.
- Added `scripts/claude-loom-restart-guard.sh`, which blocks user prompts when the
  current session has a restart-required marker from rule synchronization.
- Added `scripts/claude-clean-rules.sh`, which removes managed generated rule
  files for explicit user/project cleanup.
- Added `examples/adapters/claude-plugin-install/README.md` to describe the
  hybrid fixture and its limitations.
- Ran `claude plugin validate .` from the repository root.
- Ran the sync script under a temporary `HOME` and verified generated `loom.md`
  plus a one-line managed manifest in `~/.claude/rules/loom/`.
- Ran the sync script with a temporary `CLAUDE_PROJECT_DIR` containing
  `.claude/settings.json` with `{"enabledPlugins":{"loom@test":true}}`, and
  verified generated `loom.md` plus a one-line managed manifest in the project
  `.claude/rules/loom/` without writing user-level rules.
- Ran the sync script in a temporary project with `.claude/settings.json` that did
  not enable `loom` and verified it kept using the existing user-level rule sync
  instead of writing project-local rules.
- Ran the sync script twice against an already-current user-level install and
  verified the generated rule file's mtime stayed unchanged.
- Ran script-level failure/safety probes for missing source rules, unmanaged extra
  destination `.md` files, symlinked destinations, unsafe manifest entries, old
  managed-file cleanup, and explicit cleanup.
- Ran follow-up safety probes for symlinked `loom.md`, symlinked manifest,
  symlinked parent directories before `mkdir -p`, non-regular manifest paths,
  pending markers, and normal sync after hardening.
- Ran three oracle critique passes and recorded the final review in
  `critique:claude-plugin-integration-review`.
- Ran local marketplace add/install in a temporary `HOME`; removing the duplicate
  `hooks` manifest field resolved the marketplace install hook-load error.
- Re-ran runtime first-session guard and second-session load probes after removing
  the duplicate `hooks` manifest field.
- Ran final post-marketplace-install oracle critique; no local/prototype blockers
  remained.
- Ran isolated Claude Code `-p` probes with the real `HOME` for auth but with
  `~/.claude/rules` temporarily moved aside. A temporary project enabled
  `loom@test` in `.claude/settings.json` and loaded the local plugin with
  `--plugin-dir`.
- Re-ran the isolated first-session probe after adding the restart guard with
  `--output-format stream-json --include-hook-events --verbose` to capture hook
  output.

# Artifacts

Claude plugin and marketplace validation output:

```text
Validating marketplace manifest: /Users/alexanderbutler/code_projects/personal/agent-loom/.claude-plugin/marketplace.json

Validation passed
```

Rule sync and guard smoke output:

```text
global sync: generated loom.md and one-line manifest
project sync: generated loom.md and one-line manifest
marker cleared on current sync
missing source: guard blocked with sync-failed marker
unmanaged extra markdown: guard blocked with sync-failed marker
symlink destination: guard blocked with sync-failed marker
unsafe manifest: guard blocked with sync-failed marker
old managed files cleaned
aggregate user rules cleaned
symlinked loom.md: guard blocked with sync-failed marker
symlinked manifest: guard blocked with sync-failed marker
symlinked parent directory: guard blocked before creating rules through symlink
non-regular manifest directory: guard blocked with sync-failed marker
pending marker: guard blocked prompt
local marketplace install: loom@agent-loom installed without hook-load errors
```

First project-session probe with global rules moved aside:

```json
{"knows_loom": false, "source": "no Loom instructions in loaded context", "one_sentence": "No instructions about Loom are present in my loaded context."}
```

Post-run inspection from the same probe:

```text
SYNC_STATUS=project_rules_present
GLOBAL_STATUS=global_rules_absent_during_probe
```

Second project-session probe against the same temporary project, with global
rules moved aside again:

```json
{"knows_loom": true, "source": ".claude/rules/loom/*.md", "one_sentence": "Loom is a mandatory Markdown-native operating protocol that uses typed records, layered truth ownership, an outer scoping loop and a Ralph inner execution loop with bounded packets, plus critique and wiki layers, to keep AI work recoverable across disposable context windows."}
```

Restart guard runtime probe on first project session:

```json
{"decision":"block","reason":"Loom rules were just installed at /private/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/tmp.WvQbvMYbgl/project/.claude/rules/loom, but Claude loaded instructions before those files existed. Your prompt was not processed. Start a new Claude session in this project, then resubmit the prompt so Loom always-on rules are loaded."}
```

The same stream output reported zero API cost and no model usage for that blocked
prompt, with `SYNC_STATUS=project_rules_present` after the run.

Aggregate-rule restart guard runtime probe:

```json
{"decision":"block","reason":"Loom rules were just installed at /private/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/tmp.RRhNiGLS9q/project/.claude/rules/loom, but Claude loaded instructions before those files existed. Your prompt was not processed. Start a new Claude session in this project, then resubmit the prompt so Loom always-on rules are loaded."}
```

The same stream output reported `SYNC_STATUS=project_loom_md_present` and zero
model usage for the blocked prompt.

Second project-session probe after the restart guard blocked the first prompt:

```json
{"knows_loom": true, "source": ".claude/rules/loom/loom.md", "one_sentence": "Loom is a mandatory Markdown-native operating protocol that uses layered artifacts, outer/inner loops, and bounded packets to keep AI work recoverable and truthful across disposable context windows."}
```

Second-session probe after removing the duplicate `hooks` manifest field:

```json
{"knows_loom": true, "source": ".claude/rules/loom/loom.md", "one_sentence": "Loom is a mandatory Markdown-native operating protocol that uses typed artifact layers, an outer scoping loop and a Ralph inner execution loop, and bounded packets to keep AI work recoverable, truthful, and auditable across disposable context windows."}
```

Relevant files:

- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `hooks/hooks.json`
- `scripts/claude-sync-rules.sh`
- `scripts/claude-loom-restart-guard.sh`
- `scripts/claude-clean-rules.sh`
- `examples/adapters/claude-plugin-install/README.md`
- `INSTALL.md`
- `.loom/research/loom-install-distribution-methods.md`
- `.loom/plans/install-experience-harness-adapters.md`

# Supports Claims

- `ticket:q7h1d05q` acceptance criterion: if a plugin fixture is created,
  `.claude-plugin/plugin.json` and component paths match Claude plugin docs.
- `ticket:q7h1d05q` marketplace expectation: `.claude-plugin/marketplace.json`
  validates and exposes plugin `loom` from marketplace `agent-loom`.
- `ticket:q7h1d05q` acceptance criterion: skills remain discoverable `SKILL.md`
  directories in the chosen path, structurally through the plugin manifest.
- `ticket:q7h1d05q` acceptance criterion: optional commands remain explicit
  invocation surfaces and do not become protocol owners, structurally through the
  plugin manifest.
- `ticket:q7h1d05q` acceptance criterion: chosen path preserves always-on Loom
  rules through a documented Claude static instruction surface, structurally
  through generated `loom.md` files written into user or project
  `.claude/rules/loom/`.
- `ticket:q7h1d05q` project-scope safety expectation: project-local rules are
  selected only when project Claude settings explicitly enable the `loom` plugin,
  not merely because `.claude/` exists.
- `ticket:q7h1d05q` runtime timing expectation: a project-local plugin-enabled
  first session can install rules, but the rules are loaded on the next session.
- `ticket:q7h1d05q` restart safety expectation: if rules are installed or updated
  after initial instruction loading, user prompts should be blocked before Claude
  proceeds without Loom operating knowledge.
- `ticket:q7h1d05q` sync-hardening expectation: missing sources, symlinked
  destinations, unsafe manifest entries, and unmanaged destination Markdown files
  fail closed through guard-readable markers.
- `critique:claude-plugin-integration-review` acceptance expectation: final oracle
  pass found no blockers for local/prototype acceptance.
- `ticket:q7h1d05q` completion posture: local/prototype work is ready for owner
  acceptance, with release-packaging risks explicit.

# Challenges Claims

- Challenges any claim that a Claude plugin alone is a complete Loom install: the
  fetched Claude docs do not describe install-time plugin scripts or a manifest
  field for arbitrary always-on rules.
- Challenges the assumption that `${CLAUDE_PLUGIN_ROOT}` is the user or project
  `.claude` directory: fetched docs define it as the plugin installation
  directory, and local `claude plugin list --json` showed project-scoped plugins
  installed under `~/.claude/plugins/cache/...` with a separate `projectPath`.

# Environment

Commit: 700bd5f
Branch: main
Runtime: Claude Code 2.1.119, `claude plugin validate`, local shell smoke test
OS: darwin
Relevant config: local repository root used as plugin root; temporary `HOME` and
temporary `CLAUDE_PROJECT_DIR` used for sync smoke tests

# Validity

Valid for: structural plugin manifest/hook compatibility with Claude Code 2.1.119
and script-level user/project rule synchronization under temporary directories on
2026-04-25.
Recheck when: Claude plugin manifest schema changes, Claude adds plugin-owned
static instruction loading, hook lifecycle behavior changes, or the plugin is
prepared for marketplace release.

# Limitations

- This does not prove runtime skill invocation inside an interactive Claude Code
  session.
- This proves local marketplace add/install in a temporary `HOME`, but does not
  prove marketplace update behavior or audit final cache contents for broad
  distribution.
- Runtime probe confirmed `UserPromptSubmit` blocks the first prompt after
  bootstrap sync before any model call is made.
- Runtime probe showed project rules synchronized by the `SessionStart` hook were
  not loaded into that same first session; they were loaded on the next session.
- Project/local scope detection currently relies on project Claude settings
  containing an enabled `loom` plugin entry. The script uses `python3` JSON parsing
  when available and a narrow normalized-JSON fallback otherwise.
- Claude docs do not describe a plugin uninstall hook, so cleanup on plugin
  disable/uninstall is explicit via `scripts/claude-clean-rules.sh`, not automatic.
- The local marketplace entry uses source `./`, so release packaging still needs a
  cache-content review before broad distribution.
- The oracle critique accepted the current state for local/prototype use but kept
  broad marketplace packaging, cleanup UX, Windows support, and exact plugin-ID
  matching as release-hardening risks.
- Final oracle pass also noted runtime skill/command invocation from an installed
  marketplace plugin remains unproven.

# Result

`claude plugin validate .` accepted the marketplace manifest and plugin manifest.
The sync script generated one managed `loom.md` file into temporary Claude
user-rule and project-rule directories, avoided project-rule writes for an
unrelated `.claude/settings.json`, no-oped when the destination was already
current, and failed closed for unsafe sync states. Isolated Claude Code runtime
probes showed project rules were present after the first session but only entered
context on the second session. The prompt guard blocked that first unsafe prompt
path and prevented model execution before restart.

# Interpretation

The evidence supports an automated Claude hybrid prototype where the plugin
distributes skills and command wrappers and automatically installs bundled rules
into Claude's real rule surfaces on plugin-enabled session start. It does not make
first-session instruction loading possible, but it prevents first-session work from
proceeding without Loom after a bootstrap sync. Uninstall cleanup is explicit via
`scripts/claude-clean-rules.sh`, not automatic. `${CLAUDE_PLUGIN_ROOT}` should be
treated as the bundled source path, not the loaded rule destination.

# Related Records

- `ticket:q7h1d05q`
- `critique:claude-plugin-integration-review`
- `plan:install-experience-harness-adapters`
- `research:loom-install-distribution-methods`
