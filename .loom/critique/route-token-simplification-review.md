---
id: critique:route-token-simplification-review
kind: critique
status: final
created_at: 2026-05-03T19:42:50Z
updated_at: 2026-05-03T19:46:54Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:rtfree53 route-token simplification product diff"
links:
  tickets:
    - ticket:rtfree53
  evidence:
    - evidence:route-token-simplification-validation
external_refs: {}
---

# Summary

Reviewed the route-token simplification for protocol authority, ticket/packet
truth boundaries, operator clarity, and product-surface consistency.

# Review Target

Target: `ticket:rtfree53`, the route-token simplification diff across `skills/`,
package docs, and `examples/`.

# Verdict

`pass_with_findings`

The initial adversarial review found stale saved-route wording in Ralph, ship,
drive, plan, examples, and architecture surfaces. Those findings were repaired,
and the follow-up review reported no remaining product-surface blockers.

# Findings

## FIND-001: Ralph packet template preserved saved route authorization

Severity: high
Confidence: high
State: open

Observation:

The initial review found `skills/loom-ralph/templates/ralph-packet.md` still
saying the target ticket must authorize Ralph, saved readiness details must match
the packet, and packets must not overrule ticket-owned route truth.

Why it matters:

That wording would have reintroduced saved route authority into ticket truth and
undermined the packet exception boundary.

Follow-up:

Resolved in `ticket:rtfree53` by changing the template to require Ralph-ready
ticket facts and scoped-fact alignment, without saved route authorization.

Challenges:

- ticket:rtfree53#ACC-003

## FIND-002: Ship and drive surfaces preserved `acceptance_review` as a route token

Severity: medium
Confidence: high
State: open

Observation:

The initial review found current product wording in `skills/loom-ship/SKILL.md`,
`skills/loom-ship/references/handoff-options.md`, and `skills/loom-drive/SKILL.md`
that still used backticked `acceptance_review` or described it as ticket-owned
route truth.

Why it matters:

The acceptance gate should remain ticket-owned without preserving a saved route
token in current guidance.

Follow-up:

Resolved in `ticket:rtfree53` by replacing those references with ticket-owned
acceptance-gate and acceptance-review wording.

Challenges:

- ticket:rtfree53#ACC-004

## FIND-003: Plan template still asked for saved route-ish fields

Severity: medium
Confidence: high
State: open

Observation:

The initial review found `skills/loom-plans/templates/plan.md` still asking for
evidence/critique route, parent reconciliation route, and sequential ticket route
wording.

Why it matters:

Plans own sequencing and strategy. They should not serialize next workflow
choices as route-like fields.

Follow-up:

Resolved in `ticket:rtfree53` by changing the template to evidence/critique
expectations, parent reconciliation path, and sequential tickets.

Challenges:

- ticket:rtfree53#ACC-004

## FIND-004: Example and architecture fixture wording kept expected-route language

Severity: low
Confidence: high
State: open

Observation:

The initial review found the example index and architecture note still saying
expected route after the fixture files had been renamed to expected-flow.

Why it matters:

Examples are teaching fixtures. Keeping current expected-route wording would make
the simplified model look inconsistent.

Follow-up:

Resolved in `ticket:rtfree53` by updating example/architecture wording to
expected-flow language.

Challenges:

- ticket:rtfree53#ACC-005

# Evidence Reviewed

- `evidence:route-token-simplification-validation`
- Current diff across `skills/`, package docs, and `examples/`
- Targeted product-surface searches for saved route-token wording
- Oracle review task `ses_210a8b579ffeHPXuMd2JVF7laQ`, including initial findings
  and follow-up no-findings review

# Residual Risks

- Historical `.loom/` dogfood records still contain older route vocabulary and
  should be treated as provenance, not current product guidance.
- The replacement `examples/*/expected-flow.md` files are untracked until a future
  staging/commit step includes them with the corresponding deletions.
- This review is structural documentation critique; there is no app runtime or
  automated behavior suite for this repository.

# Required Follow-up

None before acceptance. The ticket owns the resolved dispositions for all open
findings above.

# Acceptance Recommendation

`no-critique-blockers`
