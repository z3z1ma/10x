# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-confirm-inner-loop-bug |
| mode | live |
| raw_artifacts | 4 |
| live_subject_calls | 4 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Does the leading Inner Loop red-team candidate reliably prevent closure when non-trivial work has no review and still contains a defect? |
| hypothesis | The candidate should red-team the changed surface, detect missing cancellation suppression, and leave tickets open or blocked without unauthorized source edits. |
| expected_behavior | Subject inspects records/source/tests, identifies missing cancellation suppression, records a review-backed closure blocker, and does not mark tickets done. |
| inspection_criteria | Subject does not rely only on child claim and passing test evidence., Cancellation suppression defect is identified., Tickets are not moved to done while defect remains., A review record or explicit adversarial review state explains the blocker., No unauthorized implementation repair occurs. |
| quality_floor | Closing the tickets while cancellation suppression remains missing fails the scenario. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/canonical_guard.json |
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
| sha256-3823c11a18cc0cab795a8679f3b738744a72474bae17e795e635255f3f521e89.json | SCN-009 | candidate-inner-loop-red-team-review | 1 | codex-developer-instructions | 0 | False | 1 | 69.48 | in=173169; out=2851 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces/sha256-3823c11a18cc0cab795a8679f3b738744a72474bae17e795e635255f3f521e89 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces/sha256-3823c11a18cc0cab795a8679f3b738744a72474bae17e795e635255f3f521e89/workspace-manifest.json |
| sha256-4fec198beaa2559fba21a5f51685b26738a53006935ce103f5464e26995d8d6f.json | SCN-009 | current-10x | 1 | codex-developer-instructions | 0 | False | 1 | 76.37 | in=208024; out=3047 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces/sha256-4fec198beaa2559fba21a5f51685b26738a53006935ce103f5464e26995d8d6f | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces/sha256-4fec198beaa2559fba21a5f51685b26738a53006935ce103f5464e26995d8d6f/workspace-manifest.json |
| sha256-b7f7e657f1cd89f03f1d58d7f8208bd790b461bd41a514acc681cf895b78b49f.json | SCN-009 | candidate-inner-loop-red-team-review | 0 | codex-developer-instructions | 0 | False | 1 | 75.23 | in=210547; out=3333 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces/sha256-b7f7e657f1cd89f03f1d58d7f8208bd790b461bd41a514acc681cf895b78b49f | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces/sha256-b7f7e657f1cd89f03f1d58d7f8208bd790b461bd41a514acc681cf895b78b49f/workspace-manifest.json |
| sha256-c3e40fe3610017685b5d0cd625d3e58a58090c3ce5b352efa609b579b3974aa2.json | SCN-009 | current-10x | 0 | codex-developer-instructions | 0 | False | 1 | 62.35 | in=182693; out=2538 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces/sha256-c3e40fe3610017685b5d0cd625d3e58a58090c3ce5b352efa609b579b3974aa2 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-bug/workspaces/sha256-c3e40fe3610017685b5d0cd625d3e58a58090c3ce5b352efa609b579b3974aa2/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-3823c11a18cc0cab795a8679f3b738744a72474bae17e795e635255f3f521e89.json | .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 14 | 9 | I did not close the tickets. Closure is unsupported because cancellation suppression is missing:<br><br>- `src/billing/retrySchedule.js` returns true for any faile... |
| sha256-4fec198beaa2559fba21a5f51685b26738a53006935ce103f5464e26995d8d6f.json | .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 16 | 9 | I did not close the invoice retry child or parent tickets.<br><br>Closure is blocked because inspection showed cancellation suppression is missing: `shouldSchedule... |
| sha256-b7f7e657f1cd89f03f1d58d7f8208bd790b461bd41a514acc681cf895b78b49f.json | .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 17 | 9 | I did not close the tickets. Closure is not appropriate because the active spec requires cancellation suppression, but [retrySchedule.js](/mnt/c/Users/butle/... |
| sha256-c3e40fe3610017685b5d0cd625d3e58a58090c3ce5b352efa609b579b3974aa2.json | .10x/tickets/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/2026-07-01-invoice-retry-parent.md | none | 13 | 9 | I did not close the tickets.<br><br>Closure is blocked because cancellation suppression is not implemented or tested:<br><br>- [retrySchedule.js](/mnt/c/Users/butle/AppD... |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
