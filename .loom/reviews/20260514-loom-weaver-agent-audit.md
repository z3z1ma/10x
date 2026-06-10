# Loom Weaver Agent Audit

Status: recorded
Created: 2026-05-14
Updated: 2026-05-14
Target: .loom/tickets/done/20260514-loom-weaver-agent.md

## Summary

Ralph audit of the first Loom Weaver implementation returned `changes-needed`.
It found one contributor-guidance gap in `AGENTS.md`; the audit did not identify
material blockers in the Loom Weaver prompt, initial package checks, or harness
support wording then under review.

## Target

The audit targeted `.loom/tickets/done/20260514-loom-weaver-agent.md` after the first
implementation packet and evidence record, before the operator later revised the
Codex route away from a bundled Core skill.

## Audit Scope And Lenses

Scope covered the ticket acceptance criteria, implementation diff, evidence
sufficiency, harness support honesty, `.loom/` write boundary, and
product-surface leakage. The audit was read-only and did not rerun checks.

## Context And Evidence Reviewed

- Ralph packet: `former packet 20260514T230124Z-loom-weaver-agent-audit` - bounded review contract.
- `.loom/tickets/done/20260514-loom-weaver-agent.md` - target scope and acceptance.
- `.loom/specs/loom-weaver-agent.md` - behavior contract.
- `.loom/research/20260514-direct-interactive-agent-surfaces.md` - harness support research.
- `.loom/evidence/20260514-loom-weaver-implementation-validation.md` - prior implementation validation evidence.
- `former packet 20260514T223622Z-loom-weaver-agent-implementation` - implementation packet and worker output.
- Source paths named by the audit packet, including Core agent files, plugin manifests, docs, `AGENTS.md`, and current diff.

## Findings

### FIND-001: Dogfooding Guidance Omitted Core Agent Surfaces

Severity: medium
Confidence: high

`AGENTS.md` still said to keep model-visible behavior only in `loom-core/skills/`
and `loom-playbooks/skills/`, omitting `loom-core/agents/`. This contradicted
the new agent-surface policy elsewhere in `AGENTS.md` and weakened the contributor

Required follow-up: update the Dogfooding guidance to include `loom-core/agents/`
as a model-visible behavior surface and mention agent prompts alongside skills
where manifests/hooks/docs only expose or restate shipped behavior.

## Verdict

`changes-needed`. The ticket should not proceed to closure until `FIND-001` is
fixed and a fresh audit reviews the revised final state.

## Required Follow-up

- Fix `AGENTS.md` contributor guidance.
- Re-audit the final implementation after the Codex route change and finding fix.

## Residual Risk

The audit did not rerun smoke, pack, Claude, Gemini, Cursor, or live harness
runtime checks. Cursor plugin behavior remained unvalidated by a local validator.
OpenCode permission enforcement and live agent switching were inspected through
source and recorded evidence only, not exercised at runtime.

## Related Records

- `former packet 20260514T230124Z-loom-weaver-agent-audit` - Ralph review packet.
- `.loom/tickets/done/20260514-loom-weaver-agent.md` - consuming ticket that owns finding disposition.
- `.loom/evidence/20260514-loom-weaver-codex-agent-followup-validation.md` - later evidence that the finding was fixed and Codex route changed.
