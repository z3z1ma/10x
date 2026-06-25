Status: active
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
