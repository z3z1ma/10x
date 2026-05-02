---
id: packet:ralph-ticket-revtgt7x-20260502T202813Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:revtgt7x
mode: execution
change_class: record-hygiene
style: reference-first
verification_posture: observation-first
iteration: 2
created_at: 2026-05-02T20:28:13Z
updated_at: 2026-05-02T20:32:53Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - ticket:revtgt7x
    - evidence:review-target-shape-validation
    - packet:ralph-ticket-revtgt7x-20260502T202813Z
  paths:
    - skills/loom-records/references/packet-frontmatter.md
    - skills/loom-critique/templates/critique-packet.md
    - .loom/tickets/20260502-revtgt7x-canonicalize-review-target-shape.md
    - .loom/evidence/20260502-review-target-shape-validation.md
    - .loom/packets/ralph/20260502T202813Z-ticket-revtgt7x-iter-02.md
parent_merge_scope:
  records:
    - ticket:revtgt7x
    - evidence:review-target-shape-validation
    - packet:ralph-ticket-revtgt7x-20260502T202813Z
  paths:
    - .loom/critique/review-target-shape-rereview.md
source_fingerprint:
  git_commit: b7c076f5105c2c241ac3b7ec932eb6f8a165c86f
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: b7c076f5105c2c241ac3b7ec932eb6f8a165c86f
  git_status_summary: dirty
  compiled_from:
    - initiative:skills-corpus-council-precision-pass
    - plan:skills-corpus-council-precision-pass
    - ticket:revtgt7x
    - critique:review-target-shape-review
    - evidence:review-target-shape-validation
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
  max_excerpt_lines_per_file: 140
  avoid_full_file_reads: true
sources:
  constitution:
    - constitution:main
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:revtgt7x
  critique:
    - critique:review-target-shape-review
  evidence:
    - evidence:review-target-shape-validation
  references:
    - skills/loom-records/references/packet-frontmatter.md
    - skills/loom-critique/templates/critique-packet.md
links:
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:revtgt7x
  critique:
    - critique:review-target-shape-review
---

# Mission

Resolve `critique:review-target-shape-review#REVTGT7X-CRIT-001` without
normalizing historical critique packets or adding validation runtime.

# Bound Context

This is the second Ralph iteration for `ticket:revtgt7x`. The first iteration
made the direct critique record shape scalar and the critique packet shape
structured. Mandatory oracle critique found that the new wording reads as if all
existing critique packets must have the new `summary`, `ref`, and `paths` fields,
which would make older consumed critique packets look invalid.

# Source Snapshot

The current diff is dirty from the first implementation, parent packet
reconciliation, and `critique:review-target-shape-review`. Baseline commit is
`b7c076f5105c2c241ac3b7ec932eb6f8a165c86f`.

Known older consumed critique packets that use legacy `review_target` shape:

- `.loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md`
- `.loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md`

# Change Class

Declared as `record-hygiene`; repair should clarify grammar and compatibility
without changing critique ownership.

# Verification Targets

- `ticket:revtgt7x#ACC-001`
- `ticket:revtgt7x#ACC-003`
- `ticket:revtgt7x#ACC-004`
- `critique:review-target-shape-review#REVTGT7X-CRIT-001`

# Task For This Iteration

1. Add a concise legacy compatibility boundary to the critique-packet
   `review_target` grammar so the current template shape applies to new/current
   critique packets while older consumed packets with `kind` plus `diff` remain
   understandable as legacy compatibility.
2. Prefer the smallest product-surface edit. Do not bulk-normalize historical
   critique packets unless the compatibility note proves insufficient.
3. If needed for operator clarity, add a short note to the critique packet
   template that the template describes new packet authoring.
4. Refresh `evidence:review-target-shape-validation` with after-repair searches,
   including a targeted search of historical critique packet `review_target`
   shapes and `git diff --check`.
5. Update `ticket:revtgt7x` to `review_required` with the finding disposition
   pending re-critique and next route set to mandatory oracle re-critique. Do not
   close the ticket.

# Verification Posture

`observation-first`.

Record the targeted before/after or after-repair observations for the legacy
compatibility wording and historical critique packets, plus `git diff --check`.

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- resolving the finding requires a migration of historical critique packets;
- resolving the finding would add schema validation or a parser;
- resolving the finding would change critique ownership or packet authority;
- the repair reveals broader packet grammar incompatibility outside the ticket.

# Output Contract

Return outcome, files changed, records changed, exact repair choice, validation
commands/results, risks, and ticket recommendation. Include whether the ticket
should proceed to mandatory oracle re-critique profiles `records-grammar` and
`operator-clarity`.

# Working Notes

Parent recorded first critique in `.loom/critique/review-target-shape-review.md`.

# Child Output

Outcome: `stop`

Files changed:

- `skills/loom-records/references/packet-frontmatter.md`
- `skills/loom-critique/templates/critique-packet.md`
- `.loom/evidence/20260502-review-target-shape-validation.md`
- `.loom/tickets/20260502-revtgt7x-canonicalize-review-target-shape.md`
- `.loom/packets/ralph/20260502T202813Z-ticket-revtgt7x-iter-02.md`

Records changed:

- `evidence:review-target-shape-validation`
- `ticket:revtgt7x`
- `packet:ralph-ticket-revtgt7x-20260502T202813Z`

Exact repair choice:

- Added a scoped legacy compatibility boundary in
  `skills/loom-records/references/packet-frontmatter.md`: newly compiled
  critique packets require `kind` plus `summary`, while older consumed critique
  packets with only `kind` plus `diff` are understandable legacy support
  artifacts and do not need retroactive migration solely for that shape.
- Added a short template note that
  `skills/loom-critique/templates/critique-packet.md` describes new critique
  packet authoring and points legacy compatibility to the packet-frontmatter
  reference.
- Did not normalize historical critique packets and did not add a parser,
  schema, or runtime.

Validation commands/results:

- `rg -n "review_target|legacy|newly compiled|new critique packet authoring" "skills/loom-records/references/packet-frontmatter.md" "skills/loom-critique/templates/critique-packet.md"`
  - Found current authoring wording at `packet-frontmatter.md:131`, legacy
    compatibility wording at `packet-frontmatter.md:137-140`, and template
    new-authoring note at `critique-packet.md:71-72`.
- `rg -n -C 4 "review_target:|kind:|diff:|summary:|ref:|paths:" ".loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md" ".loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md"`
  - Confirmed both targeted historical critique packets are `status: consumed`
    and use legacy `review_target` mappings with `kind: code_change` plus
    `diff` only.
- `git diff --check`
  - No output; command exited successfully.

Residual risks:

- Mandatory oracle re-critique has not yet run, so `ticket:revtgt7x#ACC-005`
  remains open.
- The ticket still names `records-grammar` as a required profile even though the
  prior critique noted it is not a separately named profile in
  `skills/loom-critique/references/critique-lens.md`; this repair did not widen
  scope to address that naming issue.

Ticket recommendation:

- Keep `ticket:revtgt7x` in `review_required`.
- Proceed to mandatory oracle re-critique with profiles `records-grammar` and
  `operator-clarity`.

# Parent Merge Notes

Parent accepted the bounded repair for critique handoff. The repair stayed within
scope by documenting legacy compatibility for older consumed critique packets,
refreshing evidence, and leaving `ticket:revtgt7x` in `review_required` for
mandatory oracle re-critique.
