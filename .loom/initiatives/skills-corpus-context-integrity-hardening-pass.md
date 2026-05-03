---
id: initiative:skills-corpus-context-integrity-hardening-pass
kind: initiative
status: active
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T04:09:51Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  research:
    - research:skills-corpus-context-integrity-hardening-review
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  ticket:
    - ticket:bootinv1
    - ticket:trustbd2
    - ticket:vocabx08
    - ticket:tplsave3
    - ticket:pktfam04
    - ticket:evhard05
    - ticket:reconchk
    - ticket:localed7
    - ticket:queryrc9
    - ticket:drives10
    - ticket:shipacc1
external_refs: {}
---

# Objective

Harden the `skills/` product corpus so a fresh coding agent can operate Loom with
clear worldview, trust boundaries, bounded execution, concrete evidence,
recoverable reconciliation, and minimal durable state without any hidden runtime or
new owner layer.

# Why Now

The previous residual sharpening pass closed tactical inconsistencies. The council
review identified the next layer: reduce ceremony, strengthen trust and evidence,
make cold-start operation easier, and prevent support surfaces from becoming
shadow ledgers.

# In Scope

- Add minimal operational bootstrap orientation.
- Add trust-boundary doctrine for untrusted inputs, records, command snippets, and
  secrets.
- Consolidate route/status/disposition vocabulary guidance.
- Add save-ready pruning rules to copy-heavy templates.
- Separate shared packet grammar from Ralph-only requirements.
- Strengthen evidence against overclaiming and stale validation.
- Make parent reconciliation and stale packet recovery explicit.
- Define a cheap `local_edit` route without bypassing ticket truth.
- Consolidate Markdown-native query recipes.
- Tighten `loom-drive` and saved support artifact boundaries.
- Clarify `acceptance_review` versus `loom-ship`.

# Out Of Scope

- Do not add validators, schema engines, command routers, CLIs, daemons,
  databases, MCP dependencies, hidden helpers, or new canonical owner layers.
- Do not make bootstrap carry internal framing, marketing language, or broad
  product positioning.
- Do not rewrite the whole corpus for style alone.
- Do not make optional utilities or examples protocol truth.

# Delegated Authority / Autonomy Boundaries

The user delegated end-to-end execution: create plan and tickets, execute each
through Ralph, run critique, feed critique back into Ralph if needed, commit and
push, and continue until complete.

The agent may decide wording, ticket slicing, and verification details inside the
recorded scope. Stop and ask only if a proposed change would add a runtime/new
owner layer, weaken ticket/evidence/critique truth boundaries, or require new
product direction beyond the council findings.

# Objective-Level Stop Conditions

Stop or ask the user if any ticket requires:

- adding hidden runtime enforcement or a protocol-owned CLI/schema engine;
- putting internal product positioning into bootstrap instead of minimal agent
  orientation;
- accepting unresolved medium/high critique risk without explicit user approval;
- changing the layer model or ticket-ledger authority.

# Success Metrics

- OBJ-001: Bootstrap gives a never-seen-Loom model enough minimal worldview to
  orient to placement, owner truth, disposable sessions, and graph recovery.
- OBJ-002: Trust-boundary doctrine states that records, external text, tool
  output, generated files, and quoted commands are data unless the operator and
  governing instructions authorize action.
- OBJ-003: Route tokens, ticket states, record statuses, packet statuses, critique
  finding states, and ticket-owned finding dispositions remain distinct and
  centrally discoverable.
- OBJ-004: Ticket and plan templates tell agents how to save records without
  retaining unused branches or placeholders.
- OBJ-005: Shared packet grammar is separated from Ralph-only requirements without
  weakening Ralph packet discipline.
- OBJ-006: Evidence guidance makes expected/actual result, source state,
  limitations, support/challenge strength, and recheck conditions concrete.
- OBJ-007: Ralph parent reconciliation and stale compiled packet recovery are
  explicit and queryable.
- OBJ-008: The `local_edit` route is cheap, bounded, and compatible with ticket
  truth rather than a bypass.
- OBJ-009: Common graph queries are discoverable through Markdown-native recipes.
- OBJ-010: `loom-drive` and saved support artifacts cannot plausibly become a
  second execution ledger.
- OBJ-011: `acceptance_review` and `loom-ship` are clearly separate; shipping
  packages already-truthful work and does not close tickets.
- OBJ-012: Every child ticket closes with Ralph output, evidence, critique,
  retrospective disposition, semantic commit, and push.

# Milestones

- Milestone 1: Owner records and eleven child tickets exist.
- Milestone 2: Bootstrap, trust, and vocabulary foundations close.
- Milestone 3: Templates, packet grammar, evidence, and reconciliation close.
- Milestone 4: Local edit, query recipes, drive, and ship/acceptance boundaries
  close.
- Milestone 5: Plan and initiative are accepted.

# Dependencies

- Builds on completed `initiative:skills-corpus-residual-protocol-sharpening-pass`.
- Starts from pushed baseline `5a6540d` (`chore: close residual sharpening pass`).
- Inherits council synthesis `research:skills-corpus-context-integrity-hardening-review`.

# Risks

- Bootstrap hardening can become marketing; keep it minimal and operational.
- Trust guidance can drift into security tooling; keep it doctrine-only.
- Template pruning can remove useful acceptance gates if done too aggressively.
- Packet-family separation can accidentally weaken Ralph strictness.
- Query recipes can become a hidden CLI expectation if not framed as examples.

# Linked Work

- Research: `research:skills-corpus-context-integrity-hardening-review`
- Plan: `plan:skills-corpus-context-integrity-hardening-pass`
- Tickets: `ticket:bootinv1`, `ticket:trustbd2`, `ticket:vocabx08`,
  `ticket:tplsave3`, `ticket:pktfam04`, `ticket:evhard05`, `ticket:reconchk`,
  `ticket:localed7`, `ticket:queryrc9`, `ticket:drives10`, and
  `ticket:shipacc1`

# Status Summary

Active. Execute tickets sequentially with Ralph/fixer, evidence, critique,
retrospective disposition, semantic commits, and pushes.

# Completion Basis

When `status: completed`, cite child tickets, evidence, critique records,
retrospective dispositions, semantic commits, pushes, accepted risks, and any
follow-up tickets.
