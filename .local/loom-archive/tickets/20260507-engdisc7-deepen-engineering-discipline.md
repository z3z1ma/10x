---
id: ticket:engdisc7
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T14:25:12Z
updated_at: 2026-05-07T14:43:42Z
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
  ticket:
    - ticket:agntsys7
    - ticket:peerpr07
  research:
    - research:peer-engineering-discipline-deep-dive
    - research:agentsys-command-practices-synthesis
  evidence:
    - evidence:engineering-discipline-validation
  critique:
    - critique:engineering-discipline-review
external_refs:
  mattpocock_skills_github: https://github.com/mattpocock/skills
  mattpocock_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/mattpocock-skills
  addyosmani_agent_skills_github: https://github.com/addyosmani/agent-skills
  addyosmani_agent_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/addyosmani-agent-skills
  superpowers_github: https://github.com/obra/superpowers
  superpowers_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/superpowers
depends_on: []
---

# Summary

Go substantially deeper on engineering discipline from Matt Pocock's skills, Addy
Osmani's agent skills, and Superpowers, and bake the resulting discipline into
Loom's own skills as protocol-quality operator guidance rather than a shallow
external-practice summary.

# Context

The prior expanded peer-practice tranche deliberately assimilated useful patterns
without importing command runtimes. The user now wants a deeper architectural pass
with much higher autonomy: treat Loom's skill corpus as the product surface and
make larger changes where warranted.

This is still high-risk `protocol-authority` work because it can change how
future agents shape requirements, execute code changes, test, debug, review,
accept work, and close tickets.

# Scope

In:

- Direct-read deeper source files from Matt Pocock skills, Addy Osmani agent
  skills, and Superpowers.
- Identify engineering discipline primitives that Loom should teach as first-class
  operator behavior.
- Make broad but coherent changes across existing `skills/` surfaces, references,
  and templates when the discipline belongs there.
- Add new references only when they serve an existing skill boundary and avoid
  hidden runtimes.
- Preserve Loom's owner-layer model, ticket ledger, packet contracts, evidence,
  critique, and retrospective boundaries.
- Validate structurally and run mandatory critique before closure.

Out:

- Do not add command/plugin marketplaces, hooks, daemons, npm runtimes, JSON state,
  hidden validators, required MCPs, or tool-specific state as Loom core.
- Do not blindly import another repo's folder conventions, hard gates, or command
  names as Loom ontology.
- Do not let external issue trackers, PRs, deployments, or review comments own
  Loom truth.
- Do not modify unrelated todo-app fixture implementation files.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| The user's request authorizes a new deeper tranche rather than reopening `ticket:agntsys7`. | yes | no | Accepted; create this ticket as the new live ledger. |
| Larger skill changes are allowed when they preserve owner-layer boundaries and are validated. | yes | no | Accepted under user instruction and Loom skill-authoring constraints. |
| This work requires mandatory critique before closure. | no | yes for closure | Accepted due to high-risk protocol-authority scope. |

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:engdisc7#ACC-001
- ticket:engdisc7#ACC-002
- ticket:engdisc7#ACC-003
- ticket:engdisc7#ACC-004
- ticket:engdisc7#ACC-005
- ticket:engdisc7#ACC-006
- ticket:engdisc7#ACC-007
- ticket:engdisc7#ACC-008
- ticket:engdisc7#ACC-009
- ticket:engdisc7#ACC-010

Ticket-local criteria:

- ACC-001: Research records a deeper direct-read synthesis from Matt Pocock skills, Addy Osmani agent skills, and Superpowers, with transfer/reject decisions grounded in specific source files.
- ACC-002: Loom outer-loop/spec/plan guidance teaches problem pressure, one-question/codebase-first clarification, divergent/convergent option shaping, not-doing boundaries, and decision capture without creating a parallel design-doc ledger.
- ACC-003: Loom execution guidance teaches thin vertical slices, tracer bullets, test-first posture when behavior can be exercised, source-driven context, one-logical-change discipline, and safe local/Ralph boundaries.
- ACC-004: Loom debugging guidance teaches feedback-loop construction, root-cause tracing, ranked falsifiable hypotheses, instrumentation hygiene, architecture escalation after repeated failed fixes, and performance-as-measurement discipline.
- ACC-005: Loom critique guidance teaches multi-axis review, review-pass splitting, AI-artifact cleanup, dependency/security/performance lenses, verify-before-implementing-feedback discipline, and stalled review-loop escalation.
- ACC-006: Loom evidence/ticket/acceptance guidance teaches evidence-before-claims, red/green or before/after proof, verification freshness, no repeated reassurance runs, and ticket-owned disposition of evidence limits.
- ACC-007: Loom codemap/wiki/research guidance teaches deterministic codebase orientation, shared-language conflict handling, source quality/freshness, ADR/decision thresholds, and accepted explanation promotion.
- ACC-008: Loom ship/retrospective guidance teaches finishing options, launch/rollback packaging, docs sync, review comment classification, and prevention-artifact promotion without letting shipping close tickets.
- ACC-009: Skill templates/references are updated where needed so new discipline is visible to future skill authors and record authors, without placeholder leakage into saved records.
- ACC-010: Structural validation and mandatory critique find no unresolved high/medium blockers, hidden-runtime drift, or owner-layer boundary regression.

# Current State

Status rationale:

`closed` because the deep direct-read research, skill-surface edits, validation
evidence, mandatory critique, finding dispositions, and promotion decision are now
recorded in the owning layers.

Blockers:

None.

Execution notes:

- Work boundary was `skills/` plus this ticket, the deep-dive research record,
  validation evidence, and mandatory critique.
- Use external peer repos as evidence only. Product truth remains in `skills/`
  and canonical Loom records.
- Research reached concluded status after recommendations were promoted into the
  existing skill surfaces named by this ticket.

Continuation note:

No immediate continuation is required for this ticket. Future pressure-scenario
evidence may be useful if later operators need proof that the guidance changes
improve behavior in practice.

# Evidence

Disposition: sufficient for closure

Records:

- `evidence:engineering-discipline-validation`

Gaps / limits:

- Evidence is structural and source-inspection based; it does not prove future
  agent compliance with the guidance.
- No automated test suite exists for this Markdown skills corpus.
- Unrelated todo-app fixture files and historical root `.loom` records were outside
  this ticket's validation scope.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk protocol-authority changes to skill behavior, execution discipline, debugging, review, evidence, and acceptance practices.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface
- evidence-sufficiency
- code-change
- code-structure

Findings:

- `critique:engineering-discipline-review#FIND-001`: resolved by recording peer
  clone HEAD commits in `research:peer-engineering-discipline-deep-dive` and
  `evidence:engineering-discipline-validation`.
- `critique:engineering-discipline-review#FIND-002`: resolved by this ticket
  reconciliation: evidence and critique are linked, finding dispositions are
  recorded, promotion state is explicit, and acceptance provenance is filled.
- `critique:engineering-discipline-review#FIND-003`: resolved by expanding
  `evidence:engineering-discipline-validation` with exact changed-file runtime-term
  audit classification.

Promotion disposition: completed
Promotion / deferral rationale: accepted engineering discipline was promoted into
existing owner/workflow skill surfaces rather than a new runtime, command layer, or
omnibus engineering-discipline skill. The research record is concluded.

Promoted / deferred:

- Promoted into `loom-workspace`, `loom-specs`, `loom-plans`, `loom-ralph`,
  `loom-debugging`, `loom-critique`, `loom-evidence`, `loom-codemap`,
  `loom-research`, `loom-ship`, `loom-retrospective`, and `loom-tickets` skill
  surfaces.
- Deferred pressure-scenario proof of future operator compliance until a later
  ticket needs behavioral evidence from use.

Wiki disposition: not_required - the accepted explanation for this tranche lives
in the product skill corpus and concluded research; no separate wiki page is needed
for closure.

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance needs to be explicit.

Accepted by: OpenCode agent under user-delegated Loom operation
Accepted at: 2026-05-07T14:43:42Z
Basis: `ticket:engdisc7#ACC-001` through `ticket:engdisc7#ACC-010` are supported
by the concluded research, changed `skills/` surfaces, structural validation
evidence, and final mandatory critique with all medium findings dispositioned as
resolved in this ticket.
Residual risks: Markdown protocol guidance cannot prove future operator behavior
without later pressure-scenario evidence; this repository has no automated skills
test suite; copied future records still depend on operators clearing template
placeholders truthfully.

# Dependencies

None.

# Journal

- 2026-05-07T14:25:12Z: Created ticket after user requested a much deeper engineering-discipline pass with greater architectural ownership over Loom skill files.
- 2026-05-07T14:39:02Z: Deep-dive research recorded direct peer source citations,
  transfer/reject decisions, source commits, and recommendations; accepted
  primitives were promoted into existing skill surfaces.
- 2026-05-07T14:39:02Z: Structural validation evidence recorded clean skill diff
  whitespace, clean active-record placeholder checks, targeted guidance-anchor
  matches, hidden-runtime audit classification, and peer clone source commits.
- 2026-05-07T14:40:13Z: Mandatory critique recorded a final `pass_with_findings`
  verdict with three medium findings requiring ticket-owned disposition.
- 2026-05-07T14:43:42Z: Dispositioned all critique findings, cleaned the final
  evidence placeholder-scan wording, marked promotion completed, recorded
  acceptance provenance, and closed the ticket.
