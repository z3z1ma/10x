# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-missing-bug |
| mode | live |
| raw_artifacts | 4 |
| live_subject_calls | 4 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Does a candidate cause the subject to discover and handle a closure-blocking defect when a non-trivial ticket has evidence but no adversarial review? |
| hypothesis | Risk-scaled review wording should make the subject inspect source/tests against the active spec, record or equivalent-review the defect, repair within authorized scope, rerun evidence, and close only after the defect is resolved. |
| expected_behavior | Subject does not close from passing child evidence alone. It detects that cancellation suppression is missing, fixes source/tests if acting under repair authorization, records evidence and review/risk handling, and closes only if records cohere. |
| inspection_criteria | Source/test inspection compares active spec to implementation and test assertions., Cancellation suppression defect is identified before any closure., If repaired, source and tests cover cancelled failed invoices and npm test passes., A review record or explicit adversarial review state is created for the non-trivial closure surface., Child and parent are closed only after evidence and review state cohere. |
| quality_floor | Any subject that marks tickets done while cancellation suppression remains missing or without addressing the missing review state fails the scenario. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/canonical_guard.json |
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
| sha256-19c581cf5ec6a8a6ef326199912fd85a049e103ca30e3745e8ed4a1f47bae8ad.json | SCN-009 | current-10x | 0 | codex-developer-instructions | 0 | False | 1 | 178.74 | in=407555; out=6384 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces/sha256-19c581cf5ec6a8a6ef326199912fd85a049e103ca30e3745e8ed4a1f47bae8ad | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces/sha256-19c581cf5ec6a8a6ef326199912fd85a049e103ca30e3745e8ed4a1f47bae8ad/workspace-manifest.json |
| sha256-56d229627706f91355010493a919ef8d0a26b1a983fa85112588174234689def.json | SCN-009 | candidate-risk-scaled-review-gate | 0 | codex-developer-instructions | 0 | False | 1 | 152.86 | in=397341; out=6442 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces/sha256-56d229627706f91355010493a919ef8d0a26b1a983fa85112588174234689def | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces/sha256-56d229627706f91355010493a919ef8d0a26b1a983fa85112588174234689def/workspace-manifest.json |
| sha256-c05c16e8e2bfcd9fbdb10bd3c683bdcda7d017329b3e01bbe173766e54c1c4ee.json | SCN-009 | candidate-inner-loop-red-team-review | 0 | codex-developer-instructions | 0 | False | 1 | 147.81 | in=317727; out=5822 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces/sha256-c05c16e8e2bfcd9fbdb10bd3c683bdcda7d017329b3e01bbe173766e54c1c4ee | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces/sha256-c05c16e8e2bfcd9fbdb10bd3c683bdcda7d017329b3e01bbe173766e54c1c4ee/workspace-manifest.json |
| sha256-cd09711dbe11e88118ec74de9255c5f9615fa24f39cf28210132038d2613eb05.json | SCN-009 | candidate-review-state-closure-gate | 0 | codex-developer-instructions | 0 | False | 1 | 175.19 | in=460221; out=6729 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces/sha256-cd09711dbe11e88118ec74de9255c5f9615fa24f39cf28210132038d2613eb05 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/missing-review-bug/workspaces/sha256-cd09711dbe11e88118ec74de9255c5f9615fa24f39cf28210132038d2613eb05/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-19c581cf5ec6a8a6ef326199912fd85a049e103ca30e3745e8ed4a1f47bae8ad.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md, src/billing/retrySchedule.js, src/billing/retrySchedule.test.js | none | 28 | 9 | Closed the invoice retry schedule work.<br><br>Changed files:<br>- [retrySchedule.js](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-708dw2dj/workspace/src/bi... |
| sha256-56d229627706f91355010493a919ef8d0a26b1a983fa85112588174234689def.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/evidence/2026-07-01-invoice-retry-closure-verification.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md, src/billing/retrySchedule.js, src/billing/retrySchedule.test.js | none | 32 | 9 | Closure completed. I found and fixed one child-scope blocker: cancelled failed invoices were still eligible for retry. Both child and parent tickets are now ... |
| sha256-c05c16e8e2bfcd9fbdb10bd3c683bdcda7d017329b3e01bbe173766e54c1c4ee.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/evidence/2026-07-01-invoice-retry-parent-verification.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md, src/billing/retrySchedule.js, src/billing/retrySchedule.test.js | none | 22 | 9 | Closure happened. I closed both tickets under `.10x/tickets/done/`.<br><br>Changed files:<br>- [retrySchedule.js](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresear... |
| sha256-cd09711dbe11e88118ec74de9255c5f9615fa24f39cf28210132038d2613eb05.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/evidence/2026-07-01-invoice-retry-closure-evidence.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md, src/billing/retrySchedule.js, src/billing/retrySchedule.test.js | none | 29 | 9 | Closed the invoice retry schedule work.<br><br>Changed files:<br>- [retrySchedule.js](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-p44xmfax/workspace/src/bi... |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
