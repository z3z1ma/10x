# Playbook Explicit Macro Docs Tests

ID: packet:20260515T235318Z-playbook-explicit-macro-docs-tests
Type: Packet
Status: consumed
Created: 2026-05-15 23:53 UTC
Updated: 2026-05-16 00:07 UTC
Target: ticket:20260515-playbook-explicit-macro-docs-tests
Packet Kind: Ralph
Mode: execution
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: implementation-1
Risk: medium - updates validation expectations around Core natural routing and explicit Playbook invocation.
Verification Posture: observation-first
Change Class: docs and activation validation alignment

## Mission

Update the final docs/tests validation surface so Loom Playbooks are described and checked as explicit optional workflow macros or explicit-only skills, not natural-prompt auto-activated Playbooks. Run available static/package validation and leave `ticket:20260515-playbook-explicit-macro-docs-tests` ready for audit or honestly blocked.

## Context Bundle

Records:

- `ticket:20260515-playbook-explicit-macro-docs-tests` - target scope and acceptance.
- `plan:20260515-playbook-explicit-macros` - broader conversion strategy and final milestone.
- `spec:playbook-explicit-macros` - explicit macro behavior contract.
- `research:20260515-playbook-command-surfaces` - harness-specific command and explicit-only constraints.
- `evidence:20260515-playbook-activation-stacking` - old failure mode that natural Playbook activation tests should stop rewarding.
- `ticket:20260515-opencode-playbook-commands` and `audit:20260515-opencode-playbook-commands` - OpenCode command behavior.
- `ticket:20260515-native-playbook-explicit-surfaces` and `audit:20260515-native-playbook-explicit-surfaces` - Claude/Cursor/Codex explicit-only behavior.
- `ticket:20260515-gemini-playbook-commands` and `audit:20260515-gemini-playbook-commands` - Gemini command behavior.

Files:

- `CLAUDE.md` - stale acceptance prose that currently expects `loom-idea-refine` natural activation.
- `tests/skill-triggering/` - stale natural-prompt Playbook activation scripts and prompts.
- `README.md`, `INSTALL.md`, `ARCHITECTURE.md`, `loom-playbooks/README.md`, `AGENTS.md` - human-facing guidance and validation prose that may need final alignment.
- `loom-playbooks/loom-playbooks.mjs`, `loom-playbooks/package.json`, `loom-playbooks/commands/*.toml`, `loom-playbooks/playbooks/**/SKILL.md` - source behavior to validate or cite.

## Read Scope

- `.loom/tickets/20260515-playbook-explicit-macro-docs-tests.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/research/20260515-playbook-command-surfaces.md`
- `.loom/evidence/20260515-playbook-activation-stacking.md` if present
- `.loom/tickets/20260515-opencode-playbook-commands.md`
- `.loom/audit/20260515-opencode-playbook-commands.md`
- `.loom/tickets/20260515-native-playbook-explicit-surfaces.md`
- `.loom/audit/20260515-native-playbook-explicit-surfaces.md`
- `.loom/tickets/20260515-gemini-playbook-commands.md`
- `.loom/audit/20260515-gemini-playbook-commands.md`
- `CLAUDE.md`
- `README.md`
- `INSTALL.md`
- `ARCHITECTURE.md`
- `AGENTS.md`
- `loom-playbooks/README.md`
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/commands/*.toml`
- `loom-playbooks/playbooks/**/SKILL.md`
- `tests/skill-triggering/**`
- Current git diff and status.

## Write Scope

Records Or Artifacts:

- `.loom/tickets/20260515-playbook-explicit-macro-docs-tests.md` - update Current State and Journal with implementation evidence and review posture.
- this packet - fill `## Worker Output` and update `Status:`.

Source Paths:

- `CLAUDE.md`
- `README.md`
- `INSTALL.md`
- `ARCHITECTURE.md`
- `loom-playbooks/README.md`
- `tests/skill-triggering/**`
- Package smoke files only if needed to align final validation, such as `loom-playbooks/loom-playbooks.mjs` or package-local smoke expectations.

## Source Snapshot

Known stale surfaces before launch:

- `CLAUDE.md` says a natural prompt `Let's make a react todo list` should route to `loom-idea-refine`.
- `tests/skill-triggering/run-all.sh` includes natural-prompt checks for `loom-idea-refine` and `loom-debugging-and-error-recovery` Playbooks.
- `tests/skill-triggering/run-test.sh` treats detecting a named skill as the only success mode.
- Adapter implementation tickets closed with clear audits, and `loom-playbooks/skills/` is intentionally absent after corpus relocation.

## Task

Implement the smallest docs/tests alignment that satisfies the target ticket:

- Update stale docs so natural prompts are expected to activate Core routing, not Playbook autoactivation.
- Describe Playbooks as explicit optional workflow macros or explicit-only skills per supported harness, without claiming Codex custom slash commands.
- Update activation tests so representative natural prompts fail if Playbook commands or explicit-only Playbook skills are invoked implicitly while Core routing remains available.
- Add positive explicit-invocation coverage for the local runnable surface where feasible, likely OpenCode command registration or package smoke/source inspection if a live harness command invocation is not reliable.
- Keep validation scripts honest about skipped unavailable harnesses.
- Run available package checks and `git diff --check`.
- Do not reopen prior adapter implementation tickets unless concrete validation finds a mismatch; if so, stop and report the mismatch.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, stay inside its scope, update named records, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Targeted grep/source inspection proving stale natural Playbook activation claims were removed or rewritten.
- Source inspection of updated test fixtures showing negative natural-prompt coverage and positive explicit-invocation coverage or an honest documented limit.
- Run `npm --prefix loom-core run smoke`.
- Run `npm --prefix loom-playbooks run smoke`.
- Run `npm --prefix loom-playbooks run pack:check`.
- Run `gemini extensions validate "$PWD/loom-playbooks"` if Gemini command files or package metadata remain relevant to the final validation.
- Run `claude plugin validate "$PWD/loom-playbooks"` if Claude plugin metadata remains relevant and the validator is available.
- Run `git diff --check`.

## Stop Conditions

- Stop if updated tests would require networked, credentialed, destructive, or unavailable harness behavior to claim success.
- Stop if validation reveals an adapter implementation mismatch that belongs to a prior ticket.
- Stop if docs require a product-direction choice not already settled in the spec, plan, research, or tickets.
- Stop before modifying unrelated product-visible Loom doctrine beyond this ticket's docs/tests scope.

## Output Contract

The worker must update this packet and target ticket or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

## Worker Output

Outcome: stop.

Files changed:

- `CLAUDE.md`
- `README.md`
- `INSTALL.md`
- `ARCHITECTURE.md`
- `loom-playbooks/README.md`
- `loom-playbooks/package.json`
- `tests/skill-triggering/run-test.sh`
- `tests/skill-triggering/run-all.sh`

Records changed:

- `.loom/tickets/20260515-playbook-explicit-macro-docs-tests.md`
- `.loom/packets/ralph/20260515T235318Z-playbook-explicit-macro-docs-tests.md`

Evidence, review findings, validation output, or observations gathered:

- Updated `CLAUDE.md` so the React todo natural-prompt acceptance test expects Core Loom routing or shaping and explicitly says Playbooks must not auto-load from that prompt.
- Updated human-facing docs to describe Playbooks as explicit workflow macros or explicit-only skills per harness: OpenCode command entries, Gemini extension commands, Claude/Cursor explicit-only skills, and Codex explicit-only skills without custom slash-command claims.
- Updated `tests/skill-triggering/run-test.sh` so natural-prompt runs can fail on forbidden Playbook tool invocations while still checking expected Core skill routing or visible Core routing for `none` cases.
- Updated `tests/skill-triggering/run-all.sh` so representative natural prompts forbid implicit Playbook activation and the suite includes positive static OpenCode command coverage via `npm --prefix loom-playbooks run smoke`.
- Source inspection: `rg --glob '!.loom/**' 'auto-triggers.*loom-idea-refine|then routes to\s+`loom-idea-refine`|skill descriptions are the activation surface|trigger-oriented skill descriptions|OpenCode playbook package for optional Loom workflow skills' .` produced no matches.
- Source inspection: `rg --glob '!.loom/**' 'loom-playbooks/skills|skills/` tree' .` produced no matches.
- `bash -n tests/skill-triggering/run-test.sh` passed.
- `bash -n tests/skill-triggering/run-all.sh` passed.
- `npm --prefix loom-core run smoke` passed with `ok: true` and `activationChecks.ok: true`.
- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `commandCount: 25`, `macroCount: 25`, `registeredPlaybookSkillPaths: []`, and `playbookSkillPathsRegistered: false`.
- `npm --prefix loom-playbooks run pack:check` passed and included the package entrypoint plus `playbooks/` corpus.
- `gemini extensions validate "$PWD/loom-playbooks"` passed.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `git diff --check` passed.

What was not verified or reviewed:

- Did not run live `opencode run` natural-prompt activation tests because claiming success from them would require networked, credentialed harness behavior, matching the packet stop condition.
- Did not run root/Core Gemini validation because this packet did not change root/Core Gemini manifests or bootstrap files.
- Did not create a final audit record; the target ticket now needs audit for ACC-005.

Blockers, risks, or assumptions discovered:

- Residual risk remains that live harness behavior can differ from static source/package validation. The updated tests are ready to check negative Playbook activation when a live OpenCode run is appropriate, but this packet does not claim that live result.

Recommended next move for the consuming surface:

- Run a bounded Ralph audit for `ticket:20260515-playbook-explicit-macro-docs-tests`, focused on ACC-001 through ACC-005 and especially whether static/package evidence plus the live-harness limitation is sufficient for the final activation-behavior claim.
