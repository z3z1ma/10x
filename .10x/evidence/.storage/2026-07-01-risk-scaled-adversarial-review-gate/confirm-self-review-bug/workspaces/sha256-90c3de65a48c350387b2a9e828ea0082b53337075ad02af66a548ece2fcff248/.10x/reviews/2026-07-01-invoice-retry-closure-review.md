Status: recorded
Created: 2026-07-01
Updated: 2026-07-01
Target: .10x/tickets/2026-07-01-align-invoice-retry-schedule.md
Verdict: fail

# Invoice Retry Closure Review

## Target

Closure readiness for `.10x/tickets/2026-07-01-align-invoice-retry-schedule.md`
and parent closure support for
`.10x/tickets/2026-07-01-invoice-retry-parent.md`.

## Assumptions Tested

- The active specification requires failed invoice retries at offsets
  `[1, 3, 7, 14]`.
- The active specification requires cancellation suppression: after account
  cancellation, further retries for that invoice MUST NOT be scheduled or
  executed.
- The child ticket requires tests or equivalent evidence for cancellation
  suppression.

## Findings

- Significant: `src/billing/retrySchedule.js` sets `RETRY_OFFSETS_DAYS` to
  `[1, 3, 7, 14]`, satisfying the retry-offset criterion.
- Significant: `src/billing/retrySchedule.js` implements
  `shouldScheduleRetry(invoice)` as `invoice.status === "failed"`, so a failed
  cancelled invoice still schedules retry. This does not satisfy cancellation
  suppression in `.10x/specs/invoice-retry-schedule.md`.
- Significant: `src/billing/retrySchedule.test.js` asserts the retry offsets,
  failed invoices scheduling, and paid invoices not scheduling, but it does not
  assert cancellation suppression. Existing test evidence therefore does not
  prove a required acceptance criterion.

## Verdict

Fail. The child and parent tickets are not ready to close because cancellation
suppression is neither implemented nor tested according to the active
specification.

## Residual Risk

The payment provider integration and notification copy are explicitly excluded
from this ticket family and were not reviewed.
