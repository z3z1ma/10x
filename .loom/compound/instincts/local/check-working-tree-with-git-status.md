---
id: check-working-tree-with-git-status
title: Check working tree state with git status
trigger: Before resuming edits or after tool activity that may change repository state
confidence: 0.8200
status: active
domain: workflow
source: local
created_at: 2026-02-15T21:06:52.548579Z
updated_at: 2026-02-16T00:07:15.797505Z
tags: workflow, git, state-awareness, safety
notes: This pattern appears around coordination and validation transitions, reducing state drift risk before next actions.
---

## Action
Run `git status --porcelain` (or `git status --short`) at key checkpoints to confirm current working tree state before proceeding with additional edits or coordination commands.

## Evidence
- ts=2026-02-15T23:42:50.144244Z source_id=obs-git-status-234250 source_hash=git-status-porcelain
- ts=2026-02-15T23:48:41.974840Z source_id=obs-git-status-234841 source_hash=git-status-short
- ts=2026-02-15T23:50:04.029376Z source_id=obs-git-status-235004 source_hash=git-status-porcelain
- ts=2026-02-15T23:50:38.678586Z source_id=obs-git-status-235038 source_hash=git-status-porcelain
- ts=2026-02-15T23:50:44.063915Z source_id=obs-git-status-235044 source_hash=git-status-short-clean-checkpoint
- ts=2026-02-15T23:51:27.453273Z source_id=obs-git-status-235127 source_hash=git-status-short-branch-merge-queue
- ts=2026-02-15T23:52:00.101203Z source_id=obs-git-status-235200 source_hash=git-status-short-ticket-checkpoint
- ts=2026-02-15T23:52:38.978527Z source_id=obs-git-status-235238 source_hash=git-status-short-clean-after-commit
- ts=2026-02-15T23:53:50.200319Z source_id=obs-git-status-235350 source_hash=git-status-porcelain
- ts=2026-02-15T23:54:36.194631Z source_id=obs-git-status-235436 source_hash=git-status-porcelain
- ts=2026-02-15T23:54:55.362053Z source_id=obs-git-status-235455 source_hash=git-status-porcelain
- ts=2026-02-16T00:01:29.233006Z source_id=obs-git-status-000129 source_hash=git-status-short-checkpoint
- ts=2026-02-16T00:06:54.400484Z source_id=obs-git-status-000654 source_hash=git-status-short-branch-pre-merge

## Notes
This pattern appears around coordination and validation transitions, reducing state drift risk before next actions.
