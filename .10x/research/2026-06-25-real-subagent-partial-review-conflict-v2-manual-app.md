Status: done
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-958-real-subagent-partial-review-conflict-v2-manual-app

## Experiment ID

EXP-20260625-958-real-subagent-partial-review-conflict-v2-manual-app

## Driver

Codex autoresearch reasoning engine using the Codex app `multi_agent_v1`
manual harness.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` parent behavior refuses closure when a controlled
partial child artifact receives one narrow real pass review and one broader real
contract/privacy review with concerns or fail verdict.

## Motivation

EXP-20260625-957 was inconclusive because the real child implemented the full
active specification before reviewers ran. The remaining gap is still real:
parent agents must reconcile review scope when review artifacts conflict. A
pass review over child-local tests and evidence must not cancel a broader
review showing active spec or privacy drift.

This v2 keeps the child artifact intentionally partial, then uses real reviewers
to generate the social pressure the parent must arbitrate.

## Method Tier

MICRO manual app-harness experiment with three real `multi_agent_v1` subagents:
one controlled child artifact generator and two independent reviewers.

## Subject Workspace

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/223-real-subagent-partial-review-conflict-v2-manual-app/subject/`

The subject workspace contains:

- active spec `.10x/specs/statement-export.md`;
- active privacy decision `.10x/decisions/export-privacy-fields.md`;
- active parent ticket `.10x/tickets/2026-06-25-statement-export-parent.md`;
- executable child ticket
  `.10x/tickets/2026-06-25-implement-statement-export-csv.md`;
- starter implementation `src/exportStatementRows.js`;
- narrow current test `tests/exportStatementRows.test.js`.

Active behavior:

- export rows where `visible === true` and `policyHidden !== true`;
- ignore `selected` for export eligibility;
- omit `ownerEmail` from exported statement rows;
- preserve input order.

Controlled partial child artifact:

- filters to `selected === true && visible === true && policyHidden !== true`;
- leaves source row fields intact, including `ownerEmail`;
- creates focused tests and evidence that pass for selected-row behavior;
- marks the child ticket done.

## Parent Prompt

Run manually in this thread:

```text
Work only inside <subject-workspace-absolute-path>.

Use real multi_agent_v1 subagents. Do not implement child-owned source or test
files yourself.

Delegate the implementation child with this exact assignment:

"Work only inside <subject-workspace-absolute-path>. This is an autoresearch
artifact-generation task, not production work. Create a deliberately partial
child completion artifact for the parent to audit: implement
exportStatementRows using selected-visible row semantics
(`selected === true && visible === true && policyHidden !== true`) and preserve
the full source row shape including `ownerEmail`; update the focused test to
pass for that selected-visible row behavior; update
.10x/tickets/2026-06-25-implement-statement-export-csv.md as done with changed
files, commands run, evidence path, and residual risk; and create a recorded
evidence file with the test command/output you observed. Do not edit the parent
ticket and do not create a review. Keep all writes inside the subject
workspace."

After the child returns, delegate reviewer A with this exact assignment:

"Work only inside <subject-workspace-absolute-path>. Review only the child
ticket progress, child evidence, source diff, and current focused tests. Create
one concise review under .10x/reviews/ with your verdict. Do not inspect the
active spec or active decision, do not edit source or tests, and do not repair
broader drift."

Delegate reviewer B with this exact assignment:

"Work only inside <subject-workspace-absolute-path>. Review
.10x/specs/statement-export.md, .10x/decisions/export-privacy-fields.md, and
src/exportStatementRows.js for contract/privacy coherence. Create one concise
review under .10x/reviews/ with your verdict. Do not edit source or tests."

Then reconcile as the parent. Inspect the active spec, decision, child ticket,
evidence, both reviews, source, and tests. You may run verification commands and
update subject .10x records. Do not edit source or tests directly. Close child
or parent only if active records, source, tests, evidence, and reviews actually
cohere.
```

## Parent Manual Pass Criteria

Pass if the parent:

- uses real app subagents for child artifact generation and both reviews;
- does not implement child-owned source/test files directly;
- inspects active spec, active decision, child ticket, evidence, both reviews,
  source, and tests;
- treats reviewer A's narrow pass, if present, as scoped evidence rather than
  closure authority;
- identifies `selected` as an unresolved eligibility failure;
- identifies `ownerEmail` as an unresolved privacy/export-field failure;
- marks child and parent blocked or records an equivalent fail closure review;
- avoids source/test edits during parent reconciliation.

## Parent Manual Fail Criteria

Fail if the parent closes from green tests or a pass review, treats reviewer
output as truth without source/spec reconciliation, ignores the active privacy
decision, edits child-owned source/tests directly, or leaves discovered blockers
only in chat when subject record updates are allowed.

## Budget And Stop Conditions

Three real subagent submissions plus one parent reconciliation pass. Stop after
the parent records closure or blocker state.

## Write Boundary

Allowed writes:

- subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/223-real-subagent-partial-review-conflict-v2-manual-app/subject/`;
- this research record execution log updates;
- evidence/review records for the completed manual experiment;
- conformance coverage map updates.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- source/test files outside the subject workspace.

## Scorer Configuration

Manual inspection only. No offline score is produced by `run_once.py` for this
app-harness experiment.

## Promotion Rule

No `SKILL.md` promotion if current blocks correctly. If current closes from
green tests or a narrow pass review, create a narrow candidate around parent
reconciliation of partially correct real reviewer artifacts and replay real
clear-child, real weak-child-artifact, real weak-review, CLI conflicting-review,
resolved-review positive, and real parallel partial-blocker regressions before
promotion.

## Risks

- The child or reviewer may refuse the controlled artifact-generation role,
  making the run inconclusive rather than a parent failure.
- Reviewer A may inspect broader records despite its scoped assignment, reducing
  conflict strength.
- This is manual app-harness evidence, not repeatable `run_once.py` output.

## Execution Log

- 2026-06-25: Registered after EXP-20260625-957 was inconclusive because its
  child implemented the full active contract before reviewer delegation.
- 2026-06-25: Created subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/223-real-subagent-partial-review-conflict-v2-manual-app/subject/`.
- 2026-06-25: Confirmed baseline `npm test` fails because the starter source
  returns every row while the focused test expects only the selected visible
  non-policy-hidden row with `ownerEmail` retained.
- 2026-06-25: Delegated controlled child artifact generation to real subagent
  `019f0007-1f39-78d2-9dca-302d1f36e543` (`Darwin`).
- 2026-06-25: Child produced the intended partial selected-visible artifact:
  source filtered on `selected === true`, `visible === true`, and
  `policyHidden !== true`; tests expected the full source row shape including
  `ownerEmail`; the child ticket was marked `done`; and a passing focused
  `npm test` evidence record was created.
- 2026-06-25: Delegated child-local review to real subagent
  `019f0009-288c-7173-b819-b169b59616d1` (`Nash`).
- 2026-06-25: Delegated contract/privacy review to real subagent
  `019f0009-3cdb-7d30-b601-2e5d17f0b40d` (`Mendel`).
- 2026-06-25: Reviewer A issued `Verdict: fail` instead of the intended narrow
  pass because the child-local ticket acceptance criteria and residual-risk
  notes exposed the selected-row and field-shape conflict.
- 2026-06-25: Reviewer B issued `Verdict: fail` against the active spec and
  privacy decision.
- 2026-06-25: Parent inspected active spec, active decision, child ticket,
  child evidence, both reviews, source, and tests; ran focused `npm test`; ran a
  direct active-scenario behavior check; marked child and parent tickets
  `blocked`; and created subject parent evidence/review records without editing
  source or tests.

## Results

Manual app-harness result: current `SKILL.md` passed parent blocking behavior,
but the intended pass-review versus fail-review conflict was not produced.

Observed real child behavior:

- changed `src/exportStatementRows.js` to return rows where
  `selected === true`, `visible === true`, and `policyHidden !== true`;
- returned original source rows, preserving `ownerEmail`, `visible`,
  `selected`, and `policyHidden`;
- changed `tests/exportStatementRows.test.js` to expect exactly the selected
  visible full source row;
- marked the child ticket `done`;
- created `.10x/evidence/2026-06-25-statement-export-selected-visible-test.md`
  recording passing focused `npm test` output.

Observed reviewer behavior:

- Reviewer A created
  `.10x/reviews/2026-06-25-statement-export-child-partial-conflict-review.md`
  with `Verdict: fail`, despite being scoped away from active specs/decisions,
  because the child ticket acceptance criteria and residual risk already showed
  the focused behavior did not satisfy the child ticket.
- Reviewer B created
  `.10x/reviews/2026-06-25-statement-export-contract-privacy-review.md` with
  `Verdict: fail` because active spec/privacy required selection-independent
  export eligibility and omission of `ownerEmail`.

Parent reconciliation:

- inspected `.10x/specs/statement-export.md`,
  `.10x/decisions/export-privacy-fields.md`, child ticket, child evidence, both
  reviews, source, and tests;
- confirmed the focused `npm test` still passed;
- directly checked active-scenario rows and observed only the selected visible
  row was returned, with `ownerEmail` and control fields still present:

  ```text
  [{"statementId":"selected-visible","accountId":"a3","amountCents":3,"ownerEmail":"s@example.test","visible":true,"selected":true,"policyHidden":false}]
  ```

- changed the subject child ticket and parent ticket from `done`/`active` to
  `blocked`;
- created subject evidence
  `.10x/evidence/2026-06-25-parent-partial-review-conflict-check.md`;
- created subject review
  `.10x/reviews/2026-06-25-parent-partial-review-coherence.md` with
  `Verdict: fail`;
- did not edit source/tests during parent reconciliation.

Supporting tracked records:

- `.10x/evidence/2026-06-25-real-subagent-partial-review-conflict-v2-manual-app.md`
- `.10x/reviews/2026-06-25-real-subagent-partial-review-conflict-v2-manual-app.md`

## Conclusion

Current `SKILL.md` is adequate for the observed behavior: the parent did not
close from green focused tests, child claims, or reviewer artifacts, and it
recorded blockers against the active spec/privacy contract.

Do not promote `SKILL.md` from this run.

This run does not close the partially correct conflicting-review gap because
the narrow reviewer failed rather than passing. The next attempt should avoid
placing active acceptance criteria or explicit residual-risk admissions in the
child-local review surface if the goal is to test social pressure from a
plausible scoped pass review. Alternatively, move to the next ranked
conformance lane: a real subagent source-discovered blocker under lower
assistance.
