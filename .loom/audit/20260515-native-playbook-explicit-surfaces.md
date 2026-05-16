# Native Playbook Explicit Surfaces Audit

ID: audit:20260515-native-playbook-explicit-surfaces
Type: Audit
Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Audited: 2026-05-15 22:18 UTC
Target: ticket:20260515-native-playbook-explicit-surfaces

## Summary

Ralph audit reviewed the Claude, Cursor, and Codex explicit-only Playbook implementation against `ticket:20260515-native-playbook-explicit-surfaces` ACC-001 through ACC-005. The verdict was clear with no material findings within scope.

## Target

The audit targeted native Playbook plugin surfaces for Claude Code, Cursor, and Codex: manifest metadata, all 25 Playbook `SKILL.md` frontmatter files, and all 25 Codex `agents/openai.yaml` policy files.

The audit did not target OpenCode, Gemini, broad docs, final activation tests, package pack output, or live runtime invocation in Claude, Cursor, or Codex.

## Audit Scope And Lenses

Scope:

- Challenge ACC-001 through ACC-005 for the native adapter ticket.
- Verify Claude and Cursor explicit-only metadata coverage.
- Verify Codex explicit-only policy coverage and absence of unsupported custom slash-command claims.
- Challenge the shared-body strategy for ACC-004.
- Check changed native product-visible content for contributor-only leakage.

Lenses:

- acceptance
- explicit-only semantics
- scope
- evidence sufficiency
- product-surface leakage
- downstream risk

## Context And Evidence Reviewed

- Ralph packet: `packet:20260515T221555Z-native-playbook-explicit-surfaces-audit` - bounded review contract and returned audit output.
- `ticket:20260515-native-playbook-explicit-surfaces` - target ticket acceptance and current state.
- `packet:20260515T220601Z-native-playbook-explicit-surfaces` - implementation packet and worker output.
- `ticket:20260515-playbook-macro-catalog` - prerequisite catalog ticket.
- `audit:20260515-playbook-macro-catalog` - clear audit of the catalog seam.
- `plan:20260515-playbook-explicit-macros` - sequencing and remaining work.
- `spec:playbook-explicit-macros` - behavior contract.
- `research:20260515-playbook-command-surfaces` - source-backed native adapter constraints.
- `AGENTS.md` - product-surface leakage and adapter constraints.
- `loom-playbooks/.claude-plugin/plugin.json` - Claude manifest.
- `loom-playbooks/.cursor-plugin/plugin.json` - Cursor manifest.
- `loom-playbooks/.codex-plugin/plugin.json` - Codex manifest and interface text.
- `loom-playbooks/skills/**/SKILL.md` - Playbook frontmatter and shared bodies.
- `loom-playbooks/skills/**/agents/openai.yaml` - Codex explicit-only policy files.

Observed validation from the Ralph audit run:

- 25 `disable-model-invocation: true` entries across 25 Playbook `SKILL.md` files.
- 25 `policy.allow_implicit_invocation: false` entries across 25 Playbook `agents/openai.yaml` files.
- Native plugin manifests keep `skills: "./skills/"` and describe Playbooks as explicit-only workflow lenses invoked deliberately after `loom-core` routing.
- Codex plugin metadata does not claim custom slash commands, custom prompt commands, or plugin-contributed command files.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `git diff --check` passed.
- Targeted leakage search found no material contributor-only leakage in changed native product-visible surfaces.

## Findings

None - no material findings within audited scope.

## Verdict

`clear` - ACC-001 through ACC-005 are supported within the reviewed scope. Claude and Cursor explicit-only behavior is supported by `disable-model-invocation: true` on all 25 Playbooks plus successful Claude plugin validation. Codex explicit-only behavior is supported by one `agents/openai.yaml` policy file per Playbook with `allow_implicit_invocation: false`, and Codex metadata avoids unsupported slash-command claims. The shared-body strategy is acceptable for this native explicit-only skill route because native adapter surfaces reuse the canonical Playbook `SKILL.md` corpus directly and add explicit-only metadata rather than copying divergent command bodies; true command-surface tickets should continue consuming the macro catalog body.

This verdict does not claim live Claude, Cursor, or Codex runtime invocation, Cursor or Codex validator coverage, Gemini conversion, OpenCode behavior, broad docs, tests, package pack output, or final activation behavior.

## Required Follow-up

- Close `ticket:20260515-native-playbook-explicit-surfaces` if the consuming ticket accepts the runtime-validation limits as residual risk.
- Handle Gemini command conversion in `ticket:20260515-gemini-playbook-commands`.
- Handle docs, tests, and final activation validation in `ticket:20260515-playbook-explicit-macro-docs-tests`.
- True command-surface tickets should continue using `readPlaybookMacroCatalog().body`; native explicit-only skill adapters intentionally rely on explicit-only metadata plus the shared `SKILL.md` body source.

## Residual Risk

- Runtime behavior depends on Claude, Cursor, and Codex honoring the researched explicit-only metadata. This audit observed Claude plugin validation and source inspection, not live runtime invocation.
- Cursor and Codex native validators were not run because no validator commands were listed in the repository instructions or required by the packet.
- Native explicit-only skill surfaces do not include the generated macro preamble from `readPlaybookMacroCatalog().body`; explicit-only metadata carries the invocation boundary for these adapters.

## Related Records

- `ticket:20260515-native-playbook-explicit-surfaces` - consuming ticket.
- `packet:20260515T221555Z-native-playbook-explicit-surfaces-audit` - Ralph review packet that produced this verdict.
- `packet:20260515T220601Z-native-playbook-explicit-surfaces` - implementation packet reviewed by this audit.
- `audit:20260515-playbook-macro-catalog` - prior clear audit for the shared catalog seam.
- `spec:playbook-explicit-macros` - behavior contract.
