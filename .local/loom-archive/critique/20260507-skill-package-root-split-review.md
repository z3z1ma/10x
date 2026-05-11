---
id: critique:skill-package-root-split-review
kind: critique
status: final
created_at: 2026-05-07T22:17:35Z
updated_at: 2026-05-07T22:17:35Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:u9vtemj3 package-root skill split"
links:
  ticket:
    - ticket:u9vtemj3
  packet:
    - packet:ralph-ticket-u9vtemj3-20260507T220907Z
    - packet:ralph-ticket-u9vtemj3-20260507T221312Z
  evidence:
    - evidence:skill-package-root-split-check
  spec:
    - spec:core-and-playbooks-package-contract
  decision:
    - decision:0008
external_refs: {}
---

# Summary

Reviewed the physical split of the skill corpus into `loom-core/skills` and
`loom-playbooks/skills`, including moved skill membership, root `skills/`
retirement, playbook dependency wording, stale path cleanup, evidence, and Ralph
packet reconciliation state.

# Review Target

Direct implementation critique of `ticket:u9vtemj3`, Ralph packets
`packet:ralph-ticket-u9vtemj3-20260507T220907Z` and
`packet:ralph-ticket-u9vtemj3-20260507T221312Z`, evidence
`evidence:skill-package-root-split-check`, and source changes under
`loom-core/**`, `loom-playbooks/**`, and deleted root `skills/**`.

Profiles: `protocol-change`, `operator-surface`, and `code-structure`.

# Verdict

`changes_required`

The source layout split is structurally correct for the scoped ticket, but at
review time the ticket ledger, packet lifecycle, and evidence wording were not
truthful enough for closure.

# Findings

## FIND-001: Live ticket and packet lifecycle are stale

Severity: high
Confidence: high
State: open

Observation:

At review time, the ticket still said Ralph iteration 01 was being launched and
evidence was pending/none, while the evidence record said both packets had run
and passed. Both Ralph packets still had `status: compiled` with pending child
output.

Why it matters:

Tickets are the live execution ledger, and packet lifecycle status must be
truthful after child output is reconciled. Closing work without this reconciliation
would violate Loom's execution discipline.

Follow-up:

Update both packets with child output and parent merge notes, move them to
terminal lifecycle status, and update the ticket with evidence, critique, finding
dispositions, and acceptance truth.

Challenges:

- spec:core-and-playbooks-package-contract#ACC-001
- spec:core-and-playbooks-package-contract#ACC-002
- spec:core-and-playbooks-package-contract#ACC-003
- spec:core-and-playbooks-package-contract#ACC-007

## FIND-002: Evidence overstates `git diff --check` coverage

Severity: medium
Confidence: high
State: open

Observation:

The evidence record said `git diff --check -- loom-core loom-playbooks` validated
package-root whitespace, but new package-root files were untracked at review time,
so normal `git diff --check` did not check their contents.

Why it matters:

Evidence must distinguish observed checks from inferred checks. The source looked
clean under independent scan, but the record overstated which command proved that.

Follow-up:

Amend evidence to name the actual observed trailing-whitespace scan on package-root
Markdown files and separate it from tracked-deletion diff checks.

Challenges:

- spec:core-and-playbooks-package-contract#ACC-001
- spec:core-and-playbooks-package-contract#ACC-003

## FIND-003: Iteration 01 packet write scope over-granted package root authority

Severity: medium
Confidence: high
State: open

Observation:

The ticket expected child write scope to include `skills/**`, `loom-core/skills/**`,
and `loom-playbooks/skills/**`, while the iteration 01 packet granted
`loom-core/**` and `loom-playbooks/**`.

Why it matters:

The packet contract should fail closed. Even though source inspection found no
out-of-scope package metadata or manifest writes, the packet permitted more than
the ticket intended.

Follow-up:

Record the over-grant as ticket-owned accepted risk or resolution before closure,
with evidence that no out-of-scope files were changed and later packets use
narrower scopes.

Challenges:

- spec:core-and-playbooks-package-contract#ACC-003

# Evidence Reviewed

- `decision:0008`
- `spec:core-and-playbooks-package-contract#ACC-001`, `#ACC-002`, `#ACC-003`, and
  `#ACC-007`
- `ticket:u9vtemj3`
- Ralph packets for iterations 01 and 02
- `evidence:skill-package-root-split-check`
- Source tree membership under `loom-core/skills` and `loom-playbooks/skills`
- Root `skills/*/SKILL.md` absence
- Playbook dependency wording in playbook `SKILL.md` files
- Remaining `repo-root skills` mention in core as a negative warning
- Package-root path scans and diff checks

# Residual Risks

- Harness manifests, public docs, examples, package metadata, and runtime install
  behavior remain intentionally out of scope.
- New package-root files are untracked until staging/commit review happens.
- Full `spec:core-and-playbooks-package-contract#ACC-007` is not globally
  satisfied; this ticket covers only the moved skill corpus.

# Required Follow-up

Ticket closure requires ticket-owned dispositions for FIND-001, FIND-002, and
FIND-003 after evidence and packet reconciliation.

# Acceptance Recommendation

`blocker-disposition-needed`
