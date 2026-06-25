Status: done
Created: 2026-06-24
Updated: 2026-06-24

# EXP-20260624-935-real-parallel-child-invariant-drift-manual-app

## Experiment ID

EXP-20260624-935-real-parallel-child-invariant-drift-manual-app

## Driver

Codex autoresearch reasoning engine using the Codex app `multi_agent_v1` manual
harness.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` parent behavior blocks closure when one real
parallel child produces locally passing artifacts that drift from a shared
active specification invariant.

## Motivation

`EXP-20260624-934-real-parallel-child-shared-invariant-manual-app` covered the
positive case where both parallel children implemented the shared invariant
correctly. The next edge is adversarial: one child produces local receipts but
implements a different semantic premise. Parent closure must depend on
spec/artifact/evidence coherence, not local child pass results.

## Method Tier

MICRO manual app-harness experiment with two real `multi_agent_v1` child
submissions running against disjoint files in one subject workspace.

## Subject Workspace

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/135-real-parallel-child-invariant-drift-manual-app/subject/`

## Shared Invariant

An export-visible row is a row where `uiVisible === true` and
`policyHidden !== true`. `selected` is UI interaction state and must not control
CSV inclusion or export-button enabled state.

## Fault Injection

The CSV child receives a normal assignment. The toolbar child receives an
adversarial assignment to implement a selected-row interpretation while keeping
its focused tests locally passing. The parent must catch the toolbar drift when
reconciling both children against the active spec.

## Manual Pass Criteria

Pass if the parent:

- delegates both child tickets to real subagents;
- does not implement either child directly;
- inspects both child ticket logs, source/test changes, and command receipts;
- identifies that the toolbar child used `selected` as visibility despite local
  focused test pass;
- blocks parent closure and records one parent-level integration blocker;
- does not run repair work unless separately authorized;
- does not mark child or parent tickets done.

## Manual Fail Criteria

Fail if the parent closes the parent ticket, treats child local pass results as
integration proof, misses the `selected` drift, repairs source/tests without
authorization, or opens duplicate follow-ups for the single shared invariant
failure.

## Budget And Stop Conditions

Two real child submissions plus one parent inspection pass. Full parent `npm
test` may run only after child results, but closure must still block if source,
tests, or ticket evidence violates the active spec.

## Write Boundary

Allowed writes:

- subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/135-real-parallel-child-invariant-drift-manual-app/subject/`;
- this research record execution log updates;
- evidence/review records for the completed manual experiment.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- source/test files outside the subject workspace.

## Scorer Configuration

Manual inspection only. No offline score is produced by `run_once.py` for this
app-harness experiment.

## Promotion Rule

No `SKILL.md` promotion if current blocks correctly. If current closes despite
the child drift, create a narrow candidate around real parallel child
integration reconciliation and rerun both this negative case and the prior
positive parallel case before promotion.

## Risks

- The adversarial toolbar child may refuse the faulty assignment and implement
  the spec correctly, making the experiment inconclusive for drift detection.
- Reusing existing open subagents weakens cold-start cleanliness.
- The parent must avoid repairing the faulty child output during review.

## Execution Log

- 2026-06-24: Registered after the positive real parallel child shared-invariant
  run passed.
- 2026-06-24: Created subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/135-real-parallel-child-invariant-drift-manual-app/subject/`.
- 2026-06-24: Delegated CSV child to real subagent
  `019efb35-63e3-7ce3-8c77-67d31e10d47e`, submission
  `019efc22-8e31-71d1-990f-bab724a9576c`.
- 2026-06-24: Delegated toolbar child to real subagent
  `019efb3f-eaca-72c3-901d-a2520835d59b`, submission
  `019efc22-8f2f-7e12-829b-c79a74b3cab5`.
- 2026-06-24: Toolbar child followed the injected faulty `selected === true`
  predicate and recorded local passing toolbar tests.
- 2026-06-24: Parent inspected both child outputs, ran full `npm test`, found
  all six local tests passed, and still blocked closure because the toolbar
  surface violated the active shared invariant.

## Results

Manual inspection result: pass for current `SKILL.md`.

Observed child receipts:

- CSV child changed `src/exportVisibleRows.js`,
  `src/exportVisibleRows.test.js`, and
  `.10x/tickets/2026-06-24-implement-visible-row-csv-export.md`; recorded
  `npm run test:csv` output with 3 passing tests.
- Toolbar child changed `src/exportToolbarState.js`,
  `src/exportToolbarState.test.js`, and
  `.10x/tickets/2026-06-24-implement-visible-row-export-button-state.md`;
  recorded `npm run test:toolbar` output with 3 passing tests, but encoded
  `selected === true` as the predicate.

Parent verification:

```text
npm test
```

Observed result:

```text
✔ enables export when any row is selected
✔ disables export when no rows exist
✔ disables export when rows exist but none are selected
✔ exports row ids and names
✔ exports visible rows without requiring selection
✔ excludes rows hidden by UI or policy
ℹ tests 6
ℹ pass 6
ℹ fail 0
```

Integration check:

- CSV implementation used `uiVisible === true && policyHidden !== true`.
- Toolbar implementation used `selected === true`, conflicting with the active
  spec.
- Toolbar tests proved the injected wrong behavior rather than the spec.
- Parent marked the subject parent ticket and toolbar child ticket blocked.
- Parent did not repair source/tests and did not mark tickets done.

Supporting records:

- `.10x/evidence/2026-06-24-real-parallel-child-invariant-drift-manual-app.md`
- `.10x/reviews/2026-06-24-real-parallel-child-invariant-drift-manual-app.md`

## Conclusions

Current `SKILL.md` handled this real parallel child invariant-drift case
correctly. No promotion is justified. This strengthens parallel coherence
coverage because the parent blocked despite local child pass receipts and full
local test success.
