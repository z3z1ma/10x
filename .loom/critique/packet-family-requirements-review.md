---
id: critique:packet-family-requirements-review
kind: critique
status: final
created_at: 2026-05-03T05:20:23Z
updated_at: 2026-05-03T05:20:23Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:pktfam04 diff da8d30a..working-tree initial review"
links:
  ticket:
    - ticket:pktfam04
  evidence:
    - evidence:packet-family-requirements-validation
  packet:
    - packet:ralph-ticket-pktfam04-20260503T050940Z
external_refs: {}
---

# Summary

Initial mandatory oracle critique for `ticket:pktfam04` after separating shared
packet grammar from family-specific packet requirements.

# Review Target

Current working-tree diff from baseline
`da8d30aedcd6c2dc3b89226e8d70068a9ef29aea`, covering packet-frontmatter grammar,
Ralph packet contract/template, critique/wiki packet templates, ticket, evidence,
and Ralph packet records.

Required critique profiles: `packet-safety`, `protocol-change`, and
`workflow-boundary`.

# Verdict

`changes_required` - one medium finding blocks acceptance until remediated or
ticket-dispositioned.

# Findings

## FIND-001: `change_class` uses a critique-profile label, not a valid change class

Severity: medium
Confidence: high
State: open

Observation:

The ticket and Ralph packet used `change_class: packet-safety`, but
`packet-safety` is a required critique profile, not a valid `change_class` value.
Valid values are defined in `skills/loom-records/references/change-class.md` and
listed in `skills/loom-records/references/packet-frontmatter.md`.

Why it matters:

`change_class` drives evidence, critique, and verification routing. Mixing
critique-profile vocabulary with mutation-class vocabulary makes the record graph
less reliable for future agents.

Follow-up:

Change the ticket and packet `change_class` to a valid value, likely
`protocol-authority`, while keeping `packet-safety` under required critique
profiles. If `packet-safety` is intended as a new change class, that requires an
explicit product grammar change, which appears out of scope.

Challenges:

- `ticket:pktfam04#ACC-005`

# Profile Results

- `packet-safety`: pass for product changes. Shared support blocks remain visible;
  Ralph remains strict; critique/wiki avoid fake precision without losing
  target/source/write/merge metadata.
- `protocol-change`: changes required due `FIND-001`. No runtime, schema,
  validator, or new-owner-layer assumption was found in the product diff.
- `workflow-boundary`: pass. Packets remain support artifacts; critique/wiki are
  not made Ralph-governed; ticket remains the live execution ledger.

# Evidence Reviewed

- Target diff from `da8d30aedcd6c2dc3b89226e8d70068a9ef29aea`
- `git status --short`
- `git diff --check` over target paths: passed with no output
- `ticket:pktfam04`
- `evidence:packet-family-requirements-validation`
- `packet:ralph-ticket-pktfam04-20260503T050940Z`
- `skills/loom-records/references/packet-frontmatter.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `skills/loom-critique/templates/critique-packet.md`
- `skills/loom-wiki/templates/wiki-packet.md`
- `skills/loom-records/references/change-class.md`

# Acceptance Coverage

- `ticket:pktfam04#ACC-001`: supported. Shared required fields are separated from
  family-owned support blocks.
- `ticket:pktfam04#ACC-002`: supported. Ralph `source_fingerprint`,
  `execution_context`, `context_budget`, write/merge scope, and
  `verification_posture` remain strict.
- `ticket:pktfam04#ACC-003`: supported. Critique/wiki guidance permits honest
  `unknown`/`none` without allowing metadata-free packets.
- `ticket:pktfam04#ACC-004`: supported. Evidence records targeted searches and
  `git diff --check`; critique independently confirmed the whitespace check.
- `ticket:pktfam04#ACC-005`: not satisfied until `FIND-001` is resolved or
  dispositioned.

# Residual Risks

- Validation is manual and structural; no automated protocol validator exists by
  design.
- Historical packets are not migrated; future authors must follow the clarified
  grammar.

# Required Follow-up

Resolve `FIND-001`, update or recheck evidence as needed, then run mandatory
critique re-review before acceptance.

# Acceptance Recommendation

`follow-up-needed-before-acceptance`
