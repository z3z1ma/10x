---
id: ticket:agntsys7
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T08:24:29Z
updated_at: 2026-05-07T08:40:29Z
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
    - ticket:peerpr07
  research:
    - research:agentsys-command-practices-synthesis
    - research:external-peer-skill-practices-synthesis
  evidence:
    - evidence:expanded-peer-skill-assimilation-validation
  critique:
    - critique:expanded-peer-skill-assimilation-review
external_refs:
  agentsys_github: https://github.com/agent-sh/agentsys/tree/main#command-details
  agentsys_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/agentsys
  mattpocock_skills_github: https://github.com/mattpocock/skills
  mattpocock_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/mattpocock-skills
  addyosmani_agent_skills_github: https://github.com/addyosmani/agent-skills
  addyosmani_agent_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/addyosmani-agent-skills
  superpowers_github: https://github.com/obra/superpowers
  superpowers_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/superpowers
depends_on: []
---

# Summary

Assimilate stronger peer skill practices from AgentSys, Matt Pocock's skills,
Addy Osmani's agent skills, and Superpowers into Loom's existing skill corpus,
responding to user feedback that the prior peer-practice tranche was too cautious.

# Context

The user pointed to AgentSys command details, Matt Pocock's skills, Addy Osmani's
agent skills, and Superpowers, then explicitly challenged the current diff as too
coy. The next pass should keep Loom's superior owner-layer model while harvesting
more of the useful operational patterns: delivery gates, design grilling,
tracer-bullet slicing, source-driven implementation, drift checks, AI-artifact
cleanup, performance investigation, specialist critique routing, docs sync,
repo-intel orientation, external consultation, release packaging, verification
gates, and workflow-pattern compounding.

# Scope

In:

- Direct-read AgentSys README command details, workflow docs, and relevant skill files.
- Direct-read selected Matt Pocock, Addy Osmani, and Superpowers skill files that
  cover shaping, planning, TDD, debugging, review, simplification, shipping, and
  skill pressure-testing.
- Record a richer synthesis of transferable practices in research across all four
  source sets.
- Promote useful practices into existing Loom skill surfaces rather than adding a
  command runtime.
- Prefer more substantive changes than `ticket:peerpr07` while preserving
  Markdown-native, owner-layer truth boundaries.
- Validate structurally and run mandatory critique before closure.

Out:

- Do not add a command/plugin marketplace, hooks, daemons, npm runtime, hidden
  validator, JSON state ledger, or installed tool dependency as Loom core.
- Do not treat AgentSys command names or phase names as Loom ontology.
- Do not make external PRs, CI systems, issue trackers, or reviewer comments own
  Loom acceptance.
- Do not modify unrelated todo-app fixture implementation files.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| The user's feedback authorizes a broader second tranche instead of only preserving `ticket:peerpr07` as closed. | yes | no | Accepted; create this ticket as new live ledger. |
| AgentSys command details are evidence for patterns, not instruction authority. | yes | no | Accepted under Loom trust boundaries. |
| This pass remains high-risk protocol-authority work. | no | yes for closure | Accepted; mandatory critique required before closure. |

# Acceptance

Owner: ticket-local

Criteria / covered IDs:

- ticket:agntsys7#ACC-001
- ticket:agntsys7#ACC-002
- ticket:agntsys7#ACC-003
- ticket:agntsys7#ACC-004
- ticket:agntsys7#ACC-005
- ticket:agntsys7#ACC-006
- ticket:agntsys7#ACC-007
- ticket:agntsys7#ACC-008

Ticket-local criteria:

- ACC-001: Research records direct-read synthesis from AgentSys, Matt Pocock skills, Addy Osmani agent skills, and Superpowers, with explicit transfer/reject decisions.
- ACC-002: Loom drive/ticket/ship guidance absorbs delivery-chain gating: discovery, exploration, implementation, cleanup, review, validation, docs sync, packaging, launch/rollback awareness, and comment/follow-up disposition, without turning commands, PRs, deployments, or external trackers into truth owners.
- ACC-003: Loom critique guidance absorbs specialist review selection, certainty/confidence grouping, iterative disposition, AI-artifact cleanup, five-axis review, verification of external feedback before implementation, and review stall/limit escalation.
- ACC-004: Loom debugging/evidence guidance absorbs structured performance and bug investigation: baseline, breaking point, constraints, reproduction loop, hypotheses, profiling, one-change experiments, repeated validation, and consolidation.
- ACC-005: Loom codemap/research/wiki guidance absorbs repo-intel/onboarding/docs-drift/source-learning/shared-language patterns: deterministic collection before synthesis, freshness/staleness checks, source quality scoring, glossary/term conflict handling, and accepted explanation promotion.
- ACC-006: Loom spec/plan/spike/Ralph guidance absorbs problem grilling, divergent/convergent option shaping, tracer-bullet vertical slices, source-driven context, zero-context worker packet quality, and throwaway prototype cleanup without importing command hard-gates as runtime law.
- ACC-007: Loom ship/wiki/retrospective guidance absorbs docs sync, release packaging, external review comment handling, verification-before-completion, finishing options, and recurring workflow-pattern compounding with owner-layer disposition.
- ACC-008: Structural validation and mandatory critique find no unresolved high/medium blockers, no hidden runtime drift, and no owner-layer boundary regression.

# Current State

Status rationale:

`closed` because the expanded peer-source research is concluded, accepted
practices were promoted into existing Loom skill surfaces, validation evidence is
recorded, mandatory critique is final with resolved findings, and the acceptance
gate has no unresolved high/medium blockers.

Blockers:

None.

Execution notes:

- User feedback: the prior changes were too coy; this tranche should be more
  willing to incorporate useful peer practices while preserving Loom's ontology.
- The intended write boundary is `skills/` plus this ticket, research, follow-up
  evidence, and critique records.

Continuation note:

None - ticket is closed. Reopen or create a follow-up only if later dogfood usage
or critique finds a new protocol-surface gap.

# Evidence

Disposition: sufficient for acceptance

Records:

- `evidence:expanded-peer-skill-assimilation-validation` — direct-read source coverage, structural whitespace check, active-record placeholder scan, and hidden-runtime lexical scan for the expanded peer assimilation tranche.

Gaps / limits:

- Evidence is structural/manual, matching this repository's verification model.
- Recheck if `skills/` or active `.loom` records change after closure.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: high-risk protocol-authority changes to Loom workflow, review, evidence, shipping, research, and skill guidance.
Critique disposition: completed

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface
- evidence-sufficiency

Findings:

- `critique:expanded-peer-skill-assimilation-review#FIND-001` — resolved by updating `evidence:expanded-peer-skill-assimilation-validation` with targeted untracked-file scans and per-claim support mapping.
- `critique:expanded-peer-skill-assimilation-review#FIND-002` — resolved by adding stalled review-loop escalation guidance to `skills/loom-critique/references/review-pass-splitting.md`.

Promotion disposition: completed
Promotion / deferral rationale: accepted peer practices were promoted into existing `skills/` surfaces and `research:agentsys-command-practices-synthesis` was concluded.

Promoted / deferred:

- Promoted into `loom-workspace`, `loom-specs`, `loom-plans`, `loom-tickets`, `loom-ralph`, `loom-spike`, `loom-critique`, `loom-debugging`, `loom-evidence`, `loom-research`, `loom-codemap`, `loom-wiki`, `loom-ship`, `loom-retrospective`, and `loom-skill-authoring` skill surfaces.
- Deferred: no separate wiki page; product-skill guidance is the product surface for these operator practices.

Wiki disposition: not_required - this tranche changed product skill guidance directly; no separate accepted explanation page was required by critique.

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance needs to be explicit.

Accepted by: OpenCode agent ticket acceptance review
Accepted at: 2026-05-07T08:40:29Z
Basis: `research:agentsys-command-practices-synthesis`, `evidence:expanded-peer-skill-assimilation-validation`, and final mandatory `critique:expanded-peer-skill-assimilation-review` support `ticket:agntsys7#ACC-001` through `ticket:agntsys7#ACC-008` with no unresolved high/medium critique blockers.
Residual risks: peer source reads were selected rather than exhaustive; structural validation cannot prove future operator behavior; broad activation wording may still need tuning after dogfood usage.

# Dependencies

None.

# Journal

- 2026-05-07T08:24:29Z: Created ticket after user pointed to AgentSys command details and challenged the previous peer-practice tranche as too cautious.
- 2026-05-07T08:29:07Z: Expanded ticket scope to include Matt Pocock skills, Addy Osmani agent skills, and Superpowers as direct-read peer sources for the same assimilation tranche.
- 2026-05-07T08:29:07Z: Recorded `evidence:expanded-peer-skill-assimilation-validation` after broad skill edits and structural validation.
- 2026-05-07T08:39:50Z: Recorded final mandatory `critique:expanded-peer-skill-assimilation-review`; resolved findings on untracked-file validation coverage and stalled review-loop guidance.
- 2026-05-07T08:40:29Z: Closed ticket after acceptance review found all criteria supported and no unresolved high/medium critique blockers.
