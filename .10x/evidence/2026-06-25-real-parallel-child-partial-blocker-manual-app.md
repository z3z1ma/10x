Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-real-parallel-child-partial-blocker-manual-app.md

# Real Parallel Child Partial-Progress Blocker Manual App Evidence

## What Was Observed

Ran `EXP-20260625-975-real-parallel-child-partial-blocker-manual-app` as a
manual Codex app-harness experiment with two real child subagents.

Subject workspace:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/175-real-parallel-child-partial-blocker-manual-app/subject/`

Delegation:

- CSV child: subagent `019efb35-63e3-7ce3-8c77-67d31e10d47e`, submission
  `019efd9a-f01b-7512-9a9e-8e8a786fae67`.
- Summary child: subagent `019efb3f-eaca-72c3-901d-a2520835d59b`, submission
  `019efd9a-f245-7422-97e2-38e13975af55`.

Observed child outcomes:

- CSV child implemented `src/exportSettledInvoices.js`, added
  `tests/exportSettledInvoices.test.js`, recorded `npm run test:csv` passing,
  and moved its ticket to
  `.10x/tickets/done/2026-06-25-add-settled-invoice-csv-export.md`.
- Summary child marked
  `.10x/tickets/2026-06-25-add-invoice-export-summary-state.md` blocked because
  the product note asked to enable/count by selected invoices while the active
  spec says `selected` must not affect summary enabled state or count.
- Summary child did not edit `src/exportSummaryState.js` and did not create
  `tests/exportSummaryState.test.js`.

Parent outcome:

- Parent inspected child tickets, source, tests, and absence of summary tests.
- Parent ran focused and full subject tests.
- Parent updated
  `.10x/tickets/2026-06-25-invoice-export-parent.md` to `Status: blocked`.
- Parent repaired the live parent reference to the moved CSV done ticket.
- Parent preserved the blocked summary child and did not close the parent.

Focused verification command:

```bash
npm run test:csv
```

Observed output:

```text
> test:csv
> node --test tests/exportSettledInvoices.test.js

✔ exports only settled non-voided invoice ids (1.829417ms)
✔ ignores selected state (0.091667ms)
ℹ tests 2
ℹ suites 0
ℹ pass 2
ℹ fail 0
```

Full subject verification command:

```bash
npm test
```

Observed output:

```text
> test
> node --test tests/*.test.js

✔ exports only settled non-voided invoice ids (1.566083ms)
✔ ignores selected state (0.097916ms)
ℹ tests 2
ℹ suites 0
ℹ pass 2
ℹ fail 0
```

## Procedure

1. Created the manual subject workspace under ignored evidence storage.
2. Sent parallel child assignments to two real `multi_agent_v1` subagents with
   disjoint write scopes.
3. Waited for both child final messages.
4. Inspected the summary child ticket and confirmed it blocked on the active
   spec conflict without source/test edits.
5. Inspected the CSV child done ticket, implementation, and tests.
6. Ran `npm run test:csv` and `npm test` from the subject workspace.
7. Updated the subject parent ticket to blocked and repaired its live reference
   to the moved CSV done ticket.

## What This Supports Or Challenges

Supports that current `SKILL.md` can preserve a mixed parent state after real
parallel child execution: one child done with evidence, one sibling blocked on
unresolved semantics, and the parent blocked rather than closed.

Supports adding partial-progress blocker coverage to the multi-agent parallel
coherence lane.

## Limits

This is manual app-harness evidence, not a repeatable `run_once.py` Codex CLI
experiment.

There is no no-10x control arm.

The summary child prompt explicitly named the spec conflict, so this is
positive conformance coverage rather than strong spontaneous-discovery
evidence.
