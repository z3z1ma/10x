---
id: ticket:pbcore26
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-08T17:08:33Z
updated_at: 2026-05-08T17:22:43Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  spec:
    - spec:core-and-playbooks-package-contract
  ticket:
    - ticket:pbalign8
  evidence:
    - evidence:playbook-current-core-alignment-audit
external_refs: {}
depends_on: []
---

# Summary

Audit `loom-playbooks` against current `loom-core` doctrine and patch any clear
playbook drift so optional workflows remain routes over core owner layers, not a
second protocol.

# Context

The prior playbook/core alignment ticket is closed. This follow-up starts from
the current split package contract and checks the present playbook corpus against
current core doctrine, especially owner-layer routing, ticket acceptance,
evidence, critique, Ralph outcomes, support boundaries, and core dependency
failure behavior.

# Scope

In:

- Audit `loom-playbooks/README.md` and `loom-playbooks/skills/**/*.md` against
  `loom-core` owner-layer, ticket, evidence, critique, packet, support, and
  package-boundary vocabulary.
- Patch high-confidence playbook wording that conflicts with core-owned doctrine
  or could teach a playbook as a canonical truth owner.
- Record proportionate evidence and, if meaningful edits land, critique the final
  playbook diff before closure.

Out:

- Changing `loom-core` doctrine, package membership, manifests, generated
  adapters, scripts, validators, or hidden runtimes.
- Reopening `ticket:pbalign8`.
- Broad style rewrites unrelated to core alignment.

Assumptions / decision triggers:

- Core doctrine is authoritative for owner layers, status lifecycle, tickets,
  evidence, critique, Ralph, support surfaces, and trust boundaries.
  - Reversible: no
  - Blocks execution: no
  - Disposition: accepted from using-Loom doctrine and
    `spec:core-and-playbooks-package-contract`
- If audit finds ambiguity in core itself rather than playbook drift, this ticket
  should stop or open a separate core owner-layer follow-up instead of changing
  core opportunistically.
  - Reversible: yes
  - Blocks execution: only for the affected finding
  - Disposition: fail closed if encountered

# Acceptance

Owner: spec-owned plus ticket-local criteria for this sweep.

Criteria / covered IDs:

- `spec:core-and-playbooks-package-contract#REQ-004`
- `spec:core-and-playbooks-package-contract#REQ-005`
- `spec:core-and-playbooks-package-contract#REQ-008`
- `ticket:pbcore26#ACC-001`
- `ticket:pbcore26#ACC-002`
- `ticket:pbcore26#ACC-003`

Ticket-local criteria, only when no spec owns the reusable contract:

- ACC-001: Playbook guidance does not redefine canonical owner layers, ticket
  state, acceptance disposition, evidence sufficiency, critique verdicts, or
  Ralph packet outcomes.
- ACC-002: Playbook dependency and installation guidance fails closed when core
  is absent and does not duplicate `using-loom` or core owner-layer skills.
- ACC-003: Any patched wording, if needed, preserves the playbook's workflow
  value while routing durable facts back to core owner records.

# Current State

Status rationale:

Closed. The audit found no actionable playbook/core drift, no playbook source
changes were needed, validation evidence is recorded, and critique was not
required because no product guidance changed.

Blockers:

None.

Execution notes:

- Existing untracked `loom.zip` was present before this ticket and is outside
  scope.

Continuation note:

Next action: None for this ticket. Recheck if core doctrine, package contract,
or playbook skill prose changes.

# Evidence

Disposition: sufficient

Records:

- evidence:playbook-current-core-alignment-audit — supports
  `spec:core-and-playbooks-package-contract#REQ-004`,
  `spec:core-and-playbooks-package-contract#REQ-005`,
  `spec:core-and-playbooks-package-contract#REQ-008`, and
  `ticket:pbcore26#ACC-001` through `ticket:pbcore26#ACC-003`.

Gaps / limits:

- Semantic alignment cannot be proven completely by grep. This audit paired
  targeted scans with manual review and independent read-only audit passes, but
  future operator use may still expose softer wording drift.

# Review And Follow-Through

Critique policy: recommended
Critique rationale: This affects optional skill guidance that can change future
operator routing and closure behavior, but should align to existing core doctrine
rather than creating new authority.
Critique disposition: not_required

Required critique profiles:

- None - no playbook guidance or package behavior changed.

Findings:

- None - no critique required because the ticket accepted an audit result with no
  product-source edits.

Promotion disposition: not_required
Promotion / deferral rationale: The audit found no new durable behavior, policy,
or explanation to promote beyond the evidence and ticket acceptance record.

Promoted / deferred:

- None - no promotion artifact needed.

Wiki disposition: not_required - no accepted explanation changed.

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance
needs to be explicit.

Accepted by: OpenCode agent on operator request
Accepted at: 2026-05-08T17:22:43Z
Basis: Accepted because independent read-only audits, targeted scans, manual
review, package smoke checks, playbook dry-run pack validation, core smoke check,
and diff/status checks found no actionable playbook/core alignment drift and no
playbook source changes were needed. All playbook skills declare the core
dependency, playbooks do not preload or duplicate `using-loom`, and risky-looking
status/outcome/disposition vocabulary is framed as support-local facts,
non-Ralph transport summaries, core Ralph outcomes, or ticket-owned dispositions.
Residual risks: Semantic drift can use wording not covered by targeted scans;
future changes to core doctrine, package contract, or playbook prose should rerun
this audit posture.

# Dependencies

No hard upstream prerequisites. This ticket follows the closed
`ticket:pbalign8` alignment pass and remains constrained by the package contract
spec.

# Journal

- 2026-05-08T17:08:33Z: Created active ticket for a current playbook/core
  alignment sweep requested by the operator.
- 2026-05-08T17:22:43Z: Completed audit and validation. No playbook edits were
  required; recorded `evidence:playbook-current-core-alignment-audit`, marked
  critique and promotion not required, and accepted/closed the ticket.
