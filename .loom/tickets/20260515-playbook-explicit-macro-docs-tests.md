# Playbook Explicit Macro Docs And Tests

ID: ticket:20260515-playbook-explicit-macro-docs-tests
Type: Ticket
Status: review
Created: 2026-05-15
Updated: 2026-05-16
Risk: medium - rewrites validation expectations around Loom activation behavior and must avoid stale acceptance claims.
Priority: medium - final alignment ticket after package surfaces change.
Depends On: ticket:20260515-opencode-playbook-commands, ticket:20260515-native-playbook-explicit-surfaces, ticket:20260515-gemini-playbook-commands

## Summary

Update docs, activation tests, smoke expectations, and final validation so Loom Playbooks are tested and described as explicit macros. The closure claim is that human-facing guidance and executable checks no longer expect natural prompts to auto-trigger Playbooks, while explicit Playbook invocation remains validated where feasible.

## Related Records

- `plan:20260515-playbook-explicit-macros` - defines the broader conversion and final validation milestone.
- `spec:playbook-explicit-macros` - defines negative natural-prompt and positive explicit-invocation requirements.
- `research:20260515-playbook-command-surfaces` - constrains harness-specific documentation language.
- `evidence:20260515-playbook-activation-stacking` - records the old failure mode tests should stop rewarding.
- `CLAUDE.md` - currently claims `Let's make a react todo list` should route to `loom-idea-refine`.
- `tests/skill-triggering/` - currently includes natural-prompt Playbook activation expectations.
- `loom-playbooks/README.md` and package docs - likely human-facing Playbook install and behavior prose to align.

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

Review. Ralph packet `packet:20260515T235318Z-playbook-explicit-macro-docs-tests` returned `stop`: stale docs now describe Playbooks as explicit optional workflow macros or explicit-only skills, `CLAUDE.md` no longer expects `Let's make a react todo list` to route to `loom-idea-refine`, and activation tests now include negative natural-prompt Playbook checks plus positive OpenCode command-registration smoke coverage.

Evidence gathered: active-doc grep outside `.loom/` found no stale `loom-idea-refine` natural-routing claim, trigger-description Playbook activation wording, old optional workflow-skills package description, or `loom-playbooks/skills` active path references; `bash -n tests/skill-triggering/run-test.sh` and `bash -n tests/skill-triggering/run-all.sh` passed; `npm --prefix loom-core run smoke` passed; `npm --prefix loom-playbooks run smoke` passed with `commandCount: 25`, `macroCount: 25`, `registeredPlaybookSkillPaths: []`, and `playbookSkillPathsRegistered: false`; `npm --prefix loom-playbooks run pack:check` passed; `gemini extensions validate "$PWD/loom-playbooks"` passed; `claude plugin validate "$PWD/loom-playbooks"` passed; `git diff --check` passed.

Not verified: live natural-prompt `opencode run` activation was not executed because it would require networked, credentialed harness behavior, which the packet stop conditions excluded as a basis for claiming success. The next honest move is final audit for ACC-005, focused on whether the docs/tests evidence supports the activation-behavior claim.

## Journal

- 2026-05-15: Created ticket from `plan:20260515-playbook-explicit-macros`; depends on adapter conversion tickets.
- 2026-05-15: Set status to active after Gemini command ticket closure and launched `packet:20260515T235318Z-playbook-explicit-macro-docs-tests` for docs/tests/final validation implementation.
- 2026-05-16: `packet:20260515T235318Z-playbook-explicit-macro-docs-tests` returned `stop`: updated stale docs, revised activation test scripts for negative natural-prompt Playbook checks and static explicit OpenCode command coverage, ran syntax/source inspections plus Core/Playbooks smoke, Playbooks pack dry-run, Gemini Playbooks extension validation, Claude Playbooks plugin validation, and `git diff --check`. Moved ticket to review for final audit; live OpenCode natural-prompt runs remain unverified due networked/credentialed harness behavior.
