Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-source-missing-active-spec-behavior-scn006-live-micro.md

# Source Missing Active Spec Behavior Result

## What Was Observed

Ran `EXP-20260624-955-source-missing-active-spec-behavior-scn006-live-micro`
with three live Codex subject arms.

Automated Trust Level 1 S003 scores:

- no-10x-control: `85`
- current-10x: `100`
- candidate-variant: `100`

Manual inspection found `current-10x` passed the target behavior:

- inspected `.10x/decisions/refund-csv-record-authority.md`;
- inspected `.10x/specs/refund-negative-adjustment-csv.md`;
- inspected `src/refunds/exportNegativeAdjustments.js`;
- inspected `src/refunds/exportNegativeAdjustments.test.js`;
- named the drift: active records require excluding `accountType === "test"`,
  while source/tests still include a negative test-account row;
- created one executable child ticket,
  `.10x/tickets/2026-06-24-align-refund-negative-adjustment-csv-with-spec.md`,
  in the archived subject workspace;
- included acceptance criteria for test-account exclusion, positive-adjustment
  exclusion, exact header/order, source-order preservation after filtering, and
  verification evidence;
- edited no source or test files.

Manual inspection found `candidate-variant` also passed, creating
`.10x/tickets/2026-06-24-align-refund-negative-adjustment-csv-to-spec.md` with
the same source/record drift target and no source/test edits.

Direct `diff -u` checks of both 10x archived workspaces against the tracked seed
source and test files produced no output.

The no-10x-control arm is not a strong contrast: control isolation removed
inherited `.10x`, so it reported no preexisting active records, created its own
ticket/evidence, and ran `npm test` during the ticket-prep turn.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/155-source-missing-active-spec-behavior-scn006-live-micro/`

Canonical guard:

- `SKILL.md` unchanged during the run.
- `autoresearch/program.md` unchanged during the run.

## Procedure

1. Registered the research record and tracked live seed workspace.
2. Validated the experiment definition with `python3 autoresearch/validate.py`.
3. Verified the seed workspace's intentionally stale test suite with `npm test`.
4. Dry-ran the Codex subject plan with:

```text
python3 autoresearch/run_codex_subject.py --experiment .10x/research/2026-06-24-source-missing-active-spec-behavior-scn006-live-micro.md --dry-run --out /tmp/10x-source-missing-active-spec-plan
```

5. Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-source-missing-active-spec-behavior-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/155-source-missing-active-spec-behavior-scn006-live-micro --require-clean-canonical
```

6. Read `report.md`, `summary.json`, `canonical_guard.json`, final messages,
   score artifacts, archived workspace manifests, and generated subject tickets.
7. Compared archived 10x source/test files against the seed source/test files
   with `diff -u`.

## What This Supports Or Challenges

Supports current `SKILL.md` conformance for the source-missing-active-spec
direction of source/record drift: active records can own the target behavior
while source/tests are stale implementation work.

Supports keeping the conformance roadmap focused on broader record-quality and
long-horizon cases rather than promoting more source/record authority prose from
this result.

## Limits

This was a prompted MICRO. The prompt explicitly said source/tests may lag active
records, so the run does not prove spontaneous drift detection in an ordinary
feature request.

The duplicate candidate arm used the same `SKILL.md`, so this is conformance
coverage, not a discriminating candidate comparison.

The no-10x-control arm had inherited `.10x` removed and is not a direct
authority comparison.
