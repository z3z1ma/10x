Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-mixed-record-authority-cold-start-scn006-live-micro.md

# Mixed Record Authority Cold Start Result

## What Was Observed

Ran `EXP-20260624-961-mixed-record-authority-cold-start-scn006-live-micro`
with three live Codex subject arms and an empty prior transcript.

Automated Trust Level 1 S003 scores:

- no-10x-control: `65`
- current-10x: `100`
- candidate-variant: `100`

Manual inspection found `current-10x` passed the target behavior:

- inspected active `.10x/specs/invoice-retry-export.md`;
- inspected active `.10x/decisions/invoice-retry-export-policy.md`;
- inspected superseded `.10x/specs/superseded/invoice-retry-export-v1.md`;
- inspected superseded `.10x/decisions/superseded/invoice-retry-window-v1.md`;
- inspected done
  `.10x/tickets/done/2026-06-10-include-cancelled-invoice-retries.md`;
- inspected cancelled
  `.10x/tickets/cancelled/2026-06-12-enterprise-only-invoice-retry-export.md`;
- inspected stale `.10x/research/2025-12-01-retired-invoice-status-api.md`;
- inspected `.10x/evidence/2026-06-10-cancelled-invoice-prototype.md`;
- inspected `src/invoices/exportRetryInvoices.js`;
- inspected `src/invoices/exportRetryInvoices.test.js`;
- inspected `package.json`;
- created one executable child ticket,
  `.10x/tickets/2026-06-25-implement-active-invoice-retry-export.md`, in the
  archived subject workspace;
- treated active records as authority and all terminal, superseded, stale, and
  old evidence records as historical context;
- captured source/test drift from stale `delinquent` and enterprise-only
  behavior;
- edited no source or test files and did not run tests.

Manual inspection found `candidate-variant` also passed, creating
`.10x/tickets/2026-06-24-align-invoice-retry-export-with-active-policy.md`.

Direct `diff -u` checks of both 10x archived workspaces against the tracked seed
source and test files produced no output.

The no-10x-control arm failed the authority target after inherited `.10x` was
removed. It created `.10x/tickets/2026-06-25-tighten-invoice-retry-export-eligibility.md`
from source/tests only and preserved stale `delinquent` plus enterprise-only
eligibility.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/161-mixed-record-authority-cold-start-scn006-live-micro/`

Canonical guard:

- `SKILL.md` unchanged during the run.
- `autoresearch/program.md` unchanged during the run.

## Procedure

1. Created a tracked mixed-authority live seed containing active, done,
   cancelled, superseded, stale research, old evidence, source, and test
   signals.
2. Validated the fixture test with `npm test` in the seed workspace.
3. Validated the experiment definition with `python3 autoresearch/validate.py`.
4. Dry-ran the Codex subject plan with:

```text
python3 autoresearch/run_codex_subject.py --experiment .10x/research/2026-06-24-mixed-record-authority-cold-start-scn006-live-micro.md --dry-run --out /tmp/10x-mixed-record-plan
```

5. Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-mixed-record-authority-cold-start-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/161-mixed-record-authority-cold-start-scn006-live-micro --require-clean-canonical
```

6. Read `report.md`, `canonical_guard.json`, final messages, archived workspace
   manifests, and generated subject tickets.
7. Compared archived 10x source/test files against the seed source/test files
   with `diff -u`.

## What This Supports Or Challenges

Supports current `SKILL.md` conformance for mixed record graph authority. In a
single cold-start workspace, current selected active records over tempting done,
cancelled, superseded, stale research, old evidence, and stale source/test
signals.

Challenges the idea that another broad lifecycle authority instruction is
needed now; the stronger mixed case passed without a candidate overlay.

## Limits

The prompt named the invoice retry export surface. This is focused cold-start
coverage, not fully open-ended repository triage.

The duplicate candidate arm used the same `SKILL.md`, so this is conformance
coverage, not a discriminating candidate comparison.
