---
id: packet:ralph-ticket-revtgt7x-20260502T201800Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:revtgt7x
mode: execution
change_class: record-hygiene
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-02T20:18:00Z
updated_at: 2026-05-02T20:23:00Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - ticket:revtgt7x
    - evidence:review-target-shape-validation
    - packet:ralph-ticket-revtgt7x-20260502T201800Z
  paths:
    - skills/loom-critique/templates/critique.md
    - skills/loom-critique/templates/critique-packet.md
    - skills/loom-critique/SKILL.md
    - skills/loom-critique/references/critique-lens.md
    - skills/loom-records/references/frontmatter.md
    - skills/loom-records/references/packet-frontmatter.md
    - .loom/tickets/20260502-revtgt7x-canonicalize-review-target-shape.md
    - .loom/evidence/20260502-review-target-shape-validation.md
    - .loom/packets/ralph/20260502T201800Z-ticket-revtgt7x-iter-01.md
parent_merge_scope:
  records:
    - ticket:revtgt7x
    - evidence:review-target-shape-validation
    - packet:ralph-ticket-revtgt7x-20260502T201800Z
  paths:
    - .loom/critique/review-target-shape-review.md
source_fingerprint:
  git_commit: b7c076f5105c2c241ac3b7ec932eb6f8a165c86f
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: b7c076f5105c2c241ac3b7ec932eb6f8a165c86f
  git_status_summary: clean
  compiled_from:
    - initiative:skills-corpus-council-precision-pass
    - plan:skills-corpus-council-precision-pass
    - ticket:revtgt7x
    - ticket:pktlife6
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
  max_source_files: 10
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
  references:
    - skills/loom-critique/templates/critique.md
    - skills/loom-critique/templates/critique-packet.md
    - skills/loom-records/references/frontmatter.md
    - skills/loom-records/references/packet-frontmatter.md
links:
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:revtgt7x
---

# Mission

Make `review_target` grammar explicit across critique records and critique
packets so authors know whether the field is scalar, structured, or an allowed
family-specific variant.

# Bound Context

This is the seventh ticket in `plan:skills-corpus-council-precision-pass` and
covers `initiative:skills-corpus-council-precision-pass#OBJ-007`. Dependency
`ticket:pktlife6` is closed. This is a record-hygiene change with mandatory oracle
critique by user instruction.

# Source Snapshot

Council finding `CR-007` observed `review_target` appears as a scalar in critique
records and a mapping in critique packets.

Current observations:

- `skills/loom-critique/templates/critique.md` uses scalar
  `review_target: <record ref | code change target>`.
- `skills/loom-critique/templates/critique-packet.md` uses mapping
  `review_target.kind` and `review_target.diff`.
- `skills/loom-records/references/frontmatter.md` only says critique records may
  add `review_target`.
- `skills/loom-records/references/packet-frontmatter.md` calls `review_target`
  critique-family grammar but does not fully contrast critique record and packet
  shapes.

# Change Class

Declared as `record-hygiene`; this normalizes record/template grammar without
changing critique ownership.

# Verification Targets

- `initiative:skills-corpus-council-precision-pass#OBJ-007`
- `ticket:revtgt7x#ACC-001`
- `ticket:revtgt7x#ACC-002`
- `ticket:revtgt7x#ACC-003`
- `ticket:revtgt7x#ACC-004`

# Task For This Iteration

1. Capture before-state `review_target` searches in critique templates and records
   frontmatter guidance.
2. Choose the smallest clear grammar: either one canonical shape, or two explicitly
   allowed variants for critique records versus critique packets.
3. Update critique record and critique packet templates plus frontmatter guidance
   so the chosen shape is explicit, grep-friendly, and human-readable.
4. Preserve direct artifact critique usability and packetized critique detail.
5. Create `.loom/evidence/20260502-review-target-shape-validation.md`.
6. Update `ticket:revtgt7x` to `review_required` with evidence, claim matrix,
   retrospective/promotion disposition pending, and critique-next recommendation.
   Do not close it.

# Verification Posture

`observation-first`.

Record before/after searches for `review_target`, `Review Target`, and
`review target`, plus `git diff --check`.

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- the fix would require bulk-normalizing historical critique records;
- the fix would add schema validation or a parser;
- the fix would change critique ownership or ticket acceptance rules;
- the fix would make direct artifact critique unnecessarily heavy.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
validation commands/results, risks, and ticket recommendation. Include whether
the ticket should proceed to mandatory oracle critique profiles:
`records-grammar` and `operator-clarity`.

# Working Notes

Parent compiled from clean `main` at `b7c076f5105c2c241ac3b7ec932eb6f8a165c86f`.

# Child Output

Outcome: `stop` — bounded implementation iteration completed and ticket moved to
`review_required` for mandatory critique.

Files changed:

- `skills/loom-critique/templates/critique.md`
- `skills/loom-critique/templates/critique-packet.md`
- `skills/loom-critique/SKILL.md`
- `skills/loom-critique/references/critique-lens.md`
- `skills/loom-records/references/frontmatter.md`
- `skills/loom-records/references/packet-frontmatter.md`
- `.loom/tickets/20260502-revtgt7x-canonicalize-review-target-shape.md`
- `.loom/evidence/20260502-review-target-shape-validation.md`
- `.loom/packets/ralph/20260502T201800Z-ticket-revtgt7x-iter-01.md`

Records changed:

- `ticket:revtgt7x` — status set to `review_required`, evidence linked, claim
  matrix updated for ACC-001 through ACC-004 as evidence-supported pending
  critique, ACC-005 left open, critique and retrospective/promotion dispositions
  left pending.
- `evidence:review-target-shape-validation` — records before/after
  `review_target`, `Review Target`, and `review target` searches plus
  `git diff --check` result.
- `packet:ralph-ticket-revtgt7x-20260502T201800Z` — child output appended; packet
  lifecycle remains parent-owned.

Before/after observations:

- Before: direct critique template used scalar `review_target`, critique packet
  template used structured `review_target`, and shared frontmatter guidance only
  said critique records may add `review_target` while packet frontmatter did not
  fully contrast record and packet shapes.
- After: direct critique records are documented as scalar, grep-friendly target
  handles; critique packets are documented as structured mappings with `kind`,
  `summary`, `ref`, `diff`, and optional `paths`; critique skill/lens guidance
  now names the family-specific distinction.

Validation:

- Ran required before/after search:
  `rg -n "review_target|Review Target|review target" ...` against critique
  templates, critique skill/lens guidance, and frontmatter references. Full
  output is recorded in `evidence:review-target-shape-validation`.
- Ran `git diff --check`; no output, command exited successfully.

Risks:

- No historical critique records were bulk-normalized.
- No schema validation or parser was added.
- Critique ownership and ticket acceptance rules were not changed.
- Mandatory oracle critique remains pending; this output does not close the
  ticket.

Recommended next route: mandatory oracle critique with profiles `records-grammar`
and `operator-clarity`.

# Parent Merge Notes

Parent accepted the bounded child output for critique handoff. Ticket
`ticket:revtgt7x` truthfully reflects `review_required`, links
`evidence:review-target-shape-validation`, and leaves acceptance/closure pending
mandatory oracle critique.
