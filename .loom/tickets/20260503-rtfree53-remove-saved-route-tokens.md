---
id: ticket:rtfree53
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T19:42:50Z
updated_at: 2026-05-03T19:46:54Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  evidence:
    - evidence:route-token-simplification-validation
  critique:
    - critique:route-token-simplification-review
external_refs: {}
depends_on: []
---

# Summary

Remove saved workflow-choice and route-token mechanics from current Loom product
surfaces while preserving bounded packet contracts.

# Context

The user asked to continue simplifying the protocol so owner records do not carry
serialized `next route`, `Route`, route-readiness, or route-token fields. Tickets
should instead expose enough state, blockers, acceptance, evidence, critique,
linked-owner, and journal facts for an agent to reason about the next action.

# Why Now

Saved route fields create a second scheduling surface and weaken the ticket as
the live execution ledger. The simplification needed to be reconciled across
skills, templates, package framing, and internal examples before the corpus could
truthfully teach the new model.

# Scope

- Remove current-product instructions that ask tickets, plans, workspace
  snapshots, support handoffs, or ship/drive surfaces to serialize a next route
  or route-token value.
- Keep packet contracts explicit for bounded child work, including scope, stop
  conditions, output contract, and child outcome vocabulary when the packet
  family owns it.
- Update package docs and internal examples to use owner/workflow choice and
  expected-flow language rather than expected-route fixtures.
- Preserve compatibility file paths such as
  `skills/loom-records/references/route-vocabulary.md` while changing their
  meaning to workflow-selection guidance.
- Record structural validation and mandatory critique for the protocol-authority
  change.

# Out Of Scope

- Do not migrate historical `.loom/` dogfood records that still preserve prior
  route-token wording as execution provenance.
- Do not add runtime enums, command routers, validators, helper scripts, or a new
  owner layer.
- Do not remove packet contract fields that make bounded child work auditable.
- Do not commit changes; commit/staging remains operator-owned.

# Acceptance Criteria

- ACC-001: Current product guidance says owner records should not serialize next
  workflow choices as `next route`, `Route`, route-readiness, route-token, or
  equivalent saved fields.
- ACC-002: Ticket template and readiness guidance omit `# Next Move / Next Route`,
  `# Route Readiness`, and route-token lifecycle fields; continuation is inferred
  from ticket facts.
- ACC-003: Packet guidance preserves the bounded contract exception without
  allowing packets to overrule ticket-owned truth.
- ACC-004: Ship, drive, plan, workspace, Ralph, bootstrap, and package-framing
  docs use owner/workflow/acceptance-gate language rather than saved route-token
  language, including removal of current-product `acceptance_review` token uses.
- ACC-005: Internal examples use expected-flow fixtures and wording instead of
  current expected-route fixture guidance.
- ACC-006: Structural validation passes and mandatory critique has no unresolved
  blocker for acceptance.

# Coverage

Covers:

- ticket:rtfree53#ACC-001
- ticket:rtfree53#ACC-002
- ticket:rtfree53#ACC-003
- ticket:rtfree53#ACC-004
- ticket:rtfree53#ACC-005
- ticket:rtfree53#ACC-006

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| ticket:rtfree53#ACC-001 | evidence:route-token-simplification-validation | critique:route-token-simplification-review | supported |
| ticket:rtfree53#ACC-002 | evidence:route-token-simplification-validation | critique:route-token-simplification-review | supported |
| ticket:rtfree53#ACC-003 | evidence:route-token-simplification-validation | critique:route-token-simplification-review | supported |
| ticket:rtfree53#ACC-004 | evidence:route-token-simplification-validation | critique:route-token-simplification-review | supported |
| ticket:rtfree53#ACC-005 | evidence:route-token-simplification-validation | critique:route-token-simplification-review | supported |
| ticket:rtfree53#ACC-006 | evidence:route-token-simplification-validation | critique:route-token-simplification-review | supported |

# Execution Notes

Implemented as local Markdown edits across current product surfaces and examples.
Ralph was not used because this was an in-context reconciliation pass, but the
risk class is high because the edits change protocol authority and operator
behavior.

# Blockers

None.

# Evidence

Evidence status: sufficient for structural acceptance at the observed source
state.

Evidence record:

- evidence:route-token-simplification-validation supports all ticket-local
  acceptance criteria and records the remaining intentional compatibility/prohibitory
  route-wording matches.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: the change edits protocol-authority surfaces, ticket/packet
truth boundaries, workflow selection guidance, package framing, and examples.

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface

Findings:

- critique:route-token-simplification-review#FIND-001 — resolved by replacing
  Ralph packet route-authorization wording with Ralph-readiness and scoped-fact
  wording in `skills/loom-ralph/templates/ralph-packet.md`.
- critique:route-token-simplification-review#FIND-002 — resolved by replacing
  product `acceptance_review` token wording with ticket-owned acceptance-gate
  language in ship and drive surfaces.
- critique:route-token-simplification-review#FIND-003 — resolved by replacing
  saved route-ish fields in `skills/loom-plans/templates/plan.md`.
- critique:route-token-simplification-review#FIND-004 — resolved by renaming and
  rewording example fixture guidance to expected-flow language and updating
  `ARCHITECTURE.md`.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- The accepted simplification was promoted directly into the owning product
  surfaces: ticket/readiness templates, records/workspace/drive/Ralph/ship/plan
  guidance, package docs, bootstrap references, and examples.

Deferred / not-required rationale:

No separate wiki, research, spec, plan, initiative, constitution, or memory
promotion is required because the durable lesson is the product-surface protocol
guidance itself.

# Wiki Disposition

N/A - no wiki promotion needed.

# Acceptance Decision

Accepted by: OpenCode
Accepted at: 2026-05-03T19:46:54Z
Basis: `evidence:route-token-simplification-validation` and
`critique:route-token-simplification-review` support all acceptance criteria;
mandatory critique findings were repaired and have ticket-owned dispositions.
Residual risks: Historical `.loom/` records still contain older route-token
provenance and should not be treated as current product guidance. The renamed
`examples/*/expected-flow.md` files are untracked until the operator or a future
commit stages them with the corresponding `expected-route.md` deletions.

# Dependencies

None.

# Journal

- 2026-05-03T19:42:50Z: Reconciled the route-token simplification across product
  surfaces, examples, validation evidence, and mandatory critique.
- 2026-05-03T19:46:54Z: Ran final structural validation, confirmed critique
  repairs, accepted the evidence, and closed this bounded ticket.
