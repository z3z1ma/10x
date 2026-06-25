Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-lower-assistance-multibatch-ratification-batch1-scn001-live-micro.md

# Lower-Assistance Multibatch Ratification Batch 1 Result

## What Was Observed

Ran `EXP-20260625-951-lower-assistance-multibatch-ratification-batch1-scn001-live-micro`
with one repetition for no-10x-control, current-10x, and duplicate-current.

Raw artifacts:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/216-lower-assistance-multibatch-ratification-batch1-scn001-live-micro/`

`canonical_guard.json` reported `SKILL.md` and `autoresearch/program.md`
unchanged during the run.

Manual inspection found current and duplicate-current preserved the first
answer batch:

- refund cap `$250`;
- refund low-risk predicate `riskTier === "low"`;
- audit retention `90 days`;
- audit closed-account exclusion.

Both canonical arms kept remaining blockers visible and created no executable
implementation ticket. Changed canonical files were limited to `.10x` specs,
the active shaping ticket, and in current-10x one knowledge record. No source
or test files changed.

## Procedure

1. Registered the fixture and batch-1 experiment record.
2. Ran:

   ```bash
   python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-lower-assistance-multibatch-ratification-batch1-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/216-lower-assistance-multibatch-ratification-batch1-scn001-live-micro --require-clean-canonical
   ```

3. Inspected raw artifacts, archived workspace manifests, changed files,
   updated records, and final messages.

## What This Supports Or Challenges

This supports using the current-10x and duplicate-current raw outputs as real
prior context for the batch-2 continuation.

## Limits

Batch 1 is not a full verdict on multibatch ratification. It only verifies that
the first answer batch was preserved and that the subject did not prematurely
enter implementation.
