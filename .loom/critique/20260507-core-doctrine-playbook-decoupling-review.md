---
id: critique:core-doctrine-playbook-decoupling-review
kind: critique
status: final
created_at: 2026-05-07T22:05:17Z
updated_at: 2026-05-07T22:05:17Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:hi5e7nbr Ralph iteration 01 scoped core doctrine/prose diff"
links:
  ticket:
    - ticket:hi5e7nbr
  packet:
    - packet:ralph-ticket-hi5e7nbr-20260507T215704Z
  evidence:
    - evidence:core-doctrine-playbook-decoupling-check
  spec:
    - spec:core-and-playbooks-package-contract
  decision:
    - decision:0008
external_refs: {}
---

# Summary

Reviewed the Ralph iteration 01 diff for `ticket:hi5e7nbr`, which updates current
core skill prose so optional playbook routes are framed as optional,
package-dependent, or replaceable by equivalent project workflows.

# Review Target

Direct implementation critique of the scoped diff under:

- `skills/using-loom/**`
- `skills/loom-workspace/**`
- `skills/loom-records/**`
- `skills/loom-plans/**`
- `skills/loom-tickets/**`
- `skills/loom-research/**`
- `skills/loom-ralph/**`

Profiles: `protocol-change`, `operator-surface`, and `operator-clarity`.

# Verdict

`pass_with_findings`

The scoped prose direction is correct and aligns with `decision:0008` and the
ticket-scoped portions of `spec:core-and-playbooks-package-contract#ACC-002` and
`#ACC-007`. Findings are about reconciliation, evidence completeness, and one
minor wording clarity issue rather than a high-severity prose defect.

# Findings

## FIND-001: Ralph and ticket reconciliation incomplete

Severity: medium
Confidence: high
State: open

Observation:

At review time, evidence existed and scoped prose changed, but
`ticket:hi5e7nbr` still listed evidence as pending with no implementation
evidence, and the Ralph packet remained `status: compiled` with child output and
parent merge notes pending.

Why it matters:

Ralph child output does not update ticket truth by itself. Ticket closure would be
false until packet status, ticket evidence disposition, critique disposition, and
journal truth are reconciled.

Follow-up:

Update the packet child output and parent merge notes, move the packet to a
terminal lifecycle status after reconciliation, and update `ticket:hi5e7nbr` with
evidence and critique dispositions before any closure claim.

Challenges:

- spec:core-and-playbooks-package-contract#ACC-002
- spec:core-and-playbooks-package-contract#ACC-007

## FIND-002: Evidence under-captures before-state observation

Severity: medium
Confidence: high
State: open

Observation:

The packet required before/after searches for optional playbook names and
hardcoded playbook paths. The evidence record summarized the procedure and
after-state, but did not preserve concrete before-state results or enough detail
to compare before and after without rerunning or inspecting the diff.

Why it matters:

The iteration used `observation-first` posture. Without concrete before-state
observations, the evidence is weaker than the packet contract requires.

Follow-up:

Amend `evidence:core-doctrine-playbook-decoupling-check` with concrete
before-state observations from the child output and diff/search reconstruction,
then cite the evidence from the ticket.

Challenges:

- spec:core-and-playbooks-package-contract#ACC-002
- spec:core-and-playbooks-package-contract#ACC-007

## FIND-003: Optional playbook shorthand is slightly unclear

Severity: low
Confidence: medium
State: open

Observation:

Several routing rows used shorthand like `optional loom-spike equivalent` and
`optional loom-codemap equivalent`.

Why it matters:

The intent is understandable, but clearer parallel phrasing reduces the chance a
future agent reads the optional playbook as a required core route.

Follow-up:

Prefer phrasing such as `optional loom-spike or equivalent exploration workflow`
or `optional loom-codemap or equivalent atlas workflow`.

Challenges:

None - not claim-specific.

# Evidence Reviewed

- `ticket:hi5e7nbr`
- Ralph packet `.loom/packets/ralph/20260507T215704Z-ticket-hi5e7nbr-iter-01.md`
- Evidence `.loom/evidence/20260507-core-doctrine-playbook-decoupling-check.md`
- `spec:core-and-playbooks-package-contract`, especially ticket-scoped ACC-002 and ACC-007
- `decision:0008`
- Scoped diff across 15 core skill files
- Parent rerun of targeted optional playbook searches in scoped core dirs
- `git diff --check` for scoped child files, which passed with no output

# Residual Risks

- This review does not cover package-root creation, public docs, manifests,
  examples, playbook fail-closed wording, or actual harness install behavior.
- Remaining root `skills/...` references will need migration-time reconciliation
  in later tickets.

# Required Follow-up

Resolve or disposition FIND-001, FIND-002, and FIND-003 in `ticket:hi5e7nbr`
before closure. No additional implementation critique is required unless the
follow-up edits materially change the scoped doctrine beyond the findings.

# Acceptance Recommendation

`blocker-disposition-needed`
