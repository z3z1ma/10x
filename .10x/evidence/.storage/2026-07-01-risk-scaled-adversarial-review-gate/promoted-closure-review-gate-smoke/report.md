# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-promoted-closure-gate-smoke |
| mode | live |
| raw_artifacts | 3 |
| live_subject_calls | 3 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Does the promoted canonical review gate preserve the intended closure behavior across the three decisive scenarios? |
| hypothesis | The edited SKILL.md should create a review-backed clean closure, block a real defect, and preserve the exact trivial fast path. |
| expected_behavior | Current SKILL.md closes the clean non-trivial ticket with a review, does not close the defective ticket, and fixes only README.md for the trivial typo. |
| inspection_criteria | Clean pass scenario creates a fresh closure review and moves child and parent to done without implementation edits., Bug scenario detects missing cancellation suppression and does not move tickets to done., Trivial scenario edits only README.md and creates no .10x records., Canonical guard reports SKILL.md and autoresearch/program.md unchanged during the run. |
| quality_floor | Closing clean work without review, closing defective work, or adding review ceremony to trivial work fails the smoke check. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/canonical_guard.json |
| raw trial artifacts | 3 found |
| codex command metadata | 3 found |
| codex stdout JSONL | 3 found |
| codex stderr | 3 found |
| codex last assistant messages | 3 found |
| prompts | 3 found |
| instruction artifacts | 3 found |
| workspace manifests | 3 found |
| archived workspaces | 3 found |

## Trial Artifacts

| Artifact | Scenario | Arm | Rep | Instruction delivery | Command exits | Timed out | Turns | Wall seconds | Tokens | Archived workspace | Workspace manifest |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sha256-231b77113499d3f2a85dfc87ab78438bf93785587334078d90628ae9a3d2161b.json | SCN-010 | current-10x-promoted | 0 | codex-developer-instructions | 0 | False | 1 | 17.67 | in=106104; out=431 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/workspaces/sha256-231b77113499d3f2a85dfc87ab78438bf93785587334078d90628ae9a3d2161b | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/workspaces/sha256-231b77113499d3f2a85dfc87ab78438bf93785587334078d90628ae9a3d2161b/workspace-manifest.json |
| sha256-6cec388f1062e3ff437986cfc0f1254a08ac6d9c721c8902e625897f1b2b2b01.json | SCN-009 | current-10x-promoted | 0 | codex-developer-instructions | 0 | False | 1 | 47.63 | in=140329; out=1939 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/workspaces/sha256-6cec388f1062e3ff437986cfc0f1254a08ac6d9c721c8902e625897f1b2b2b01 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/workspaces/sha256-6cec388f1062e3ff437986cfc0f1254a08ac6d9c721c8902e625897f1b2b2b01/workspace-manifest.json |
| sha256-9c044aec5db523f740373654909a91c6a7e67b1224cc0409eae28ba361bc7864.json | SCN-009 | current-10x-promoted | 0 | codex-developer-instructions | 0 | False | 1 | 122.86 | in=342973; out=5181 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/workspaces/sha256-9c044aec5db523f740373654909a91c6a7e67b1224cc0409eae28ba361bc7864 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/promoted-closure-review-gate-smoke/workspaces/sha256-9c044aec5db523f740373654909a91c6a7e67b1224cc0409eae28ba361bc7864/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-231b77113499d3f2a85dfc87ab78438bf93785587334078d90628ae9a3d2161b.json | README.md | none | 3 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-32g2txxx/workspace/README.md:3): `succesful` → `successful`.<br><br>Verified the old spell... |
| sha256-6cec388f1062e3ff437986cfc0f1254a08ac6d9c721c8902e625897f1b2b2b01.json | none | none | 13 | 9 | I did not close either ticket.<br><br>Closure blocker: the child does not satisfy the active spec. The implementation still schedules retry for any failed invoice,... |
| sha256-9c044aec5db523f740373654909a91c6a7e67b1224cc0409eae28ba361bc7864.json | .10x/evidence/2026-07-01-invoice-retry-child-test-output.md, .10x/reviews/2026-07-01-invoice-retry-closure-review.md, .10x/tickets/done/2026-07-01-align-invoice-retry-schedule.md, .10x/tickets/done/2026-07-01-invoice-retry-parent.md | none | 26 | 9 | Closed both tickets as appropriate.<br><br>Changed only `.10x` records:<br>- Added closure review: [.10x/reviews/2026-07-01-invoice-retry-closure-review.md](/mnt/c/Us... |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
