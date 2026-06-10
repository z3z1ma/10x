# Record Skill Kernels

Status: done
Created: 2026-05-25
Updated: 2026-05-25

Legacy note: Risk — high - rewrites the Core record station skills that preserve graph truth, execution state, evidence, audit, and reusable knowledge.

Priority: high - compresses the main portable protocol after the session kernel.
Depends-On: .loom/tickets/done/20260525-session-kernel-compression.md

## Summary

Compress the Core record skills and references into station kernels. The closure claim is that each surface still teaches its owner truth, lifecycle, inspect/write/update path, stop conditions, and critical non-examples with materially less repeated prose.

## Related Records

- `.loom/tickets/20260525-loom-protocol-compression.md` - owns sequencing and validation posture.
- `.loom/specs/loom-protocol-compression.md` - defines record skill compression requirements, especially REQ-004 and REQ-005.
- `.loom/specs/ticket-owned-worker-handoffs.md` - ticket and Ralph compression must preserve worker handoff behavior.
- `.loom/tickets/done/20260525-session-kernel-compression.md` - provides the compressed shared session vocabulary this ticket should consume.
- `AGENTS.md` - product-surface leakage and validation constraints.

## Scope

May change Core record skills and references under:

- `loom-core/skills/loom-constitution/**`
- `loom-core/skills/loom-specs/**`
- `loom-core/skills/loom-plans/**`
- `loom-core/skills/loom-tickets/**`
- `loom-core/skills/loom-research/**`
- `loom-core/skills/loom-evidence/**`
- `loom-core/skills/loom-audit/**`
- `loom-core/skills/loom-knowledge/**`
- `loom-core/skills/loom-retrospective/**`
- `loom-core/skills/loom-ralph/**`

Templates may change only when wording becomes stale or prevents station-kernel behavior. Do not change record filenames, IDs, statuses, or directory structure unless a specific skill's behavior requires it and the ticket records why. Do not edit Playbooks, agent prompts, or public docs except for links that would break because of reference topology changes.

First Ralph boundary: compress one skill family at a time, preserve required record shapes and lifecycle behavior, run checks, and update the ticket with before/after counts.

Stop if a skill family reveals a behavior change rather than compression; split or route back to specs/constitution.

## Acceptance

- ACC-001: Each compressed record skill clearly states its station owner truth, use triggers, read/inspect path, write/update path, status or lifecycle rules, stop conditions, and critical non-examples.
  - Evidence: Source inspection matrix or evidence record mapping each skill to required station content.
  - Audit: Fresh-context final audit should challenge missing station behavior.

- ACC-002: Skill references are retained, merged, or removed according to `.loom/specs/loom-protocol-compression.md#REQ-005`, with no orphaned references or broken links.
  - Evidence: Source inspection and targeted grep for referenced file names.
  - Audit: Review should challenge references that became manuals or missing detail cards.

- ACC-003: Ticket, Ralph, evidence, and audit skills preserve the execution spine: one ticket, bounded Ralph, evidence as backpressure, audit as inspection, worker output as claim.
  - Evidence: Source inspection against `.loom/specs/ticket-owned-worker-handoffs.md` and `.loom/specs/loom-protocol-compression.md#REQ-001`.
  - Audit: Review should specifically challenge behavior loss in the execution spine.

- ACC-004: Before/after line counts show material compression or the ticket explains why retained prose is necessary for behavior preservation.
  - Evidence: Recorded `wc -l` output or evidence record.
  - Audit: Review should challenge both over-compression and unnecessary retained verbosity.

- ACC-005: Core package validation passes for touched packaged surfaces.
  - Evidence: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, and `git diff --check` outputs recorded or cited.
  - Audit: Final audit should inspect the evidence limits.

## Current State

Closed. Dependency `.loom/tickets/done/20260525-session-kernel-compression.md` is closed. Three bounded Ralph worker runs compressed all Core record skill families: execution spine (`loom-tickets`, `loom-ralph`, `loom-evidence`, `loom-audit`), direction-setting (`loom-constitution`, `loom-specs`, `loom-plans`, `loom-research`), and reusable learning (`loom-knowledge`, `loom-retrospective`). Evidence is recorded at `.loom/evidence/20260525-execution-spine-record-skill-kernels-validation.md`, `.loom/evidence/20260525-direction-record-skill-kernels-validation.md`, and `.loom/evidence/20260525-reusable-learning-record-skill-kernels-validation.md`. Fresh-context audit is recorded at `.loom/reviews/20260525-record-skill-kernels-audit.md` with verdict pass with non-blocking risks and no material findings. Residual risks are source-review limits, no live model-behavior simulation, and adjacent surfaces not audited by this ticket.

Files changed in this run:

- `loom-core/skills/loom-tickets/SKILL.md`
- `loom-core/skills/loom-tickets/references/acting-on-tickets.md`
- `loom-core/skills/loom-tickets/references/creating-tickets.md`
- `loom-core/skills/loom-tickets/references/ticket-shape.md`
- `loom-core/skills/loom-tickets/templates/ticket.md`
- `loom-core/skills/loom-ralph/SKILL.md`
- `loom-core/skills/loom-ralph/references/run-shape.md`
- `loom-core/skills/loom-ralph/references/running-ralph.md`
- `loom-core/skills/loom-ralph/references/verification-posture.md`
- `loom-core/skills/loom-evidence/SKILL.md`
- `loom-core/skills/loom-evidence/references/creating-evidence.md`
- `loom-core/skills/loom-evidence/references/evidence-quality.md`
- `loom-core/skills/loom-evidence/templates/dossier.md`
- `loom-core/skills/loom-evidence/templates/observation.md`
- `loom-core/skills/loom-audit/SKILL.md`
- `loom-core/skills/loom-audit/references/audit-lenses.md`
- `loom-core/skills/loom-audit/references/audit-shape.md`
- `loom-core/skills/loom-audit/references/findings-and-verdicts.md`
- `loom-core/skills/loom-audit/templates/audit.md`
- `loom-core/skills/loom-constitution/SKILL.md`
- `loom-core/skills/loom-constitution/references/core-constitution.md`
- `loom-core/skills/loom-constitution/references/decision-records.md`
- `loom-core/skills/loom-constitution/references/principle-fragments.md`
- `loom-core/skills/loom-constitution/references/roadmap-records.md`
- `loom-core/skills/loom-specs/SKILL.md`
- `loom-core/skills/loom-specs/references/spec-shape.md`
- `loom-core/skills/loom-plans/SKILL.md`
- `loom-core/skills/loom-plans/references/creating-plans.md`
- `loom-core/skills/loom-plans/references/plan-shape.md`
- `loom-core/skills/loom-plans/references/slicing-work.md`
- `loom-core/skills/loom-research/SKILL.md`
- `loom-core/skills/loom-research/references/research-shape.md`
- `loom-core/skills/loom-research/references/source-handling.md`
- `loom-core/skills/loom-knowledge/SKILL.md`
- `loom-core/skills/loom-knowledge/references/knowledge-shape.md`
- `loom-core/skills/loom-knowledge/references/retrieval-and-loading.md`
- `loom-core/skills/loom-knowledge/references/maintaining-knowledge.md`
- `loom-core/skills/loom-knowledge/templates/atlas.md`
- `loom-core/skills/loom-knowledge/templates/concept.md`
- `loom-core/skills/loom-knowledge/templates/entity.md`
- `loom-core/skills/loom-knowledge/templates/note.md`
- `loom-core/skills/loom-knowledge/templates/preference.md`
- `loom-core/skills/loom-knowledge/templates/procedure.md`
- `loom-core/skills/loom-knowledge/templates/reference.md`
- `loom-core/skills/loom-knowledge/templates/troubleshooting.md`
- `loom-core/skills/loom-retrospective/SKILL.md`
- `loom-core/skills/loom-retrospective/references/promotion-and-prevention.md`

Validation passed for the execution-spine run: before/after line counts, `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, `git diff --check`, targeted behavior/source searches, packet-retirement search, reference-link search, and product-surface leakage search. The four touched families dropped from 2,372 to 1,358 lines.

Validation passed for the direction-setting run: before/after line counts, `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, `git diff --check`, targeted behavior/source searches, reference-link search, and product-surface leakage search. `git diff --check` was rerun after evidence/ticket record updates. The four touched families dropped from 2,880 to 1,648 lines.

Validation passed for the reusable-learning run: before/after line counts, `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, `git diff --check` before and after record updates, targeted behavior/source searches, reference-link search, and product-surface leakage search. The two touched families dropped from 1,047 to 846 lines. No uncompressed record skill families remain. Ticket is in `review`; closure still needs fresh-context audit.

## Journal

- 2026-05-25: Created ticket with dependency on session kernel compression.
- 2026-05-25: Set status to `active` after session-kernel compression closed.
- 2026-05-25: Bounded execution-spine run compressed `loom-tickets`, `loom-ralph`, `loom-evidence`, and `loom-audit` within source scope. Line count changed from 2,372 to 1,358 lines across the 19 touched files. Validation passed: Core smoke, Core pack check, `git diff --check`, targeted behavior/source searches, packet-retirement search, reference-link search, and product-surface leakage search. Evidence recorded at `.loom/evidence/20260525-execution-spine-record-skill-kernels-validation.md`. Remaining record skill families are constitution, specs, plans, research, knowledge, and retrospective; ticket stays `active`.
- 2026-05-25: Bounded direction-setting run compressed `loom-constitution`, `loom-specs`, `loom-plans`, and `loom-research` within source scope. Line count changed from 2,880 to 1,648 lines across the 21 touched files. Validation passed: Core smoke, Core pack check, `git diff --check` before and after record updates, targeted behavior/source searches, reference-link search, and product-surface leakage search. Evidence recorded at `.loom/evidence/20260525-direction-record-skill-kernels-validation.md`. Remaining record skill families are knowledge and retrospective; ticket stays `active`.
- 2026-05-25: Bounded reusable-learning run compressed `loom-knowledge` and `loom-retrospective` within source scope. Line count changed from 1,047 to 846 lines across the 14 touched files. Validation passed: Core smoke, Core pack check, `git diff --check` before and after record updates, targeted behavior/source searches, reference-link search, and product-surface leakage search. Evidence recorded at `.loom/evidence/20260525-reusable-learning-record-skill-kernels-validation.md`. No uncompressed record skill families remain; ticket moved to `review` pending fresh-context audit.
- 2026-05-25: Fresh-context audit recorded at `.loom/reviews/20260525-record-skill-kernels-audit.md`. Verdict: pass with non-blocking risks; no material findings. Audit reran Core smoke, Core pack check, and `git diff --check`, challenged line counts, reference/template links, execution-spine preservation, product-surface leakage, and behavior loss. Ticket remains `review` for coordinator-owned closure disposition.
- 2026-05-25: Coordinator closed ticket. ACC-001 through ACC-005 are supported by three evidence dossiers and fresh-context audit; no source follow-up required by audit.
