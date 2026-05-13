# Ralph Language Consolidation

ID: ticket:20260513-ralph-language-consolidation
Type: Ticket
Status: closed
Created: 2026-05-13
Updated: 2026-05-13
Risk: medium - changes core skill language that controls worker handoff and audit routing semantics.

## Summary

Consolidate model-visible Loom skill language around Ralph as the canonical worker and audit handoff concept. The current corpus still uses `fresh-context`, `fresh context`, `separate-context`, and `separate context` as primary concepts in several places, which makes Ralph look like one option instead of the centered worker mechanism.

The closure claim is that shipped skills describe worker delegation and substantive audit review through Ralph packets, while audit records remain the durable place that records the returned adversarial judgment.

## Related Records

- `ticket:20260510-ralph-audit-handoff-doctrine` - prior bounded work that made on-disk Ralph packets the worker and audit handoff contract.
- `research:20260510-loom-loop-failure-analysis` - identifies the earlier failure mode where worker handoffs could bypass Ralph.

## Scope

May change:

- `loom-core/skills/**`
- `loom-playbooks/skills/**`
- `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, and package READMEs when they
  restate the same worker or audit language
- `.loom/tickets/20260513-ralph-language-consolidation.md`
- `.loom/evidence/**` if validation output needs durable preservation

Must not change:

- historical `.loom` records except this ticket and any new evidence for this work
- adapter manifests, hooks, packaging, or runtime mechanics
- existing uncommitted user edits except where this ticket must edit the same current file text

## Acceptance

- ACC-001: Model-visible skill prose no longer uses `fresh-context` or `separate-context` language as the primary way to describe Ralph work.
  - Evidence: targeted grep over `loom-core/skills` and `loom-playbooks/skills` for `fresh-context`, `fresh context`, `separate-context`, and `separate context` after the edit.
  - Audit: separate audit is not required for this terminology-only slice if grep evidence and diff inspection show no behavior expansion beyond Ralph-centered wording.

- ACC-002: `loom-audit` describes substantive audit review as a Ralph review packet and the audit record as the place where the returned adversarial judgment is recorded.
  - Evidence: source inspection of `loom-core/skills/loom-audit/**` and `loom-core/skills/loom-ralph/**` after the edit.
  - Audit: separate audit is not required for this terminology-only slice if the affected text preserves the existing packet-before-audit mechanics.

- ACC-003: Playbook skills that mention delegated review or audit route the work through `loom-ralph` and `loom-audit` without centering `fresh-context` terminology.
  - Evidence: source inspection and targeted grep of `loom-playbooks/skills` after the edit.
  - Audit: separate audit is not required for this terminology-only slice if the changed playbook text remains routing-only and does not add new workflow requirements.

- ACC-004: Human-facing docs that restate Core worker or audit semantics use Ralph-centered language instead of stale `fresh-context` wording.
  - Evidence: targeted grep over non-historical docs after the edit.
  - Audit: separate audit is not required for this terminology-only slice if the doc changes mirror the skill language.

## Evidence

- `evidence:20260513-ralph-language-consolidation-checks` - targeted term scans, source-diff inspection, smoke checks, pack checks, and `git diff --check` for this terminology consolidation.

## Current State

Closed. Shipped Core and Playbooks skill prose no longer uses `fresh-context`, `fresh context`, `separate-context`, or `separate context` as the worker/audit handoff language. `loom-audit` now centers substantive audit review on Ralph review packets and records the returned adversarial judgment in audit. The affected playbooks route delegated review/audit through `loom-ralph` and `loom-audit` without context-shape terminology. Non-historical docs that restate Core worker or audit semantics now use Ralph-centered wording. Separate audit was not performed per the acceptance criteria's terminology-only audit waiver.

## Journal

- 2026-05-13: Created ticket from operator request to consolidate worker and audit language around Ralph and stop centering `fresh-context` or `separate-context` terminology in skills.
- 2026-05-13: Updated shipped Core and Playbooks skill prose plus non-historical docs to center Ralph packets/Ralph-backed audit instead of context-shape terminology; recorded `evidence:20260513-ralph-language-consolidation-checks`; closed after acceptance evidence passed.
