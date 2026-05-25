# Playbook Doc Compression Alignment Audit

ID: audit:20260525-playbook-doc-compression-alignment-audit
Type: Audit
Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Audited: 2026-05-25
Target: ticket:20260525-playbook-doc-compression-alignment

## Summary

Fresh-context Ralph audit reviewed the Playbook/doc compression alignment ticket, its validation evidence, related behavior specs, targeted source diffs, generated command surfaces, and rerun package checks. The pass found no blocking drift: Playbooks remain explicit optional macros, generated command files are synchronized, and docs restate the compressed protocol without becoming model-visible second doctrine.

## Target

The target was `ticket:20260525-playbook-doc-compression-alignment`, including its closure-readiness claims for `ACC-001` through `ACC-005`. The concrete file set reviewed was `loom-playbooks/playbooks/**/SKILL.md`, `loom-playbooks/commands/*.toml`, `loom-playbooks/loom-playbooks.mjs`, `PROTOCOL.md`, `ARCHITECTURE.md`, and the current git diff for those paths.

## Audit Scope And Lenses

Lenses used: acceptance, claim and evidence, generated-file drift, surface boundary, explicit Playbook behavior, product-surface leakage, and follow-through.

The pass challenged whether:

- Playbooks remain explicit optional macros instead of ambient natural-prompt skills.
- Playbook routing language preserves Core surface ownership, evidence, audit, ticket, and ticket-owned Ralph discipline without duplicating full Core doctrine.
- Generated TOML commands match the Playbook source and generator output.
- Human docs restate the compressed protocol succinctly without becoming the source of model doctrine.
- Evidence supports line counts, command generation, smoke/pack checks, explicit-only behavior claims, and leakage searches.

Out of scope: live OpenCode, Claude, Codex, Cursor, or Gemini natural-prompt harness runs; unrelated dirty Core compression changes already present in the worktree; broad quality review of every earlier compression ticket; and source fixes.

## Context And Evidence Reviewed

- Ralph review run: current session acting inside the ticket-owned bounded audit request from `ticket:20260525-playbook-doc-compression-alignment`.
- `.loom/tickets/20260525-playbook-doc-compression-alignment.md` - target ticket state, scope, acceptance, evidence expectations, and review posture.
- `.loom/evidence/20260525-playbook-doc-compression-alignment-validation.md` - validation dossier for line counts, generation, smoke/pack, diff check, explicit-only posture, and leakage searches.
- `.loom/specs/loom-protocol-compression.md` - compression behavior contract, especially `REQ-001`, `REQ-008`, and `REQ-009`.
- `.loom/specs/playbook-explicit-macros.md` - explicit Playbook macro behavior contract, especially `REQ-001`, `REQ-008`, `REQ-009`, `REQ-010`, `REQ-011`, `REQ-012`, and `REQ-013`.
- `.loom/knowledge/playbook-activation-tests-procedure.md` - validation limits for static command-registration smoke versus live natural-prompt behavior.
- `.loom/plans/20260525-loom-protocol-compression.md` - sequencing and stop conditions for Playbook/doc alignment.
- `AGENTS.md` - contributor constraints for product-surface leakage and validation commands.
- `loom-playbooks/loom-playbooks.mjs` - explicit macro preamble, command generation, OpenCode command registration, smoke inspection, and no Playbook skill-path registration.
- `loom-playbooks/playbooks/loom-test-driven-development/SKILL.md`, `loom-playbooks/playbooks/loom-parallel-worker-coordination/SKILL.md`, and `loom-playbooks/playbooks/loom-code-review-and-quality/SKILL.md` - representative Playbook source inspection for shortened Core routing and preserved evidence/audit/Ralph discipline.
- `loom-playbooks/commands/loom-test-driven-development.toml` - representative generated command inspection matching source plus generator preamble.
- `PROTOCOL.md` and `ARCHITECTURE.md` - human-doc restatements of compressed protocol and product boundary.
- `git status --short` - confirmed broader dirty worktree exists, with many unrelated Core compression changes outside this audit scope.
- `git diff -- loom-playbooks/playbooks loom-playbooks/commands loom-playbooks/loom-playbooks.mjs PROTOCOL.md ARCHITECTURE.md` - reviewed targeted diff shape.
- `git diff --stat -- loom-playbooks/playbooks loom-playbooks/commands loom-playbooks/loom-playbooks.mjs PROTOCOL.md ARCHITECTURE.md` - confirmed 53 targeted files changed with 134 insertions and 319 deletions.
- `npm --prefix loom-playbooks run smoke` - passed with `ok: true`, `doesNotPreloadCoreDoctrine: true`, `commandCount: 25`, `macroCount: 25`, no missing commands, no registered Playbook skill paths, and no explicit description prefix failures.
- `npm --prefix loom-playbooks run pack:check` - passed smoke and dry-run package check for 53 package files.
- `git diff --check` - passed with no output.
- Generated command catalog check - passed with `macrosOk: true`, `commandOk: true`, `macroCount: 25`, `commandCount: 25`, `missingCommands: []`, `registeredPlaybookSkillPaths: []`, `explicitDescriptionPrefixFailures: []`, and `staleCommands: []`.
- `wc -l loom-playbooks/playbooks/*/SKILL.md loom-playbooks/commands/*.toml README.md PROTOCOL.md ARCHITECTURE.md loom-core/README.md loom-playbooks/README.md` - current targeted total is 8,661 lines, matching the evidence dossier's after count.
- Targeted stale-doctrine searches over Playbook source, generated commands, `PROTOCOL.md`, and `ARCHITECTURE.md` - no stale verbose Playbook routing block or removed activation phrasing found in those touched surfaces.
- Targeted product-surface leakage search over `loom-playbooks` - only `doesNotPreloadCoreDoctrine` in `loom-playbooks/loom-playbooks.mjs` smoke output code matched; no model-visible Playbook body or command leakage was identified.

## Findings

None - no material findings within audited scope.

## Verdict

Pass with non-blocking risks. The inspected source, diff, generated command files, and rerun validation support the ticket's Playbook/doc alignment claims: Playbooks remain explicit optional macros, generated commands are synchronized with the canonical Playbook source and generator, Core routing/evidence/audit/ticket-owned Ralph discipline remains present in compressed Playbook language, and `PROTOCOL.md` / `ARCHITECTURE.md` stay human-facing restatements rather than model-visible second doctrine.

The verdict does not claim ticket closure by itself. It says no blocking audit findings were found in this pass, and the consuming ticket may use this audit alongside the evidence dossier when deciding closure.

## Required Follow-up

No blocking follow-up before closure from this audit pass.

Before closure, the ticket should explicitly carry the residual validation limit already stated in evidence: static package inspection and generation checks support explicit-only behavior, but they do not prove live natural-prompt behavior in every supported harness.

## Residual Risk

- Live harness behavior was not exercised. The audit did not run OpenCode, Claude, Codex, Cursor, or Gemini natural-prompt activation tests; it relied on static explicit-command registration, `disable-model-invocation: true` frontmatter, no Playbook skill-path registration, generated command checks, and prior knowledge about validation limits.
- The broader worktree contains many unrelated Core compression changes. This audit reviewed only the Playbook/doc alignment paths named in the target request and did not certify unrelated Core changes.
- Human docs were inspected for `PROTOCOL.md` and `ARCHITECTURE.md` because those were the changed docs in the targeted diff. Root/package README line counts were checked through the evidence command shape, but this pass did not perform a fresh full prose review of unchanged README content.
- Product-surface leakage search was targeted, not exhaustive semantic proof. It reduces risk for the listed leakage terms but cannot prove every possible contributor-facing phrase is absent.

## Related Records

- `ticket:20260525-playbook-doc-compression-alignment` - consuming ticket.
- `evidence:20260525-playbook-doc-compression-alignment-validation` - validation dossier this audit challenged.
- `spec:loom-protocol-compression` - compression and product-surface hygiene contract.
- `spec:playbook-explicit-macros` - explicit Playbook macro behavior contract.
- `knowledge:playbook-activation-tests-procedure` - explains live versus static activation validation limits.
- `plan:20260525-loom-protocol-compression` - parent compression plan.
