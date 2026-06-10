# Playbook Macro Catalog Audit

Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Target: .loom/tickets/done/20260515-playbook-macro-catalog.md

## Summary

Ralph audit reviewed the Playbook macro catalog implementation against `.loom/tickets/done/20260515-playbook-macro-catalog.md` ACC-001 through ACC-005. The verdict was clear with no material findings within scope.

## Target

The audit targeted the catalog-only implementation slice for `.loom/tickets/done/20260515-playbook-macro-catalog.md`, especially the diff in `loom-playbooks/loom-playbooks.mjs` that added `readPlaybookMacroCatalog()`, `inspectPlaybookMacroCatalog()`, explicit optional macro preamble framing, and smoke/introspection checks.

The review did not target downstream adapter command generation, native explicit-only packaging, Gemini TOML commands, docs, pack output, or activation tests.

## Audit Scope And Lenses

Scope:

- Challenge ACC-001 through ACC-005 for the catalog ticket.
- Review whether every Playbook is represented in the derived catalog.
- Review whether catalog-facing descriptions and bodies frame Playbooks as explicit optional macros.
- Review whether the seam prevents body drift for later adapter tickets.
- Review scope discipline and product-surface leakage risk.

Lenses:

- acceptance
- scope
- evidence sufficiency
- implementation fit
- product-surface leakage
- follow-through for downstream tickets

Out of scope:

- OpenCode command registration.
- Claude, Cursor, or Codex explicit-only packaging.
- Gemini command TOML files.
- Human-facing docs and activation tests.
- Exhaustive semantic review of every Playbook body beyond representative checks and catalog invariants.

## Context And Evidence Reviewed

- Ralph packet: `former packet 20260515T214608Z-playbook-macro-catalog-audit` - bounded audit contract and returned review output.
- `.loom/tickets/done/20260515-playbook-macro-catalog.md` - target ticket, acceptance, scope, current state, and closure question.
- `former packet 20260515T213657Z-playbook-macro-catalog` - implementation packet and worker output.
- `.loom/specs/playbook-explicit-macros.md` - behavior contract for explicit Playbook macros.
- `.loom/tickets/20260515-playbook-explicit-macros.md` - downstream sequencing and dependency context.
- `.loom/research/20260515-playbook-command-surfaces.md` - source-backed harness constraints.
- `.loom/research/20260515-playbooks-core-activation-pressure.md` - activation pressure failure mode.
- `.loom/evidence/20260515-playbook-activation-stacking.md` - prior observed stacking and test gap.
- `AGENTS.md` - product-surface leakage and package-shape constraints.
- `loom-playbooks/loom-playbooks.mjs` - implementation diff under review.
- `loom-playbooks/package.json` - package inclusion baseline.
- `loom-playbooks/skills/**/SKILL.md` - current Playbook corpus.

Observed validation from the Ralph audit run:

- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `skillCount: 25`, `macroCount: 25`, `macroChecks.ok: true`, no missing macros, and no automatic description failures.
- Node catalog invariant check passed with 25 skills, 25 macros, same ordered set, no missing or extra macros, no bad descriptions, no missing preambles, and no empty bodies.
- Representative macro inspection covered idea refinement, debugging, frontend UI engineering, source-driven development, incremental implementation, security and hardening, and shipping and launch.
- `git diff --check` passed.
- Targeted leakage search found no material contributor-only leakage. The only noted match was a generic debugging phrase, `test harness to system under test`, not package/test-harness leakage.

## Findings

None - no material findings within audited scope.

## Verdict

`clear` - Within the bounded audit scope, ACC-001 through ACC-005 are supported by source inspection and narrow validation. The implementation represents all 25 current Playbooks through the derived macro catalog, frames catalog descriptions and bodies as explicit optional workflow macros, preserves Core surface ownership and evidence/audit/Ralph discipline in representative checks, provides a shared exported seam that downstream adapter tickets can consume without copying bodies manually, and avoids material contributor-only leakage in reviewed product-visible macro content.

This verdict does not claim downstream adapter conversion, docs, pack output, or activation tests are complete.

## Required Follow-up

- Close `.loom/tickets/done/20260515-playbook-macro-catalog.md` if the consuming ticket accepts the residual risks as downstream-ticket concerns.
- Downstream adapter tickets should consume `readPlaybookMacroCatalog().body` rather than raw `SKILL.md` content so they preserve the explicit macro preamble.
- `.loom/tickets/done/20260515-opencode-playbook-commands.md` must remove OpenCode `config.skills.paths` registration for Playbooks; the catalog ticket intentionally did not do that.

## Residual Risk

- Later adapter tickets could accidentally bypass the catalog and copy raw Playbook bodies, losing the explicit macro preamble.
- OpenCode still registers `skills/` through `config.skills.paths` until `.loom/tickets/done/20260515-opencode-playbook-commands.md` runs.
- The audit used representative body checks rather than exhaustive semantic review of all 25 Playbook bodies.

## Related Records

- `.loom/tickets/done/20260515-playbook-macro-catalog.md` - consuming ticket that should disposition this audit.
- `former packet 20260515T214608Z-playbook-macro-catalog-audit` - Ralph review packet that produced the audit judgment.
- `former packet 20260515T213657Z-playbook-macro-catalog` - implementation packet reviewed by this audit.
- `.loom/specs/playbook-explicit-macros.md` - behavior contract the audit used.
