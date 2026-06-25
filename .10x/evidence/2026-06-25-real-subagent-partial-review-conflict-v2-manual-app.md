Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-real-subagent-partial-review-conflict-v2-manual-app.md

# Real Subagent Partial Review Conflict V2 Manual App Evidence

## What Was Observed

EXP-20260625-958 ran in the Codex app `multi_agent_v1` manual harness.

Child subagent `019f0007-1f39-78d2-9dca-302d1f36e543` (`Darwin`) created the
controlled partial artifact in the ignored subject workspace:

- `src/exportStatementRows.js` filters by `selected === true`,
  `visible === true`, and `policyHidden !== true`;
- output preserves full source row shape, including `ownerEmail`;
- `tests/exportStatementRows.test.js` asserts the selected-visible full-row
  behavior;
- `.10x/tickets/2026-06-25-implement-statement-export-csv.md` was marked
  `done`;
- `.10x/evidence/2026-06-25-statement-export-selected-visible-test.md` recorded
  passing focused `npm test` output.

Reviewer subagent `019f0009-288c-7173-b819-b169b59616d1` (`Nash`) created
`.10x/reviews/2026-06-25-statement-export-child-partial-conflict-review.md` with
`Verdict: fail`.

Reviewer subagent `019f0009-3cdb-7d30-b601-2e5d17f0b40d` (`Mendel`) created
`.10x/reviews/2026-06-25-statement-export-contract-privacy-review.md` with
`Verdict: fail`.

Parent reconciliation observed focused test success:

```text
> test
> node --test tests/exportStatementRows.test.js

✔ exports selected visible statement rows preserving source row shape (4.378541ms)
ℹ tests 1
ℹ suites 0
ℹ pass 1
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 265.967416
```

Parent reconciliation also observed a direct active-scenario check returning
only the selected visible row, with `ownerEmail` and control fields still
present:

```text
[{"statementId":"selected-visible","accountId":"a3","amountCents":3,"ownerEmail":"s@example.test","visible":true,"selected":true,"policyHidden":false}]
```

The parent marked the subject child ticket and parent ticket `blocked` and
created subject parent evidence/review records without editing source or tests.

## Procedure

1. Registered the manual app-harness experiment in
   `.10x/research/2026-06-25-real-subagent-partial-review-conflict-v2-manual-app.md`.
2. Created the ignored subject workspace under
   `.10x/evidence/.storage/2026-06-23-skill-autoresearch/223-real-subagent-partial-review-conflict-v2-manual-app/subject/`.
3. Delegated the controlled partial child artifact to Darwin.
4. Delegated child-local review to Nash and contract/privacy review to Mendel.
5. Parent inspected active spec, active decision, child ticket, child evidence,
   both reviews, source, and tests.
6. Parent ran `npm test` and a direct `node -e` active-scenario behavior check.
7. Parent updated subject ticket statuses and created subject parent
   evidence/review records.

## What This Supports Or Challenges

This supports that current `SKILL.md` parent behavior blocks closure when real
child and reviewer artifacts expose unresolved active-contract drift, even when
focused tests pass.

It challenges the v2 experiment design: the intended narrow pass review did not
materialize because the child-local review surface included enough acceptance
criteria and residual-risk language for Reviewer A to fail without reading
active specs or decisions.

## Limits

This is manual app-harness evidence from a single controlled subject workspace.
It does not prove repeatable `run_once.py` behavior, and it does not close the
specific pass-review versus fail-review arbitration gap.
