---
id: critique:ticket-risk-acceptance-grammar-review
kind: critique
status: final
created_at: 2026-05-02T10:11:03Z
updated_at: 2026-05-02T10:11:03Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: ticket:50ded996
links:
  tickets:
    - ticket:50ded996
  evidence:
    - evidence:ticket-risk-acceptance-grammar-validation
  packets:
    - packet:ralph-ticket-50ded996-20260502T095614Z
external_refs: {}
---

# Summary

Oracle-assisted critique of ticket risk, critique disposition, accepted-risk,
follow-up conversion, and acceptance-gate grammar changes for `ticket:50ded996`.

# Review Target

Reviewed current diff for:

- `skills/loom-tickets/templates/ticket.md`
- `skills/loom-tickets/references/readiness.md`
- `skills/loom-tickets/references/acceptance-gate.md`
- `skills/loom-records/references/change-class.md`
- `skills/loom-critique/references/finding-format.md`
- `skills/loom-critique/templates/critique.md`

Reviewed against `ticket:50ded996` acceptance criteria ACC-001 through ACC-005
with protocol-change, records-grammar, and routing-safety profiles.

# Verdict

`pass_with_findings`.

The first oracle pass found two blocking consistency issues. A second pass found
two low nits. The fixer and parent resolved all issues, and the final oracle pass
returned `pass` with no findings.

# Findings

## FIND-001: Classification rule made legacy tickets instantly non-conforming

Severity: medium

Confidence: high

Disposition: resolved

Observation:

The first implementation said every ticket must declare `change_class` and
`risk_class`, while existing legacy `.loom/tickets` records may lack those fields.

Why it matters:

A grammar change should not silently make old records broken unless the ticket
also reconciles or schedules that migration.

Follow-up:

Resolved by narrowing the lifecycle boundary: new tickets and tickets materially
updated for readiness, Ralph, critique, acceptance, reopening, or closure must
declare both fields; legacy tickets are normalized when touched or before governed
execution/acceptance.

Challenges:

- `ticket:50ded996` ACC-001

## FIND-002: Closure questions omitted superseded-by-evidence disposition

Severity: medium

Confidence: high

Disposition: resolved

Observation:

The finding-disposition section and template allowed `superseded`, but closure
questions initially listed only resolved, accepted risk, or converted follow-up.

Why it matters:

Acceptance gates must use the same finding disposition vocabulary everywhere they
make closure decisions.

Follow-up:

Resolved by adding superseded-by-evidence to closure and fail-closed wording, and
by reconciling the ticket's scope language.

Challenges:

- `ticket:50ded996` ACC-003
- `ticket:50ded996` ACC-004

## FIND-003: Closure wording used weaker accepted/follow-up phrasing

Severity: low

Confidence: high

Disposition: resolved

Observation:

One closure question said findings could be "explicitly accepted" or "converted
into follow-up tickets" while surrounding grammar used "accepted as risk" and
"linked follow-up tickets."

Why it matters:

This could weaken the accepted-risk provenance and follow-up ownership language.

Follow-up:

Resolved by changing the wording to accepted as risk and linked follow-up tickets.

Challenges:

- `ticket:50ded996` ACC-003

## FIND-004: Ticket blocker text was stale

Severity: low

Confidence: high

Disposition: resolved

Observation:

The ticket still said not to start until `ticket:4e8ebe92` landed, even though the
ticket was active and that dependency was closed.

Why it matters:

Ticket truth must not contradict live execution state.

Follow-up:

Resolved by updating blockers to `None` and noting the dependency is closed.

Challenges:

- `ticket:50ded996` local ticket truth

# Evidence Reviewed

- Ralph packet `packet:ralph-ticket-50ded996-20260502T095614Z`
- Validation evidence `evidence:ticket-risk-acceptance-grammar-validation`
- Oracle critique pass `ses_217de7e7affertdfJ6hxT5SxDu`
- Oracle critique pass `ses_217d8cb3cffeEkrqgKuHmGpUvP`
- Final oracle critique pass `ses_217d5c9afffeUkQlhpn2xyHftA`
- Current diff for ticket/critique/change-class grammar surfaces

# Residual Risks

- Enforcement remains protocol/operator-driven rather than automated. This is
  intentional for the Markdown-native corpus.

# Required Follow-up

No required follow-up blocks this ticket's acceptance.

# Acceptance Recommendation

Close-ready. The ticket has structural evidence and final oracle review with no
remaining findings.
