Status: done
Created: 2026-06-27
Updated: 2026-06-27
Depends-On: .10x/specs/10x-autoresearch-loop.md, .10x/decisions/autoresearch-live-trial-scientist-inspection.md

# Add OpenCode Autoresearch Harness

## Scope

Add OpenCode as a live subject harness for the existing 10x autoresearch loop
without changing the scientist-led method.

Included:

- Support experiment definitions with `harness: opencode-cli` and OpenCode
  model IDs such as `openai/gpt-5.5`.
- Preserve the existing registered scientific contract, arms, scenarios,
  budgets, workspace isolation, command metadata, prompts, raw artifacts,
  workspace archives, summaries, reports, and canonical guard behavior.
- Keep Codex behavior backward-compatible while introducing generic
  `live_subject_calls` metadata.
- Add a small harness adapter boundary that future subject CLIs can reuse
  without adding a loop controller or automatic scoring.
- Update docs, template, and active spec wording so a fresh scientist can choose
  Codex or OpenCode without guessing.
- Verify with unit tests, dry-run planning, OpenCode CLI help/latest docs, and
  at least one empirical OpenCode trial if the local environment can run it.
- Record evidence and adversarial review before closure.

Excluded:

- Reintroducing fixture-backed scoring, calibration labels, or answer keys.
- Mutating canonical `SKILL.md`.
- Adding scheduler, daemon, queue, database, or promotion automation.
- Delegating scientist rubric judgment to the runner.

## Acceptance Criteria

- AC-001: `run_once.py` accepts both `codex-cli` and `opencode-cli` harness
  definitions through one clear live-subject path.
- AC-002: OpenCode samples write parity artifacts under `<out>/opencode/`,
  including command metadata, process output, prompts, raw artifacts, workspace
  manifests, archived workspaces, `summary.json`, `plan.json`, and report rows.
- AC-003: Raw artifacts expose `live_subject_calls` and preserve
  `live_codex_calls` for backward compatibility.
- AC-004: OpenCode command construction is based on current official docs and
  local help where available, and uses provider/model syntax for
  `openai/gpt-5.5`.
- AC-005: Documentation and the experiment template explain supported harness
  values, artifact paths, and OpenCode prerequisites without adding a second
  way to run the loop.
- AC-006: Unit tests and validation pass.
- AC-007: Empirical dry-run and live-run evidence is recorded, with any
  environment limitation stated plainly.
- AC-008: Adversarial review passes or records residual risk with a durable
  owner before the ticket is closed.

## Progress and Notes

- 2026-06-27: Opened from user request to add OpenCode support with
  `openai/gpt-5.5`, preserve parity, empirically test, review, commit, and
  push.
- 2026-06-27: Renamed the generalized lower-level live subject runner to
  `autoresearch/run_subject.py`; `run_once.py` remains the canonical one-shot
  loop command.
- 2026-06-27: Added `opencode-cli` support, generic `live_subject_calls`,
  OpenCode artifact directories, OpenCode JSON stdout/usage parsing, harness-
  aware reports, docs, knowledge, tests, and clean-rerun semantics.
- 2026-06-27: Verified with unit tests, validation, OpenCode 1.17.11 help,
  OpenAI OAuth credential inspection, dry-run planning, and a live
  `openai/gpt-5.5` smoke trial. Evidence:
  `.10x/evidence/2026-06-27-opencode-autoresearch-harness.md`. Research:
  `.10x/research/2026-06-27-opencode-cli-harness-research.md`. Review:
  `.10x/reviews/2026-06-27-opencode-autoresearch-harness-review.md`.

## Blockers

None.

## Closure

All acceptance criteria met. Residual risks are documented in the review and do
not block use: OpenCode must be installed on `PATH`, provider/model access can
change, and authenticated home state is outside complete runner control.
