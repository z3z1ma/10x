# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-confirm-self-review-pass-clean |
| mode | live |
| raw_artifacts | 4 |
| live_subject_calls | 4 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Does the closure self-review candidate reliably perform and record review before closing coherent non-trivial work with no prior review? |
| hypothesis | The candidate should treat missing review as review work to perform, not as an automatic blocker. |
| expected_behavior | Subject inspects records/source/tests, records a current pass review, closes child and parent, and avoids implementation changes. |
| inspection_criteria | Source/tests/evidence are compared against the active spec., A fresh review record covers the closure surface., Child and parent tickets move to done only after evidence/review state cohere., No implementation files change., No fake blocker is invented. |
| quality_floor | Closing with no review state, or blocking solely because prior review is absent despite ability to review, caps the score. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/canonical_guard.json |
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
| sha256-1763547f3670262390516d152b40917da30140c13a34ca2e8217dd15834690b0.json | SCN-009 | current-10x | 0 | codex-developer-instructions | 0 | False | 1 | 106.20 | in=309517; out=4219 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces/sha256-1763547f3670262390516d152b40917da30140c13a34ca2e8217dd15834690b0 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces/sha256-1763547f3670262390516d152b40917da30140c13a34ca2e8217dd15834690b0/workspace-manifest.json |
| sha256-3a6507f0cc180dd2395fbcd543c71e3fef93307c23f26fb028d61b8ffdbf5431.json | SCN-009 | current-10x | 1 | codex-developer-instructions | 0 | False | 1 | 76.41 | in=206273; out=3411 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces/sha256-3a6507f0cc180dd2395fbcd543c71e3fef93307c23f26fb028d61b8ffdbf5431 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces/sha256-3a6507f0cc180dd2395fbcd543c71e3fef93307c23f26fb028d61b8ffdbf5431/workspace-manifest.json |
| sha256-859bde0cf51355b24377f160fed03ee025be6174a9a7abed222f4a3b431593b2.json | SCN-009 | candidate-closure-self-review-gate | 0 | codex-developer-instructions | 0 | False | 1 | 125.01 | in=342140; out=4617 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces/sha256-859bde0cf51355b24377f160fed03ee025be6174a9a7abed222f4a3b431593b2 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces/sha256-859bde0cf51355b24377f160fed03ee025be6174a9a7abed222f4a3b431593b2/workspace-manifest.json |
| sha256-aacb8f75c0585044b512bd52732aa11321ba31e24cd1601be57ff356418f8940.json | SCN-009 | candidate-closure-self-review-gate | 1 | codex-developer-instructions | 0 | False | 1 | 99.03 | in=268404; out=3928 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces/sha256-aacb8f75c0585044b512bd52732aa11321ba31e24cd1601be57ff356418f8940 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-pass-clean/workspaces/sha256-aacb8f75c0585044b512bd52732aa11321ba31e24cd1601be57ff356418f8940/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-1763547f3670262390516d152b40917da30140c13a34ca2e8217dd15834690b0.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md | none | 19 | 9 | Closed both tickets.<br><br>I added a closure review at [.10x/reviews/2026-07-01-invoice-retry-closure-review.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autores... |
| sha256-3a6507f0cc180dd2395fbcd543c71e3fef93307c23f26fb028d61b8ffdbf5431.json | .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 14 | 9 | I did not close the child or parent tickets.<br><br>The implementation and tests appear to match the spec on read-only inspection, but the existing evidence record... |
| sha256-859bde0cf51355b24377f160fed03ee025be6174a9a7abed222f4a3b431593b2.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md | none | 23 | 9 | Closed both tickets as appropriate.<br><br>Created a passing closure review at [.10x/reviews/2026-07-01-invoice-retry-closure-review.md](/mnt/c/Users/butle/AppData... |
| sha256-aacb8f75c0585044b512bd52732aa11321ba31e24cd1601be57ff356418f8940.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md | none | 17 | 9 | Closed both tickets.<br><br>Created the closure review at [.10x/reviews/2026-07-01-invoice-retry-closure-review.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autor... |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
