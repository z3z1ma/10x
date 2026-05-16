# OpenCode Playbook Commands Audit

ID: packet:20260515T215943Z-opencode-playbook-commands-audit
Type: Packet
Status: consumed
Created: 2026-05-15 21:59 UTC
Updated: 2026-05-15 22:02 UTC
Target: ticket:20260515-opencode-playbook-commands
Packet Kind: Ralph
Mode: review
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: audit-1
Risk: medium - ticket closure claims OpenCode no longer exposes Playbooks as implicit skills.
Review Lens: audit, acceptance, scope, OpenCode activation semantics, package evidence
Change Class: OpenCode command package review

## Mission

Perform a bounded adversarial audit of `ticket:20260515-opencode-playbook-commands` against ACC-001 through ACC-005 and the `loom-playbooks/loom-playbooks.mjs` diff. Determine whether the ticket can honestly close or whether changes are needed before OpenCode Playbooks are treated as explicit commands.

## Context Bundle

Records:

- `ticket:20260515-opencode-playbook-commands` - target ticket, acceptance, current state, and implementation summary.
- `packet:20260515T215226Z-opencode-playbook-commands` - implementation packet and worker output.
- `ticket:20260515-playbook-macro-catalog` - closed prerequisite catalog ticket.
- `audit:20260515-playbook-macro-catalog` - clear audit of the catalog seam.
- `plan:20260515-playbook-explicit-macros` - sequencing and downstream context.
- `spec:playbook-explicit-macros` - behavior contract for OpenCode command exposure.
- `research:20260515-playbook-command-surfaces` - OpenCode command config support.
- `AGENTS.md` - package and product-surface constraints.

Evidence Or Artifacts:

- Worker output in `packet:20260515T215226Z-opencode-playbook-commands` reports smoke, pack dry-run, direct Node import, and `git diff --check` evidence.

Files, Diffs, Or External References:

- `loom-playbooks/loom-playbooks.mjs` - implementation diff to review.
- `loom-playbooks/package.json` - package file inclusion and scripts.
- `loom-playbooks/skills/**/SKILL.md` - runtime source corpus for the command catalog.

## Read Scope

- `.loom/tickets/20260515-opencode-playbook-commands.md`
- `.loom/packets/ralph/20260515T215226Z-opencode-playbook-commands.md`
- `.loom/tickets/20260515-playbook-macro-catalog.md`
- `.loom/audit/20260515-playbook-macro-catalog.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/research/20260515-playbook-command-surfaces.md`
- `AGENTS.md`
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/skills/**/SKILL.md`
- Current git diff for the OpenCode ticket implementation.

## Write Scope

Records Or Artifacts:

- this packet - fill `## Worker Output`, update `Status:`, and include findings and verdict.

Source Paths:

- None - this is a review packet. Do not edit source or tickets. Return findings for the parent to record and disposition.

## Source Snapshot

Current implementation summary to challenge:

- `readPlaybookCommands()` derives OpenCode command entries from `readPlaybookMacroCatalog()`.
- `configureOpenCode()` now writes `config.command[name]` and does not add Playbook `config.skills.paths`.
- Smoke output checks command count, catalog alignment, no registered Playbook skill paths, command dedupe, macro checks, and no Core doctrine preload.
- `loom-playbooks/package.json` still packs `loom-playbooks.mjs` and `skills/`, which are needed because the command catalog derives bodies from `skills/**/SKILL.md` at runtime.

## Task

Review the target ticket, diff, and evidence. Focus on:

- ACC-001: Does `configureOpenCode()` register explicit `config.command` entries and avoid Playbook `config.skills.paths`?
- ACC-002: Are commands aligned with `readPlaybookMacroCatalog()` names, descriptions, and prompt bodies?
- ACC-003: Does smoke now validate explicit command behavior rather than implicit trigger descriptions?
- ACC-004: Does package dry-run include files needed for runtime command operation?
- ACC-005: Are syntax and package changes clean enough for this ticket?
- Scope: Did the implementation avoid native adapters, Gemini, docs, and activation tests?
- Risk: Is there any reason OpenCode command semantics are overclaimed by the implementation or ticket wording?

Do not fix issues. Return findings with file/line or record references when practical, plus a verdict.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, perform the bounded audit, update this packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Review `loom-playbooks/loom-playbooks.mjs` source and current diff.
- Review target ticket acceptance and implementation packet output.
- Run `npm --prefix loom-playbooks run smoke` if useful.
- Run a direct Node import/config check if useful.
- Run `npm --prefix loom-playbooks run pack:check` or inspect prior output if fresh run is too expensive.
- Findings should use `FIND-*` IDs for material issues, or say no material findings within scope.
- Verdict should be one of `clear`, `concerns`, `changes-needed`, or `inconclusive`, with limits.

## Stop Conditions

- Stop and return `inconclusive` if the source diff changes under review.
- Stop instead of modifying source or tickets.
- Stop and name missing context if OpenCode command semantics cannot be judged from local source and records.

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

The review output must include any `FIND-*` findings and a bounded audit verdict that can be recorded under `.loom/audit/`.

## Worker Output

Outcome: stop

Files changed:

- None.

Records changed:

- `.loom/packets/ralph/20260515T215943Z-opencode-playbook-commands-audit.md`

Evidence, review findings, validation output, or observations gathered:

- Reviewed `ticket:20260515-opencode-playbook-commands`, implementation packet `packet:20260515T215226Z-opencode-playbook-commands`, prerequisite catalog ticket and audit, plan, spec, research, `AGENTS.md`, `loom-playbooks/loom-playbooks.mjs`, `loom-playbooks/package.json`, scoped implementation diff, and the 25-file Playbook skill corpus path set.
- Source inspection confirms `configureOpenCode()` derives command entries via `readPlaybookCommands()` from `readPlaybookMacroCatalog()`, writes `config.command[name]`, and no longer writes `config.skills.paths` for `loom-playbooks/skills`.
- Source inspection confirms each command template is exactly the catalog macro `body` and each command description is exactly the catalog macro `description`; smoke also checks missing command drift against the catalog.
- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `commandCount: 25`, `macroCount: 25`, `commandChecks.ok: true`, `missingCommands: []`, `registeredPlaybookSkillPaths: []`, `playbookSkillPathsRegistered: false`, `doesNotPreloadCoreDoctrine: true`, `commandEntriesAreDeduped: true`, and no macro description failures.
- Direct Node import/config check passed with `commandCount: 25`, `macroCount: 25`, `skillPathCount: 0`, and `missing: []`.
- `npm --prefix loom-playbooks run pack:check` passed. The dry-run included `loom-playbooks.mjs`, `package.json`, `README.md`, and all 25 `skills/**/SKILL.md` files required by the runtime catalog reader.
- `git diff --check` passed with no output.

Review findings:

- No material `FIND-*` findings within this packet's bounded scope.

Verdict:

- `clear` - ACC-001 through ACC-005 are supported within the reviewed scope. OpenCode Playbooks are registered through explicit `config.command` entries derived from the canonical macro catalog, the Playbook skill directory is not registered through OpenCode `config.skills.paths`, smoke now validates command behavior and catalog alignment instead of implicit trigger-description quality, package dry-run includes the runtime files needed for command operation, and syntax/package checks passed.
- This verdict does not claim live OpenCode TUI invocation, negative natural-prompt activation coverage, native adapter conversion, Gemini command conversion, docs/tests completion, or closure of downstream plan items outside `ticket:20260515-opencode-playbook-commands`.

What was not verified or reviewed:

- No live OpenCode TUI command invocation was run.
- No negative natural-prompt activation harness test was run; this ticket's scoped proof is source/config-level removal of Playbook `skills.paths` registration plus command registration smoke.
- No Claude, Cursor, Codex, Gemini, docs, or broader activation test surfaces were reviewed.
- No exhaustive semantic audit of all 25 Playbook bodies was repeated; the already-clear catalog audit covers the shared macro-body seam, and this audit checked that OpenCode consumes that seam.

Blockers, risks, or assumptions discovered:

- No blockers discovered.
- Residual risk: OpenCode command semantics are judged from local source-backed research, config mutation source inspection, and package smoke/import checks, not an interactive OpenCode runtime invocation.
- Residual risk: negative natural-prompt activation coverage remains a broader spec/plan requirement and should be handled by downstream docs/tests/final validation, not silently claimed by this ticket.

Recommended next move for the consuming surface:

- Record a matching audit record for `ticket:20260515-opencode-playbook-commands`, then the parent can close the ticket if it accepts the stated residual risks and keeps broader negative activation/docs/adapter work routed to the remaining plan tickets.
