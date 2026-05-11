---
id: packet:ralph-ticket-sibpkt7-20260502T230712Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:sibpkt7
mode: execution
change_class: protocol-authority
risk_class: medium
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-02T23:07:12Z
updated_at: 2026-05-02T23:15:30Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - ticket:sibpkt7
    - evidence:sibling-packet-ticket-anchor-validation
    - packet:ralph-ticket-sibpkt7-20260502T230712Z
  paths:
    - skills/loom-critique/templates/critique-packet.md
    - skills/loom-wiki/templates/wiki-packet.md
    - .loom/tickets/20260502-sibpkt7-make-sibling-packet-ticket-anchors-optional.md
    - .loom/evidence/20260502-sibling-packet-ticket-anchor-validation.md
    - .loom/packets/ralph/20260502T230712Z-ticket-sibpkt7-iter-01.md
parent_merge_scope:
  records:
    - ticket:sibpkt7
    - evidence:sibling-packet-ticket-anchor-validation
    - packet:ralph-ticket-sibpkt7-20260502T230712Z
  paths:
    - skills/loom-critique/templates/critique-packet.md
    - skills/loom-wiki/templates/wiki-packet.md
    - .loom/tickets/20260502-sibpkt7-make-sibling-packet-ticket-anchors-optional.md
    - .loom/evidence/20260502-sibling-packet-ticket-anchor-validation.md
    - .loom/packets/ralph/20260502T230712Z-ticket-sibpkt7-iter-01.md
source_fingerprint:
  git_commit: 4dde3b78a6f032e95a21fc03847d7a403923c42a
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: 4dde3b78a6f032e95a21fc03847d7a403923c42a
  git_status_summary: clean
  compiled_from:
    - initiative:skills-corpus-template-grammar-safety-pass
    - plan:skills-corpus-template-grammar-safety-pass
    - ticket:sibpkt7
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
  max_source_files: 6
  max_excerpt_lines_per_file: 160
  avoid_full_file_reads: false
sources:
  initiative:
    - initiative:skills-corpus-template-grammar-safety-pass
  plan:
    - plan:skills-corpus-template-grammar-safety-pass
  ticket:
    - ticket:sibpkt7
  records:
    - skills/loom-critique/templates/critique-packet.md
    - skills/loom-wiki/templates/wiki-packet.md
    - skills/loom-critique/SKILL.md
    - skills/loom-wiki/SKILL.md
    - skills/loom-records/references/packet-frontmatter.md
links:
  ticket:
    - ticket:sibpkt7
---

# Mission

Make critique and wiki packet templates safe for non-ticket-centered targets by
making ticket anchors optional and explicit.

# Bound Context

This is the seventh ticket in `plan:skills-corpus-template-grammar-safety-pass`
and covers `initiative:skills-corpus-template-grammar-safety-pass#OBJ-007`.
Critique and wiki are sibling workflows. Their packets may target records, pages,
diffs, source sets, or accepted explanation without a ticket owning the immediate
target. Tickets still own live execution state when a ticket exists.

# Source Snapshot

Baseline commit: `4dde3b78a6f032e95a21fc03847d7a403923c42a`, matching
`origin/main`. Worktree was clean before packet creation.

Parent before-state search found:

- `skills/loom-critique/templates/critique-packet.md:6` sets `target:
  ticket:<token>`.
- `skills/loom-critique/templates/critique-packet.md:30-37` includes
  `parent_merge_scope` with `ticket:<token>` and comments for `None - <rationale>`.
- `skills/loom-wiki/templates/wiki-packet.md:20-27` includes
  `parent_merge_scope` with `ticket:<token>` and comments for `None - <rationale>`.
- Both templates already say critique/wiki packets are not Ralph-governed.

# Change Class

Declared as `protocol-authority`; risk is medium because sibling packet templates
can accidentally make tickets mandatory where critique or wiki truth is centered
elsewhere.

# Verification Targets

- `initiative:skills-corpus-template-grammar-safety-pass#OBJ-007`
- `ticket:sibpkt7#ACC-001`
- `ticket:sibpkt7#ACC-002`
- `ticket:sibpkt7#ACC-003`
- `ticket:sibpkt7#ACC-004`

# Task For This Iteration

1. Capture before-state searches for ticket refs, `None - rationale`,
   `parent_merge_scope`, critique/wiki packet targets, and Ralph-governed wording
   in the targeted critique/wiki packet templates.
2. Update `skills/loom-critique/templates/critique-packet.md` so critique packets
   support non-ticket review targets while preserving ticket-centered examples
   where tickets are real review targets.
3. Update `skills/loom-wiki/templates/wiki-packet.md` so wiki packets support
   non-ticket synthesis targets while preserving ticket-centered reconciliation
   where a ticket actually owns follow-through.
4. Make absent ticket refs and absent parent merge targets explicit with `None -
   <rationale>` examples where appropriate.
5. Keep critique/wiki packet discipline separate from Ralph; do not add Ralph
   `verification_posture` or implementation-loop obligations to sibling packets.
6. Update `ticket:sibpkt7` to `review_required` with evidence linked, claim
   matrix current, and next route `critique`.
7. Record `evidence:sibling-packet-ticket-anchor-validation` with before/after
   searches and `git diff --check`.
8. Fill this packet's `# Child Output`. The parent will mark the packet consumed
   after reconciliation.

# Verification Posture

`observation-first`.

Capture before/after searches for the sibling packet ticket-anchor terms above.
Run `git diff --check` after edits.

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- the fix would remove ticket links where tickets actually own execution;
- the fix would make critique/wiki packets canonical owner layers;
- the fix would make critique/wiki packets Ralph-governed or add Ralph
  `verification_posture` to them;
- the fix would require broader packet-frontmatter redesign outside the targeted
  templates;
- the fix would add validators, automation, schema enforcement, command wrappers,
  runtime requirements, hidden helpers, or a new owner layer;
- the source fingerprint is materially stale before launch.

# Output Contract

Return outcome, files changed, records changed, before/after observation
commands/results, `git diff --check` result, residual risks, self-review
concerns, and ticket recommendation. Include whether the ticket should proceed to
mandatory oracle critique with profiles `owner-boundary`, `records-grammar`, and
`operator-clarity`.

# Working Notes

Parent created this packet after confirming `ticket:accspec6` was closed and
pushed and the worktree was clean at the source fingerprint.

# Child Output

Outcome: `stop`.

Changed files / records:

- `skills/loom-critique/templates/critique-packet.md`
- `skills/loom-wiki/templates/wiki-packet.md`
- `.loom/tickets/20260502-sibpkt7-make-sibling-packet-ticket-anchors-optional.md`
- `.loom/evidence/20260502-sibling-packet-ticket-anchor-validation.md`
- `.loom/packets/ralph/20260502T230712Z-ticket-sibpkt7-iter-01.md`

Evidence gathered:

- Before-state searches showed critique `target: ticket:<token>` and critique/wiki
  `parent_merge_scope` examples directly carrying `ticket:<token>` while both
  templates already preserved non-Ralph wording.
- After-state searches show critique and wiki `target` placeholders now allow
  non-ticket targets, parent merge examples say ticket refs are used only when a
  ticket owns execution/follow-through, and `None - <rationale>` examples remain
  explicit for absent merge targets.
- Ralph-governed wording remains boundary-preserving: critique/wiki templates
  still say they do not use Ralph `verification_posture` and are not Ralph
  implementation packets.
- `git diff --check`: passed with no output.

Ticket recommendation:

- `ticket:sibpkt7` is updated to `review_required` with
  `evidence:sibling-packet-ticket-anchor-validation` linked.
- Claim matrix marks `OBJ-007` and `ACC-001` through `ACC-004` as
  `supported_pending_review`; `ACC-005` remains open pending mandatory oracle
  critique.
- Next route is `critique`.
- Recommended mandatory oracle critique profiles: `owner-boundary`,
  `records-grammar`, and `operator-clarity`.

Residual risks / self-review concerns:

- Validation is structural and observational only; no automated schema or runtime
  exists for these Markdown templates.
- The wording is intentionally concise and template-local; oracle critique should
  verify that operators will not misread the optional ticket examples as removing
  ticket reconciliation when a ticket actually owns execution.

# Parent Merge Notes

Parent accepted the child output as scoped and routed the ticket to mandatory
oracle critique. Parent reconciliation removed an obsolete ticket `Route:` line,
expanded ticket coverage to include ticket-local acceptance IDs, confirmed
`git diff --check` passes, and confirmed the evidence is sufficient for critique
routing.

Initial oracle critique found the packet's `parent_merge_scope.paths` was empty
and critique packet prose mentioned source sets without structured encoding
guidance. Parent resolved both by listing concrete parent-reconciled paths in
this packet and clarifying path-set review encoding in the critique packet
template.
