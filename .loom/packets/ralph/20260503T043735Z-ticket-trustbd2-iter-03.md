---
id: packet:ralph-ticket-trustbd2-20260503T043735Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:trustbd2
mode: execution
change_class: protocol-authority
risk_class: high
style: reference-first
verification_posture: observation-first
iteration: 3
created_at: 2026-05-03T04:37:35Z
updated_at: 2026-05-03T04:39:02Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - decision:0005
  paths:
    - claude-hooks/hooks.json
    - .loom/constitution/decisions/decision-0005-skill-packaged-bootstrap-doctrine.md
parent_merge_scope:
  records:
    - ticket:trustbd2
  paths:
    - .loom/tickets/20260503-trustbd2-add-trust-boundary-doctrine.md
    - .loom/evidence/20260503-trust-boundary-doctrine-validation.md
    - .loom/critique/trust-boundary-doctrine-review.md
    - .loom/packets/ralph/20260503T043735Z-ticket-trustbd2-iter-03.md
source_fingerprint:
  git_commit: fc29933b16d483abd6d376f0ea8563b7e3e62cba
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: fc29933b16d483abd6d376f0ea8563b7e3e62cba
  git_status_summary: dirty
  git_status_detail: dirty with trustbd2 implementation, evidence, ticket, and packets pending final repair
  compiled_from:
    - ticket:trustbd2
    - critique finding TRUSTBD2-ORC-004
    - critique finding TRUSTBD2-ORC-005
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
  max_source_files: 4
  max_excerpt_lines_per_file: 80
  avoid_full_file_reads: true
sources:
  ticket:
    - ticket:trustbd2
  critique_findings:
    - TRUSTBD2-ORC-004
    - TRUSTBD2-ORC-005
  files:
    - .claude-plugin/plugin.json
    - INSTALL.md
    - claude-hooks/hooks.json
    - .loom/constitution/decisions/decision-0005-skill-packaged-bootstrap-doctrine.md
links: {}
---

# Mission

Repair remaining `ticket:trustbd2` critique findings `TRUSTBD2-ORC-004` and
`TRUSTBD2-ORC-005`.

# Bound Context

The Claude plugin manifest declares `claude-hooks/hooks.json` as the hook config,
and `INSTALL.md` says that hook emits ordered `loom-bootstrap` references as
same-session `SessionStart` hook stdout. The hook still emits only references
`01` through `07`, while the mandatory bootstrap doctrine now includes
`08-trust-boundaries.md`. Critique also found `decision:0005` frontmatter
`updated_at` was stale after the decision mutation.

# Verification Targets

- `ticket:trustbd2#ACC-001`
- `ticket:trustbd2#ACC-002`
- `ticket:trustbd2#ACC-003`
- `ticket:trustbd2#ACC-004`

# Task For This Iteration

Make the smallest repair:

1. Update `claude-hooks/hooks.json` so SessionStart emits
   `08-trust-boundaries.md` after `07-validation-and-honesty.md`.
2. Update `decision:0005` `updated_at` to `2026-05-03T04:37:35Z`.

Do not edit evidence, ticket, critique, packet records, installer docs, plugin
manifest, or product doctrine. The parent will refresh evidence and ticket truth.

# Verification Posture

Observation-first. Report before/after observations for:

- Claude hook references `01` through `08`;
- `decision:0005` `updated_at` metadata;
- `git diff --check`.

# Stop Conditions

Stop if the repair would require changing Claude plugin mechanics beyond adding
the explicit reference hook or changing bootstrap doctrine content.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
`git diff --check` result, self-review, blockers/residual risks, and recommended
ticket state/next route.

# Working Notes

Parent compiled this packet after mandatory critique returned
`TRUSTBD2-ORC-004` and `TRUSTBD2-ORC-005`.

# Child Output

Outcome: stop - required repairs completed.

Files changed:

- `claude-hooks/hooks.json`
- `.loom/constitution/decisions/decision-0005-skill-packaged-bootstrap-doctrine.md`

Records changed:

- `decision:0005`

Before observations:

- Claude `SessionStart` hook emitted references `01` through `07`;
  `08-trust-boundaries.md` was absent.
- `decision:0005` frontmatter `updated_at` was `2026-04-26T06:35:59Z`.

After observations:

- Claude `SessionStart` hook emits references `01` through `08` in order, with
  `08-trust-boundaries.md` after `07-validation-and-honesty.md`.
- `decision:0005` frontmatter `updated_at` is `2026-05-03T04:37:35Z`.

Validation: child `git diff --check` passed with no output. Child also validated
hook JSON syntax successfully.

Self-review: no concerns; edits stayed inside the strict child write scope.

Blockers/residual risks: no child blockers. Parent still needs evidence refresh
and ticket/critique reconciliation.

Recommendation: keep ticket active during parent reconciliation; next route is
parent merge, evidence repair, then acceptance/critique disposition review.

# Parent Merge Notes

Accepted child output as in scope. Parent will refresh evidence for the Claude
hook preload surface and rerun mandatory critique.
