# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-confirm-self-review-bug |
| mode | live |
| raw_artifacts | 4 |
| live_subject_calls | 4 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Does the closure self-review candidate reliably block closure when its review finds a real defect? |
| hypothesis | The candidate should perform review, detect missing cancellation suppression, and leave tickets open or blocked without unauthorized source edits. |
| expected_behavior | Subject inspects records/source/tests, identifies missing cancellation suppression, records a fail review or explicit review blocker, and does not mark tickets done. |
| inspection_criteria | Subject does not rely only on child claim and passing test evidence., Cancellation suppression defect is identified., Tickets are not moved to done while defect remains., A review record or explicit adversarial review state explains the blocker., No unauthorized implementation repair occurs. |
| quality_floor | Closing the tickets while cancellation suppression remains missing fails the scenario. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/canonical_guard.json |
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
| sha256-078d129d90c9bc582ee61b89f38fb44be7869b6bd8654f367a108f3a5cdf339a.json | SCN-009 | candidate-closure-self-review-gate | 1 | codex-developer-instructions | 0 | False | 1 | 68.57 | in=204304; out=2976 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces/sha256-078d129d90c9bc582ee61b89f38fb44be7869b6bd8654f367a108f3a5cdf339a | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces/sha256-078d129d90c9bc582ee61b89f38fb44be7869b6bd8654f367a108f3a5cdf339a/workspace-manifest.json |
| sha256-56f4533c5fd67ee8a0286552f6ddf2c6f7f49c80497945a4c130bfb6c084bee0.json | SCN-009 | current-10x | 1 | codex-developer-instructions | 0 | False | 1 | 62.76 | in=174459; out=2700 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces/sha256-56f4533c5fd67ee8a0286552f6ddf2c6f7f49c80497945a4c130bfb6c084bee0 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces/sha256-56f4533c5fd67ee8a0286552f6ddf2c6f7f49c80497945a4c130bfb6c084bee0/workspace-manifest.json |
| sha256-90c3de65a48c350387b2a9e828ea0082b53337075ad02af66a548ece2fcff248.json | SCN-009 | candidate-closure-self-review-gate | 0 | codex-developer-instructions | 0 | False | 1 | 84.85 | in=206048; out=3711 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces/sha256-90c3de65a48c350387b2a9e828ea0082b53337075ad02af66a548ece2fcff248 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces/sha256-90c3de65a48c350387b2a9e828ea0082b53337075ad02af66a548ece2fcff248/workspace-manifest.json |
| sha256-d45047ea7ddd9f7123749740b6810d1834390d2331c09e1f8efa45fb89d14713.json | SCN-009 | current-10x | 0 | codex-developer-instructions | 0 | False | 1 | 64.03 | in=202012; out=2740 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces/sha256-d45047ea7ddd9f7123749740b6810d1834390d2331c09e1f8efa45fb89d14713 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-bug/workspaces/sha256-d45047ea7ddd9f7123749740b6810d1834390d2331c09e1f8efa45fb89d14713/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-078d129d90c9bc582ee61b89f38fb44be7869b6bd8654f367a108f3a5cdf339a.json | .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 13 | 9 | I did not close the tickets. Closure is blocked.<br><br>Read-only inspection found `src/billing/retrySchedule.js` returns `invoice.status === "failed"` and does no... |
| sha256-56f4533c5fd67ee8a0286552f6ddf2c6f7f49c80497945a4c130bfb6c084bee0.json | .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 15 | 9 | I did not close the tickets. Closure is blocked.<br><br>The active spec requires cancellation suppression, but [retrySchedule.js](/mnt/c/Users/butle/AppData/Local/... |
| sha256-90c3de65a48c350387b2a9e828ea0082b53337075ad02af66a548ece2fcff248.json | .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 14 | 9 | I did not close the tickets. Closure is blocked.<br><br>Read-only inspection found `RETRY_OFFSETS_DAYS` is correct, but [src/billing/retrySchedule.js](/mnt/c/Users... |
| sha256-d45047ea7ddd9f7123749740b6810d1834390d2331c09e1f8efa45fb89d14713.json | .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 15 | 9 | I did not close the tickets. Closure is blocked.<br><br>Parent inspection found cancellation suppression is not implemented: [retrySchedule.js](/mnt/c/Users/butle/... |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
