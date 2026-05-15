# Playbook Activation Stacking Observations

ID: evidence:20260515-playbook-activation-stacking
Type: Evidence Dossier
Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Observed: 2026-05-14 to 2026-05-15

## Summary

This dossier preserves observations that Loom Playbooks can stack multiple
workflow skills during simple natural prompts, and that current activation checks
prove expected skill presence without checking for unwanted additional playbook
activation.

## Observations

- Observation: Current Core smoke passes and still enforces strong activation.
  - Procedure/source: `npm --prefix loom-core run smoke` from the repository root on 2026-05-15.
  - Actual result: command exited successfully with `"ok": true`, `skillCount: 11`, `usingLoomFileCount: 8`, `bootstrapInjectionPartCount: 1`, `bootstrapInjectionIsDeduped: true`, and `activationChecks.ok: true`. The reported required activation phrase count was `18` with no missing phrases.

- Observation: Current Playbooks smoke passes and exposes 25 workflow skills without preloading Core doctrine.
  - Procedure/source: `npm --prefix loom-playbooks run smoke` from the repository root on 2026-05-15.
  - Actual result: command exited successfully with `"ok": true`, `skillCount: 25`, `usingLoomReferenceCount: 0`, `doesNotPreloadCoreDoctrine: true`, and `activationChecks.ok: true`.

- Observation: The previous live OpenCode natural-prompt test for `loom-idea-refine` also invoked a second playbook.
  - Procedure/source: inspected `/tmp/loom-tests/1778771862/skill-triggering/loom-idea-refine/opencode-output.json`, produced by the 2026-05-14 activation test for prompt `Let's make a react todo list`.
  - Actual result: `rg -o '"input":\{"name":"[^"]+"\}' ... | sort | uniq -c` found:

```text
      1 "input":{"name":"loom-frontend-ui-engineering"}
      1 "input":{"name":"loom-idea-refine"}
```

- Observation: The previous live OpenCode natural-prompt test for `loom-tickets` also invoked two additional playbooks.
  - Procedure/source: inspected `/tmp/loom-tests/1778772037/skill-triggering/loom-tickets/opencode-output.json`, produced by the 2026-05-14 activation test for prompt `Create a ticket for the auth cleanup work and start implementing it.`
  - Actual result: the same scan found:

```text
      1 "input":{"name":"loom-incremental-implementation"}
      1 "input":{"name":"loom-security-and-hardening"}
      1 "input":{"name":"loom-tickets"}
```

- Observation: The previous live OpenCode natural-prompt tests for `loom-debugging-and-error-recovery` and `loom-ralph` did not show extra top-level skill invocations in the same scan.
  - Procedure/source: inspected `/tmp/loom-tests/1778771985/skill-triggering/loom-debugging-and-error-recovery/opencode-output.json` and `/tmp/loom-tests/1778772121/skill-triggering/loom-ralph/opencode-output.json`.
  - Actual result: scans found one `loom-debugging-and-error-recovery` invocation in the debugging run and one `loom-ralph` invocation in the Ralph run.

- Observation: The natural-prompt activation test runner checks for expected skill presence, not absence of additional playbook activation.
  - Procedure/source: source inspection of `tests/skill-triggering/run-test.sh`.
  - Actual result: lines 60-65 define a skill-tool pattern and expected skill-name pattern, then pass when both are found. The script does not fail when other Loom skills are also invoked.

- Observation: The natural-prompt activation suite is narrow.
  - Procedure/source: source inspection of `tests/skill-triggering/run-all.sh`.
  - Actual result: the suite only expects `loom-idea-refine`, `loom-debugging-and-error-recovery`, `loom-tickets`, and `loom-ralph`.

## What This Shows

- `research:20260515-playbooks-core-activation-pressure` - supports - Playbooks are currently exposed as 25 trigger-oriented workflow skills, and current smoke checks still treat that exposure as valid.
- `research:20260515-playbooks-core-activation-pressure` - supports - Natural prompts can load multiple workflow playbooks in one run.
- `research:20260515-playbooks-core-activation-pressure` - supports - The current activation tests are compliance tests for expected skill invocation, not precision tests for preserving a single route or suppressing unnecessary playbook pressure.

## What This Does Not Show

This evidence does not prove that every harness behaves like OpenCode. The live
activation logs cited here are OpenCode 1.14.48 runs from 2026-05-14. The current
2026-05-15 smoke checks verify package and activation shape, not live model
behavior. The `/tmp/loom-tests/...` log paths are local transient artifacts; the
key excerpts above preserve the material observations.

## Related Records

- `research:20260515-playbooks-core-activation-pressure` - consumes this evidence.
- `evidence:20260513-superpowers-style-activation-checks` - earlier activation-validation dossier whose live log paths were inspected.
- `ticket:20260513-superpowers-style-activation-doctrine` - introduced the Superpowers-style activation posture that made these checks important.
