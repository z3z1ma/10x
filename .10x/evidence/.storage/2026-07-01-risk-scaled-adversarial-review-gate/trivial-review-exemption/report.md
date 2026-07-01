# 10x Autoresearch Trial Report

Source: `.10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption`

## Summary

| Field | Value |
| --- | --- |
| experiment_id | EXP-20260701-risk-review-trivial-exemption |
| mode | live |
| raw_artifacts | 4 |
| live_subject_calls | 4 |
| summary | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/summary.json |
| plan | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/plan.json |
| raw_output_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/raw |
| workspace_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces |
| prompt_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/prompts |
| harness_artifact_dir | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/codex |

## Scientific Contract

| Field | Value |
| --- | --- |
| question | Do review-gate candidates preserve the exact trivial edit fast path? |
| hypothesis | Good review wording should not create tickets, reviews, evidence records, or multi-step process for an exact typo fix. |
| expected_behavior | Subject edits only README.md to fix `succesful` to `successful`, reports the change, and creates no .10x review or ticket ceremony. |
| inspection_criteria | README.md typo is fixed., No .10x records are created., No review record is created., No unrelated source or metadata files change., Response remains concise. |
| quality_floor | Any ticket/review/evidence ceremony for the exact typo fix caps the candidate. |
| verdict_record_path | .10x/evidence/2026-07-01-risk-scaled-adversarial-review-gate.md |

## Artifact Inspection Checklist

Presence only; the scientist still judges whether each artifact supports the claim.

| Artifact class | Status |
| --- | --- |
| summary.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/summary.json |
| plan.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/plan.json |
| canonical_guard.json | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/canonical_guard.json |
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
| sha256-55162d6a28aefb8227d546eb812b598088fe6b92239eb19c9d0b54ccaa4e31b4.json | SCN-010 | candidate-inner-loop-red-team-review | 0 | codex-developer-instructions | 0 | False | 1 | 17.59 | in=107009; out=414 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces/sha256-55162d6a28aefb8227d546eb812b598088fe6b92239eb19c9d0b54ccaa4e31b4 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces/sha256-55162d6a28aefb8227d546eb812b598088fe6b92239eb19c9d0b54ccaa4e31b4/workspace-manifest.json |
| sha256-6bb9d3983f2890a6611e45846ec1431ae396b45a81973382e29cda340091b92e.json | SCN-010 | candidate-risk-scaled-review-gate | 0 | codex-developer-instructions | 0 | False | 1 | 17.03 | in=107134; out=383 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces/sha256-6bb9d3983f2890a6611e45846ec1431ae396b45a81973382e29cda340091b92e | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces/sha256-6bb9d3983f2890a6611e45846ec1431ae396b45a81973382e29cda340091b92e/workspace-manifest.json |
| sha256-e2b8d2cab5f160d658aaecdf65371be9006ba65fd7ad867b4d943b35305a6694.json | SCN-010 | candidate-review-state-closure-gate | 0 | codex-developer-instructions | 0 | False | 1 | 15.09 | in=106853; out=300 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces/sha256-e2b8d2cab5f160d658aaecdf65371be9006ba65fd7ad867b4d943b35305a6694 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces/sha256-e2b8d2cab5f160d658aaecdf65371be9006ba65fd7ad867b4d943b35305a6694/workspace-manifest.json |
| sha256-e39bff7df397791a72a39c5dc87440e958b789d6af21e127f1bf293255090adb.json | SCN-010 | current-10x | 0 | codex-developer-instructions | 0 | False | 1 | 18.03 | in=106029; out=415 | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces/sha256-e39bff7df397791a72a39c5dc87440e958b789d6af21e127f1bf293255090adb | .10x/evidence/.storage/2026-07-01-risk-scaled-adversarial-review-gate/trivial-review-exemption/workspaces/sha256-e39bff7df397791a72a39c5dc87440e958b789d6af21e127f1bf293255090adb/workspace-manifest.json |

## Workspace And Tool Trace

| Artifact | Changed files | Suppressed changed files | Tool events | Raw references | Last assistant message |
| --- | --- | --- | --- | --- | --- |
| sha256-55162d6a28aefb8227d546eb812b598088fe6b92239eb19c9d0b54ccaa4e31b4.json | README.md | none | 3 | 9 | Updated [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-48e92hn0/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verified with `... |
| sha256-6bb9d3983f2890a6611e45846ec1431ae396b45a81973382e29cda340091b92e.json | README.md | none | 3 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-4d1ts7m2/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verified the targ... |
| sha256-e2b8d2cab5f160d658aaecdf65371be9006ba65fd7ad867b4d943b35305a6694.json | README.md | none | 3 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-2i6vr28q/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verified the corr... |
| sha256-e39bff7df397791a72a39c5dc87440e958b789d6af21e127f1bf293255090adb.json | README.md | none | 3 | 9 | Fixed [README.md](/mnt/c/Users/butle/AppData/Local/Temp/10x-autoresearch-xnvit_82/workspace/README.md:3): `succesful` is now `successful`.<br><br>Verified the READ... |

## Scientist Inspection

This report does not grade, aggregate, or promote a candidate.

Inspect the raw transcript, command artifacts, workspace manifest, changed files, and expected behavior for each scenario. Record rubric judgments, verdicts, limits, and any promotion or rejection rationale in durable `.10x/research/`, `.10x/evidence/`, or `.10x/reviews/` records.

## Report Limits

- This report is a secondary view over saved trial artifacts.
- Unknown means the field was absent, null, or not numeric in the loaded artifact.
- The runner does not replace the LLM researcher's rubric inspection.
