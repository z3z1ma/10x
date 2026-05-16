# Playbook Explicit Macro Docs Tests Followup Audit

ID: packet:20260516T002254Z-playbook-explicit-macro-docs-tests-audit-followup
Type: Packet
Status: consumed
Created: 2026-05-16 00:22 UTC
Updated: 2026-05-16 00:25 UTC
Target: ticket:20260515-playbook-explicit-macro-docs-tests
Packet Kind: Ralph
Mode: review
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: audit-2
Risk: medium - verifies final activation-risk claim after FIND-001 fix.
Review Lens: audit, acceptance, FIND-001 disposition, negative Playbook activation coverage, evidence sufficiency
Change Class: final docs/tests validation review

## Mission

Perform a follow-up adversarial audit of `ticket:20260515-playbook-explicit-macro-docs-tests` after the FIND-001 fix. Determine whether ACC-002 and ACC-005 are now supported and whether the ticket can close with the documented live-harness limitation.

## Context Bundle

Records:

- `ticket:20260515-playbook-explicit-macro-docs-tests` - target ticket, current finding disposition, and validation evidence.
- `audit:20260516-playbook-explicit-macro-docs-tests` - prior `changes-needed` audit with FIND-001.
- `packet:20260516T001257Z-playbook-explicit-macro-docs-tests-audit` - prior audit packet output.
- `packet:20260515T235318Z-playbook-explicit-macro-docs-tests` - implementation packet and original validation output.
- `plan:20260515-playbook-explicit-macros` and `spec:playbook-explicit-macros` - intended behavior and final validation milestone.

Files:

- `tests/skill-triggering/run-test.sh` - should now derive all Playbook names by default and fail on any Playbook invocation.
- `tests/skill-triggering/run-all.sh` - should now call the runner without prompt-specific forbidden subsets so all Playbooks are forbidden.
- `CLAUDE.md`, `README.md`, `INSTALL.md`, `ARCHITECTURE.md`, `loom-playbooks/README.md`, and `loom-playbooks/package.json` - docs/package surfaces changed by the implementation packet.
- `loom-playbooks/playbooks/**` - source set used by the test runner to derive full forbidden Playbook names.

## Read Scope

- `.loom/tickets/20260515-playbook-explicit-macro-docs-tests.md`
- `.loom/audit/20260516-playbook-explicit-macro-docs-tests.md`
- `.loom/packets/ralph/20260516T001257Z-playbook-explicit-macro-docs-tests-audit.md`
- `.loom/packets/ralph/20260515T235318Z-playbook-explicit-macro-docs-tests.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- Current git diff for docs/tests/package files.
- `tests/skill-triggering/run-test.sh`
- `tests/skill-triggering/run-all.sh`
- `tests/skill-triggering/prompts/*.txt`
- `loom-playbooks/playbooks/**/SKILL.md`
- `CLAUDE.md`
- `README.md`
- `INSTALL.md`
- `ARCHITECTURE.md`
- `loom-playbooks/README.md`
- `loom-playbooks/package.json`

## Write Scope

Records Or Artifacts:

- this packet - fill `## Worker Output`, update `Status:`, and include findings and verdict.

Source Paths:

- None - this is a review packet. Do not edit source or tickets. Return findings for the parent to record and disposition.

## Source Snapshot

Follow-up state to challenge:

- `tests/skill-triggering/run-test.sh` now defaults `FORBIDDEN_PLAYBOOKS` to `all`, derives names from `loom-playbooks/playbooks/loom-*`, fails if no Playbook names are found, and checks every derived name against the OpenCode log.
- `tests/skill-triggering/run-all.sh` no longer passes prompt-specific forbidden subsets; every representative natural-prompt case uses the runner default and forbids all Playbooks.
- Validation after the fix passed: `bash -n` for both scripts, Core smoke, Playbooks smoke, Playbooks pack check, Gemini Playbooks extension validation, Claude Playbooks plugin validation, and `git diff --check`.
- Live `opencode run` natural-prompt activation remains intentionally unverified because it requires networked, credentialed harness behavior.

## Task

Review the FIND-001 fix and final closure story. Focus on:

- Whether natural-prompt tests now fail on any Playbook invocation rather than selected subsets.
- Whether expected Core skills such as `using-loom`, `loom-tickets`, and `loom-ralph` can still be observed without confusing them with Playbook names.
- Whether the docs/tests/package evidence now supports ACC-001 through ACC-005 within the documented static/local validation limits.
- Whether live-harness non-execution is honestly documented as residual risk rather than overclaimed.

Do not fix issues. Return findings with file/line or record references when practical, plus a verdict.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, perform the bounded audit, update this packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Source inspect `run-test.sh` and `run-all.sh` for the all-Playbook negative check.
- Source inspect docs for stale natural Playbook activation claims only if needed to support the final verdict.
- Rerun feasible static/package checks, especially `bash -n` for scripts, Core smoke, Playbooks smoke, Playbooks pack check, adapter validators touched by the ticket, and `git diff --check`.
- Findings should use `FIND-*` IDs for material issues, or say no material findings within scope.
- Verdict should be one of `clear`, `concerns`, `changes-needed`, or `inconclusive`, with limits.

## Stop Conditions

- Stop and return `inconclusive` if target docs/tests change under review.
- Stop instead of modifying source or tickets.
- Stop and name missing context if the follow-up claim cannot be judged from local source and package validation.

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

- `.loom/packets/ralph/20260516T002254Z-playbook-explicit-macro-docs-tests-audit-followup.md` - updated packet status and filled this Worker Output.

Evidence, review findings, validation output, or observations gathered:

- Source inspection of `tests/skill-triggering/run-test.sh:29-41` found the runner now defaults `FORBIDDEN_PLAYBOOKS` to `all`, derives every `loom-*` Playbook directory name from `loom-playbooks/playbooks/`, fails if no names are found, and still supports explicit `none` or CSV overrides.
- Source inspection of `tests/skill-triggering/run-test.sh:78-91` found negative checks now iterate over the full derived Playbook set by default and fail when any forbidden Playbook name appears in the OpenCode log patterns reviewed by the test.
- Source inspection of `tests/skill-triggering/run-test.sh:93-110` found expected Core routing remains observable separately: `none` cases require visible Core Loom routing, while `loom-tickets` and `loom-ralph` cases still check expected Core skill activation without adding those Core names to the forbidden Playbook set.
- Source inspection of `tests/skill-triggering/run-all.sh:9-24` found representative natural-prompt cases now call the runner without prompt-specific forbidden subsets, so each case uses the default all-Playbook negative check.
- Source inspection of `loom-playbooks/playbooks/**/SKILL.md` found 25 Playbook `SKILL.md` files, matching the Playbooks smoke output and the derived-directory strategy.
- Source inspection of `CLAUDE.md:14-17`, `README.md:168-199`, `INSTALL.md:112-181`, `INSTALL.md:229-272`, `ARCHITECTURE.md:99-139`, `loom-playbooks/README.md:87-90`, and `loom-playbooks/package.json:4` found docs/package wording continues to describe Playbooks as explicit macros or explicit-only skills, not natural-prompt auto-loaded Playbooks.
- Scoped `git diff -- CLAUDE.md README.md INSTALL.md ARCHITECTURE.md loom-playbooks/README.md loom-playbooks/package.json tests/skill-triggering/run-test.sh tests/skill-triggering/run-all.sh tests/skill-triggering/prompts` showed the FIND-001 follow-up diff is limited to `tests/skill-triggering/run-test.sh` and `tests/skill-triggering/run-all.sh`.
- `bash -n tests/skill-triggering/run-test.sh` passed.
- `bash -n tests/skill-triggering/run-all.sh` passed.
- `npm --prefix loom-core run smoke` passed with `ok: true` and `activationChecks.ok: true`.
- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `commandCount: 25`, `macroCount: 25`, `registeredPlaybookSkillPaths: []`, and `playbookSkillPathsRegistered: false`.
- `npm --prefix loom-playbooks run pack:check` passed and the dry-run tarball included `loom-playbooks.mjs` plus the `playbooks/` corpus.
- `gemini extensions validate "$PWD/loom-playbooks"` passed.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `git diff --check` passed.

Findings:

- No material FIND-* findings within this packet's read scope.

Bounded audit verdict: `clear`.

ACC-002 and ACC-005 are now supported within the packet's local/static validation boundary. The prior FIND-001 false-positive gap is resolved because the natural-prompt runner forbids all Playbook names by default and the suite no longer narrows that check per prompt. ACC-001, ACC-003, and ACC-004 remain supported by the inspected docs/package wording and successful static/package/adapter validation. This verdict does not claim live natural-prompt `opencode run` behavior was executed successfully; it accepts the ticket's documented live-harness limitation as an honest residual risk.

What was not verified or reviewed:

- Live `opencode run` natural-prompt activation was not executed because it requires networked, credentialed harness behavior and the ticket already documents that limit.
- Root/Core Gemini validation was not run because this packet targets the Playbooks follow-up and the reviewed diff did not change root/Core Gemini manifests or bootstrap files.
- Exhaustive semantic review of every Playbook body was not performed; this audit used the Playbook directory set to judge the all-Playbooks negative coverage and relied on prior adapter/package validation for explicit macro surfaces.

Blockers, risks, or assumptions discovered:

- No blocker found.
- Residual risk remains that live harness behavior may differ from static/package validation until a credentialed OpenCode integration run is deliberately performed.
- The negative log check is as strong as the reviewed OpenCode log patterns in `run-test.sh`; this audit did not produce a live log proving every possible harness log shape.

Recommended next move for the consuming surface:

- Record this follow-up audit result under the audit surface or ticket closure story, then close `ticket:20260515-playbook-explicit-macro-docs-tests` if the parent accepts the documented live-harness limitation and residual risk.
