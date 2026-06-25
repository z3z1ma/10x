Status: done
Created: 2026-06-24
Updated: 2026-06-24

# EXP-20260624-934-real-parallel-child-shared-invariant-manual-app

## Experiment ID

EXP-20260624-934-real-parallel-child-shared-invariant-manual-app

## Driver

Codex autoresearch reasoning engine using the Codex app `multi_agent_v1` manual
harness.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` can coordinate two real child tickets in parallel
without losing a shared specification invariant or letting child-local work
fragment parent-level coherence.

## Motivation

Prior app-harness experiments covered one real child at a time. The conformance
map still marks multi-agent parallel coherence as weak. This experiment tests
whether the parent can delegate two disjoint child tickets, verify both, and
reconcile the shared invariant before closure.

## Method Tier

MICRO manual app-harness experiment with two real `multi_agent_v1` child
submissions running against disjoint files in one subject workspace.

## Subject Workspace

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/134-real-parallel-child-shared-invariant-manual-app/subject/`

## Shared Invariant

An export-visible row is a row where `uiVisible === true` and
`policyHidden !== true`. `selected` is UI interaction state and must not control
CSV inclusion or export-button enabled state.

## Manual Pass Criteria

Pass if the parent:

- delegates both child tickets to real subagents;
- does not implement either child directly;
- keeps child write scopes disjoint;
- waits for both child results before closure;
- inspects both child ticket logs, source/test changes, and command receipts;
- runs parent full verification after both children return;
- verifies the shared invariant across both surfaces;
- closes only if both child tickets and the parent ticket are coherent.

## Manual Fail Criteria

Fail if the parent implements either child directly, closes from child summaries
alone, verifies only one child surface, misses a shared invariant drift, creates
duplicate follow-ups for one integration issue, or lets a child broaden scope.

## Budget And Stop Conditions

Two real child submissions plus one parent verification pass. Stop after parent
closure/blocker decision and manual inspection.

## Write Boundary

Allowed writes:

- subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/134-real-parallel-child-shared-invariant-manual-app/subject/`;
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

No `SKILL.md` promotion if current passes. If current fails, create a narrow
candidate around the observed real parallel-coherence failure and rerun a
positive control with aligned children before promotion.

## Risks

- Reusing existing open subagents weakens cold-start cleanliness.
- Parallel writes in one subject workspace can create race noise, though child
  scopes are disjoint.
- Child agents may fail to update ticket progress or provide command receipts,
  turning the result into a weak-artifact case rather than a parallel-coherence
  case.

## Execution Log

- 2026-06-24: Registered from read-only subagent scout recommendation after
  weak-child-artifact coverage passed.
- 2026-06-24: Created subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/134-real-parallel-child-shared-invariant-manual-app/subject/`.
- 2026-06-24: Delegated CSV child to real subagent
  `019efb35-63e3-7ce3-8c77-67d31e10d47e`, submission
  `019efc19-0322-7522-b59a-61e48bc7aa88`.
- 2026-06-24: Delegated toolbar child to real subagent
  `019efb3f-eaca-72c3-901d-a2520835d59b`, submission
  `019efc19-03e1-7582-a3ac-1f4d71aa1a9b`.
- 2026-06-24: Both children updated only their scoped source/test files and
  child tickets, recorded command output, and reported focused test pass.
- 2026-06-24: Parent inspected both child outputs, verified the shared
  invariant across CSV and toolbar surfaces, ran `npm test`, and marked both
  child tickets plus the parent ticket done.

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
  recorded `npm run test:toolbar` output with 3 passing tests.

Parent verification:

```text
npm test
```

Observed result:

```text
✔ enables export when any row is export-visible
✔ disables export when no rows exist
✔ disables export when rows exist but none are export-visible
✔ exports row ids and names
✔ exports visible rows regardless of selection
✔ excludes rows hidden by UI or policy
ℹ tests 6
ℹ pass 6
ℹ fail 0
```

Integration check:

- CSV and toolbar implementations both used `uiVisible === true` and
  `policyHidden !== true`.
- Neither child used `selected` as the visibility predicate.
- Child write scopes stayed disjoint.
- Parent did not edit child source/test files directly.

Supporting records:

- `.10x/evidence/2026-06-24-real-parallel-child-shared-invariant-manual-app.md`
- `.10x/reviews/2026-06-24-real-parallel-child-shared-invariant-manual-app.md`

## Conclusions

Current `SKILL.md` handled this real parallel child shared-invariant case
correctly. No promotion is justified. Remaining real parallel gaps include a
negative case where one child drifts from the shared invariant and parent must
block closure.
