---
id: critique:review-target-shape-review
kind: critique
status: final
created_at: 2026-05-02T20:27:44Z
updated_at: 2026-05-02T20:27:44Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:revtgt7x diff b7c076f..working-tree"
links:
  ticket:
    - ticket:revtgt7x
  evidence:
    - evidence:review-target-shape-validation
  packet:
    - packet:ralph-ticket-revtgt7x-20260502T201800Z
external_refs: {}
---

# Summary

Reviewed the `ticket:revtgt7x` implementation that documents direct critique
records as scalar `review_target` handles and critique packets as structured
`review_target` mappings.

# Review Target

Current working-tree diff from baseline
`b7c076f5105c2c241ac3b7ec932eb6f8a165c86f`, covering the ticket, evidence,
Ralph packet, and changed critique/frontmatter templates and references.

# Verdict

`changes_required` - the new critique-packet grammar needs an explicit legacy
compatibility boundary or existing consumed critique packets become invalid by
the new wording.

# Findings

## REVTGT7X-CRIT-001: Critique-packet grammar retroactively invalidates older packets

Severity: medium
Confidence: high
State: open

Observation:

`skills/loom-records/references/packet-frontmatter.md` now says critique packet
`review_target.kind` and `review_target.summary` are required, with unavailable
scalar fields written as `none`. Existing consumed critique packets still use
the older `review_target` mapping with only `kind` and `diff`, including:

- `.loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md`
- `.loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md`

Why it matters:

The grammar reads as universally required rather than scoped to new critique
packets or current templates. That makes existing durable packet records appear
invalid without migration and weakens operator clarity for ACC-001 and ACC-003.

Follow-up:

Before acceptance, either explicitly scope the required shape to new/current
critique packets and add a legacy compatibility note for older `kind` plus
`diff` critique packets, or normalize the existing critique packets and record
that reconciliation.

Challenges:

- `ticket:revtgt7x#ACC-001`
- `ticket:revtgt7x#ACC-003`

# Evidence Reviewed

- `git status --short`
- `git diff --check b7c076f5105c2c241ac3b7ec932eb6f8a165c86f` - no output
- Current diff from baseline `b7c076f5105c2c241ac3b7ec932eb6f8a165c86f`
- `.loom/tickets/20260502-revtgt7x-canonicalize-review-target-shape.md`
- `.loom/evidence/20260502-review-target-shape-validation.md`
- `.loom/packets/ralph/20260502T201800Z-ticket-revtgt7x-iter-01.md`
- Changed product files listed by the ticket
- Existing `.loom/packets/critique/*.md` critique packets
- Existing `.loom/critique/*` scalar `review_target` usage

# Residual Risks

`records-grammar` is used as a ticket-required profile but is not itself a named
profile in `skills/loom-critique/references/critique-lens.md`; this critique
treated it as the record-shape lens requested by the ticket.

# Required Follow-up

Resolve `REVTGT7X-CRIT-001` and run a mandatory re-critique before acceptance.

# Acceptance Recommendation

Active follow-up required.
