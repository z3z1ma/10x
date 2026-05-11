---
id: ticket:peerpr07
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T08:12:05Z
updated_at: 2026-05-07T08:21:41Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  constitution:
    - constitution:main
  decision:
    - decision:0006
    - decision:0007
  research:
    - research:external-peer-skill-practices-synthesis
    - research:external-skill-activation-deep-dive
    - research:skill-template-benchmark-synthesis
  evidence:
    - evidence:peer-skill-practices-validation
  critique:
    - critique:peer-skill-practices-review
external_refs:
  superpowers_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/superpowers
  everything_claude_code_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/everything-claude-code
  compound_engineering_plugin_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/compound-engineering-plugin
depends_on: []
---

# Summary

Assimilate the highest-quality peer skill practices into Loom's existing skill
corpus while preserving Loom's Markdown-native, skills-only, owner-layer model.

# Context

The user clarified that Loom should not import external command/plugin systems or
create new workflow layers. Peer repositories are useful as evidence for improving
Loom's skill doctrine: sharper questioning, verification-before-claim discipline,
pressure-tested skill authoring, and safer parent/child execution guidance.

# Scope

In:

- Record direct-read peer-practice synthesis in research.
- Strengthen existing Loom skill guidance for problem shaping, objective driving,
  specs, plans, tickets/local execution, Ralph packets, validation/evidence, and
  skill authoring.
- Keep all durable product guidance in `skills/` Markdown references, templates,
  and `SKILL.md` files.
- Preserve Loom's owner-layer model, ticket ledger, Ralph packet contract, evidence
  boundary, and critique gate.

Out:

- Do not add a new canonical owner layer, new command surface, plugin requirement,
  hook requirement, runtime, helper script, hidden validator, or external tracker
  dependency.
- Do not copy peer workflows wholesale or use peer terms as Loom ontology.
- Do not let explorer-agent summaries, external repos, hooks, plugins, worktrees,
  or command pipelines become instruction authority or project truth.
- Do not modify unrelated todo-app fixture implementation files.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| Useful peer practices should be translated into existing skills, not added as new skills. | yes | no | Accepted from user clarification and `decision:0006` / `decision:0007`. |
| Direct reads of benchmark files are sufficient source evidence for this tranche. | yes | no | Accepted; explorer output is only topology. |
| Changes affect protocol-authority guidance and therefore require mandatory critique before closure. | no | yes for closure | Accepted. |

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:peerpr07#ACC-001
- ticket:peerpr07#ACC-002
- ticket:peerpr07#ACC-003
- ticket:peerpr07#ACC-004
- ticket:peerpr07#ACC-005
- ticket:peerpr07#ACC-006

Ticket-local criteria:

- ACC-001: Research records direct-read synthesis from peer repos and explicitly rejects command/plugin/runtime adoption as Loom truth.
- ACC-002: Existing Loom shaping skills pressure-test fuzzy product, behavior, architecture, or workflow requests before specs, plans, tickets, or implementation depend on hidden assumptions.
- ACC-003: Validation/evidence guidance makes completion, fixed, passing, ready-to-merge, and child-output claims require fresh evidence for the exact claim.
- ACC-004: Plan/ticket/Ralph guidance improves slice specificity, write-scope clarity, parallel/subagent safety, and parent reconciliation without making plans or agent reports live ledgers.
- ACC-005: Skill-authoring guidance absorbs pressure-scenario and description-shortcut lessons without requiring a hidden test harness.
- ACC-006: Structural validation and mandatory critique find no unresolved high/medium blockers, no hidden runtime drift, and no owner-layer boundary regression.

# Current State

Status rationale:

`closed` because the direct-read research was recorded and concluded, the existing
skill surfaces were updated within scope, structural validation evidence was
recorded, mandatory critique completed, and all critique findings have
ticket-owned dispositions.

Blockers:

None.

Execution notes:

- Peer repo scans were rechecked manually from source files after the user warned not to rely on explorer-agent conclusions.
- The write boundary stayed within `skills/` plus this ticket, research, evidence,
  and critique records.
- Critique found plan-template drift, stale ticket evidence reconciliation, and an
  untracked-file whitespace evidence gap; each finding has been dispositioned below.

Continuation note:

Closed; no continuation needed for this tranche unless later review reopens one of
the accepted residual risks.

# Evidence

Disposition: completed

Records:

- `evidence:peer-skill-practices-validation`

Gaps / limits:

- None blocking. Evidence is structural and freshness-limited to the observed
  source state; it does not prove future operator uptake of the wording.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk protocol-authority change to Loom skill doctrine, shaping, verification, execution, and skill-authoring guidance.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface

Findings:

- `critique:peer-skill-practices-review#FIND-001` — `resolved`: restored
  `# Milestones` to `skills/loom-plans/templates/plan.md` so the template matches
  the plan-shape core section list.
- `critique:peer-skill-practices-review#FIND-002` — `resolved`: reconciled
  `evidence:peer-skill-practices-validation` and
  `critique:peer-skill-practices-review` into this ticket's evidence, review,
  acceptance, and journal sections.
- `critique:peer-skill-practices-review#FIND-003` — `resolved`: updated
  `evidence:peer-skill-practices-validation` with targeted trailing-whitespace
  scans for the untracked peer-practice records and
  `skills/loom-tickets/references/local-execution.md`.

Promotion disposition: completed
Promotion / deferral rationale: durable peer-practice lessons were promoted into existing `skills/` surfaces and `research:external-peer-skill-practices-synthesis` was concluded.

Promoted / deferred:

- Promoted into existing `loom-workspace`, `loom-drive`, `loom-specs`,
  `loom-plans`, `loom-records`, `loom-evidence`, `loom-tickets`, `loom-ralph`,
  and `loom-skill-authoring` surfaces.
- Deferred: no new command, hook, plugin, helper, hidden validator, or owner layer.

Wiki disposition: not_required - this ticket updates product-facing skills directly; no separate project wiki page is needed unless critique finds a reusable explanation gap.

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance needs to be explicit.

Accepted by: OpenCode agent ticket-owned acceptance review
Accepted at: 2026-05-07T08:21:41Z
Basis: `evidence:peer-skill-practices-validation` supports the structural portions of `ticket:peerpr07#ACC-001` through `ticket:peerpr07#ACC-006`; `critique:peer-skill-practices-review` is final; all open medium/high critique findings have ticket-owned `resolved` dispositions; no hidden-runtime adoption or owner-layer boundary regression remains known.
Residual risks: Prose guidance can still be misapplied by future operators; critique did not exhaustively re-read every external source line cited by the research; broader working tree includes prior intended changes outside this ticket's current tranche.

# Dependencies

None.

# Journal

- 2026-05-07T08:12:05Z: Created ticket and research after direct peer repo reads and user clarification that Loom should assimilate practices into existing skills only.
- 2026-05-07T08:17:33Z: Recorded `evidence:peer-skill-practices-validation` with structural checks, hidden-runtime lexical scan, marker scan, placeholder scan, and example-fixture duplication check.
- 2026-05-07T08:20:29Z: Mandatory critique recorded as `critique:peer-skill-practices-review`; findings covered plan-template drift, stale ticket reconciliation, and untracked-file whitespace coverage.
- 2026-05-07T08:20:29Z: Restored `# Milestones` to the plan template and updated evidence with targeted trailing-whitespace scans for untracked peer-practice review targets.
- 2026-05-07T08:21:41Z: Reconciled evidence and critique findings, concluded the peer-practice research, recorded promotion disposition, accepted residual risks, and closed the ticket.
