# Playbook Explicit Macro Docs And Tests

Status: done
Created: 2026-05-15
Updated: 2026-05-16

Legacy note: Risk — medium - rewrites validation expectations around Loom activation behavior and must avoid stale acceptance claims.

Priority: medium - final alignment ticket after package surfaces change.
Depends-On: .loom/tickets/done/20260515-opencode-playbook-commands.md, .loom/tickets/done/20260515-native-playbook-explicit-surfaces.md, .loom/tickets/done/20260515-gemini-playbook-commands.md

## Summary

Update docs, activation tests, smoke expectations, and final validation so Loom Playbooks are tested and described as explicit macros. The closure claim is that human-facing guidance and executable checks no longer expect natural prompts to auto-trigger Playbooks, while explicit Playbook invocation remains validated where feasible.

## Related Records

- `.loom/tickets/20260515-playbook-explicit-macros.md` - defines the broader conversion and final validation milestone.
- `.loom/specs/playbook-explicit-macros.md` - defines negative natural-prompt and positive explicit-invocation requirements.
- `.loom/research/20260515-playbook-command-surfaces.md` - constrains harness-specific documentation language.
- `.loom/evidence/20260515-playbook-activation-stacking.md` - records the old failure mode tests should stop rewarding.
- `.loom/reviews/20260516-playbook-explicit-macro-docs-tests.md` - first final audit; recorded FIND-001 and changes-needed verdict.
- `.loom/reviews/20260516-playbook-explicit-macro-docs-tests-followup.md` - follow-up clear audit after FIND-001 fix.
- `.loom/knowledge/playbook-activation-tests-procedure.md` - retrospective prevention note for future activation test changes.
- `CLAUDE.md` - formerly claimed `Let's make a react todo list` should route to `loom-idea-refine`; now aligned with Core-first natural routing.
- `tests/skill-triggering/` - formerly included natural-prompt Playbook activation expectations; now checks against implicit Playbook invocation.
- `loom-playbooks/README.md` and package docs - human-facing Playbook install and behavior prose aligned by this ticket.

## Scope

May change human-facing docs that describe Playbooks, activation, supported harness syntax, validation, or package behavior. Likely files include `CLAUDE.md`, root/package READMEs, adapter docs, and any test README or fixtures.

May change activation test scripts and fixtures to add negative natural-prompt checks and positive explicit macro invocation checks where the harness can run them. Tests should distinguish Core skill activation from Playbook macro invocation.

May update package smoke outputs only as needed to align with final adapter behavior. Must not introduce a new runtime app, daemon, dashboard, database, or external dependency.

Must not reopen implementation choices from the prior adapter tickets unless validation finds a concrete mismatch; if found, block or route back to the owning ticket instead of hiding it in docs.

## Acceptance

- ACC-001: Docs no longer state that natural prompts should auto-trigger Playbooks such as `loom-idea-refine`; they describe Playbooks as explicit optional workflow macros or explicit-only skills per harness.
  - Evidence: Targeted grep/source inspection over docs for stale natural Playbook activation claims.
  - Audit: Review should challenge whether docs still make Playbooks sound like mandatory first-action routes.

- ACC-002: Test fixtures include negative coverage showing representative natural prompts do not auto-load Playbooks while Core routing remains available.
  - Evidence: Source inspection of tests and live output where feasible.
  - Audit: Review should challenge false positives that only check expected activation and ignore extra Playbook invocations.

- ACC-003: Test fixtures or smoke checks include positive coverage for explicit Playbook invocation in at least the local runnable harness surface, with documented limits for harnesses that cannot be validated locally.
  - Evidence: Test output, smoke output, or documented source-inspection evidence tied to each supported harness.
  - Audit: Review should challenge whether explicit macro discoverability was assumed rather than checked.

- ACC-004: Final package checks pass or document unavailable harness validators honestly.
  - Evidence: `npm --prefix loom-core run smoke`, `npm --prefix loom-playbooks run smoke`, `npm --prefix loom-playbooks run pack:check`, adapter validation commands touched by the implementation, and `git diff --check` as applicable.
  - Audit: Command evidence is sufficient for static package validity; activation behavior still needs review.

- ACC-005: A final audit record or explicit audit waiver addresses the main risk: Playbooks should no longer auto-activate from ordinary natural prompts while remaining explicitly invokable.
  - Evidence: `.loom/audit/` record from a Ralph review packet, or a ticket journal entry explaining why separate audit would not add useful trust after source and command evidence.
  - Audit: This criterion owns the final audit posture.

## Current State

Closed. Ralph packet `former packet 20260515T235318Z-playbook-explicit-macro-docs-tests` returned `stop`: stale docs now describe Playbooks as explicit optional workflow macros or explicit-only skills, `CLAUDE.md` no longer expects `Let's make a react todo list` to route to `loom-idea-refine`, and activation tests now include negative natural-prompt Playbook checks plus positive OpenCode command-registration smoke coverage.

Evidence gathered: active-doc grep outside `.loom/` found no stale `loom-idea-refine` natural-routing claim, trigger-description Playbook activation wording, old optional workflow-skills package description, or `loom-playbooks/skills` active path references; `bash -n tests/skill-triggering/run-test.sh` and `bash -n tests/skill-triggering/run-all.sh` passed; `npm --prefix loom-core run smoke` passed; `npm --prefix loom-playbooks run smoke` passed with `commandCount: 25`, `macroCount: 25`, `registeredPlaybookSkillPaths: []`, and `playbookSkillPathsRegistered: false`; `npm --prefix loom-playbooks run pack:check` passed; `gemini extensions validate "$PWD/loom-playbooks"` passed; `claude plugin validate "$PWD/loom-playbooks"` passed; `git diff --check` passed.

Audit state: `.loom/reviews/20260516-playbook-explicit-macro-docs-tests.md` returned `changes-needed` with FIND-001. FIND-001 is resolved by updating `tests/skill-triggering/run-test.sh` to derive the full Playbook name set from `loom-playbooks/playbooks/` by default and by updating `tests/skill-triggering/run-all.sh` so every natural-prompt case forbids any Playbook invocation, not a prompt-specific subset. Validation after the fix passed: `bash -n tests/skill-triggering/run-test.sh`, `bash -n tests/skill-triggering/run-all.sh`, `npm --prefix loom-core run smoke`, `npm --prefix loom-playbooks run smoke`, `npm --prefix loom-playbooks run pack:check`, `gemini extensions validate "$PWD/loom-playbooks"`, `claude plugin validate "$PWD/loom-playbooks"`, and `git diff --check`. Follow-up audit `.loom/reviews/20260516-playbook-explicit-macro-docs-tests-followup.md` returned `clear` with no material findings, supporting closure for ACC-001 through ACC-005 within the documented static/local validation boundary.

Not verified: live natural-prompt `opencode run` activation was not executed because it would require networked, credentialed harness behavior, which the packet stop conditions excluded as a basis for claiming success.

## Journal

- 2026-05-15: Created ticket from `.loom/tickets/20260515-playbook-explicit-macros.md`; depends on adapter conversion tickets.
- 2026-05-15: Set status to active after Gemini command ticket closure and launched `former packet 20260515T235318Z-playbook-explicit-macro-docs-tests` for docs/tests/final validation implementation.
- 2026-05-16: `former packet 20260515T235318Z-playbook-explicit-macro-docs-tests` returned `stop`: updated stale docs, revised activation test scripts for negative natural-prompt Playbook checks and static explicit OpenCode command coverage, ran syntax/source inspections plus Core/Playbooks smoke, Playbooks pack dry-run, Gemini Playbooks extension validation, Claude Playbooks plugin validation, and `git diff --check`. Moved ticket to review for final audit; live OpenCode natural-prompt runs remain unverified due networked/credentialed harness behavior.
- 2026-05-16: Recorded `.loom/reviews/20260516-playbook-explicit-macro-docs-tests.md`; verdict `changes-needed`. FIND-001 says natural-prompt tests only forbid selected Playbook names per prompt and could miss implicit invocation of another Playbook. Returned ticket to active for test fix.
- 2026-05-16: Resolved FIND-001 by changing natural-prompt tests to derive and forbid all Playbook names by default, then reran syntax checks, Core smoke, Playbooks smoke, Playbooks pack check, Gemini Playbooks validation, Claude Playbooks validation, and `git diff --check`; all passed. Moved ticket back to review for repeat audit.
- 2026-05-16: Recorded `.loom/reviews/20260516-playbook-explicit-macro-docs-tests-followup.md`; verdict `clear`, no material findings. Closed ticket with residual live-harness limitation documented.
- 2026-05-16: Retrospective promotion created `.loom/knowledge/playbook-activation-tests-procedure.md` so future activation-test changes preserve the all-Playbook negative check and live-harness limitation.
