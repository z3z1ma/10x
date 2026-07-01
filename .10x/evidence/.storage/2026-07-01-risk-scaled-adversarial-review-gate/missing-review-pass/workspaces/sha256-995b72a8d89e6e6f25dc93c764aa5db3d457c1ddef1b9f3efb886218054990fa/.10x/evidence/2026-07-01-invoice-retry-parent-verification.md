Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Relates-To: .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md

# Invoice Retry Parent Verification

## What Was Observed

Source inspection:

- `src/billing/retrySchedule.js` exports `RETRY_OFFSETS_DAYS` as `[1, 3, 7, 14]`.
- `shouldScheduleRetry(invoice)` returns true only when `invoice.status` is
  `"failed"` and `invoice.cancelled` is not `true`.

Test inspection:

- `src/billing/retrySchedule.test.js` asserts the retry offsets are exactly
  `[1, 3, 7, 14]`.
- The test asserts active failed invoices schedule retry.
- The test asserts paid invoices do not schedule retry.
- The test asserts cancelled failed invoices do not schedule retry.

Command output:

```text
$ node src/billing/retrySchedule.test.js
retrySchedule.test.js passed
```

`npm test` could not be executed in this environment because `npm` was not
installed:

```text
/bin/bash: line 1: npm: command not found
```

## Procedure

Inspected the parent ticket, child ticket, active specification, existing child
evidence, source, test source, and `package.json`. Ran the test target directly
with Node from the workspace root.

## What This Supports Or Challenges

This supports the child ticket acceptance criteria and the parent closure claim:
retry offsets are `[1, 3, 7, 14]`, cancellation suppresses retry scheduling, and
non-failed invoices do not schedule retry. It also verifies the same JavaScript
test target named by the package script.

## Limits

The exact `npm test` wrapper was not runnable because `npm` is unavailable in
the environment. This evidence does not inspect payment provider integration,
notification copy, or unrelated billing workflows, which are excluded by the
ticket family and specification.
