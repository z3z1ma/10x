---
id: initiative:skills-corpus-perfection-council-followup
kind: initiative
status: completed
created_at: 2026-05-02T15:25:50Z
updated_at: 2026-05-02T17:41:49Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  plan:
    - plan:skills-corpus-perfection-council-followup
  ticket:
    - ticket:3twzep5n
    - ticket:4ilnwsnl
    - ticket:lqiw3hvp
    - ticket:yk89awl5
    - ticket:u02z7o9j
    - ticket:9c2delu8
    - ticket:wfxfu4zp
  evidence:
    - evidence:skills-corpus-perfection-completion-validation
  critique:
    - critique:skills-corpus-perfection-completion-review
external_refs: {}
---

# Objective

Turn the council review of `README.md` and `skills/**` into a completed,
evidence-backed, critique-reviewed skills-corpus refinement pass that makes Loom
more precise, self-consistent, and operationally clear without adding runtime
creep, command-wrapper truth, or new canonical owner layers.

# Why Now

The previous sharpening pass completed major protocol improvements. The latest
council review found the next quality frontier: not missing doctrine, but grammar
drift at the seams between tickets, critique, packets, drive handoffs, workspace
support records, README public framing, and templates. These seams are where
fresh agents are most likely to guess.

# In Scope

- Normalize critique, ticket, and drive disposition vocabulary.
- Canonicalize packet frontmatter grammar and align packet templates.
- Resolve support artifact grammar for drive handoffs and workspace harness
  support records.
- Align README public framing with bootstrap authority.
- Clarify ticket-local acceptance IDs and route-neutral readiness guidance.
- Simplify `loom-drive` continuity/checkpoint/tranche vocabulary.
- Run the low-risk hygiene sweep identified by the council review.
- For each ticket, use Ralph with a fixer subagent, record evidence, run oracle
  critique, resolve findings, close truthfully, run retrospective disposition,
  and commit/push before moving to the next ticket.

# Out Of Scope

- Adding a hidden runtime, daemon, database, MCP dependency, required CLI, or
  command wrapper as protocol truth.
- Creating a new canonical owner layer.
- Treating examples, `.loom/`, `.opencode/`, or optional utilities as product
  truth for this pass except where records are updated to track work.
- Rewriting the entire corpus for style alone.
- Release packaging or PR creation unless separately requested.

# Success Metrics

- OBJ-001: Critique finding state, ticket critique disposition, and drive
  continuity wording no longer conflict or imply shadow acceptance ownership.
- OBJ-002: Packet frontmatter grammar has one canonical shared reference and
  Ralph, critique, and wiki packet templates align with it.
- OBJ-003: Drive handoff and workspace harness support artifacts have explicit
  non-canonical grammar, paths, lifecycle, and owner boundaries.
- OBJ-004: README public framing is as strict as bootstrap on workflow skills,
  packets, ledgers, and bounded implementation routing.
- OBJ-005: Ticket-local `ACC-*` references and route-neutral readiness are clear
  enough for evidence, critique, and fresh agents to cite without guessing.
- OBJ-006: `loom-drive` uses a smaller, coherent continuity vocabulary while
  preserving checkpoint safety and parent-loop autonomy.
- OBJ-007: The hygiene findings are resolved: `OBJ-*` query coverage, tree
  diagrams, memory status examples, template headings, `external_refs`, research
  link verbs, and install-safe template-copy wording.
- OBJ-008: Every child ticket is closed with evidence, oracle critique, explicit
  retrospective disposition, semantic commit, and push.

# Milestones

- Milestone 1: Owner records and seven tickets exist with dependencies and
  acceptance criteria.
- Milestone 2: Shared grammar tickets close first, so later public framing and
  drive simplification inherit settled terms.
- Milestone 3: README/ticket/drive refinements close after the shared grammar
  base is stable.
- Milestone 4: Hygiene sweep and final plan/initiative acceptance close the pass.

# Dependencies

- Depends on the council review returned in task session
  `ses_216cb35c0ffeL3CpfPWKSfxLIO`.
- Uses the completed baseline from
  `plan:skills-corpus-protocol-sharpening` at commit
  `924b63d5cde499cc869a40ddc4f0c9a0772e23fe`.

# Risks

- Protocol-authority changes can introduce more drift while trying to remove it.
- Drive simplification can accidentally remove safety gates if vocabulary is
  collapsed too aggressively.
- Template changes can train future agents more strongly than prose; they need
  critique even when small.
- Low-risk hygiene can hide behavior changes if batched too broadly.

# Linked Work

- Plan: `plan:skills-corpus-perfection-council-followup`
- Tickets: `ticket:3twzep5n`, `ticket:4ilnwsnl`, `ticket:lqiw3hvp`,
  `ticket:yk89awl5`, `ticket:u02z7o9j`, `ticket:9c2delu8`,
  `ticket:wfxfu4zp`

# Status Summary

Completed. The council review was decomposed into seven Ralph-sized tickets, each
closed with evidence, oracle critique, retrospective disposition, semantic commit,
and push. Completion evidence and oracle completion critique support the final
acceptance decision.

# Completion Basis

Completed at: 2026-05-02T17:41:49Z

Success metric coverage:

- OBJ-001: supported by `ticket:3twzep5n`,
  `evidence:disposition-acceptance-vocabulary-validation`,
  `critique:disposition-acceptance-vocabulary-review`, and completion critique
  repair of critique-owned finding-state wording.
- OBJ-002: supported by `ticket:4ilnwsnl`,
  `evidence:packet-frontmatter-grammar-validation`, and
  `critique:packet-frontmatter-grammar-review`.
- OBJ-003: supported by `ticket:lqiw3hvp`,
  `evidence:support-artifact-grammar-validation`, and
  `critique:support-artifact-grammar-review`.
- OBJ-004: supported by `ticket:yk89awl5`,
  `evidence:readme-bootstrap-authority-validation`, and
  `critique:readme-bootstrap-authority-review`.
- OBJ-005: supported by `ticket:u02z7o9j`,
  `evidence:ticket-local-acceptance-readiness-validation`, and
  `critique:ticket-local-acceptance-readiness-review`.
- OBJ-006: supported by `ticket:9c2delu8`,
  `evidence:drive-continuity-vocabulary-validation`, and
  `critique:drive-continuity-vocabulary-review`.
- OBJ-007: supported by `ticket:wfxfu4zp`,
  `evidence:corpus-hygiene-sweep-validation`, and
  `critique:corpus-hygiene-sweep-review`.
- OBJ-008: supported by all seven closed child tickets, their evidence and
  critique records, retrospective dispositions, pushed semantic commits, and
  `evidence:skills-corpus-perfection-completion-validation`.

Completion critique: `critique:skills-corpus-perfection-completion-review`
returned `pass` after two closure-readiness findings were resolved.

Accepted residual risks: validation and critique were structural/textual; there is
no automated schema or rendered-document validation for this Markdown corpus.

Follow-up tickets: none.
