---
id: packet:ralph-ticket-gitstat26-20260503T075047Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:gitstat26
mode: execution
change_class: protocol-authority
risk_class: high
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-03T07:50:47Z
updated_at: 2026-05-03T07:54:00Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - None - child returns output only; parent reconciles ticket, evidence, critique, and packet status.
  paths:
    - skills/loom-records/references/packet-frontmatter.md
    - skills/loom-ralph/references/packet-contract.md
    - skills/loom-ralph/templates/ralph-packet.md
    - skills/loom-critique/templates/critique-packet.md
    - skills/loom-wiki/templates/wiki-packet.md
parent_merge_scope:
  records:
    - ticket:gitstat26
  paths:
    - .loom/tickets/20260503-gitstat26-add-machine-readable-dirty-state.md
    - .loom/evidence/20260503-git-dirty-state-fingerprint-validation.md
    - .loom/critique/git-dirty-state-fingerprint-review.md
    - .loom/packets/ralph/20260503T075047Z-ticket-gitstat26-iter-01.md
source_fingerprint:
  git_commit: 110728f57e570bc047b828e0d5158bf641fb9c87
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: 110728f57e570bc047b828e0d5158bf641fb9c87
  git_status_summary: dirty
  git_status_detail: parent-owned ticket and packet records are modified/untracked for launch; child write-scope files are clean relative to 110728f
  compiled_from:
    - ticket:gitstat26
    - ticket:netgate25
    - plan:skills-corpus-context-integrity-hardening-pass
    - initiative:skills-corpus-context-integrity-hardening-pass
    - research:skills-corpus-third-pass-follow-up-validation
execution_context:
  branch: main
  push_remote: origin
  worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
  isolation: none
  git_shared_metadata_mutations: forbidden
  destructive_commands: forbidden
  network: forbidden
context_budget:
  posture: normal
  max_source_files: 8
  max_excerpt_lines_per_file: 180
  avoid_full_file_reads: true
sources:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-third-pass-follow-up-validation
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  ticket:
    - ticket:gitstat26
    - ticket:netgate25
  files:
    - skills/loom-records/references/packet-frontmatter.md
    - skills/loom-ralph/references/packet-contract.md
    - skills/loom-ralph/templates/ralph-packet.md
    - skills/loom-critique/templates/critique-packet.md
    - skills/loom-wiki/templates/wiki-packet.md
links: {}
---

# Mission

Make packet Git dirty state machine-readable while preserving human-readable
status detail.

# Bound Context

`ticket:gitstat26` covers `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-027`.
Packet source fingerprints currently use broad `clean|dirty|unknown` values,
which hides whether tracked files, untracked files, or both caused the dirty
state. This matters because parent launch-freshness checks and child stop
conditions need a grep-friendly signal without introducing a Git helper runtime
or moving truth ownership into Git.

Frontmatter follows `skills/loom-records/references/packet-frontmatter.md`.
Ralph-specific obligations follow `skills/loom-ralph/references/packet-contract.md`.

# Source Snapshot

- `skills/loom-records/references/packet-frontmatter.md` currently documents
  `git_status_summary: <clean|dirty|unknown>` in the common packet shape and in
  the source fingerprint section.
- `skills/loom-ralph/references/packet-contract.md` repeats the same broad
  `clean|dirty|unknown` grammar for Ralph packets.
- Ralph, critique, and wiki packet templates all use
  `git_status_summary: <clean|dirty|unknown>` and keep `git_status_detail` for
  short human detail or `unknown - rationale`.
- `ticket:gitstat26` requires preserving `clean` and `unknown` with rationale
  while adding dirty categories such as `dirty_tracked`, `dirty_untracked`, and
  `dirty_mixed`.

# Change Class

Declared as `protocol-authority` with high risk. The edit changes launch-safety
fingerprint grammar and must stay Markdown-native: no runtime, schema engine,
validator, command wrapper, generated index, or new owner layer.

# Verification Targets

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-027`
- `ticket:gitstat26#ACC-001`
- `ticket:gitstat26#ACC-002`
- `ticket:gitstat26#ACC-003`
- `ticket:gitstat26#ACC-004`

# Task For This Iteration

Make the smallest coherent dirty-state grammar edit:

1. Add or clarify machine-readable `git_status_summary` values that distinguish
   `dirty_tracked`, `dirty_untracked`, and `dirty_mixed`.
2. Preserve `clean` and `unknown`, with `unknown - <rationale>` or equivalent
   rationale guidance when the parent cannot inspect status safely.
3. Preserve `git_status_detail` as the place for short human-readable status
   detail, examples, or unknown rationale.
4. Update Ralph, critique, and wiki packet templates if needed so copied packets
   use the revised grammar.
5. Keep Git as provenance/freshness metadata only; do not make Git the truth owner
   for acceptance, evidence, critique, or ticket state.
6. Do not add a Git helper runtime, validator, schema engine, command wrapper,
   generated index, hidden helper, or new owner layer.

# Verification Posture

Observation-first. Before and after editing, report targeted observations for:

- where `clean|dirty|unknown` currently appears in packet fingerprint guidance
  and templates;
- where the revised machine-readable dirty categories appear afterward;
- whether `clean` and `unknown` remain available with rationale guidance;
- whether `git_status_detail` remains available for human context;
- absence of runtime/helper/schema/validator/command-wrapper/new-owner-layer
  requirements.

Run `git diff --check` after editing.

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- satisfying the ticket would require runtime Git inspection, a validator, a
  schema engine, a command wrapper, generated files, or a new owner layer;
- the guidance would make Git status authoritative over ticket acceptance,
  evidence, or critique;
- governing records or child-write-scope files have materially changed from the
  source fingerprint;
- the desired grammar cannot preserve both machine-readable summary and
  human-readable detail.

Do not run `git fetch`, remote edits, Git config edits, destructive commands, or
shared Git metadata mutations. Do not edit parent-owned `.loom` records.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
`git diff --check` result, self-review, blockers/residual risks, and recommended
ticket state/next route.

# Working Notes

Parent compiled from clean `main` at `110728f` after closing and pushing
`ticket:netgate25`. Saving this packet and activating the ticket made the
worktree dirty before child launch; those parent-owned `.loom` records are outside
child write scope. The product files in `child_write_scope.paths` remain clean
relative to `110728f` at launch.

# Child Output

Outcome: `stop`

Files changed:

- `skills/loom-records/references/packet-frontmatter.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `skills/loom-critique/templates/critique-packet.md`
- `skills/loom-wiki/templates/wiki-packet.md`

Records changed by child:

- None. Parent retained ticket, evidence, critique, and packet reconciliation.

Observed result:

- Before: scoped files had no local diffs/status.
- Before: `clean|dirty|unknown` appeared in packet fingerprint guidance/templates
  at `skills/loom-records/references/packet-frontmatter.md`,
  `skills/loom-ralph/references/packet-contract.md`,
  `skills/loom-ralph/templates/ralph-packet.md`,
  `skills/loom-critique/templates/critique-packet.md`, and
  `skills/loom-wiki/templates/wiki-packet.md`.
- After: revised machine-readable categories appear in all five scoped packet
  guidance/template surfaces: `dirty_tracked`, `dirty_untracked`, and
  `dirty_mixed`.
- After: `clean` and `unknown` remain valid summary values.
- After: `unknown - <rationale>` guidance remains in `git_status_detail`, and
  added prose says `unknown` is only for unsafe or untruthful status inspection.
- After: `git_status_detail` remains the human-readable detail/rationale field in
  all templates and references.
- After: no runtime/helper/schema/validator/command-wrapper/generated-index or
  new-owner-layer requirement was added; changes are Markdown guidance/template
  only.

Verification:

- `git diff --check` passed with no output.

Self-review:

- Stayed inside `child_write_scope.paths`.
- Did not modify `.loom` records.
- Preserved Git as provenance/freshness metadata, not ticket/evidence/critique
  authority.
- Updated directly related Ralph, critique, and wiki packet templates.

Blockers or residual risks:

- No blockers.
- Historical `.loom` packets still contain legacy `clean|dirty|unknown` values,
  but they are outside this ticket's child write scope.

Recommendation:

- Move `ticket:gitstat26` to mandatory critique.

# Parent Merge Notes

- 2026-05-03T07:54:00Z: Parent accepted the bounded implementation output,
  recorded `evidence:git-dirty-state-fingerprint-validation`, marked this packet
  `consumed`, and moved `ticket:gitstat26` to `review_required` for mandatory
  critique.
