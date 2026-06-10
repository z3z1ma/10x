# Playbook Explicit Macro Docs Tests Audit

Status: recorded
Created: 2026-05-16
Updated: 2026-05-16
Target: .loom/tickets/done/20260515-playbook-explicit-macro-docs-tests.md

## Summary

Ralph audited the final docs/tests validation for `.loom/tickets/done/20260515-playbook-explicit-macro-docs-tests.md`. The review found one material test false-positive gap and returned a `changes-needed` verdict.

## Target

The audit targeted the docs/tests alignment work from `former packet 20260515T235318Z-playbook-explicit-macro-docs-tests`, especially the natural-prompt activation test changes in `tests/skill-triggering/run-all.sh` and `tests/skill-triggering/run-test.sh`.

## Audit Scope And Lenses

Scope was limited to ACC-001 through ACC-005 for the docs/tests ticket: stale docs claims, negative natural-prompt Playbook coverage, positive explicit invocation coverage, final package checks, and final activation-risk audit posture.

The review lenses were audit, acceptance, activation behavior, evidence sufficiency, docs leakage, and test false positives.

Out of scope: live `opencode run` natural-prompt execution, root/Core Gemini validation, and exhaustive semantic review of every Playbook body.

## Context And Evidence Reviewed

- Ralph packet: `former packet 20260516T001257Z-playbook-explicit-macro-docs-tests-audit` - bounded review contract and worker output.
- Implementation packet: `former packet 20260515T235318Z-playbook-explicit-macro-docs-tests` - docs/tests implementation output and validation summary.
- Ticket: `.loom/tickets/done/20260515-playbook-explicit-macro-docs-tests.md` - ACC-001 through ACC-005 and current review state.
- Source files: `CLAUDE.md`, `README.md`, `INSTALL.md`, `ARCHITECTURE.md`, `loom-playbooks/README.md`, `loom-playbooks/package.json`, `loom-playbooks/loom-playbooks.mjs`, `tests/skill-triggering/run-test.sh`, and `tests/skill-triggering/run-all.sh`.
- Validation run by the auditor: `bash -n tests/skill-triggering/run-test.sh`, `bash -n tests/skill-triggering/run-all.sh`, `npm --prefix loom-core run smoke`, `npm --prefix loom-playbooks run smoke`, `npm --prefix loom-playbooks run pack:check`, `gemini extensions validate "$PWD/loom-playbooks"`, `claude plugin validate "$PWD/loom-playbooks"`, and `git diff --check`.

## Findings

### FIND-001: Natural-Prompt Tests Forbid Only Selected Playbooks

`tests/skill-triggering/run-all.sh:9-14` and `tests/skill-triggering/run-test.sh:64-78` do not prove representative natural prompts avoid all implicit Playbook activation. The runner only fails on the explicit comma-separated forbidden list for each case, and `run-all.sh` supplies partial lists such as `loom-security-and-hardening,loom-incremental-implementation` for the ticket prompt and `loom-parallel-worker-coordination` for the Ralph prompt. If a natural prompt implicitly invoked any other Playbook, the negative check would still pass.

This challenges ACC-002 and ACC-005 because the false-positive gap leaves the "do not auto-load Playbooks" claim insufficiently supported. Follow-up should make natural-prompt cases fail on any Playbook invocation, ideally by deriving the full Playbook name set from `loom-playbooks`.

## Verdict

`changes-needed` - docs alignment and package/static validation are supported within the reviewed scope, and ACC-001, ACC-003, and ACC-004 are mostly supported with documented live-harness limits. ACC-002 and ACC-005 are not ready for closure because the current negative test logic checks selected forbidden Playbooks rather than the invariant that no Playbook macro or explicit-only Playbook skill was implicitly invoked from ordinary natural prompts.

## Required Follow-up

Update the activation tests so natural-prompt cases fail on any Playbook invocation while still allowing expected Core record skills such as `using-loom`, `loom-tickets`, or `loom-ralph`. Rerun the static/package checks and repeat a bounded audit for ACC-002 and ACC-005 before closure.

## Residual Risk

- Live `opencode run` natural-prompt activation remains unverified because it requires networked, credentialed harness behavior.
- Root/Core Gemini validation was not run because the implementation did not change root/Core Gemini manifests or bootstrap files.

## Related Records

- `.loom/tickets/done/20260515-playbook-explicit-macro-docs-tests.md` - consuming ticket and finding disposition owner.
- `former packet 20260516T001257Z-playbook-explicit-macro-docs-tests-audit` - Ralph review output backing this audit.
- `former packet 20260515T235318Z-playbook-explicit-macro-docs-tests` - implementation packet under review.
