# OpenCode Playbook Commands Implementation

ID: packet:20260515T215226Z-opencode-playbook-commands
Type: Packet
Status: consumed
Created: 2026-05-15 21:52 UTC
Updated: 2026-05-15 22:05 UTC
Target: ticket:20260515-opencode-playbook-commands
Packet Kind: Ralph
Mode: execution
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: 1
Risk: medium - changes OpenCode package registration from implicit skills to explicit commands.
Verification Posture: observation-first
Change Class: OpenCode package command surface

## Mission

Implement `ticket:20260515-opencode-playbook-commands`: convert the OpenCode Playbooks package from implicit `config.skills.paths` registration to explicit `config.command` entries derived from the canonical macro catalog.

## Context Bundle

Records:

- `ticket:20260515-opencode-playbook-commands` - target ticket, scope, acceptance, and current state.
- `ticket:20260515-playbook-macro-catalog` - closed prerequisite that created `readPlaybookMacroCatalog()`.
- `audit:20260515-playbook-macro-catalog` - clear audit verdict for the macro catalog seam.
- `plan:20260515-playbook-explicit-macros` - sequencing and validation posture for the broader conversion.
- `spec:playbook-explicit-macros` - behavior contract, especially OpenCode true command requirements.
- `research:20260515-playbook-command-surfaces` - source-backed finding that OpenCode supports `config.command` prompt macros from plugins.
- `AGENTS.md` - package-shape and validation constraints.

Evidence Or Artifacts:

- `packet:20260515T213657Z-playbook-macro-catalog` and `audit:20260515-playbook-macro-catalog` show the catalog has 25 macro entries and should be consumed through `readPlaybookMacroCatalog().body`.

Files, Diffs, Or External References:

- `loom-playbooks/loom-playbooks.mjs` - current OpenCode plugin entrypoint and smoke output.
- `loom-playbooks/package.json` - package file list and `smoke` / `pack:check` scripts.
- `loom-playbooks/skills/**/SKILL.md` - source corpus read by the catalog helper; should not be registered as OpenCode skills after this ticket.

## Read Scope

- `.loom/tickets/20260515-opencode-playbook-commands.md`
- `.loom/tickets/20260515-playbook-macro-catalog.md`
- `.loom/audit/20260515-playbook-macro-catalog.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/research/20260515-playbook-command-surfaces.md`
- `AGENTS.md`
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/skills/**/SKILL.md`

## Write Scope

Records Or Artifacts:

- `.loom/tickets/20260515-opencode-playbook-commands.md` - update Current State and Journal with progress, blockers, evidence, or completion disposition.
- this packet - fill `## Worker Output`, update `Status:`, and add follow-up notes when appropriate.

Source Paths:

- `loom-playbooks/loom-playbooks.mjs` - command registration, inspection, smoke output, and helper functions.
- `loom-playbooks/package.json` - package inclusion only if needed for command operation. Avoid unrelated package metadata changes.

## Source Snapshot

The catalog ticket is closed. Current `loom-playbooks/loom-playbooks.mjs` exports `readPlaybookMacroCatalog()` and `inspectPlaybookMacroCatalog()`, but `configureOpenCode()` still registers `loom-playbooks/skills` through `config.skills.paths`. Smoke output still includes `skillPath` and trigger-style activation checks. This ticket should remove the OpenCode implicit skill registration path for Playbooks and replace it with explicit command registration.

OpenCode command surface constraint from research: OpenCode config supports a `command` object whose entries can include `template`, `description`, and optional `agent`, `model`, or `subtask`. Use `command`, not an unsupported `commands` key, unless source inspection of the local package proves otherwise.

## Task

Implement the smallest OpenCode package change that satisfies `ticket:20260515-opencode-playbook-commands#ACC-001` through `ACC-005`.

Guidance:

- Derive command entries from `readPlaybookMacroCatalog()` and use each macro's `body` as the prompt template source so the explicit macro preamble is preserved.
- Do not register `loom-playbooks/skills` in `config.skills.paths` from `configureOpenCode()` after this ticket.
- Preserve `readSkillFiles()` and catalog introspection if useful for other adapters and checks.
- Update smoke output to report command count, command registration result, no Playbook skill path registration, catalog alignment, and absence of Core doctrine preload.
- Remove or stop relying on trigger-description activation checks in OpenCode smoke. It is acceptable to keep a legacy inspection helper only if smoke no longer treats implicit Playbook trigger descriptions as success.
- Keep implementation minimal and avoid broad docs, native plugin manifest, Gemini, or activation test changes.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, stay inside scope, update the ticket and packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Run `npm --prefix loom-playbooks run smoke` and record the relevant command/skill-path output.
- Run `npm --prefix loom-playbooks run pack:check` and record whether files needed for OpenCode command operation are included.
- Run `git diff --check`.
- Use source inspection or a Node import check to prove `configureOpenCode({})` produces command entries and no Playbook `skills.paths` registration.
- If `npm pack --dry-run` output is noisy, summarize only the relevant file inclusion facts in Worker Output.

## Stop Conditions

- Stop and return `blocked` if OpenCode command registration requires a command naming decision not settled by the spec and not locally reversible.
- Stop and return `blocked` if package checks reveal commands require files outside current package inclusion and the fix would widen beyond `loom-playbooks/` package files.
- Stop instead of editing Claude, Cursor, Codex, Gemini, docs, or activation tests.
- Stop if removing skill-path registration breaks Core package behavior; Core changes are out of scope.

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

If this run supports closure, acceptance, evidence, audit, research, knowledge, or future recovery, preserve this output in the packet or in a cited durable record; do not leave it only in transient launch output.

## Worker Output

Outcome: stop

Files changed:

- `loom-playbooks/loom-playbooks.mjs`

Records changed:

- `.loom/tickets/20260515-opencode-playbook-commands.md`
- `.loom/packets/ralph/20260515T215226Z-opencode-playbook-commands.md`

What changed:

- Added `readPlaybookCommands()` to derive OpenCode command entries from `readPlaybookMacroCatalog()` with each macro's `body` as `template` and catalog description as `description`.
- Changed `configureOpenCode()` to populate `config.command` and stop adding `loom-playbooks/skills` to `config.skills.paths`.
- Updated Playbooks smoke inspection to report command registration, command count, catalog alignment, absence of registered Playbook skill paths, command deduping, and absence of Core doctrine preload.
- Removed smoke reliance on broad trigger-description activation checks.

Evidence, review findings, validation output, or observations gathered:

- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `commandCount: 25`, `macroCount: 25`, `commandChecks.ok: true`, `missingCommands: []`, `registeredPlaybookSkillPaths: []`, `playbookSkillPathsRegistered: false`, `doesNotPreloadCoreDoctrine: true`, and `commandEntriesAreDeduped: true`.
- Direct Node import check passed: `configureOpenCode({})` produced `commandCount: 25`, `macroCount: 25`, `skillPathCount: 0`, and `missing: []`.
- `npm --prefix loom-playbooks run pack:check` passed; dry-run included `loom-playbooks.mjs`, `package.json`, `README.md`, and all 25 `skills/**/SKILL.md` files needed by the runtime catalog reader.
- `git diff --check` passed with no output.

What was not verified or reviewed:

- No live OpenCode TUI command invocation was run.
- No Claude, Cursor, Codex, Gemini, docs, or activation test surfaces were reviewed or changed; those are out of scope for this packet.
- No adversarial audit was performed in this run.

Blockers, risks, or assumptions discovered:

- No blockers discovered.
- Assumption: OpenCode command keys can use the stable Playbook macro names already present in the catalog; this follows the ticket and spec allowance that command naming is nonblocking when stable and explicit.
- Residual risk: acceptance should still audit whether `config.command` semantics and no-skill-path registration satisfy the intended OpenCode activation behavior.

Recommended next move for the consuming surface:

- Keep `ticket:20260515-opencode-playbook-commands` in `review` and run an acceptance/audit pass focused on OpenCode activation semantics, command/catalog alignment, and absence of implicit Playbook skill registration before closure.
