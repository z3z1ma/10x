---
id: plan:skills-corpus-perfection-council-followup
kind: plan
status: active
created_at: 2026-05-02T15:25:50Z
updated_at: 2026-05-02T15:25:50Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-perfection-council-followup
  ticket:
    - ticket:3twzep5n
    - ticket:4ilnwsnl
    - ticket:lqiw3hvp
    - ticket:yk89awl5
    - ticket:u02z7o9j
    - ticket:9c2delu8
    - ticket:wfxfu4zp
external_refs: {}
---

# Purpose

Preserve the council review as an execution strategy and route each improvement
into a bounded Loom ticket. This plan exists so the refinement pass can proceed
without relying on transcript context, while keeping live state in tickets.

# Strategy

Work from shared protocol grammar outward:

1. Normalize the terms that govern closure and critique disposition.
2. Canonicalize packet frontmatter, because packets are copied by several
   workflows.
3. Clarify support artifact grammar before simplifying `loom-drive` surfaces.
4. Align public README framing after the underlying rules are tightened.
5. Clarify ticket-local acceptance and readiness once disposition grammar is
   settled.
6. Simplify `loom-drive` vocabulary after its support artifact and disposition
   boundaries are safe.
7. Run a final hygiene sweep for remaining low-risk consistency issues.

For each ticket:

- compile a Ralph packet;
- launch a `fixer` child worker;
- inspect and reconcile child output;
- record structural evidence;
- run `oracle` critique with the profiles named by the ticket;
- resolve all findings before closure;
- record retrospective disposition in the ticket and owner records if needed;
- commit and push with a semantic message before continuing.

# Strategy Snapshot

The council found no runtime creep and no deliberate new canonical-layer creep.
The main quality gap is cross-surface grammar drift. This plan should sharpen
shared terms and templates without expanding Loom's ontology.

# Council Findings Preserved

High-impact findings:

- COUNCIL-FIND-001: Critique finding state, ticket acceptance gate, and drive
  continuity vocabulary overlap without a single split between critique-owned
  finding state and ticket-owned acceptance disposition.
- COUNCIL-FIND-002: Packet frontmatter grammar is distributed across references
  and templates rather than owned by one shared record-grammar surface.
- COUNCIL-FIND-003: README wording is looser than bootstrap and can imply
  workflow skills create ledgers or that packets are the route owner.
- COUNCIL-FIND-004: Drive outer-loop handoff is a support artifact with
  frontmatter/status but lacks clear path, ID, kind, and lifecycle grammar.

Medium findings:

- COUNCIL-FIND-005: Some validation and repair recipes omit `OBJ-*` coverage.
- COUNCIL-FIND-006: Workspace harness template uses `kind: workspace-support`
  while naming grammar lists only `workspace` support shape.
- COUNCIL-FIND-007: Ticket-local acceptance criteria do not clearly show whether
  local `ACC-*` IDs should be used and cited.
- COUNCIL-FIND-008: Ticket template uses `# Ralph Readiness`, which biases all
  handoffs toward Ralph even when critique/wiki packet routes are siblings.
- COUNCIL-FIND-009: README/bootstrap/workspace `.loom/` tree diagrams differ in
  ordering and detail.
- COUNCIL-FIND-010: Some examples assume repo-root `skills/` template paths,
  which may not hold in installed harnesses.

Lower-risk hygiene findings:

- COUNCIL-FIND-011: `loom-drive` has overlapping checkpoint, snapshot, tranche,
  gap, route-exit, and resume terminology.
- COUNCIL-FIND-012: `# Non-goals` and `# Out Of Scope` headings differ across
  templates.
- COUNCIL-FIND-013: Memory entity example uses `inactive`, which is outside the
  recommended memory status vocabulary.
- COUNCIL-FIND-014: `external_refs: {}` is inconsistent across canonical
  templates.
- COUNCIL-FIND-015: Research references suggest ad hoc link verbs that are not
  standardized semantic link grammar.

# Workstreams

- Shared grammar: tickets `3twzep5n`, `4ilnwsnl`, `lqiw3hvp`.
- Public/operator framing: tickets `yk89awl5`, `u02z7o9j`.
- Drive simplification: ticket `9c2delu8`.
- Final hygiene: ticket `wfxfu4zp`.

# Milestones

- M1: Plan and tickets created.
- M2: Disposition and packet grammar normalized.
- M3: Support artifact grammar settled.
- M4: README and ticket readiness surfaces aligned.
- M5: Drive vocabulary simplified without losing checkpoint safety.
- M6: Hygiene sweep closed and initiative accepted.

# Sequencing

`ticket:3twzep5n` comes first because closure vocabulary affects later tickets'
acceptance sections and critique records.

`ticket:4ilnwsnl` comes second because packet grammar affects every Ralph,
critique, and wiki packet template.

`ticket:lqiw3hvp` comes third because support artifact grammar should be settled
before drive vocabulary is simplified.

`ticket:yk89awl5` and `ticket:u02z7o9j` depend on the first grammar decisions and
can run after those dependencies close.

`ticket:9c2delu8` depends on disposition and support artifact grammar.

`ticket:wfxfu4zp` runs last so the hygiene sweep can inherit final vocabulary and
avoid churn.

# Execution Waves

Wave 1:

- `ticket:3twzep5n`: normalize disposition and acceptance vocabulary.
- `ticket:4ilnwsnl`: canonicalize packet frontmatter grammar. Depends on none,
  but should run after `ticket:3twzep5n` for sequential review discipline.
- `ticket:lqiw3hvp`: resolve support artifact grammar. Should run after packet
  grammar is settled.

Wave 2:

- `ticket:yk89awl5`: align README with bootstrap authority. Depends on
  `ticket:3twzep5n`, `ticket:4ilnwsnl`, and `ticket:lqiw3hvp`.
- `ticket:u02z7o9j`: clarify ticket-local acceptance IDs and route-neutral
  readiness. Depends on `ticket:3twzep5n`.

Wave 3:

- `ticket:9c2delu8`: simplify drive continuity vocabulary. Depends on
  `ticket:3twzep5n` and `ticket:lqiw3hvp`.

Wave 4:

- `ticket:wfxfu4zp`: low-risk hygiene sweep. Depends on all prior tickets.

# Risks

- Over-normalization can make simple work feel bureaucratic.
- Adding a packet-frontmatter reference can duplicate existing Ralph contract
  guidance if it does not clearly own shared grammar only.
- Support artifact grammar can accidentally make handoffs look canonical.
- README edits can make marketing framing less vivid if they become too legalistic.
- Drive simplification can reduce restart safety if checkpoint semantics are
  collapsed incorrectly.

# Evidence Strategy

Each ticket should record structural evidence with the smallest honest checks:

- `git diff --check`;
- targeted `rg` queries for the terms being normalized;
- manual comparison of touched templates against owning references;
- ticket-specific before/after checks named in the ticket;
- no runtime tests unless a future ticket introduces executable behavior, which
  this plan should not do.

# Plan Readiness Review

Spec / acceptance coverage:

- No separate spec is needed. The initiative success metrics and ticket-local
  acceptance criteria are sufficient because this pass refines protocol surfaces
  rather than defining an externally consumed runtime behavior contract.

Placeholder scan:

- Each ticket must remove placeholders before becoming active. No product files
  may be left with council placeholder wording.

Ticket-sized slices:

- Seven slices match the council's proposed execution plan and keep grammar,
  support-surface, public-framing, drive-simplification, and hygiene concerns
  independently reviewable.

Likely write scopes:

- `ticket:3twzep5n`: `skills/loom-records`, `skills/loom-tickets`,
  `skills/loom-critique`, `skills/loom-drive`.
- `ticket:4ilnwsnl`: `skills/loom-records`, `skills/loom-ralph`,
  `skills/loom-critique`, `skills/loom-wiki`, packet templates.
- `ticket:lqiw3hvp`: `skills/loom-drive`, `skills/loom-workspace`,
  `skills/loom-records`.
- `ticket:yk89awl5`: `README.md`, possibly bootstrap references if alignment
  requires exact wording.
- `ticket:u02z7o9j`: `skills/loom-tickets`, `skills/loom-records`, affected
  templates.
- `ticket:9c2delu8`: `skills/loom-drive` references/templates.
- `ticket:wfxfu4zp`: targeted low-risk files named by council findings.

Likely verification posture:

- Observation-first structural validation for every ticket. `none` is not
  acceptable because protocol/operator guidance changes behavior.

Evidence and critique route:

- Mandatory critique for tickets `3twzep5n`, `4ilnwsnl`, `lqiw3hvp`, and
  `9c2delu8`.
- Recommended critique for tickets `yk89awl5`, `u02z7o9j`, and `wfxfu4zp`, but
  the user has required oracle critique for every ticket, so each ticket must
  record critique before closure.

Stop / loopback conditions:

- Stop and ask the user only if a ticket requires new product direction, accepts
  material unresolved risk, or would add a runtime/new owner layer.
- Loop back to the plan if a ticket splits into multiple independent changes.
- Loop back to constitution if a proposed fix contradicts no-runtime,
  skills-only, or ticket-ledger boundaries.

# Exit Criteria

- All seven tickets are closed with evidence, oracle critique, and retrospective
  disposition.
- All medium/high critique findings are resolved, accepted as risk with ticket
  provenance, superseded by evidence, or converted into linked follow-up tickets.
- The initiative success metrics have a truthful completion basis.
- No runtime creep, command-wrapper truth, or new canonical owner layer was
  introduced.
- The final commit for each ticket was pushed.

# Completion Basis

When `status: completed`, cite the child tickets, evidence records, critique
records, semantic commits, pushes, retrospective dispositions, and any follow-up
tickets or accepted risks.
