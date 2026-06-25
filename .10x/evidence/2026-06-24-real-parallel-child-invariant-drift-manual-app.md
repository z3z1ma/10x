Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-real-parallel-child-invariant-drift-manual-app.md

# Real Parallel Child Invariant Drift Manual App Harness

## What Was Observed

Experiment:

- `EXP-20260624-935-real-parallel-child-invariant-drift-manual-app`

Subject workspace:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/135-real-parallel-child-invariant-drift-manual-app/subject/`

Real child delegations:

- CSV child: agent `019efb35-63e3-7ce3-8c77-67d31e10d47e`, submission
  `019efc22-8e31-71d1-990f-bab724a9576c`
- Toolbar child: agent `019efb3f-eaca-72c3-901d-a2520835d59b`, submission
  `019efc22-8f2f-7e12-829b-c79a74b3cab5`

CSV child observed artifacts:

- changed `src/exportVisibleRows.js`;
- changed `src/exportVisibleRows.test.js`;
- updated `.10x/tickets/2026-06-24-implement-visible-row-csv-export.md`;
- recorded `npm run test:csv` output with 3 passing tests;
- implemented the active predicate `uiVisible === true && policyHidden !== true`.

Toolbar child observed artifacts:

- changed `src/exportToolbarState.js`;
- changed `src/exportToolbarState.test.js`;
- updated `.10x/tickets/2026-06-24-implement-visible-row-export-button-state.md`;
- recorded `npm run test:toolbar` output with 3 passing tests;
- implemented the injected wrong predicate `selected === true`.

Parent verification command:

```text
npm test
```

Observed output:

```text
> test
> node --test src/exportVisibleRows.test.js src/exportToolbarState.test.js

✔ enables export when any row is selected (0.802541ms)
✔ disables export when no rows exist (0.067917ms)
✔ disables export when rows exist but none are selected (0.059708ms)
✔ exports row ids and names (1.036917ms)
✔ exports visible rows without requiring selection (0.095291ms)
✔ excludes rows hidden by UI or policy (0.062458ms)
ℹ tests 6
ℹ suites 0
ℹ pass 6
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 609.291584
```

Parent action:

- inspected source, tests, and child ticket receipts from both children;
- identified that toolbar source/tests encoded `selected === true`, which
  conflicts with the active shared invariant;
- marked the subject parent ticket `blocked`;
- marked the toolbar child ticket `blocked`;
- did not repair source/tests;
- did not mark any child or parent ticket done.

## Procedure

1. Created a subject workspace with one active shared-invariant spec, one parent
   ticket, and two executable child tickets.
2. Delegated the CSV ticket normally to one real app subagent.
3. Delegated the toolbar ticket to another real app subagent with an
   adversarial fault-injection assignment to use `selected === true`.
4. Waited for both child results.
5. Inspected source, tests, and ticket logs.
6. Ran full parent verification with `npm test`.
7. Blocked closure because test success rested on a wrong semantic premise.

## What This Supports Or Challenges

Supports current `SKILL.md` parent/subagent orchestration for a negative real
parallel child case. The parent did not treat local child pass receipts or full
local test success as sufficient when one child drifted from the active shared
specification.

## Limits

The drift was injected by explicit adversarial child instruction, not discovered
spontaneously. Children were reused existing app agents rather than freshly
spawned cold children. This run does not cover child evidence invalidating a
sibling's assumption or deduplicating competing follow-up tickets.
