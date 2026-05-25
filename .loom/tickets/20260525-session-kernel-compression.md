# Session Kernel Compression

ID: ticket:20260525-session-kernel-compression
Type: Ticket
Status: closed
Created: 2026-05-25
Updated: 2026-05-25
Risk: high - changes the session-start doctrine and preload surfaces that govern all Loom routing.
Priority: high - largest context-impact slice after the compression contract.
Depends On: ticket:20260525-compression-contract-inventory

## Summary

Compress `using-loom` and its preload references into the smallest complete session kernel. The closure claim is that a fresh model still receives complete Loom routing, activation, shaping, execution, proof, and safety posture from a smaller startup surface.

## Related Records

- `plan:20260525-loom-protocol-compression` - owns sequencing and validation posture.
- `spec:loom-protocol-compression` - defines compression requirements, especially REQ-001 through REQ-003.
- `constitution:main` - requires operational kernels and portability.
- `roadmap:loom-mill` - names protocol compression as the foundation chapter.
- `spec:ticket-owned-worker-handoffs` - worker handoff behavior that session doctrine must preserve.
- `ticket:20260525-compression-contract-inventory` - provides inventory and baseline.
- `AGENTS.md` - requires preload alignment when `using-loom` doctrine changes.

## Scope

May change `loom-core/skills/using-loom/SKILL.md`, files under `loom-core/skills/using-loom/references/`, and every Core preload surface that embeds or orders using-loom doctrine, including `loom-core/loom-core.mjs`, `loom-core/hooks/*`, and `loom-core/gemini-bootstrap.md` when present.

May update human docs only when they directly restate startup doctrine and would become misleading. Do not compress other record skills, Playbooks, or agent prompts in this ticket except for unavoidable reference updates caused by changed using-loom file names or preload ordering.

First Ralph boundary: inventory the current using-loom preload shape, propose the compressed kernel/reference topology, edit only this slice, then run targeted validation.

Stop if compression would weaken first-action skill activation, active knowledge loading, surface routing, ticket-owned Ralph execution, evidence/audit posture, or safety boundaries.

## Acceptance

- ACC-001: The session kernel preserves mandatory skill activation before clarifying questions, exploration, edits, tickets, Ralph runs, evidence claims, audit claims, and closure.
  - Evidence: Source inspection and targeted grep over compressed `using-loom` and preload surfaces.
  - Audit: Fresh-context final audit should challenge activation loss.

- ACC-002: The compressed startup doctrine still teaches the complete loop: shape, route durable truth, slice to tickets, execute bounded Ralph runs, preserve evidence, audit claims, and reconcile records.
  - Evidence: Source inspection against `spec:loom-protocol-compression#REQ-001` and `REQ-003`.
  - Audit: Fresh-context final audit should test whether a model could still follow the loop.

- ACC-003: All preload surfaces that include using-loom doctrine remain aligned with the compressed file and ordered references.
  - Evidence: Core smoke, Core pack check, and source inspection of preload outputs or source strings.
  - Audit: Review should challenge stale embedded doctrine.

- ACC-004: The ticket records before/after line counts and explains any retained verbosity by behavior requirement or known failure mode.
  - Evidence: Recorded `wc -l` output or evidence record.
  - Audit: Review should challenge false minimalism and unnecessary retained prose.

## Current State

Closed. The bounded source-edit run compressed `using-loom` and ordered references while preserving the existing preload topology. No preload mirror files required edits because `loom-core/loom-core.mjs`, hooks, and Gemini bootstrap still include the same ordered files dynamically. Fresh-context audit is recorded at `audit:20260525-session-kernel-compression-audit` with verdict: pass with non-blocking risks and no material findings. Residual risks are limited to external harness runtime behavior not covered by local Core smoke/pack, no behavioral simulation across multiple ambiguous tasks, and downstream compression slices not yet complete.

Files changed:

- `loom-core/skills/using-loom/SKILL.md`
- `loom-core/skills/using-loom/references/00-how-loom-thinks.md`
- `loom-core/skills/using-loom/references/01-activation-discipline.md`
- `loom-core/skills/using-loom/references/02-directory-structure.md`
- `loom-core/skills/using-loom/references/03-shaping-with-humans.md`
- `loom-core/skills/using-loom/references/04-delegating-to-workers.md`
- `loom-core/skills/using-loom/references/05-proving-the-work.md`
- `loom-core/skills/using-loom/references/06-staying-safe.md`

Validation evidence: `evidence:20260525-session-kernel-compression-validation` records before/after line counts, Core smoke, Core pack check, `git diff --check`, targeted behavior searches, and product-surface leakage search. Acceptance is satisfied by implementation evidence and fresh-context audit.

## Journal

- 2026-05-25: Created ticket with dependency on compression contract and inventory.
- 2026-05-25: Set status to `active` after inventory ticket closed. Launched first session-kernel compression run.
- 2026-05-25: Bounded source-edit run compressed `using-loom` from 955 to 722 lines and the requested preload set from 1494 to 1261 lines. Validation passed: Core smoke, Core pack check, `git diff --check`, targeted behavior/source searches, and product-surface leakage search. Recorded evidence at `evidence:20260525-session-kernel-compression-validation`; moved ticket to `review` pending fresh-context audit.
- 2026-05-25: Fresh-context audit recorded at `audit:20260525-session-kernel-compression-audit`. Verdict: pass with non-blocking risks; no material findings. Audit reran Core smoke, Core pack check, and `git diff --check`, inspected the compressed source, preload surfaces, validation evidence, and product-surface leakage searches.
- 2026-05-25: Coordinator closed ticket. ACC-001 through ACC-004 are supported by validation evidence and audit; no source follow-up required by audit.
