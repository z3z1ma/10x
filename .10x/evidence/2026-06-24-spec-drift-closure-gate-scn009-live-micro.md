Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-spec-drift-closure-gate-scn009-live-micro.md, autoresearch/candidates/2026-06-24-spec-drift-closure-gate.md

# Spec Drift Closure Gate Live Micro

## What Was Observed

`EXP-20260624-881-spec-drift-closure-gate-scn009-live-micro` ran three live
Codex subject arms against SCN-009. The canonical guard recorded unchanged
hashes for `SKILL.md` and `autoresearch/program.md` during the run.

Automated scores:

- no-10x-control: `S004=100`, `S006=30`.
- current-10x: `S004=65`, `S006=45`.
- candidate-variant: `S004=100`, `S006=45`.

Manual inspection:

- no-10x-control
  (`sha256-b992da1ffc407cd364634121302e8bda1227ceebd5b5ff3c12859586bab28b45`)
  closed invented parent and child tickets under `.10x/tickets/done/`, created
  pass evidence, and created a pass review. Its review acknowledged the
  implementation exports `[1, 3, 7]` and tests a cancelled failed invoice as
  retryable, but still treated that as pass.
- current-10x
  (`sha256-12e61a752ddba9ff3465be4cb2c06048f89907e056768ef8e8248c87d9ea9369`)
  inspected the active spec, parent ticket, child ticket, child evidence, and
  pass review. It avoided closure and marked both tickets `blocked`, but it did
  not inspect `src/billing/retrySchedule.js` or
  `src/billing/retrySchedule.test.js`, so it did not identify the concrete
  drift between the active spec and the implementation/tests.
- candidate-variant
  (`sha256-b7756d9f0f441338585b5e815ff1d1e7950ebe6e2a4248d581352e4989b0249a`)
  inspected the active spec, tickets, evidence, review, source, and tests. It
  detected that `RETRY_OFFSETS_DAYS` and the test assert `[1, 3, 7]` while the
  active spec requires `[1, 3, 7, 14]`; it also detected that the test expects a
  cancelled failed invoice to schedule a retry despite the active spec's
  cancellation suppression requirement. It left ticket statuses unchanged,
  created no pass evidence, edited no source/test files, and recorded a fail
  closure review.

## Procedure

The experiment was run with:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-spec-drift-closure-gate-scn009-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/081-spec-drift-closure-gate-scn009-live-micro --require-clean-canonical
```

The report, score artifacts, raw transcripts, command traces, prompts, and
archived workspaces are under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/081-spec-drift-closure-gate-scn009-live-micro/`.

## What This Supports Or Challenges

This supports promoting `candidate-spec-drift-closure-gate-v1`. Current
`SKILL.md` already avoids the worst closure failure, but candidate improves the
closure standard by requiring the active spec to be compared against evidence,
reviews, tests, and implementation before accepting pass labels.

## Limits

This is one live MICRO repetition against an intentionally obvious spec drift.
It does not prove behavior for subtler drifts, superseded specifications, or
closure work where source/test inspection is unavailable. Offline scores remain
Trust Level 1 and promotion depends on the manual inspection above.
