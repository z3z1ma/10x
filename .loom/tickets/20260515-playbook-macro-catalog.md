# Playbook Macro Catalog

ID: ticket:20260515-playbook-macro-catalog
Type: Ticket
Status: closed
Created: 2026-05-15
Updated: 2026-05-15
Risk: medium - establishes the shared source that later adapter packaging will consume.
Priority: high - adapter conversion tickets depend on this source or generation seam.

## Summary

Create the canonical Playbook macro catalog or generation seam for Loom Playbooks. The closure claim is that every existing Playbook is represented as an explicit optional workflow macro source, with content that preserves Loom loop order and can be consumed by downstream adapter tickets without copying divergent bodies by hand.

## Related Records

- `plan:20260515-playbook-explicit-macros` - decomposes the broader Playbook conversion and makes this the prerequisite unit.
- `spec:playbook-explicit-macros` - defines explicit macro behavior and evidence expectations.
- `research:20260515-playbook-command-surfaces` - constrains adapter targets that will consume the catalog.
- `research:20260515-playbooks-core-activation-pressure` - explains why the macro framing must avoid automatic activation pressure.
- `audit:20260515-playbook-macro-catalog` - clear Ralph-backed review of ACC-001 through ACC-005.
- `loom-playbooks/skills/` - current Playbook content source.

## Scope

May change `loom-playbooks/` files needed to create or expose a canonical macro catalog, such as a new adapter-neutral source directory, metadata files, or helper functions in `loom-playbooks/loom-playbooks.mjs` that read Playbook bodies.

May adjust Playbook headers, descriptions, and shared framing only as needed to make the catalog explicit-macro-ready, product-visible, and free of automatic trigger semantics.

Must not implement adapter-specific command registration, native plugin manifests, Gemini TOML files, docs, or activation tests except for narrow introspection needed to prove the catalog exists. Those belong to later tickets.

Must preserve Core routing: macro body text may add workflow pressure, but must not tell agents to bypass Core record skills, ticket shaping, evidence, audit, or Ralph packet procedures.

## Acceptance

- ACC-001: Every current Playbook under `loom-playbooks/skills/` is represented by the canonical macro catalog or generation seam with stable name, description, and body content usable by adapter tickets.
  - Evidence: Source inspection or package introspection lists the same Playbook set before and after the catalog change.
  - Audit: Review should challenge whether any Playbook was dropped, renamed without reason, or made ambiguous.

- ACC-002: Catalog descriptions and macro framing describe Playbooks as explicit optional workflow lenses rather than natural-language auto-activated skills.
  - Evidence: Targeted source inspection or grep over product-visible macro metadata and representative bodies.
  - Audit: Review should challenge whether broad trigger words remain positioned as mandatory first-action activation.

- ACC-003: Macro body content preserves Loom loop order and Core surface ownership.
  - Evidence: Source inspection of representative macro bodies, especially idea refinement, debugging, UI, source-driven development, incremental implementation, security, and release lenses.
  - Audit: Review should challenge whether macro content shortens required spec, plan, ticket, evidence, audit, or Ralph packet procedures.

- ACC-004: The catalog avoids adapter-specific body drift by providing a shared source or generation path for downstream command and explicit-only skill surfaces.
  - Evidence: Source inspection of the chosen catalog shape and any helper APIs.
  - Audit: Review should challenge whether later adapter tickets would still have to manually duplicate 25 bodies.

- ACC-005: Product-visible catalog content does not leak contributor-only package smoke, adapter mechanics, dogfood state, npm packaging, test harness details, or repository workflow commentary.
  - Evidence: Targeted grep/source inspection over the new or changed model-visible Playbook content.
  - Audit: Review should challenge product-surface leakage before downstream adapters propagate the content.

## Current State

Closed. Ralph packet `packet:20260515T213657Z-playbook-macro-catalog` added a derived macro catalog seam in `loom-playbooks/loom-playbooks.mjs`: `readPlaybookMacroCatalog()` wraps every current Playbook `SKILL.md` body with explicit optional macro framing, and `inspectPlaybookMacroCatalog()` verifies the generated catalog has one macro per Playbook with non-trigger-style catalog descriptions. Evidence gathered: Playbooks smoke passed with `skillCount: 25`, `macroCount: 25`, no missing macros, and no automatic description failures; package introspection showed the skill and macro name sets match exactly; representative macro inspection showed explicit framing for idea refinement, debugging, UI, source-driven development, incremental implementation, security, and release lenses; `git diff --check` passed.

Audit `audit:20260515-playbook-macro-catalog` returned `clear` with no material findings. ACC-001 through ACC-005 are satisfied for the catalog-only closure claim. Residual risk is intentionally routed to downstream adapter tickets: they must consume `readPlaybookMacroCatalog().body` instead of raw `SKILL.md` bodies, and OpenCode still registers `skills/` until `ticket:20260515-opencode-playbook-commands` runs.

## Journal

- 2026-05-15: Created ticket from `plan:20260515-playbook-explicit-macros`; adapter tickets are blocked on this shared catalog decision.
- 2026-05-15: Set status to active and launched `packet:20260515T213657Z-playbook-macro-catalog` for the canonical macro catalog implementation slice.
- 2026-05-15: `packet:20260515T213657Z-playbook-macro-catalog` returned `stop`: implemented a derived explicit macro catalog seam from the existing Playbook skill corpus, ran `npm --prefix loom-playbooks run smoke`, confirmed the macro set matches the 25-skill Playbook set, inspected representative macro framing, and ran `git diff --check`. Moved ticket to review because audit/acceptance review is the next closure step.
- 2026-05-15: Recorded clear Ralph-backed audit in `audit:20260515-playbook-macro-catalog` and closed the ticket. Adapter implementation tickets are unblocked.
