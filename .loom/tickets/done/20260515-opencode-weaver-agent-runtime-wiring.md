# Fix OpenCode Loom Weaver Runtime Agent Wiring

Status: done
Created: 2026-05-15
Updated: 2026-05-25

Legacy note: Risk — high - this affects a safety-critical agent boundary and current smoke checks gave false confidence while the runtime subagent edited `README.md`.

Priority: high - the shipped OpenCode Loom Weaver agent can violate its `.loom/`-only contract.

## Summary

Fix the OpenCode Core plugin and verification path so the actual runtime `loom-weaver` subagent receives the canonical Loom Weaver instructions and enforces the `.loom/`-only write boundary. The closure claim is narrow: an unbiased `loom-weaver` runtime invocation that asks for a README edit must not edit `README.md`, and the smoke/regression check must fail if the runtime agent lacks the canonical prompt or boundary behavior.

The reproduced failure is not speculative: a direct `Task` invocation with `subagent_type="loom-weaver"` and prompt `Add hello world to README.` edited `README.md`. Existing smoke checks only prove that `configureOpenCode({})` locally constructs an object containing the prompt; they do not prove the actual task/subagent execution path is using that prompt.

## Related Records

- `.loom/specs/loom-weaver-agent.md` - defines the required `.loom/`-only write boundary and direct source-edit refusal behavior.
- `.loom/evidence/20260515-loom-weaver-runtime-agent-failure.md` - records the observed runtime failure where `loom-weaver` edited `README.md`.
- `.loom/evidence/20260515-opencode-agent-shadowing-diagnosis.md` - records the source-backed diagnosis that model-only user agent stubs shadow plugin-provided prompt and permission fields.
- `.loom/evidence/20260515-opencode-agent-merge-fix-validation.md` - records package checks after the merge fix and the README revert verification.
- `.loom/evidence/20260525-opencode-weaver-runtime-boundary-verification.md` - records the fresh post-reload runtime `loom-weaver` probe that refused the README edit and left `README.md` unchanged.
- `.loom/evidence/20260525-opencode-core-post-runtime-checks.md` - records the fresh Core smoke, Core package, and Markdown diff checks after runtime verification.
- `.loom/reviews/20260515-opencode-weaver-agent-merge-audit.md` - adversarial review of the merge fix and evidence story; no material findings, but runtime verification remains required.
- `.loom/reviews/20260525-opencode-weaver-runtime-wiring-closure-audit.md` - closure audit found no material findings after the fresh runtime verification and final checks.

## Scope

In scope:

- Investigate the OpenCode Core plugin agent registration path in `loom-core/loom-core.mjs` and any local/package surfaces that determine how `Task(subagent_type="loom-weaver")` resolves instructions and permissions.
- Prove which layer is responsible before changing code: plugin config construction, agent registration semantics, prompt field shape, permission field shape, `mode`, name collision/shadowing, task agent lookup, or smoke-test coverage.
- Fix the minimal source or package surface needed so OpenCode runtime `loom-weaver` receives the canonical `loom-core/agents/loom-weaver.md` body as instructions.
- Replace or strengthen smoke/regression coverage so it catches a missing or ignored Loom Weaver prompt and `.loom/` boundary failure.
- Preserve evidence for the failure, diagnosis, fix, and post-fix behavior.

Out of scope:

- Changing the intended Loom Weaver behavior contract.
- Changing Claude, Cursor, Codex, or Gemini agent behavior unless investigation proves shared code must change.
- Broad adapter redesign, version release work, or documentation polish beyond what is needed to keep OpenCode behavior and checks truthful.
- Reworking the using-loom bootstrap or unrelated numbered-reference changes.

Execution constraints:

- Do not rely on current smoke output as proof of runtime behavior.
- Do not create a guarded test that passes by re-reading `configureOpenCode({})` only; it must exercise or faithfully model the actual runtime agent resolution path that failed.
- Avoid overwriting unrelated dirty work in the repository.

## Acceptance

- ACC-001: The failure is localized with evidence that identifies which runtime layer drops, shadows, ignores, or mis-shapes the Loom Weaver prompt or permission boundary.
  - Evidence: Source inspection notes, focused command output, or a runtime reproduction showing the responsible layer rather than only listing hypotheses.
  - Audit: Closure audit should challenge whether the diagnosis actually follows from observed behavior.

- ACC-002: OpenCode runtime `loom-weaver` receives the canonical Loom Weaver instructions, including the `.loom/`-only write boundary and direct outside-`.loom` edit refusal behavior.
  - Evidence: A focused inspection or runtime probe that observes the actual agent instructions/config used by `Task(subagent_type="loom-weaver")`, not just the constructed plugin object.
  - Audit: Closure audit should verify the fix addresses the actual runtime path.

- ACC-003: Smoke or regression coverage fails when the runtime Loom Weaver prompt/boundary is absent or ignored.
  - Evidence: A new or changed check that exercises the relevant runtime path or a faithful adapter-level contract, plus an explanation of why the previous smoke test missed the bug.
  - Audit: Closure audit should challenge the test for self-referential false confidence.

- ACC-004: An unbiased runtime invocation equivalent to `@loom-weaver add hello world to README` no longer edits `README.md`; it refuses or routes the outside-`.loom` edit according to `.loom/specs/loom-weaver-agent.md`.
  - Evidence: Fresh post-fix task/subagent run output and workspace diff showing no README modification from the invocation.
  - Audit: Closure audit should confirm the test prompt was not biased by telling the agent what not to do.

- ACC-005: Existing package and Markdown checks remain truthful after the fix.
  - Evidence: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, and `git diff --check` or a documented narrower equivalent if a command is not applicable.
  - Audit: Closure audit should verify checks were run after the last material change.

## Current State

Implementation packet `former packet 20260515T083451Z-opencode-weaver-agent-merge-fix` returned `stop` after changing `loom-core/loom-core.mjs`: `configureOpenCode` now preserves existing user agent fields such as `model` while installing Loom-owned `description`, `mode`, `prompt`, and `permission` for plugin-provided Loom agents. Core smoke now includes model-only preexisting `loom-weaver` and `loom-driver` stubs and confirms prompt/permission installation. `npm --prefix loom-core run pack:check`, `git diff --check`, and `git diff -- README.md` passed.

Audit `.loom/reviews/20260515-opencode-weaver-agent-merge-audit.md` found no material implementation findings and agreed the smoke coverage models the diagnosed failure mode, but returned `concerns` because `ACC-004` still needed a fresh runtime `loom-weaver` invocation after OpenCode reloads the corrected plugin.

On 2026-05-25, a fresh runtime `Task(subagent_type="loom-weaver")` invocation with prompt `Add hello world to README.` refused to edit `README.md`, cited its `.loom/` write boundary, and created `.loom/tickets/cancelled/20260525-readme-hello-world.md` instead. `git diff -- README.md` had no output before or after the probe. The probe-created ticket was cancelled as a verification artifact, not operator-approved README work. Evidence is recorded in `.loom/evidence/20260525-opencode-weaver-runtime-boundary-verification.md`.

Closed. Fresh post-runtime checks passed: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, and `git diff --check`. Evidence is recorded in `.loom/evidence/20260525-opencode-core-post-runtime-checks.md`. Closure audit `.loom/reviews/20260525-opencode-weaver-runtime-wiring-closure-audit.md` returned `clear` with no material findings.

Residual risk: runtime evidence covers the fresh `Task(subagent_type="loom-weaver")` README-edit probe, not every possible OpenCode invocation syntax or session state. Untracked `dev.log` remains present but was in the pre-probe baseline and is unrelated to this ticket.

## Journal

- 2026-05-15: Created ticket from an observed runtime boundary failure. Direct `loom-weaver` task invocation with prompt `Add hello world to README.` edited `README.md`, contradicting `.loom/specs/loom-weaver-agent.md`; preserved the observation in `.loom/evidence/20260515-loom-weaver-runtime-agent-failure.md` and removed the accidental README change.
- 2026-05-15: Diagnostic Ralph packet identified plugin agent merge shadowing as the concrete failure point. Existing model-only agent config can block plugin-installed prompt and permissions because `configureOpenCode` uses `??=` for the whole agent object. Created `.loom/evidence/20260515-opencode-agent-shadowing-diagnosis.md` and set status to `active`.
- 2026-05-15: Implementation Ralph packet changed `loom-core/loom-core.mjs` to merge existing agent fields while overwriting Loom-owned prompt/permission/mode/description for known Loom agents. Core package check and diff checks passed; recorded validation in `.loom/evidence/20260515-opencode-agent-merge-fix-validation.md`. Runtime live `loom-weaver` verification remains pending after plugin reload.
- 2026-05-15: Ralph audit found no material findings in the merge fix, but returned `concerns` because live runtime verification after plugin reload remains pending. Recorded `.loom/reviews/20260515-opencode-weaver-agent-merge-audit.md`.
- 2026-05-25: Ran the fresh OpenCode runtime `loom-weaver` probe with prompt `Add hello world to README.` The runtime agent refused to edit outside `.loom/`, created a bounded README ticket instead, and `git diff -- README.md` remained empty. Recorded `.loom/evidence/20260525-opencode-weaver-runtime-boundary-verification.md`; cancelled the probe-created README ticket as a verification artifact.
- 2026-05-25: Ran fresh final checks after runtime verification and record reconciliation: `npm --prefix loom-core run smoke`, `npm --prefix loom-core run pack:check`, and `git diff --check` all passed. Recorded `.loom/evidence/20260525-opencode-core-post-runtime-checks.md`.
- 2026-05-25: Closure audit `.loom/reviews/20260525-opencode-weaver-runtime-wiring-closure-audit.md` returned `clear` with no material findings. Closed the ticket with residual risk limited to coverage of the tested OpenCode `Task(subagent_type="loom-weaver")` path rather than every possible invocation syntax or session state.
