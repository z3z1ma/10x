# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-confirm-self-review-trivial |
| mode | live |
| raw_artifacts | 4 |
| live_subject_calls | 4 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Does the closure self-review candidate preserve the exact trivial edit fast path? |
| hypothesis | The candidate should not create tickets, reviews, evidence records, or multi-step process for an exact typo fix. |
| expected_behavior | Subject edits only README.md to fix `succesful` to `successful`, reports the change, and creates no .10x review or ticket ceremony. |
| inspection_criteria | README.md typo is fixed., No .10x records are created., No review record is created., No unrelated source or metadata files change., Response remains concise. |
| quality_floor | Any ticket/review/evidence ceremony for the exact typo fix caps the candidate. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/canonical_guard.json |
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
| sha256-04387da4842fe29282394dedf5508406998beeb7b8f179acd1d1a03ed6e63584.json | SCN-010 | candidate-closure-self-review-gate | 1 | codex-developer-instructions | 0 | False | 1 | 18.78 | in=107260; out=399 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces/sha256-04387da4842fe29282394dedf5508406998beeb7b8f179acd1d1a03ed6e63584 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces/sha256-04387da4842fe29282394dedf5508406998beeb7b8f179acd1d1a03ed6e63584/workspace-manifest.json |
| sha256-72d071fe7f9299c0623909abf1b09b02aff425056222261950da82ce70266aa7.json | SCN-010 | candidate-closure-self-review-gate | 0 | codex-developer-instructions | 0 | False | 1 | 21.25 | in=107809; out=576 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces/sha256-72d071fe7f9299c0623909abf1b09b02aff425056222261950da82ce70266aa7 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces/sha256-72d071fe7f9299c0623909abf1b09b02aff425056222261950da82ce70266aa7/workspace-manifest.json |
| sha256-b23e2a4264d0232041833433d89b2e8f8580a3e9af54540dcbd96d64e331f6eb.json | SCN-010 | current-10x | 1 | codex-developer-instructions | 0 | False | 1 | 24.24 | in=133391; out=616 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces/sha256-b23e2a4264d0232041833433d89b2e8f8580a3e9af54540dcbd96d64e331f6eb | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces/sha256-b23e2a4264d0232041833433d89b2e8f8580a3e9af54540dcbd96d64e331f6eb/workspace-manifest.json |
| sha256-f6b85f25a6fc3e982e2e12b13c5efa33310bfa20028039d53d5821c40a9640b3.json | SCN-010 | current-10x | 0 | codex-developer-instructions | 0 | False | 1 | 16.92 | in=106120; out=462 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces/sha256-f6b85f25a6fc3e982e2e12b13c5efa33310bfa20028039d53d5821c40a9640b3 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/confirm-self-review-trivial/workspaces/sha256-f6b85f25a6fc3e982e2e12b13c5efa33310bfa20028039d53d5821c40a9640b3/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-04387da4842fe29282394dedf5508406998beeb7b8f179acd1d1a03ed6e63584.json | README.md | none | 3 | 9 | Fixed the typo in [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-ch18lbpq/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verif... |
| sha256-72d071fe7f9299c0623909abf1b09b02aff425056222261950da82ce70266aa7.json | README.md | none | 5 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-4lvqogwz/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verified with `rg... |
| sha256-b23e2a4264d0232041833433d89b2e8f8580a3e9af54540dcbd96d64e331f6eb.json | README.md | none | 6 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-umfomje4/workspace/README.md:3): `succesful` → `successful`.<br><br>Verified the target li... |
| sha256-f6b85f25a6fc3e982e2e12b13c5efa33310bfa20028039d53d5821c40a9640b3.json | README.md | none | 3 | 9 | Fixed the typo in [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-7fukf4__/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verif... |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
