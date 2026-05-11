---
id: ticket:drivegt11
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T01:57:25Z
updated_at: 2026-05-03T02:11:22Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
  plan:
    - plan:skills-corpus-residual-protocol-sharpening-pass
  research:
    - research:skills-corpus-residual-audit-synthesis
  packet:
    - packet:ralph-ticket-drivegt11-20260503T020045Z
  evidence:
    - evidence:drive-route-gate-grammar-validation
  critique:
    - critique:drive-route-gate-grammar-review
external_refs: {}
depends_on: []
---

# Summary

Align drive checkpoint, README route, memory route, and `stop` route grammar.

# Context

Follow-up validation after `ticket:wssupp4` found three still-valid route and gate
wording gaps: checkpoint critique wording can imply mandatory critique may be
`not_required`; README uses `memory` as a route while route vocabulary omits it;
and `stop` route examples do not consistently require a reason or condition.

# Why Now

Route examples and checkpoint gates are copied into handoffs and recovery notes.
They must fail closed around mandatory critique and be consistent about support
memory and stopping so fresh agents do not overclaim closure or hide why a drive
stopped.

# Scope

- Correct drive checkpoint critique-gate wording so mandatory critique cannot be
  satisfied by `not_required`.
- Reconcile README memory route wording with canonical route vocabulary by either
  adding a support-memory route token or changing README prose to avoid route-token
  mismatch.
- Require `stop` route examples or guidance to name the stop reason or condition.
- Keep route tokens Markdown vocabulary, not runtime schema or skill inventory.

# Out Of Scope

- Do not add route validators, command routers, CLIs, or schemas.
- Do not make memory canonical project truth.
- Do not reopen already-closed `ticket:routebd1` or `ticket:critfail3`.

# Acceptance Criteria

- ACC-001: Drive checkpoint critique gate no longer implies mandatory critique can
  be satisfied by `not_required`.
- ACC-002: README route examples and route vocabulary agree on whether `memory` is
  a route token or support-only wording.
- ACC-003: Route vocabulary or drive examples require `stop` to carry a stop
  reason or condition when recorded.
- ACC-004: Route-token guidance still states tokens are Markdown vocabulary, not a
  runtime enum, schema, validator, command router, skill inventory, or owner layer.
- ACC-005: Evidence records before/after searches for critique gate, memory route,
  stop reason, and `git diff --check`.
- ACC-006: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-014`
- `ticket:drivegt11#ACC-001`
- `ticket:drivegt11#ACC-002`
- `ticket:drivegt11#ACC-003`
- `ticket:drivegt11#ACC-004`
- `ticket:drivegt11#ACC-005`
- `ticket:drivegt11#ACC-006`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-014` | `evidence:drive-route-gate-grammar-validation` | `critique:drive-route-gate-grammar-review` | supported |
| `ticket:drivegt11#ACC-001` through `ticket:drivegt11#ACC-006` | `evidence:drive-route-gate-grammar-validation` | `critique:drive-route-gate-grammar-review` | supported |

# Execution Notes

Likely touched surfaces include `README.md`,
`skills/loom-records/references/route-vocabulary.md`,
`skills/loom-drive/references/checkpoint-resume-protocol.md`,
`skills/loom-drive/references/continuity-contract.md`, and
`skills/loom-drive/references/tranche-decision-protocol.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:claimmx5`.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:drive-route-gate-grammar-validation` and oracle critique
`critique:drive-route-gate-grammar-review` support closure with no unresolved
findings.

# Evidence

Recorded: `evidence:drive-route-gate-grammar-validation`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: route and checkpoint gate grammar affect closure honesty,
support-memory boundaries, and resumable drive behavior.

Required critique profiles:

- routing-safety
- closure-honesty
- owner-boundary
- operator-clarity

Findings:

`critique:drive-route-gate-grammar-review#DRVGT11-ORC-001` - resolved by
updating the ticket route readiness from stale Ralph launch details to the current
critique/acceptance route.

`critique:drive-route-gate-grammar-review#DRVGT11-ORC-002` - resolved by adding
baseline before-search snippets to `evidence:drive-route-gate-grammar-validation`.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Drive checkpoint critique-gate, memory support-route, and recorded `stop`
  reason guidance were promoted directly into README, route vocabulary, and drive
  references.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the product guidance itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
touched README, route vocabulary, and drive guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T02:11:22Z
Basis: Ralph packet `packet:ralph-ticket-drivegt11-20260503T020045Z`; evidence
`evidence:drive-route-gate-grammar-validation`; oracle critique
`critique:drive-route-gate-grammar-review` with `DRVGT11-ORC-001` and
`DRVGT11-ORC-002` resolved.
Residual risks: validation is structural/manual; there is no automated
protocol-template test suite. Evidence before-state search snippets were
reconstructed from the recorded source commit and disclosed as such.

# Dependencies

None.

# Journal

- 2026-05-03T01:57:25Z: Created from follow-up validation after `ticket:wssupp4`.
- 2026-05-03T02:03:31Z: Ralph iteration
  `packet:ralph-ticket-drivegt11-20260503T020045Z` completed in scope. Evidence
  recorded in `evidence:drive-route-gate-grammar-validation`; next route is
  mandatory oracle critique.
- 2026-05-03T02:07:36Z: First oracle pass found stale route readiness and
  summarized before-search evidence. Repaired route readiness to current critique
  route and added baseline search snippets to the evidence record before rerun.
- 2026-05-03T02:11:22Z: Oracle re-critique passed with both prior findings
  resolved. Parent recorded critique, retrospective / promotion disposition, and
  accepted closure.
