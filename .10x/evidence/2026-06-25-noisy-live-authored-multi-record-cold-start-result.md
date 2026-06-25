Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-noisy-live-authored-multi-record-cold-start-scn003-live-micro.md

# Noisy Live-Authored Multi-Record Cold-Start Result

## What Was Observed

Ran `EXP-20260625-953-noisy-live-authored-multi-record-cold-start-scn003-live-micro`
with three repetitions each for no-10x-control, current-10x, and
duplicate-current.

Raw artifacts:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/218-noisy-live-authored-multi-record-cold-start-scn003-live-micro/`

`canonical_guard.json` reported `SKILL.md` and `autoresearch/program.md`
unchanged during the run.

The offline report scored current and duplicate-current at S001=90 and S002=90
for all six canonical repetitions. no-10x-control scored S001=70 and S002=70
for all three repetitions.

Manual inspection found all current and duplicate-current repetitions:

- recovered refund and audit owners from existing records;
- treated `.10x/tickets/2026-06-25-implement-privacy-audit-export.md` as the
  existing executable audit owner;
- treated `.10x/tickets/2026-06-25-shape-refund-and-audit-rollout.md` and
  `.10x/specs/refund-auto-approval.md` as the refund shaping/blocker owner;
- preserved settled audit values: fields `accountId`, `createdAt`, `status`,
  `balanceCents`; email omission; closed-account exclusion; 90-day retention;
  Data Platform ownership;
- preserved settled refund values: `$250`, `riskTier === "low"`,
  `#refund-ops`, Refund Ops ownership, one retry after 30 minutes;
- kept refund blocked on undefined `normal risk escalation`;
- rejected payout retry decision, payout risk knowledge, payout source defaults,
  and unratified refund source fields as non-authoritative for refund
  escalation semantics;
- avoided duplicate tickets/specs and source/test edits.

Workspace manifests showed every canonical repetition changed only
`.10x/tickets/2026-06-25-shape-refund-and-audit-rollout.md`.

## Procedure

1. Copied a current-10x workspace from
   `EXP-20260625-952-lower-assistance-multibatch-ratification-batch2-scn001-live-micro`
   into a tracked live seed.
2. Registered
   `.10x/research/2026-06-25-noisy-live-authored-multi-record-cold-start-scn003-live-micro.md`.
3. Ran:

   ```bash
   python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-noisy-live-authored-multi-record-cold-start-scn003-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/218-noisy-live-authored-multi-record-cold-start-scn003-live-micro --require-clean-canonical
   ```

4. Inspected the report, canonical guard, workspace manifests, final messages,
   record graph file lists, and changed shaping-ticket notes.

## What This Supports Or Challenges

This supports current `SKILL.md` for noisy live-authored cold starts. The record
graph was sufficient for cold-start agents to recover existing owners, preserve
settled values, keep unresolved semantics blocked, and reject cross-domain
authority noise without chat history.

## Limits

This is still one seeded live-authored fixture. It does not prove handoff review
quality as a separate task, exact post-blocker ratification behavior, or true
app-level subagent continuation.
