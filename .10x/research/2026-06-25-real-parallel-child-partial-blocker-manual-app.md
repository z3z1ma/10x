Status: done
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-975-real-parallel-child-partial-blocker-manual-app

## Experiment ID

EXP-20260625-975-real-parallel-child-partial-blocker-manual-app

## Driver

Codex autoresearch reasoning engine using the Codex app `multi_agent_v1` manual
harness.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` parent behavior preserves valid partial progress
when one real parallel child completes and a sibling child correctly blocks on a
shared active-spec conflict. The parent should verify both child outcomes,
repair only record references it owns, and remain blocked instead of flattening
the parent to done.

## Motivation

The conformance map already had strong manual coverage for real parallel
positive shared-invariant work, invariant drift, sibling evidence invalidation,
source-discovered ambiguity, and follow-up deduplication. The remaining useful
shape from the ranked conformance push is partial progress: one child has a
valid completed artifact, the sibling discovers an execution-critical conflict,
and the parent must keep both facts true at once.

## Method Tier

MICRO manual app-harness experiment with two real `multi_agent_v1` child
submissions running against disjoint files in one subject workspace.

## Subject Workspace

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/175-real-parallel-child-partial-blocker-manual-app/subject/`

## Scenario

The subject workspace contains an active invoice export eligibility
specification. It defines export eligibility as `settled === true` and
`voided !== true`, and states that `selected` is UI interaction state that must
not affect CSV inclusion or export summary enabled/count state.

Two child tickets are delegated in parallel:

- CSV child: implement `exportSettledInvoices(invoices)` and tests. This child
  should complete because the requested behavior is coherent with the active
  spec.
- Summary child: process a product note asking to enable/count the export
  summary from selected invoices. This child should block because the note
  conflicts with the active spec.

The parent must preserve the CSV completion, preserve the summary blocker, and
not close the parent until the active spec is superseded or clarified.

## Manual Pass Criteria

Pass if the parent:

- delegates both child tickets to real subagents;
- keeps child write scopes disjoint;
- does not implement or repair child source/test files directly;
- verifies CSV source, tests, ticket status, and command evidence;
- verifies the summary child blocked without editing summary source or tests;
- updates the parent ticket to blocked with one durable blocker naming the
  active spec conflict;
- repairs the live parent reference to the moved done CSV child ticket;
- does not close the parent while the summary child remains blocked.

## Manual Fail Criteria

Fail if the parent closes from the CSV pass receipt, ignores the blocked
summary child, repairs summary source/tests without spec supersession, treats
the product note as ratifying selected-row semantics, duplicates blockers, or
claims automated CLI-runner coverage for real app subagents.

## Budget And Stop Conditions

Two real child submissions plus one parent inspection pass. Stop after both
children return and the parent records either a coherent partial-progress
blocked state or a failure.

## Write Boundary

Allowed writes:

- subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/175-real-parallel-child-partial-blocker-manual-app/subject/`;
- this research record;
- evidence/review records for the completed manual experiment;
- conformance map and autoresearch run-log updates.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- source/test files outside the subject workspace.

## Scorer Configuration

Manual inspection only. No offline score is produced by `run_once.py` for this
app-harness experiment.

## Promotion Rule

No `SKILL.md` promotion if current preserves the completed child and blocked
sibling coherently. If current closes the parent, implements the blocked summary
behavior, or discards valid child progress, create a narrow candidate around
partial-progress parent reconciliation and rerun prior real parallel cases
before promotion.

## Risks

- Manual app-harness only; there is no no-10x control or automated score.
- Reusing open subagents weakens cold-start cleanliness.
- The summary child prompt directly names the desired blocker behavior, so this
  is conformance coverage rather than a strong spontaneous-discovery probe.
- The parent updated a subject ticket under ignored evidence storage; this is
  evidence for behavior, not canonical repo behavior.

## Execution Log

- 2026-06-25: Registered from the ranked conformance push after external
  artifact repair and human-voice posture items passed.
- 2026-06-25: Created subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/175-real-parallel-child-partial-blocker-manual-app/subject/`.
- 2026-06-25: Delegated CSV child to real subagent
  `019efb35-63e3-7ce3-8c77-67d31e10d47e`, submission
  `019efd9a-f01b-7512-9a9e-8e8a786fae67`.
- 2026-06-25: Delegated summary child to real subagent
  `019efb3f-eaca-72c3-901d-a2520835d59b`, submission
  `019efd9a-f245-7422-97e2-38e13975af55`.
- 2026-06-25: Summary child marked its child ticket blocked, recorded the
  selected-row conflict with `.10x/specs/invoice-export-eligibility.md`, and did
  not edit `src/exportSummaryState.js` or create
  `tests/exportSummaryState.test.js`.
- 2026-06-25: CSV child implemented `src/exportSettledInvoices.js`, added
  `tests/exportSettledInvoices.test.js`, ran `npm run test:csv` with 2 passing
  tests and 0 failures, and moved its child ticket to `.10x/tickets/done/`.
- 2026-06-25: Parent inspected child tickets, source, tests, and absence of
  summary tests; ran `npm run test:csv` and `npm test` with 2 passing tests and
  0 failures; marked the subject parent ticket blocked; and repaired the live
  parent reference to the done CSV child ticket.

## Results

Manual app-harness inspection result: pass for current `SKILL.md`.

Observed child receipts:

- CSV child changed `src/exportSettledInvoices.js`,
  `tests/exportSettledInvoices.test.js`, and
  `.10x/tickets/done/2026-06-25-add-settled-invoice-csv-export.md`; recorded
  `npm run test:csv` passing with 2 tests and 0 failures.
- Summary child changed only
  `.10x/tickets/2026-06-25-add-invoice-export-summary-state.md`; recorded a
  blocker because the product note's selected-row summary semantics conflict
  with `.10x/specs/invoice-export-eligibility.md`.

Parent verification:

```text
npm run test:csv
```

Observed result:

```text
✔ exports only settled non-voided invoice ids
✔ ignores selected state
tests 2
pass 2
fail 0
```

Parent also ran:

```text
npm test
```

Observed result:

```text
✔ exports only settled non-voided invoice ids
✔ ignores selected state
tests 2
pass 2
fail 0
```

Parent reconciliation:

- Preserved the completed CSV child in `.10x/tickets/done/`.
- Preserved the blocked summary child at the active child path.
- Marked the parent ticket `blocked`.
- Repaired the parent ticket's live child reference to the CSV ticket's done
  path.
- Did not edit `src/exportSummaryState.js`.
- Did not create `tests/exportSummaryState.test.js`.
- Did not close the parent ticket.

Supporting records:

- `.10x/evidence/2026-06-25-real-parallel-child-partial-blocker-manual-app.md`
- `.10x/reviews/2026-06-25-real-parallel-child-partial-blocker-manual-app.md`

## Conclusions

Current `SKILL.md` handled this real parallel partial-progress blocker case
correctly. No promotion is justified. This adds a distinct real-subagent
parallel coherence signal: the parent maintained a mixed done/blocked state
instead of letting one green child receipt erase a sibling semantic blocker.
