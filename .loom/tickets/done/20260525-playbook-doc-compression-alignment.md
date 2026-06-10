# Playbook And Doc Compression Alignment

Status: done
Created: 2026-05-25
Updated: 2026-05-25

Legacy note: Risk — medium - aligns optional Playbook and documentation surfaces with compressed Core protocol without changing Core behavior.

Priority: medium - prevents drift after Core and agent compression.
Depends-On: .loom/tickets/done/20260525-agent-prompt-kernels.md

## Summary

Align Playbooks, generated command surfaces, and human docs with the compressed Loom protocol. The closure claim is that non-Core surfaces restate the protocol succinctly without becoming a second source of doctrine.

## Related Records

- `.loom/tickets/20260525-loom-protocol-compression.md` - owns sequencing and validation posture.
- `.loom/specs/loom-protocol-compression.md` - defines portability, product-surface hygiene, and validation requirements.
- `.loom/specs/playbook-explicit-macros.md` - owns Playbook invocation behavior.
- `.loom/tickets/done/20260525-agent-prompt-kernels.md` - provides settled Core/agent compression for downstream restatements.
- `AGENTS.md` - lists package docs, product-surface leakage, and validation constraints.
- `.loom/knowledge/playbook-activation-tests-procedure.md` - preserves Playbook activation validation limits and expectations.

## Scope

May change `loom-playbooks/playbooks/**`, `loom-playbooks/commands/*.toml`, `loom-playbooks/loom-playbooks.mjs` only if generated command output needs regeneration/alignment, root/package docs such as `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, package READMEs, and tests that directly validate command generation or activation behavior.

Do not change Core skills or agent prompts except for direct fixes discovered by validation that should be routed back to earlier tickets. Do not introduce Loom Mill implementation documentation into model-visible product doctrine.

First Ralph boundary: inspect Playbook and doc references to Core protocol language, shorten repeated doctrine, regenerate/check command surfaces if needed, and validate no Playbook becomes ambient model pressure.

Stop if alignment requires changing Playbook behavior beyond `.loom/specs/playbook-explicit-macros.md` or Core compression behavior.

## Acceptance

- ACC-001: Playbook macro/source language preserves Core routing, evidence, audit, ticket, and ticket-owned Ralph discipline without repeating full Core doctrine.
  - Evidence: Source inspection against `.loom/specs/playbook-explicit-macros.md` and compressed Core surfaces.
  - Audit: Final audit should challenge Playbook drift or bypass behavior.

- ACC-002: Generated command surfaces are aligned with Playbook source when generation output is affected.
  - Evidence: Playbooks smoke/pack and targeted source/generated comparison.
  - Audit: Review should challenge stale generated files.

- ACC-003: Human docs restate the compressed protocol succinctly and do not become a second source of model doctrine.
  - Evidence: Source inspection of touched docs and targeted grep for stale verbose doctrine or product-surface leakage.
  - Audit: Final audit should inspect doc drift and leakage search limits.

- ACC-004: Playbook activation behavior remains explicit-only where required.
  - Evidence: Existing activation tests or targeted checks following `.loom/knowledge/playbook-activation-tests-procedure.md` when touched.
  - Audit: Review should challenge false-positive test gaps.

- ACC-005: Relevant validation passes.
  - Evidence: `npm --prefix loom-playbooks run smoke`, `npm --prefix loom-playbooks run pack:check`, relevant Core checks if Core is touched, and `git diff --check` outputs recorded or cited.
  - Audit: Final audit should inspect evidence sufficiency.

## Current State

Closed. First bounded run aligned Playbook source, generated command surfaces, and human docs as consumers of Core compression. Evidence is recorded at `.loom/evidence/20260525-playbook-doc-compression-alignment-validation.md`. Fresh-context audit is recorded at `.loom/reviews/20260525-playbook-doc-compression-alignment-audit.md` with a pass-with-non-blocking-risks verdict and no material findings. Residual risk: static/generation checks do not prove live natural-prompt behavior in every supported harness.

Files changed in this run:

- `loom-playbooks/playbooks/*/SKILL.md`
- `loom-playbooks/commands/*.toml`
- `loom-playbooks/loom-playbooks.mjs`
- `PROTOCOL.md`
- `ARCHITECTURE.md`
- `.loom/evidence/20260525-playbook-doc-compression-alignment-validation.md`
- `.loom/tickets/done/20260525-playbook-doc-compression-alignment.md`

Validation passed: before/after line counts, command regeneration, targeted source/generated command comparison, `npm --prefix loom-playbooks run smoke`, `npm --prefix loom-playbooks run pack:check`, `git diff --check`, targeted stale-doctrine/explicitness searches, and targeted product-surface leakage search. Core checks were not run because Core was not touched.

## Journal

- 2026-05-25: Created ticket with dependency on agent prompt compression.
- 2026-05-25: Set status to `active` after agent prompt compression closed.
- 2026-05-25: Bounded Playbook/doc alignment run compressed repeated Playbook routing prose, shortened generated macro preamble language, regenerated all 25 command TOML files, and trimmed full Core bootstrap file lists from human docs. Line count changed from 8,846 to 8,661 total lines across targeted Playbooks/docs/generated commands. Evidence recorded at `.loom/evidence/20260525-playbook-doc-compression-alignment-validation.md`; ticket moved to `review` pending fresh-context audit.
- 2026-05-25: Fresh-context audit recorded at `.loom/reviews/20260525-playbook-doc-compression-alignment-audit.md`. Verdict: pass with non-blocking risks; no material findings; residual risk is limited to live harness natural-prompt behavior not being exercised by this ticket's static/generation evidence.
- 2026-05-25: Coordinator closed ticket. ACC-001 through ACC-005 are supported by validation evidence and fresh-context audit; no source follow-up required by audit.
