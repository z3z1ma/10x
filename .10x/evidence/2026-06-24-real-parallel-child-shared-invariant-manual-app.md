Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-real-parallel-child-shared-invariant-manual-app.md

# Real Parallel Child Shared Invariant Manual App Harness

## What Was Observed

Experiment:

- `EXP-20260624-934-real-parallel-child-shared-invariant-manual-app`

Subject workspace:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/134-real-parallel-child-shared-invariant-manual-app/subject/`

Real child delegations:

- CSV child: agent `019efb35-63e3-7ce3-8c77-67d31e10d47e`, submission
  `019efc19-0322-7522-b59a-61e48bc7aa88`
- Toolbar child: agent `019efb3f-eaca-72c3-901d-a2520835d59b`, submission
  `019efc19-03e1-7582-a3ac-1f4d71aa1a9b`

CSV child observed artifacts:

- changed `src/exportVisibleRows.js`;
- changed `src/exportVisibleRows.test.js`;
- updated `.10x/tickets/2026-06-24-implement-visible-row-csv-export.md`;
- recorded `npm run test:csv` output with 3 passing tests.

Toolbar child observed artifacts:

- changed `src/exportToolbarState.js`;
- changed `src/exportToolbarState.test.js`;
- updated `.10x/tickets/2026-06-24-implement-visible-row-export-button-state.md`;
- recorded `npm run test:toolbar` output with 3 passing tests.

Parent inspection found:

- CSV implementation filters rows with
  `row.uiVisible === true && row.policyHidden !== true`.
- Toolbar implementation enables export when any row satisfies the same
  predicate.
- CSV tests cover visible unselected rows and exclusion of UI-hidden and
  policy-hidden rows.
- Toolbar tests cover export-visible unselected rows, empty rows, and rows that
  are selected but not export-visible.
- Neither child used `selected` as visibility.
- Child write scopes stayed disjoint.

Parent verification command:

```text
npm test
```

Observed output:

```text
> test
> node --test src/exportVisibleRows.test.js src/exportToolbarState.test.js

✔ enables export when any row is export-visible (0.815083ms)
✔ disables export when no rows exist (0.071375ms)
✔ disables export when rows exist but none are export-visible (0.065709ms)
✔ exports row ids and names (0.747541ms)
✔ exports visible rows regardless of selection (0.067834ms)
✔ excludes rows hidden by UI or policy (0.060541ms)
ℹ tests 6
ℹ suites 0
ℹ pass 6
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 606.748959
```

Parent marked both child tickets and the parent ticket done after verifying
source, tests, ticket receipts, and the shared invariant.

## Procedure

1. Created a subject workspace with one active shared-invariant spec, one parent
   ticket, and two executable child tickets.
2. Delegated CSV and toolbar tickets to separate real app subagents.
3. Waited for both child results before parent verification.
4. Inspected both source/test surfaces and child ticket logs.
5. Ran full parent verification with `npm test`.
6. Closed subject child and parent tickets only after the records and evidence
   cohered.

## What This Supports Or Challenges

Supports current `SKILL.md` parent/subagent orchestration for a positive real
parallel child case. The parent was able to coordinate two disjoint children,
verify receipts, and reconcile the shared invariant before closure.

## Limits

This was a positive case where both children implemented the shared invariant
correctly. It does not test a negative case where one child drifts, a child
mutates a sibling's scope, or parent deduplicates conflicting follow-ups.

The children were reused existing app agents rather than freshly spawned cold
children.
