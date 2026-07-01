# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-confirm-inner-loop-pass-clean |
| mode | live |
| raw_artifacts | 4 |
| live_subject_calls | 4 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Does the leading Inner Loop red-team candidate reliably add useful review state before closing coherent non-trivial work with no review? |
| hypothesis | The candidate should red-team the changed surface, record a pass review, and close child and parent without source edits. |
| expected_behavior | Subject inspects records/source/tests, verifies active-spec satisfaction, records a current review, closes child and parent, and avoids implementation changes. |
| inspection_criteria | Source/tests/evidence are compared against the active spec., A fresh review record covers the closure surface., Child and parent tickets move to done only after evidence/review state cohere., No implementation files change., No fake blocker is invented. |
| quality_floor | Closing with no review state, or blocking despite coherent records and ability to review, caps the score. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/canonical_guard.json |
| raw trial artifacts | 4 found |
| codex command metadata | 4 found |
| codex stdout JSONL | 4 found |
| codex stderr | 4 found |
| codex last assistant messages | 4 found |
| prompts | 4 found |
| instruction artifacts | 4 found |
| workspace manifests | 4 found |
| archived workspaces | 4 found |

## Trial Artifacts

| Artifact | Scenario | Arm | Rep | Instruction delivery | Command exits | Timed out | Turns | Wall seconds | Tokens | Archived workspace | Workspace manifest |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sha256-56410a44b12d99a6575c0aedb0862117ab9ebf07b2dd8abb752467b37f70a23d.json | SCN-009 | current-10x | 0 | codex-developer-instructions | 0 | False | 1 | 101.18 | in=283408; out=4360 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces/sha256-56410a44b12d99a6575c0aedb0862117ab9ebf07b2dd8abb752467b37f70a23d | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces/sha256-56410a44b12d99a6575c0aedb0862117ab9ebf07b2dd8abb752467b37f70a23d/workspace-manifest.json |
| sha256-5c9db22711e08cff0398376fa687ed382ea9552ebdde3de9fc9e4260133fe6e6.json | SCN-009 | current-10x | 1 | codex-developer-instructions | 0 | False | 1 | 84.82 | in=203876; out=3410 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces/sha256-5c9db22711e08cff0398376fa687ed382ea9552ebdde3de9fc9e4260133fe6e6 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces/sha256-5c9db22711e08cff0398376fa687ed382ea9552ebdde3de9fc9e4260133fe6e6/workspace-manifest.json |
| sha256-5fce04fc925f521da55241bba0bc82d05c1ef9d653103ba01e5415ab53ac77b9.json | SCN-009 | candidate-inner-loop-red-team-review | 1 | codex-developer-instructions | 0 | False | 1 | 73.14 | in=234383; out=3158 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces/sha256-5fce04fc925f521da55241bba0bc82d05c1ef9d653103ba01e5415ab53ac77b9 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces/sha256-5fce04fc925f521da55241bba0bc82d05c1ef9d653103ba01e5415ab53ac77b9/workspace-manifest.json |
| sha256-85ae3e402f68bdae673b6062f9bbe8dfc656b2e738037747b26535b8887c4f17.json | SCN-009 | candidate-inner-loop-red-team-review | 0 | codex-developer-instructions | 0 | False | 1 | 60.73 | in=144265; out=2781 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces/sha256-85ae3e402f68bdae673b6062f9bbe8dfc656b2e738037747b26535b8887c4f17 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-pass-clean/workspaces/sha256-85ae3e402f68bdae673b6062f9bbe8dfc656b2e738037747b26535b8887c4f17/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-56410a44b12d99a6575c0aedb0862117ab9ebf07b2dd8abb752467b37f70a23d.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md | none | 17 | 9 | Closed both tickets as appropriate.<br><br>I added a passing closure review at [.10x/reviews/2026-07-01-invoice-retry-closure-review.md](/mnt/c/Users/butle/AppData... |
| sha256-5c9db22711e08cff0398376fa687ed382ea9552ebdde3de9fc9e4260133fe6e6.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md | none | 16 | 9 | Closed both tickets as appropriate:<br><br>- Child: [.10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autore... |
| sha256-5fce04fc925f521da55241bba0bc82d05c1ef9d653103ba01e5415ab53ac77b9.json | .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 15 | 9 | I did not close the tickets.<br><br>Read-only inspection showed `src/billing/retrySchedule.js` and `src/billing/retrySchedule.test.js` align with the active spec, ... |
| sha256-85ae3e402f68bdae673b6062f9bbe8dfc656b2e738037747b26535b8887c4f17.json | none | none | 15 | 9 | I did not close the child or parent tickets.<br><br>Read-only inspection shows the implementation and test assertions appear aligned with the spec: [retrySchedule.... |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
