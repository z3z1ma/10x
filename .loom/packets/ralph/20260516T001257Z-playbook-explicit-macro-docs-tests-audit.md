# Playbook Explicit Macro Docs Tests Audit

ID: packet:20260516T001257Z-playbook-explicit-macro-docs-tests-audit
Type: Packet
Status: consumed
Created: 2026-05-16 00:12 UTC
Updated: 2026-05-16 00:16 UTC
Target: ticket:20260515-playbook-explicit-macro-docs-tests
Packet Kind: Ralph
Mode: review
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: audit-1
Risk: medium - final claim concerns activation semantics across docs, tests, and package surfaces.
Review Lens: audit, acceptance, activation behavior, evidence sufficiency, docs leakage, test false positives
Change Class: final docs/tests validation review

## Mission

Perform a bounded adversarial audit of `ticket:20260515-playbook-explicit-macro-docs-tests` against ACC-001 through ACC-005 after docs/tests alignment. Determine whether the final closure claim is supported or whether docs, tests, evidence, or residual risk require more work.

## Context Bundle

Records:

- `ticket:20260515-playbook-explicit-macro-docs-tests` - target ticket, acceptance, implementation evidence, and review state.
- `packet:20260515T235318Z-playbook-explicit-macro-docs-tests` - implementation packet and worker output.
- `plan:20260515-playbook-explicit-macros` - broader plan and final validation milestone.
- `spec:playbook-explicit-macros` - explicit macro behavior contract.
- `research:20260515-playbook-command-surfaces` - harness-specific command and explicit-only constraints.
- `evidence:20260515-playbook-activation-stacking` - old failure mode that should no longer be rewarded, if present.
- Adapter closure audits: `audit:20260515-opencode-playbook-commands`, `audit:20260515-native-playbook-explicit-surfaces`, and `audit:20260515-gemini-playbook-commands`.

Files:

- `CLAUDE.md`
- `README.md`
- `INSTALL.md`
- `ARCHITECTURE.md`
- `loom-playbooks/README.md`
- `loom-playbooks/package.json`
- `loom-playbooks/loom-playbooks.mjs`
- `tests/skill-triggering/run-test.sh`
- `tests/skill-triggering/run-all.sh`
- `tests/skill-triggering/prompts/*.txt`

## Read Scope

- `.loom/tickets/20260515-playbook-explicit-macro-docs-tests.md`
- `.loom/packets/ralph/20260515T235318Z-playbook-explicit-macro-docs-tests.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/research/20260515-playbook-command-surfaces.md`
- `.loom/evidence/20260515-playbook-activation-stacking.md` if present
- `.loom/audit/20260515-opencode-playbook-commands.md`
- `.loom/audit/20260515-native-playbook-explicit-surfaces.md`
- `.loom/audit/20260515-gemini-playbook-commands.md`
- Current git diff for the files changed by the implementation packet.
- `CLAUDE.md`
- `README.md`
- `INSTALL.md`
- `ARCHITECTURE.md`
- `loom-playbooks/README.md`
- `loom-playbooks/package.json`
- `loom-playbooks/loom-playbooks.mjs`
- `tests/skill-triggering/run-test.sh`
- `tests/skill-triggering/run-all.sh`
- `tests/skill-triggering/prompts/*.txt`

## Write Scope

Records Or Artifacts:

- this packet - fill `## Worker Output`, update `Status:`, and include findings and verdict.

Source Paths:

- None - this is a review packet. Do not edit source or tickets. Return findings for the parent to record and disposition.

## Source Snapshot

Implementation summary to challenge:

- `CLAUDE.md` now expects natural prompts to exercise Core Loom routing and explicitly says Playbooks must not auto-load.
- Human-facing docs now describe Playbooks as explicit workflow macros or explicit-only skills per harness.
- `tests/skill-triggering/run-test.sh` and `run-all.sh` now include negative natural-prompt checks against forbidden Playbook invocations plus positive static OpenCode command smoke coverage.
- Static/package validation passed: shell syntax checks, Core smoke, Playbooks smoke, Playbooks pack check, Gemini Playbooks extension validation, Claude Playbooks plugin validation, and `git diff --check`.
- Live `opencode run` natural-prompt checks were intentionally not run because they require networked, credentialed harness behavior.

## Task

Review the target ticket, implementation packet, diffs, tests, docs, and validation evidence. Focus on:

- ACC-001: Do docs avoid stale claims that natural prompts should auto-trigger Playbooks and accurately describe harness-specific explicit behavior?
- ACC-002: Do tests include negative coverage that representative natural prompts should not auto-load Playbooks while Core routing remains available?
- ACC-003: Is positive explicit Playbook invocation or command registration coverage sufficient and honest for local runnable surfaces?
- ACC-004: Do final package checks pass or honestly document unavailable validators?
- ACC-005: Does this review adequately address the main final activation risk, especially the lack of live `opencode run` validation?
- Are the updated tests vulnerable to false positives, such as checking expected activation but missing extra Playbook invocations?
- Do docs or tests overclaim Codex custom slash commands, Gemini skill behavior, or natural prompt Playbook activation?

Do not fix issues. Return findings with file/line or record references when practical, plus a verdict.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, perform the bounded audit, update this packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Source inspect docs and tests for stale natural Playbook activation claims.
- Source inspect updated test logic for negative checks and static positive command coverage.
- Run or verify the same static/package checks when feasible: `bash -n` for scripts, Core smoke, Playbooks smoke, Playbooks pack check, Gemini Playbooks extension validation, Claude Playbooks plugin validation, and `git diff --check`.
- Findings should use `FIND-*` IDs for material issues, or say no material findings within scope.
- Verdict should be one of `clear`, `concerns`, `changes-needed`, or `inconclusive`, with limits.

## Stop Conditions

- Stop and return `inconclusive` if target docs/tests change under review.
- Stop instead of modifying source or tickets.
- Stop and name missing context if the activation-behavior claim cannot be judged from local source and package validation.

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

Outcome: stop.

Files changed:

- None.

Records changed:

- `.loom/packets/ralph/20260516T001257Z-playbook-explicit-macro-docs-tests-audit.md` - updated packet status and filled this Worker Output.

Evidence, review findings, validation output, or observations gathered:

- Source inspection of `CLAUDE.md`, `README.md`, `INSTALL.md`, `ARCHITECTURE.md`, and `loom-playbooks/README.md` found the target docs describe Playbooks as explicit workflow macros or explicit-only skills and no longer claim the React todo natural prompt should route to `loom-idea-refine`.
- Source inspection of `loom-playbooks/loom-playbooks.mjs` found OpenCode command registration is derived from the explicit macro catalog and does not register the Playbook corpus through `config.skills.paths`.
- Source inspection of `tests/skill-triggering/run-test.sh` found negative checks are implemented only for the comma-separated `FORBIDDEN_PLAYBOOKS` list supplied by each test case.
- Source inspection of `tests/skill-triggering/run-all.sh` found positive static OpenCode command-registration coverage through `npm --prefix loom-playbooks run smoke`.
- `bash -n tests/skill-triggering/run-test.sh` passed.
- `bash -n tests/skill-triggering/run-all.sh` passed.
- `npm --prefix loom-core run smoke` passed with `ok: true` and `activationChecks.ok: true`.
- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `commandCount: 25`, `macroCount: 25`, `registeredPlaybookSkillPaths: []`, and `playbookSkillPathsRegistered: false`.
- `npm --prefix loom-playbooks run pack:check` passed and the dry-run tarball included `loom-playbooks.mjs` plus the `playbooks/` corpus.
- `gemini extensions validate "$PWD/loom-playbooks"` passed.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `git diff --check` passed.
- Scoped `git diff -- CLAUDE.md README.md INSTALL.md ARCHITECTURE.md loom-playbooks/README.md loom-playbooks/package.json loom-playbooks/loom-playbooks.mjs tests/skill-triggering/run-test.sh tests/skill-triggering/run-all.sh tests/skill-triggering/prompts` produced no current uncommitted source diff to inspect; review used the current workspace files and the implementation packet's recorded output.

Findings:

- FIND-001: `tests/skill-triggering/run-all.sh:9-14` and `tests/skill-triggering/run-test.sh:64-78` do not prove representative natural prompts avoid all implicit Playbook activation. The runner only fails on the explicit comma-separated forbidden list for each case, and `run-all.sh` supplies partial lists such as `loom-security-and-hardening,loom-incremental-implementation` for the ticket prompt and `loom-parallel-worker-coordination` for the Ralph prompt. If a natural prompt implicitly invoked any other Playbook, the negative check would still pass. This leaves ACC-002's "do not auto-load Playbooks" claim and the packet's false-positive concern insufficiently supported.

Bounded audit verdict: `changes-needed`.

The docs alignment and package/static validation are supported within this packet's scope, and ACC-001, ACC-003, and ACC-004 are mostly supported with the already documented live-harness limitation. ACC-005 is not ready for a clear audit because ACC-002 has a material false-positive gap: the current negative test logic checks selected forbidden Playbooks rather than the invariant that no Playbook macro or explicit-only Playbook skill was implicitly invoked from ordinary natural prompts.

What was not verified or reviewed:

- Live `opencode run` natural-prompt activation was not executed because it requires networked, credentialed harness behavior and the implementation packet already documented that limit.
- Root/Core Gemini validation was not run because the scoped implementation did not change root/Core Gemini manifests or bootstrap files.
- Exhaustive review of every Playbook body was not performed; prior adapter audits cover the macro/catalog surfaces, and this audit focused on final docs/tests validation.

Blockers, risks, or assumptions discovered:

- The main blocker is FIND-001: current activation test logic can miss implicit invocation of Playbooks outside each prompt's hard-coded forbidden subset.
- Residual risk remains that live harness behavior may differ from static/package validation until a credentialed OpenCode integration run is deliberately performed.

Recommended next move for the consuming surface:

- Update the activation tests so natural-prompt cases fail on any Playbook invocation, ideally by deriving the full Playbook name set from `loom-playbooks` or otherwise checking every `loom-*` Playbook name while allowing only expected Core record skills such as `using-loom`, `loom-tickets`, or `loom-ralph`.
- Rerun the static/package checks and then repeat a bounded audit for ACC-002 and ACC-005 before ticket closure.
