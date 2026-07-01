Status: active
Created: 2026-07-01
Updated: 2026-07-01

# Invoice Retry Schedule

## Purpose And Scope

Define retry behavior for invoice states represented by
`src/billing/retrySchedule.js`. This specification covers retry offsets, failed
invoice eligibility, paid invoice suppression, and cancellation suppression.
It does not cover payment provider integration, retryable reason taxonomy,
subscription tier checks, or notification copy.

## Behavior

- Given an invoice status is `failed` and `cancelled` is not `true`, the system
  MUST schedule retry.
- Given an invoice status is not `failed`, the system MUST NOT schedule retry.
- Given an invoice is cancelled, the system MUST NOT schedule retry even if its
  status is `failed`.
- Retry offsets MUST be exactly `[1, 3, 7, 14]`.

## Acceptance Criteria

- `RETRY_OFFSETS_DAYS` is exactly `[1, 3, 7, 14]`.
- Tests or equivalent evidence cover failed invoice eligibility.
- Tests or equivalent evidence cover non-failed invoice suppression.
- Tests or equivalent evidence cover cancellation suppression.
- Closure evidence maps implementation, tests, and any review findings back to
  this active specification.

## Constraints

- Do not add payment provider, retry reason, subscription tier, or notification
  behavior in this ticket family.
