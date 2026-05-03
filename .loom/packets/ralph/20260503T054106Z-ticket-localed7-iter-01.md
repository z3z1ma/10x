---
id: packet:ralph-ticket-localed7-20260503T054106Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:localed7
mode: execution
change_class: protocol-authority
risk_class: medium
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-03T05:41:06Z
updated_at: 2026-05-03T05:43:08Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - None - child returns output only; parent reconciles ticket, evidence, critique, and packet status.
  paths:
    - skills/loom-workspace/references/routing.md
    - skills/loom-tickets/references/readiness.md
    - skills/loom-records/references/route-vocabulary.md
parent_merge_scope:
  records:
    - ticket:localed7
  paths:
    - .loom/tickets/20260503-localed7-define-local-edit-route.md
    - .loom/evidence/20260503-local-edit-route-validation.md
    - .loom/critique/local-edit-route-review.md
    - .loom/packets/ralph/20260503T054106Z-ticket-localed7-iter-01.md
source_fingerprint:
  git_commit: b4f205848f5c89b27653ec529b7acd6dc4ec12f6
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: b4f205848f5c89b27653ec529b7acd6dc4ec12f6
  git_status_summary: clean
  git_status_detail: clean working tree at packet compile time
  compiled_from:
    - ticket:localed7
    - plan:skills-corpus-context-integrity-hardening-pass
    - initiative:skills-corpus-context-integrity-hardening-pass
    - research:skills-corpus-context-integrity-hardening-review
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
  max_source_files: 5
  max_excerpt_lines_per_file: 160
  avoid_full_file_reads: true
sources:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-context-integrity-hardening-review
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  ticket:
    - ticket:localed7
  files:
    - skills/loom-workspace/references/routing.md
    - skills/loom-tickets/references/readiness.md
    - skills/loom-records/references/route-vocabulary.md
links: {}
---

# Mission

Define the cheap `local_edit` route for `ticket:localed7` so Loom can remain
lightweight without creating a bypass around ticket truth or Ralph for larger work.

# Bound Context

`local_edit` is already a route token and appears in ticket readiness examples,
but the corpus does not yet clearly say when it is appropriate, what ticket update
is required when a ticket owns the work, when evidence is needed, or when to
escalate to Ralph, spec, research, or critique. Keep it as routing guidance, not a
new skill, command, owner layer, or bypass mode.

# Verification Targets

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-008`
- `ticket:localed7#ACC-001`
- `ticket:localed7#ACC-002`
- `ticket:localed7#ACC-003`
- `ticket:localed7#ACC-004`

# Task For This Iteration

Make the smallest coherent local-edit route edits:

1. Define when `local_edit` is appropriate in shared route/workspace/ticket
   guidance.
2. State that local edit does not bypass ticket-owned live state when a ticket
   owns the work.
3. Name evidence conditions and escalation triggers for behavior, protocol,
   risky, ambiguous, or implementation-sized changes.
4. Do not create a `loom-local-edit` skill, new route owner layer, command wrapper,
   bypass mode, or replacement for Ralph on implementation-sized work.

# Verification Posture

Observation-first. Before and after editing, report targeted observations for:

- `local_edit` appropriateness and write-boundary wording;
- ticket-owned live-state requirement;
- evidence conditions;
- escalation to Ralph/spec/research/critique or other owner route;
- absence of `loom-local-edit`, bypass mode, new owner layer, command wrapper, or
  weakening of Ralph for implementation-sized work.

Run `git diff --check` after editing.

# Stop Conditions

Stop and report `blocked` or `escalate` if satisfying the ticket would require a
new skill, new owner layer, command wrapper, bypass mode, or replacing Ralph for
implementation-sized work.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
`git diff --check` result, self-review, blockers/residual risks, and recommended
ticket state/next route.

# Working Notes

Parent compiled from clean `main` at `b4f2058` after closing `ticket:reconchk`.
The parent normalized the ticket's existing `change_class` from invalid
`workflow-boundary` profile vocabulary to valid `protocol-authority` before
launch.

# Child Output

Outcome: stop - bounded `local_edit` route guidance completed within child write
scope.

Files changed:

- `skills/loom-workspace/references/routing.md`
- `skills/loom-tickets/references/readiness.md`
- `skills/loom-records/references/route-vocabulary.md`

Records changed: none.

Before observations:

- `local_edit` existed as a route token, but guidance only said "tiny, safe,
  in-context mutation" and "bounded edit and write boundary".
- Ticket-owned live state, evidence conditions, and escalation triggers were
  underdefined.
- No `loom-local-edit` skill, command wrapper, owner layer, bypass mode, or Ralph
  replacement existed.

After observations:

- Scoped references now define cheap, safe, current-context use and named write
  boundaries for `local_edit`.
- Ticket-owned live-state, acceptance, evidence, critique disposition, and next
  route requirements are explicit.
- Evidence expectations are proportional to the claim, with diff/text observation
  sufficient for structural cleanup and evidence/critique routes for behavior,
  validation, protocol-authority, or risky claims.
- Escalation to `ralph`, `spec`, `research`, `critique`, `evidence`, or another
  owner route is explicit when the work is too large, risky, ambiguous,
  behavior-defining, or missing evidence.
- New text explicitly forbids treating `local_edit` as a `loom-local-edit` skill,
  command wrapper, bypass mode, new owner layer, or Ralph replacement.

Validation: `git diff --check` passed with no output.

Self-review: edits are Markdown-only, stay inside child write scope, and keep
local edits under owner-record truth instead of creating a new workflow owner.

Blockers/residual risks: no blockers. Parent still needs evidence, mandatory
critique, and ticket-owned acceptance review.

Recommendation: `review_required`; next route is parent evidence recording, then
mandatory critique.

# Parent Merge Notes

Accepted child output as in scope. Parent recorded structural evidence in
`evidence:local-edit-route-validation` and routed to mandatory critique.
