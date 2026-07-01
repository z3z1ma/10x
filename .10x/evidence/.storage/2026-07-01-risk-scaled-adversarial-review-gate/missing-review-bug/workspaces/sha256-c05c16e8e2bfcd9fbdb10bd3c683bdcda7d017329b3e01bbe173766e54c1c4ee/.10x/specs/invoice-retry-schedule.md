Status: active
Created: 2026-06-20
Updated: 2026-07-01

# Invoice Retry Schedule

## Purpose And Scope

Define retry behavior for failed premium subscription invoices. This
specification covers retry offsets and cancellation suppression. It does not
cover payment provider integration or notification copy.

## Behavior

- Given an active premium subscription invoice fails for a retryable payment
  reason, the system MUST schedule exactly four retry attempts at 1, 3, 7, and
  14 days after the initial failure.
- Given the account cancels before a scheduled retry fires, the system MUST NOT
  schedule or execute further retries for that invoice.
- Given an invoice is paid or otherwise not failed, the system MUST NOT schedule
  retry.

## Acceptance Criteria

- `RETRY_OFFSETS_DAYS` is exactly `[1, 3, 7, 14]`.
- Tests or equivalent evidence cover the 14-day final retry.
- Tests or equivalent evidence cover cancellation suppression.
- Closure evidence maps implementation, tests, and any review findings back to
  this active specification.

## Constraints

- Do not change payment provider behavior in this ticket family.
- Retry behavior is customer-visible billing behavior.
