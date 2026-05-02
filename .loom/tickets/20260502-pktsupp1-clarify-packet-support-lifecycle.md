---
id: ticket:pktsupp1
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T22:03:13Z
updated_at: 2026-05-02T22:13:36Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-template-grammar-safety-pass
  plan:
    - plan:skills-corpus-template-grammar-safety-pass
  packet:
    - packet:ralph-ticket-pktsupp1-20260502T220731Z
  evidence:
    - evidence:packet-support-lifecycle-validation
  critique:
    - critique:packet-support-lifecycle-review
external_refs: {}
depends_on: []
---

# Summary

Clarify that packets own their own support-artifact lifecycle status without
owning project truth or ticket live state.

# Context

Council finding `NC-001` found packet/support wording that can be read as saying
packets do not own lifecycle status, while shared lifecycle grammar gives packets
`compiled`, `consumed`, `superseded`, and `abandoned`.

# Why Now

Fresh agents must reconcile packet lifecycle after Ralph, critique, and wiki
packet use without accidentally treating packets as canonical owner layers.

# Scope

- Audit packet/support lifecycle wording in records, workspace, and naming
  references.
- Clarify the split between packet support lifecycle status and canonical project
  truth ownership.
- Preserve packet non-canonical support-artifact doctrine.

# Out Of Scope

- Do not make packets own live ticket state, critique verdicts, accepted wiki
  truth, or intended behavior.
- Do not add lifecycle automation or validators.

# Acceptance Criteria

- ACC-001: Product guidance says packets own their own packet lifecycle status.
- ACC-002: Product guidance still says packets do not own project truth or ticket
  live state.
- ACC-003: Packet lifecycle values align with shared status lifecycle grammar.
- ACC-004: Evidence records before/after lifecycle wording searches and
  `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-template-grammar-safety-pass#OBJ-001`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-template-grammar-safety-pass#OBJ-001` | `evidence:packet-support-lifecycle-validation` | `critique:packet-support-lifecycle-review` | supported |
| `ticket:pktsupp1#ACC-001` | `evidence:packet-support-lifecycle-validation` | `critique:packet-support-lifecycle-review` | supported |
| `ticket:pktsupp1#ACC-002` | `evidence:packet-support-lifecycle-validation` | `critique:packet-support-lifecycle-review` | supported |
| `ticket:pktsupp1#ACC-003` | `evidence:packet-support-lifecycle-validation` | `critique:packet-support-lifecycle-review` | supported |
| `ticket:pktsupp1#ACC-004` | `evidence:packet-support-lifecycle-validation` | `critique:packet-support-lifecycle-review` | supported |
| `ticket:pktsupp1#ACC-005` | `critique:packet-support-lifecycle-review` | oracle critique passed with no findings | supported |

# Execution Notes

Likely touched surfaces include `skills/loom-records/references/naming-and-ids.md`,
`skills/loom-workspace/references/workspace-tree.md`, and
`skills/loom-records/references/status-lifecycle.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:critgate2`.

# Route Readiness

Route: acceptance_review

Acceptance review readiness:
Evidence `evidence:packet-support-lifecycle-validation` and oracle critique
`critique:packet-support-lifecycle-review` support closure with no findings.

# Evidence

Recorded: `evidence:packet-support-lifecycle-validation` captures before/after
searches for packet lifecycle / support truth wording and `git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: packet lifecycle grammar affects handoff recovery and support
artifact authority.

Required critique profiles:

- owner-boundary
- records-grammar
- routing-safety

Findings:

`critique:packet-support-lifecycle-review` - no findings; mandatory oracle
critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Mandatory oracle critique passed with no findings.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Packet lifecycle ownership wording was promoted directly into
  `skills/loom-records/references/naming-and-ids.md`,
  `skills/loom-workspace/references/workspace-tree.md`, and
  `skills/loom-records/references/status-lifecycle.md`.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the product-surface wording itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
touched product guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T22:13:36Z
Basis: Ralph packet `packet:ralph-ticket-pktsupp1-20260502T220731Z`; evidence
`evidence:packet-support-lifecycle-validation`; oracle critique
`critique:packet-support-lifecycle-review` with no findings.
Residual risks: validation is structural and broader support-boundary wording
outside the targeted surfaces may need future review if later ambiguity appears.

# Dependencies

None.

# Journal

- 2026-05-02T22:03:13Z: Created from council finding `NC-001`.
- 2026-05-02T22:07:31Z: Compiled Ralph packet
  `packet:ralph-ticket-pktsupp1-20260502T220731Z` and moved ticket to `active`.
- 2026-05-02T22:08:54Z: Ralph child updated targeted packet/support lifecycle
  wording, recorded `evidence:packet-support-lifecycle-validation`, and moved
  ticket to `review_required` for mandatory critique.
- 2026-05-02T22:10:56Z: Parent reconciled the Ralph packet, normalized claim
  matrix statuses to claim-coverage vocabulary, and expanded evidence structure
  before oracle critique.
- 2026-05-02T22:13:36Z: Mandatory oracle critique
  `critique:packet-support-lifecycle-review` passed with no findings. Recorded
  retrospective / promotion disposition and accepted closure.
