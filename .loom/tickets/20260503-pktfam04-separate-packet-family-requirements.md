---
id: ticket:pktfam04
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T05:23:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-context-integrity-hardening-review
external_refs: {}
depends_on:
  - ticket:tplsave3
---

# Summary

Separate shared packet grammar from Ralph-only requirements without weakening
Ralph packet discipline.

# Context

Council found critique/wiki packets may be forced into Ralph-shaped precision or
fake `unknown` fields if shared packet requirements are too broad.

# Why Now

Packet support surfaces are central to fresh workers and packetized sibling work.
Their required fields should be accurate by family.

# Scope

- Clarify shared packet fields versus Ralph-specific fields.
- Preserve strict Ralph `source_fingerprint`, `execution_context`,
  `child_write_scope`, and `verification_posture` expectations.
- Adjust critique/wiki packet templates or references if current wording implies
  Ralph-only requirements everywhere.

# Out Of Scope

- Do not add new packet families or canonical owner layers.
- Do not weaken Ralph packet launch safety.

# Acceptance Criteria

- ACC-001: Shared packet grammar distinguishes common support fields from
  family-specific required fields.
- ACC-002: Ralph requirements remain strict and explicit.
- ACC-003: Critique/wiki packet guidance avoids fake precision while preserving
  enough review/synthesis contract metadata.
- ACC-004: Evidence records targeted packet-family searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-005`
- `ticket:pktfam04#ACC-001`
- `ticket:pktfam04#ACC-002`
- `ticket:pktfam04#ACC-003`
- `ticket:pktfam04#ACC-004`
- `ticket:pktfam04#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-005` | `evidence:packet-family-requirements-validation` | `critique:packet-family-requirements-rereview` | supported |
| `ticket:pktfam04#ACC-001` | `evidence:packet-family-requirements-validation` | `critique:packet-family-requirements-rereview` | supported |
| `ticket:pktfam04#ACC-002` | `evidence:packet-family-requirements-validation` | `critique:packet-family-requirements-rereview` | supported |
| `ticket:pktfam04#ACC-003` | `evidence:packet-family-requirements-validation` | `critique:packet-family-requirements-rereview` | supported |
| `ticket:pktfam04#ACC-004` | `evidence:packet-family-requirements-validation` | `critique:packet-family-requirements-rereview` | supported |
| `ticket:pktfam04#ACC-005` | None - critique outcome is the acceptance instrument | `critique:packet-family-requirements-rereview` | supported |

# Execution Notes

Likely touched files: `skills/loom-records/references/packet-frontmatter.md`, Ralph
packet contract/template, critique packet template, and wiki packet template.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:evhard05`.

Ralph packet `packet:ralph-ticket-pktfam04-20260503T050940Z` completed in scope,
evidence was recorded, initial critique finding was resolved, mandatory critique
re-review passed with no findings, and acceptance is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:packet-family-requirements-validation`, initial critique
`critique:packet-family-requirements-review`, and final re-review
`critique:packet-family-requirements-rereview` support closure. The only initial
finding was resolved.

# Evidence

Recorded: `evidence:packet-family-requirements-validation`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: packet grammar controls bounded worker contracts.

Required critique profiles:

- packet-safety
- protocol-change
- workflow-boundary

Findings:

`critique:packet-family-requirements-review#FIND-001` - resolved by changing the
ticket and Ralph packet `change_class` from `packet-safety` to valid
`protocol-authority`; verified by
`critique:packet-family-requirements-rereview`.

`critique:packet-family-requirements-rereview` - no new findings; mandatory
critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Shared packet grammar separation was promoted directly into
  `skills/loom-records/references/packet-frontmatter.md`.
- Ralph strictness was promoted directly into
  `skills/loom-ralph/references/packet-contract.md` and
  `skills/loom-ralph/templates/ralph-packet.md`.
- Critique/wiki fake-precision guidance was promoted directly into their packet
  templates.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to packet grammar and packet templates.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
packet grammar reference and packet templates.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T05:23:00Z
Basis: Ralph packet `packet:ralph-ticket-pktfam04-20260503T050940Z`; evidence
`evidence:packet-family-requirements-validation`; initial critique
`critique:packet-family-requirements-review`; final no-findings re-review
`critique:packet-family-requirements-rereview`.
Residual risks: Validation remains manual and structural; no automated protocol
validator exists by design. Historical packets are not migrated by this ticket.

# Dependencies

- `ticket:tplsave3`

# Journal

- 2026-05-03T04:09:51Z: Created from council packet-family requirement finding.
- 2026-05-03T05:09:40Z: Started Ralph iteration
  `packet:ralph-ticket-pktfam04-20260503T050940Z` from clean `main` at
  `da8d30a`.
- 2026-05-03T05:13:40Z: Ralph iteration
  `packet:ralph-ticket-pktfam04-20260503T050940Z` completed in scope. Evidence
  recorded in `evidence:packet-family-requirements-validation`; next route is
  mandatory critique.
- 2026-05-03T05:20:23Z: Mandatory critique found one medium frontmatter
  vocabulary issue: `packet-safety` was used as `change_class` instead of a
  critique profile. Repaired ticket and packet frontmatter to
  `change_class: protocol-authority`; next route is critique re-review.
- 2026-05-03T05:23:00Z: Mandatory critique re-review
  `critique:packet-family-requirements-rereview` passed with no findings. Parent
  dispositioned `critique:packet-family-requirements-review#FIND-001` as
  resolved and accepted closure.
