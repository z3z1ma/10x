---
id: packet:ralph-ticket-trustbd2-20260503T044557Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:trustbd2
mode: execution
change_class: protocol-authority
risk_class: high
style: reference-first
verification_posture: observation-first
iteration: 4
created_at: 2026-05-03T04:45:57Z
updated_at: 2026-05-03T04:47:20Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records: []
  paths:
    - examples/adapters/claude-plugin-install/README.md
    - examples/adapters/codex-plugin-install/README.md
parent_merge_scope:
  records:
    - ticket:trustbd2
  paths:
    - .loom/tickets/20260503-trustbd2-add-trust-boundary-doctrine.md
    - .loom/evidence/20260503-trust-boundary-doctrine-validation.md
    - .loom/critique/trust-boundary-doctrine-review.md
    - .loom/packets/ralph/20260503T044557Z-ticket-trustbd2-iter-04.md
source_fingerprint:
  git_commit: fc29933b16d483abd6d376f0ea8563b7e3e62cba
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: fc29933b16d483abd6d376f0ea8563b7e3e62cba
  git_status_summary: dirty
  git_status_detail: dirty with trustbd2 implementation, evidence, ticket, and packets pending fixture wording repair
  compiled_from:
    - ticket:trustbd2
    - critique finding TRUSTBD2-ORC-006
execution_context:
  branch: main
  push_remote: origin
  worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
  isolation: none
  git_shared_metadata_mutations: forbidden
  destructive_commands: forbidden
  network: forbidden
context_budget:
  posture: tight
  max_source_files: 2
  max_excerpt_lines_per_file: 60
  avoid_full_file_reads: true
sources:
  ticket:
    - ticket:trustbd2
  critique_findings:
    - TRUSTBD2-ORC-006
  files:
    - examples/adapters/claude-plugin-install/README.md
    - examples/adapters/codex-plugin-install/README.md
links: {}
---

# Mission

Repair `ticket:trustbd2` critique finding `TRUSTBD2-ORC-006` in internal adapter
fixture docs.

# Bound Context

The mandatory bootstrap doctrine now includes `08-trust-boundaries.md`. Internal
adapter fixtures still say Claude/Codex probes emit or see "seven" bootstrap
references. Examples are not product truth, but this repository uses them as
review fixtures and they should not preserve stale bootstrap-count wording for
current adapter behavior.

# Verification Targets

- `ticket:trustbd2#ACC-001`
- `ticket:trustbd2#ACC-004`

# Task For This Iteration

Make the smallest fixture wording repair:

1. Update the Claude adapter fixture doc to avoid stale "seven" wording for the
   current ordered bootstrap references.
2. Update the Codex adapter fixture doc to avoid stale "seven" wording for the
   current ordered bootstrap references.

Prefer "current ordered" or "eight" where it reads naturally. Do not edit
historical `.loom` evidence, tickets, research, or wiki records that describe
past observations.

# Verification Posture

Observation-first. Report before/after observations for:

- targeted stale wording in the two fixture docs;
- `git diff --check`.

# Stop Conditions

Stop if the repair would require redesigning adapter examples or changing product
doctrine.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
`git diff --check` result, self-review, blockers/residual risks, and recommended
ticket state/next route.

# Working Notes

Parent compiled this packet after mandatory critique returned
`TRUSTBD2-ORC-006`.

# Child Output

Outcome: stop - repaired `TRUSTBD2-ORC-006` wording in both adapter fixture docs.

Files changed:

- `examples/adapters/claude-plugin-install/README.md`
- `examples/adapters/codex-plugin-install/README.md`

Records changed: none.

Before observations:

- Claude fixture README had stale "seven" wording in expected properties.
- Codex fixture README had stale "all seven" wording in expected properties.

After observations:

- Claude fixture README says "current ordered" bootstrap references.
- Codex fixture README says "current ordered" bootstrap references.
- Targeted search found no remaining "seven" wording in either fixture doc.

Validation: child `git diff --check` passed with no output.

Self-review: diff was limited to requested wording repair only.

Blockers/residual risks: none identified.

Recommendation: move to `review_required`; parent should reconcile evidence/ticket
and route to critique/acceptance disposition.

# Parent Merge Notes

Accepted child output as in scope. Parent made a formatting-only line wrap in the
same two fixture docs, then refreshed evidence and routed back to mandatory
critique.
