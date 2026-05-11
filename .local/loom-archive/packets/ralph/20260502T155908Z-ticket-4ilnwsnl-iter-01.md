---
id: packet:ralph-ticket-4ilnwsnl-20260502T155908Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:4ilnwsnl
mode: execution
change_class: protocol-authority
risk_class: high
style: snapshot-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-02T15:59:08Z
updated_at: 2026-05-02T16:04:48Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - ticket:4ilnwsnl
    - evidence:packet-frontmatter-grammar-validation
  paths:
    - skills/loom-records/references/frontmatter.md
    - skills/loom-records/references/packet-frontmatter.md
    - skills/loom-records/SKILL.md
    - skills/loom-ralph/references/packet-contract.md
    - skills/loom-ralph/templates/ralph-packet.md
    - skills/loom-critique/templates/critique-packet.md
    - skills/loom-wiki/templates/wiki-packet.md
    - .loom/tickets/20260502-4ilnwsnl-canonicalize-packet-frontmatter-grammar.md
    - .loom/evidence/packet-frontmatter-grammar-validation.md
parent_merge_scope:
  records:
    - ticket:4ilnwsnl
    - plan:skills-corpus-perfection-council-followup
    - initiative:skills-corpus-perfection-council-followup
  paths:
    - .loom/packets/ralph/20260502T155908Z-ticket-4ilnwsnl-iter-01.md
    - .loom/tickets/20260502-4ilnwsnl-canonicalize-packet-frontmatter-grammar.md
source_fingerprint:
  git_commit: 330a7b2d59c284e55b2fdbbd1e4649026cb253cf
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: 330a7b2d59c284e55b2fdbbd1e4649026cb253cf
  git_status_summary: clean
  compiled_from:
    - initiative:skills-corpus-perfection-council-followup
    - plan:skills-corpus-perfection-council-followup
    - ticket:4ilnwsnl
execution_context:
  branch: main
  push_remote: origin
  worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
  isolation: none
  git_shared_metadata_mutations: forbidden
  destructive_commands: forbidden
context_budget:
  posture: normal
  max_source_files: 16
  max_excerpt_lines_per_file: 220
  avoid_full_file_reads: false
sources:
  initiative:
    - initiative:skills-corpus-perfection-council-followup
  plan:
    - plan:skills-corpus-perfection-council-followup
  ticket:
    - ticket:4ilnwsnl
  dependency:
    - ticket:3twzep5n
links: {}
---

# Mission

Create one canonical shared packet-frontmatter grammar and align Ralph, critique,
and wiki packet references/templates to it without making packets canonical truth
owners or making critique/wiki packets Ralph-governed.

# Bound Context

Governing objective:

- `initiative:skills-corpus-perfection-council-followup#OBJ-002`: Packet
  frontmatter grammar has one canonical shared reference and Ralph, critique, and
  wiki packet templates align with it.

Governing ticket:

- `ticket:4ilnwsnl` owns this live execution step.

Council finding:

- `COUNCIL-FIND-002` found packet frontmatter grammar distributed across
  `loom-records`, `loom-ralph`, `loom-critique`, and `loom-wiki` rather than
  owned by one shared record-grammar surface.

# Source Snapshot

- Branch: `main`
- Source commit: `330a7b2d59c284e55b2fdbbd1e4649026cb253cf`
- Status at compile time: clean before this packet/ticket update
- Latest pushed baseline: `330a7b2 docs: normalize critique disposition grammar`

# Change Class

`protocol-authority`, high risk. Packet frontmatter controls fresh-context
authority, child write boundaries, and parent reconciliation.

# Verification Targets

- `ticket:4ilnwsnl#ACC-001` through `ticket:4ilnwsnl#ACC-005`
- `initiative:skills-corpus-perfection-council-followup#OBJ-002`

# Task For This Iteration

Implement the smallest coherent shared packet-frontmatter grammar pass.

Required outcome:

- Add `skills/loom-records/references/packet-frontmatter.md` or an equally clear
  shared record-grammar reference.
- Update `skills/loom-records/references/frontmatter.md` and/or
  `skills/loom-records/SKILL.md` to route packet frontmatter questions to the new
  shared grammar.
- Update `skills/loom-ralph/references/packet-contract.md` so it cites the shared
  grammar for frontmatter and keeps Ralph-specific contract guidance in Ralph.
- Align these templates with the shared field set and valid values:
  `skills/loom-ralph/templates/ralph-packet.md`,
  `skills/loom-critique/templates/critique-packet.md`, and
  `skills/loom-wiki/templates/wiki-packet.md`.
- Preserve packet truth boundary: packets are durable support contracts, not
  canonical owner layers.
- Preserve sibling route boundary: critique/wiki packets reuse packet discipline,
  but are owned by critique/wiki workflows rather than Ralph.
- Create `.loom/evidence/packet-frontmatter-grammar-validation.md` with
  structural validation outputs and limitations.
- Update `ticket:4ilnwsnl` to `review_required` after child work because oracle
  critique remains mandatory.

# Verification Posture

Observation-first structural validation.

Run:

- `git diff --check`
- targeted searches for `packet_kind`, `child_write_scope`, `parent_merge_scope`,
  `source_fingerprint`, `execution_context`, `context_budget`,
  `verification_posture`, `mode:`, `style:`, and packet template frontmatter
- manual comparison of Ralph/critique/wiki packet templates against the new
  shared grammar

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- a runtime validator or hidden CLI seems necessary;
- the edit would make packets canonical truth owners;
- critique/wiki packet wording would make those packets Ralph-governed;
- the change requires broad support artifact grammar beyond packet frontmatter
  owned by `ticket:lqiw3hvp`.

# Output Contract

Return outcome, changed files and records, packet grammar decisions, validation
commands/searches and outcomes, evidence record created, ticket status
recommendation, blockers/residual risks, and whether mandatory oracle critique
can proceed.

# Working Notes

Keep shared grammar in `loom-records`; keep workflow-specific procedure in the
workflow skill. Avoid duplicated long field definitions in several places.

# Child Output

Outcome: `stop`.

Changed files:

- `skills/loom-records/references/packet-frontmatter.md`
- `skills/loom-records/references/frontmatter.md`
- `skills/loom-records/SKILL.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `skills/loom-critique/templates/critique-packet.md`
- `skills/loom-wiki/templates/wiki-packet.md`
- `.loom/evidence/packet-frontmatter-grammar-validation.md`
- `.loom/tickets/20260502-4ilnwsnl-canonicalize-packet-frontmatter-grammar.md`

Packet grammar decisions reported by child:

- packets remain support artifacts, not canonical truth owners;
- shared packet fields cover `packet_kind`, `mode`, `style`, scopes,
  fingerprint, execution context, context budget, sources, and links;
- `verification_posture` is Ralph-only for implementation packets;
- critique/wiki packets reuse packet discipline without becoming Ralph-governed;
- `mode` values align as `execution`, `review`, and `synthesis`.

Validation reported by child:

- `git diff --check` passed with no output;
- new grammar/evidence whitespace checks passed with no output;
- targeted field searches passed;
- manual comparison of Ralph/critique/wiki packet templates against shared
  grammar passed.

Ticket recommendation: `review_required`; mandatory oracle critique can proceed.

# Parent Merge Notes

Accepted for mandatory oracle critique. Parent consumed this packet after child
output.
