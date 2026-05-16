# Playbook Activation Tests Procedure

ID: knowledge:playbook-activation-tests-procedure
Type: Knowledge Procedure
Status: active
Created: 2026-05-16
Updated: 2026-05-16
Triggers: Playbook activation tests, natural prompts, skill-triggering, explicit macros, implicit Playbook invocation, tests/skill-triggering
Applies To: tests/skill-triggering/, loom-playbooks/playbooks/, Playbook explicit macro validation

## Summary

When validating that natural prompts do not auto-activate Loom Playbooks, tests should fail on any Playbook invocation, not only a prompt-specific subset of likely Playbooks.

## Use When

Use this when changing `tests/skill-triggering/`, validating Playbook explicit macro behavior, auditing activation tests, or checking regressions around natural-prompt Playbook invocation.

## Procedure

Derive the forbidden Playbook names from the current Playbook corpus, currently `loom-playbooks/playbooks/loom-*`, so the negative check tracks additions, removals, and renames.

Natural-prompt cases should use the full derived Playbook set by default. Only use a narrower CSV override or `none` when the test is explicitly not making a no-Playbook-activation claim.

Keep expected Core routing separate from forbidden Playbook checks. Core skills such as `using-loom`, `loom-tickets`, and `loom-ralph` may be expected for natural routing, but Playbook names from `loom-playbooks/playbooks/` should remain forbidden unless the prompt explicitly invokes a Playbook.

Static command-registration smoke can support explicit macro availability, but it does not prove live natural-prompt behavior. Preserve that limit when closing tickets or audits.

## Stop Or Escalate When

Stop and route to audit or ticket work if a test only forbids selected likely Playbooks while claiming no Playbooks auto-activate. That false-positive gap was FIND-001 in `audit:20260516-playbook-explicit-macro-docs-tests`.

Escalate to research or a harness-specific ticket if OpenCode log shapes change enough that `tests/skill-triggering/run-test.sh` can no longer detect Playbook invocations reliably from local logs.

## Boundaries Or Sources

This procedure covers the repository's static/local activation validation. It does not claim live harness behavior unless a credentialed, networked harness run was actually performed and recorded.

## Related Records

- `audit:20260516-playbook-explicit-macro-docs-tests` - recorded the false-positive gap where only selected Playbooks were forbidden.
- `audit:20260516-playbook-explicit-macro-docs-tests-followup` - confirmed the all-Playbook negative check resolved the finding within local/static validation limits.
- `ticket:20260515-playbook-explicit-macro-docs-tests` - closed final docs/tests ticket that introduced the current test pattern.
