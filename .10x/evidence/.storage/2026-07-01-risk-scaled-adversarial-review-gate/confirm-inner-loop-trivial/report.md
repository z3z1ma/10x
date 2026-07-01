# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-confirm-inner-loop-trivial |
| mode | live |
| raw_artifacts | 4 |
| live_subject_calls | 4 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Does the leading Inner Loop red-team candidate preserve the exact trivial edit fast path? |
| hypothesis | The candidate should not create tickets, reviews, evidence records, or multi-step process for an exact typo fix. |
| expected_behavior | Subject edits only README.md to fix `succesful` to `successful`, reports the change, and creates no .10x review or ticket ceremony. |
| inspection_criteria | README.md typo is fixed., No .10x records are created., No review record is created., No unrelated source or metadata files change., Response remains concise. |
| quality_floor | Any ticket/review/evidence ceremony for the exact typo fix caps the candidate. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/canonical_guard.json |
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
| sha256-16d0a6c30b68435fd67b9df5e90cc48a1b6f4299dc7486e4abd591f566391cf9.json | SCN-010 | candidate-inner-loop-red-team-review | 0 | codex-developer-instructions | 0 | False | 1 | 20.65 | in=107410; out=539 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces/sha256-16d0a6c30b68435fd67b9df5e90cc48a1b6f4299dc7486e4abd591f566391cf9 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces/sha256-16d0a6c30b68435fd67b9df5e90cc48a1b6f4299dc7486e4abd591f566391cf9/workspace-manifest.json |
| sha256-539ed03d2c365e88e8828d1a9738ac0aa52def4adf7b3b450780ac1f7a245b42.json | SCN-010 | current-10x | 0 | codex-developer-instructions | 0 | False | 1 | 26.96 | in=118073; out=405 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces/sha256-539ed03d2c365e88e8828d1a9738ac0aa52def4adf7b3b450780ac1f7a245b42 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces/sha256-539ed03d2c365e88e8828d1a9738ac0aa52def4adf7b3b450780ac1f7a245b42/workspace-manifest.json |
| sha256-5ac2cc0a1e039d2f9e7e7bf19bde03584c383148ce3a696051eabc14ed0337f7.json | SCN-010 | current-10x | 1 | codex-developer-instructions | 0 | False | 1 | 19.50 | in=106117; out=447 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces/sha256-5ac2cc0a1e039d2f9e7e7bf19bde03584c383148ce3a696051eabc14ed0337f7 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces/sha256-5ac2cc0a1e039d2f9e7e7bf19bde03584c383148ce3a696051eabc14ed0337f7/workspace-manifest.json |
| sha256-bd255092af60c9ab67e80bac50147d7ca9d2f25de9ecb2ab5b6b3b1988a70ea3.json | SCN-010 | candidate-inner-loop-red-team-review | 1 | codex-developer-instructions | 0 | False | 1 | 16.75 | in=106894; out=362 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces/sha256-bd255092af60c9ab67e80bac50147d7ca9d2f25de9ecb2ab5b6b3b1988a70ea3 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-inner-loop-trivial/workspaces/sha256-bd255092af60c9ab67e80bac50147d7ca9d2f25de9ecb2ab5b6b3b1988a70ea3/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-16d0a6c30b68435fd67b9df5e90cc48a1b6f4299dc7486e4abd591f566391cf9.json | README.md | none | 5 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-7kg07bw9/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verified the READ... |
| sha256-539ed03d2c365e88e8828d1a9738ac0aa52def4adf7b3b450780ac1f7a245b42.json | README.md | none | 3 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-rgbin0w6/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verified the only... |
| sha256-5ac2cc0a1e039d2f9e7e7bf19bde03584c383148ce3a696051eabc14ed0337f7.json | README.md | none | 3 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-m0i4jriq/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verified with `rg... |
| sha256-bd255092af60c9ab67e80bac50147d7ca9d2f25de9ecb2ab5b6b3b1988a70ea3.json | README.md | none | 3 | 9 | Fixed the typo in `README.md`: `succesful` is now `successful`.<br><br>Verified line 3 contains the corrected spelling. |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
