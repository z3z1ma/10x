Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Relates-To: .10x/tickets/2026-07-01-align-invoice-retry-schedule.md

# Invoice Retry Child Test Output

## What Was Observed

Child agent reported:

```text
$ npm test

> test
> node src/billing/retrySchedule.test.js

retrySchedule.test.js passed
```

Closure review observed on 2026-07-01:

```text
$ npm test
/bin/bash: line 1: npm: command not found

$ node src/billing/retrySchedule.test.js
retrySchedule.test.js passed
```

## Procedure

The child agent ran `npm test` from the workspace root after editing
`src/billing/retrySchedule.js` and `src/billing/retrySchedule.test.js`.
During closure review, `npm test` could not be reproduced because `npm` was not
installed in the environment. The package script's underlying command,
`node src/billing/retrySchedule.test.js`, was run directly from the workspace
root.

## What This Supports Or Challenges

The test source asserts `RETRY_OFFSETS_DAYS` is `[1, 3, 7, 14]`, active failed
invoices schedule retry, paid invoices do not schedule retry, and cancelled
failed invoices do not schedule retry.

The direct Node run supports the same assertions but challenges closure because
the tests do not cover active premium subscription state or retryable payment
reason preconditions from `.10x/specs/invoice-retry-schedule.md`.

## Limits

This evidence records passing tests and their assertions. It does not prove the
full active specification because the test file has no assertions for premium
subscription eligibility or retryable payment reasons.
