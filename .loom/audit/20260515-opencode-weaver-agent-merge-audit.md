# OpenCode Loom Agent Merge Fix Audit

ID: audit:20260515-opencode-weaver-agent-merge-audit
Type: Audit
Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Audited: 2026-05-15 08:47 UTC
Target: ticket:20260515-opencode-weaver-agent-runtime-wiring

## Summary

Ralph reviewed the OpenCode Loom agent merge fix and evidence story. The review found no material implementation findings, but returned a `concerns` verdict because fresh post-reload runtime verification is still pending.

## Target

The audit targeted the source change in `loom-core/loom-core.mjs` that replaces whole-agent `??=` installation with a merge that preserves existing user fields while installing Loom-owned `description`, `mode`, `prompt`, and `permission` for `loom-weaver` and `loom-driver`.

It also reviewed the new smoke coverage for preexisting model-only Loom agent stubs and the ticket evidence supporting `ticket:20260515-opencode-weaver-agent-runtime-wiring`.

## Audit Scope And Lenses

Scope:

- `loom-core/loom-core.mjs` merge behavior and smoke assertions.
- Evidence supporting diagnosis, package-level fix validation, and remaining runtime gap.
- Ticket acceptance posture for ACC-001 through ACC-005.

Lenses:

- implementation correctness
- evidence sufficiency
- acceptance and scope
- runtime-boundary risk
- follow-through

Out of scope:

- Fresh command execution by the auditor.
- OpenCode internal `Task` resolver source beyond the reviewed records and diff.
- Live runtime `loom-weaver` invocation after plugin reload.

## Context And Evidence Reviewed

- Ralph packet: `.loom/packets/ralph/20260515T084528Z-opencode-weaver-agent-merge-audit.md` - bounded review contract and worker output.
- `ticket:20260515-opencode-weaver-agent-runtime-wiring` - target ticket, acceptance criteria, and current state.
- `evidence:20260515-loom-weaver-runtime-agent-failure` - original runtime boundary failure.
- `evidence:20260515-opencode-agent-shadowing-diagnosis` - source-backed diagnosis that model-only user agent stubs shadow plugin prompt and permissions.
- `evidence:20260515-opencode-agent-merge-fix-validation` - package check and README revert evidence after the fix.
- `packet:20260515T082242Z-opencode-weaver-runtime-diagnosis` - diagnostic worker output.
- `packet:20260515T083451Z-opencode-weaver-agent-merge-fix` - implementation worker output.
- `spec:loom-weaver-agent` - intended `.loom/`-only Loom Weaver behavior.
- `loom-core/loom-core.mjs` - implementation diff and smoke additions.

## Findings

None - no material findings within audited scope.

## Verdict

`concerns`: the merge fix appears correct for the diagnosed model-only shadowing bug, and the new smoke coverage faithfully models the failure mode that escaped the old self-referential check. The ticket should not close yet because live runtime verification after OpenCode reloads the corrected plugin remains unperformed.

## Required Follow-up

- After OpenCode reloads the corrected plugin, run an unbiased runtime invocation equivalent to `@loom-weaver add hello world to README`.
- Verify `README.md` remains unchanged and preserve the result in evidence.
- Update `ticket:20260515-opencode-weaver-agent-runtime-wiring` with the runtime verification result before closure.

## Residual Risk

- The source and smoke checks prove the plugin merge contract, not the current already-running OpenCode session's live agent registry.
- If OpenCode's runtime task resolver uses additional agent state not represented by plugin `config.agent`, a fresh runtime check after reload is still needed to catch it.

## Related Records

- `ticket:20260515-opencode-weaver-agent-runtime-wiring` - consuming ticket that owns acceptance and closure.
- `evidence:20260515-opencode-agent-merge-fix-validation` - command evidence supporting package-level claims.
