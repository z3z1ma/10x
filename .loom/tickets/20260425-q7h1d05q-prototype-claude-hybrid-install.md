---
id: ticket:q7h1d05q
kind: ticket
status: complete_pending_acceptance
change_class: release-packaging
risk_class: medium
created_at: 2026-04-25T18:46:08Z
updated_at: 2026-04-26T00:59:31Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:install-experience-harness-adapters
  research:
    - research:loom-install-distribution-methods
    - research:harness-install-surfaces
  evidence:
    - evidence:claude-plugin-hybrid
  critique:
    - critique:claude-plugin-integration-review
  related:
    - ticket:ffg8elkb
external_refs:
  claude_code_docs:
    - https://code.claude.com/docs/en/plugins
    - https://code.claude.com/docs/en/plugins-reference
    - https://code.claude.com/docs/en/settings
    - https://code.claude.com/docs/en/hooks
    - https://code.claude.com/docs/en/skills
    - https://code.claude.com/docs/en/memory
    - https://code.claude.com/docs/en/plugin-marketplaces
depends_on: []
---

# Summary

Prototype and decide a Claude Code plugin install path that uses Claude's native
plugin surfaces for skills and commands while automatically synchronizing
always-on Loom rules into a real Claude instruction surface.

# Context

Claude Code has strong first-class extension support, but
`research:loom-install-distribution-methods` did not find plugin docs showing a
clean way for a plugin alone to install arbitrary always-on Loom rules. Claude's
documented static instruction surfaces are `CLAUDE.md` and user/project rules,
while plugin support is attractive for skills, commands, namespacing, and
marketplace distribution.

The current installer directly copies rules to `~/.claude/rules/loom`, skills to
`~/.claude/skills`, and commands to `~/.claude/commands`. A plugin path is only
acceptable if adding/enabling the plugin also installs or synchronizes Loom rules
into Claude's real static instruction surface without a second manual user step.

# Why Now

Claude plugin support is likely the most tempting first-class install surface,
but it must not be allowed to obscure Loom's always-on rule requirement. The
project needs a clear Claude-specific decision before changing the installer or
documenting plugin installation as the recommended path.

# Scope

- compare Claude install shapes against current docs and local feasibility:
  direct `~/.claude/rules/loom` plus `~/.claude/skills` and `~/.claude/commands`,
  plugin for skills/commands plus automatic user-rule sync, and plugin for
  skills/commands plus a managed `~/.claude/CLAUDE.md` import
- prototype a Claude plugin or fixture only if it improves the direct install
  story without hiding rule loading
- preserve always-on Loom rules through `CLAUDE.md` or user rules rather than
  hook-injected context
- preserve skills as `SKILL.md` directories
- preserve commands as explicit invocation wrappers or plugin command equivalents
- document why hooks are rejected for static rule loading, while allowing a hook
  to synchronize files into Claude's real static rule surface if evidenced
- update install docs and shell fallback only after the chosen hybrid or direct
  path is evidenced

# Non-goals

- do not use Claude hooks to inject static Loom rules as runtime context
- do not set a plugin custom agent as a substitute for installing Loom's rule
  corpus unless the ticket is explicitly reframed with evidence
- do not publish a Claude plugin marketplace package
- do not require managed enterprise settings for normal user install
- do not change canonical Loom source files to fit Claude packaging

# Acceptance Criteria

- the ticket records a clear Claude recommendation: direct install, plugin with
  automatic user-rule sync, plugin with `CLAUDE.md` import, or a justified
  deferral
- the chosen path preserves ordered always-on Loom rules through a documented
  Claude static instruction surface
- if a plugin fixture is created, `.claude-plugin/plugin.json` and component
  paths match Claude plugin docs
- skills remain discoverable `SKILL.md` directories in the chosen path
- optional commands remain explicit invocation surfaces and do not become protocol
  owners
- hook-based context loading is rejected; hook-based file synchronization is
  justified only if it writes to Claude's real static instruction surface
- validation uses a temporary `HOME` or package fixture and records what could
  not be validated in actual Claude Code runtime
- `INSTALL.md` describes the chosen Claude path and its limitations

# Coverage

Covers:

- None - no spec-owned acceptance IDs exist. This ticket consumes
  `research:loom-install-distribution-methods#claude-code` and owns ticket-local
  acceptance criteria for the Claude install slice.

# Claim Matrix

| Claim | Coverage | Evidence | Notes |
| --- | --- | --- | --- |
| Claude plugin manifest can expose canonical Loom skills and optional commands. | supported | `evidence:claude-plugin-hybrid` | `claude plugin validate .` accepted `.claude-plugin/plugin.json` with `./skills/` and `./commands/`. |
| Claude marketplace can expose the local Loom plugin. | supported | `evidence:claude-plugin-hybrid` | `claude plugin validate .` accepted `.claude-plugin/marketplace.json` for marketplace `agent-loom` and plugin `loom`. |
| Local marketplace install can install `loom@agent-loom` without plugin load errors. | supported | `evidence:claude-plugin-hybrid` | Temporary-`HOME` `claude plugin marketplace add` and `claude plugin install` succeeded after removing duplicate hook declaration from `plugin.json`. |
| Claude plugin can automatically synchronize Loom rules into a Claude-loaded user or project rule surface on plugin-enabled session start. | supported | `evidence:claude-plugin-hybrid` | `hooks/hooks.json` and `scripts/claude-sync-rules.sh` validate structurally and generate `loom.md` under temporary user and project rule roots. |
| `${CLAUDE_PLUGIN_ROOT}` is the user or project `.claude` directory. | challenged | `evidence:claude-plugin-hybrid` | Docs define it as the plugin installation directory; local project-scoped plugin entries still use `~/.claude/plugins/cache/...` as `installPath`. |
| Existence of a project `.claude/` directory should select project-local rule sync. | challenged | `evidence:claude-plugin-hybrid` | Script now requires project settings to explicitly enable `loom`; unrelated project `.claude/settings.json` kept using global rules. |
| Claude plugin installation command itself runs setup code. | challenged | `evidence:claude-plugin-hybrid` | Current docs do not describe install-time plugin script execution. |
| Synchronized project rules load in the first plugin-enabled session. | challenged | `evidence:claude-plugin-hybrid` | Runtime probe showed first session installed project rules but did not load them into context. |
| Synchronized project rules load on the next plugin-enabled session. | supported | `evidence:claude-plugin-hybrid` | Second isolated `claude -p` run in the same temp project reported Loom instructions loaded from `.claude/rules/loom/loom.md`. |
| First-session prompts should proceed after a bootstrap sync. | challenged | `evidence:claude-plugin-hybrid` | `UserPromptSubmit` restart guard blocked the prompt when the current session just installed rules. |
| Restart guard prevents model execution before Loom is loaded. | supported | `evidence:claude-plugin-hybrid` | Stream-json runtime probe showed the guard's block decision, zero API cost, and no model usage. |
| Sync failures should allow prompt processing. | challenged | `evidence:claude-plugin-hybrid` | Missing source rules, symlinked destinations, unsafe manifests, and unmanaged destination `.md` files create sync-failed markers that the guard blocks on. |
| Plugin disable/uninstall removes synchronized rules automatically. | challenged | `evidence:claude-plugin-hybrid` | Current docs do not describe an uninstall hook; cleanup is explicit via `scripts/claude-clean-rules.sh`. |

# Execution Notes

Claude facts to preserve from research:

- `~/.claude/CLAUDE.md` is a user instruction file and can import additional
  files with `@path`
- user-level rules live in `~/.claude/rules/`
- personal skills live in `~/.claude/skills/<skill-name>/SKILL.md`
- Claude plugins can include `skills/`, `commands/`, agents, hooks, MCP/LSP,
  monitors, `bin/`, and limited default settings
- Claude plugin hooks can run command hooks on `SessionStart`
- Claude plugin hooks can run command hooks on `UserPromptSubmit`, and that event
  can block prompt processing with a user-visible reason
- plugin `settings.json` supports only `agent` and `subagentStatusLine` in the
  fetched docs
- hook docs say static context should use `CLAUDE.md` instead of `SessionStart`
  hooks

Likely implementation choices:

- current chosen direction: Claude plugin with automatic rule sync
- plugin/fixture exposes canonical `skills/` and optional `commands/`
- plugin `SessionStart` hook generates one managed `loom.md` from canonical
  `rules/*.md` into a scope-appropriate Claude rule directory without printing
  rules into hook context
- project sync is selected by explicit project/local `enabledPlugins` membership
  for `loom`, not by `.claude/` directory existence
- otherwise the script verifies/synchronizes user-level `~/.claude/rules/loom/`
  and no-ops when the destination is already current
- when synchronization changes rule files for the current session, the plugin
  writes a restart-required marker and a `UserPromptSubmit` hook blocks prompts
  until the user starts a new session
- rule ordering is handled by the generated single Claude rule file, not by
  relying on Claude's ordering of multiple `.md` files
- uninstall/disable cleanup is explicit through `scripts/claude-clean-rules.sh`
- preserve current direct fallback until the hybrid path is proven

# Blockers

None.

# Next Move / Next Route

Acceptance review. Runtime validation now covers first-session restart blocking,
second-session Loom loading, fail-closed sync errors, explicit cleanup mechanics,
and local marketplace add/install without hook-load errors. The final oracle pass
found no local/prototype blockers.

# Ralph Readiness

Bounded iteration:
Prototype or structurally compare Claude direct and hybrid install paths, choose
one recommendation, and update Claude install documentation or fixtures.

Write boundary:
Claude adapter package or fixture paths, `.claude-plugin/plugin.json`,
`hooks/hooks.json`, `scripts/claude-sync-rules.sh`,
`scripts/claude-loom-restart-guard.sh`, `scripts/claude-clean-rules.sh`,
`INSTALL.md`,
`examples/adapters/` if used for fixtures, `scripts/install-loom.sh` only for a
small proven fallback adjustment, and this ticket/evidence records. Read-only
source inputs are `rules/`, `skills/`, and `commands/`.

Likely verification posture:
Observation-first structural validation plus temporary `HOME` install/uninstall
checks if direct user config mutation changes.

Expected output contract:
Chosen Claude install recommendation, changed files, validation commands and
results, explicit hook rejection or revised evidence, limitations, and ticket
state recommendation.

# Evidence

Evidence so far:

- `evidence:claude-plugin-hybrid` records current Claude docs inspection and
  `claude plugin validate .` passing for `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, plus temporary user/project smoke tests for
  `scripts/claude-sync-rules.sh`, unrelated-project behavior, current-state no-op
  behavior, fail-closed sync hazards, explicit cleanup, and runtime restart guard
  behavior.

Remaining expected evidence:

- structural inspection of any plugin fixture or direct install output
- marketplace update/cache-content inspection beyond local install validation
- disable/uninstall cleanup UX beyond the explicit cleanup script
- skill directory checks for `SKILL.md`
- command wrapper or plugin command inspection
- `git diff --check`
- explicit limitation if Claude runtime validation cannot be run

# Critique Disposition

Risk class: medium

Critique policy: recommended

Policy rationale:
Claude has multiple powerful extension mechanisms. The main risk is operator
confusion from calling a plugin install complete when always-on rules are not
actually installed.

Required critique profiles:

- operator-clarity

Findings:

`critique:claude-plugin-integration-review` records the oracle critique cycle.
Initial blocking findings around manifest safety, fail-open sync behavior, and
rule ordering were resolved. The final oracle pass found no blockers for
local/prototype acceptance. Later local marketplace install surfaced a duplicate
hook declaration, which was resolved by relying on Claude's automatic loading of
standard `hooks/hooks.json`. Remaining risks are accepted as release-packaging
follow-up: broad `source: "./"`, explicit rather than automatic cleanup, unproven
Windows support, and possible future tightening of exact plugin-ID matching.
The final post-marketplace-install oracle pass reported no local/prototype
blockers and identified only ticket closure hygiene plus release-packaging risks.

Disposition status: completed

Deferral / not-required rationale:

None.

# Wiki Disposition

Wiki promotion is optional. Promote only if the Claude hybrid decision becomes a
reusable pattern for other incomplete plugin systems.

# Acceptance Decision

Accepted by:
Accepted at:
Basis: Pending owner acceptance. Local/prototype implementation is evidenced by
  Claude plugin validation, local marketplace add/install, script-level sync and
  cleanup probes, runtime first-prompt blocking, second-session Loom loading, and
  oracle critique with no remaining local/prototype blockers.
Residual risks: Broad marketplace `source: "./"` still needs narrowed packaging or
  cache-content audit before broad release; cleanup is explicit rather than
  automatic; runtime skill/command invocation from installed marketplace plugin is
  not yet proven; exact plugin identity matching may need tightening; Windows/non-
  bash portability is unproven.

# Dependencies

Uses `research:loom-install-distribution-methods` and prior direct Claude install
proof from `ticket:ffg8elkb`. No hard ticket prerequisite blocks starting this
prototype.

# Journal

- 2026-04-25: created as the Claude Code harness ticket under
  `plan:install-experience-harness-adapters`.
- 2026-04-25: fixed prototype direction on Claude plugin for skills/commands plus
  user-level `~/.claude/rules/loom/` for always-on Loom rules. Added
  `.claude-plugin/plugin.json`, fixture notes, and `evidence:claude-plugin-hybrid`
  after `claude plugin validate .` passed. Custom agents and hook-output static
  rule loading remain rejected.
- 2026-04-25: reframed the prototype after operator clarification: the Claude
  plugin path is acceptable only if rule installation is automated. Added
  `hooks/hooks.json` and `scripts/claude-sync-rules.sh` so plugin-enabled
  `SessionStart` synchronizes canonical `rules/*.md` into
  `~/.claude/rules/loom/`. Early temporary-`HOME` smoke test copied seven rules;
  later hardening replaced multi-file copies with generated `loom.md`.
- 2026-04-25: verified `${CLAUDE_PLUGIN_ROOT}` is the plugin installation/cache
  directory, not the user or project `.claude` directory. Updated
  `scripts/claude-sync-rules.sh` to sync into project `.claude/rules/loom/` when
  project/local Claude settings enable `loom`, otherwise into user
  `~/.claude/rules/loom/`. Early temporary project smoke test copied seven rules;
  later hardening replaced multi-file copies with generated `loom.md`.
- 2026-04-25: tightened project detection: `.claude/` existence alone does not
  select project sync. The script greps normalized Claude project settings for an
  enabled `loom` plugin entry, otherwise verifies/synchronizes global rules and
  no-ops when global rules are current.
- 2026-04-26: isolated runtime probes showed project `SessionStart` sync is not
  early enough for same-session instruction loading. The first headless session
  installed `.claude/rules/loom/` but reported no Loom context; the second
  headless session in the same temporary project loaded Loom from
  `.claude/rules/loom/*.md`; later hardening uses `.claude/rules/loom/loom.md`.
- 2026-04-26: added `scripts/claude-loom-restart-guard.sh` and a
  `UserPromptSubmit` hook. When the sync script installs or updates rule files,
  it writes a per-session restart marker; the prompt guard blocks user prompts in
  that session with a restart/new-session message.
- 2026-04-26: runtime probe confirmed the restart guard blocks the first prompt
  after project rule bootstrap with zero model usage. A second session in the same
  temporary project loaded Loom from `.claude/rules/loom/*.md` and proceeded;
  aggregate-rule validation later loaded Loom from `.claude/rules/loom/loom.md`.
- 2026-04-26: added `.claude-plugin/marketplace.json` for local marketplace
  testing. Oracle critique found sync safety issues; hardened the scripts to
  generate one ordered `loom.md`, fail closed on unsafe sync states, reject
  symlinked destinations and unsafe manifests, block unmanaged destination
  Markdown, and provide `scripts/claude-clean-rules.sh` for explicit cleanup.
  Aggregate runtime probe confirmed first prompt blocking and second-session load
  from `.claude/rules/loom/loom.md`.
- 2026-04-26: completed oracle critique cycle in
  `critique:claude-plugin-integration-review`. No blockers remain for
  local/prototype acceptance after final hardening; release packaging risks remain
  explicit follow-up.
- 2026-04-26: local marketplace install showed Claude auto-loads the standard
  `hooks/hooks.json` path and errors if the manifest declares the same file.
  Removed the duplicate `hooks` field from `.claude-plugin/plugin.json`; local
  marketplace install and runtime hook probes then passed.
- 2026-04-26: final oracle pass after marketplace-install validation found no
  local/prototype blockers. Moved ticket to `complete_pending_acceptance` with
  release-packaging risks explicit.
