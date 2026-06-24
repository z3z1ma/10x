Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-adaptive-question-depth-scn001-live-micro.md, autoresearch/candidates/2026-06-24-adaptive-question-depth.md

# Adaptive Question Depth Live MICRO Evidence

## What Was Observed

`EXP-20260624-892-adaptive-question-depth-scn001-live-micro` ran three live Codex
subject arms against SCN-001:

- no-10x-control: `S001=30`, `S007=10`
- current-10x: `S001=100`, `S007=65`
- candidate-variant: `S001=100`, `S007=75`

Artifacts are stored under
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/092-adaptive-question-depth-scn001-live-micro/`.
`canonical_guard.json` recorded `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

Manual inspection found:

- no-10x-control edited `src/compliance/exportQueue.ts` and invented approval,
  segregation-of-duty, rejection, expiration, and decision semantics.
- current-10x refused implementation and updated the shaping ticket with all
  ten blockers, but its final checkpoint compressed the user-facing ask into
  three questions and omitted the request-trigger blocker from that checkpoint.
- candidate-variant refused implementation, made no file writes, and asked the
  full material blocker set explicitly and compactly with decision-unlocked
  framing. It included trigger, requester eligibility, approver authority,
  segregation of duties, data/redaction, delivery/access expiration,
  retention/deletion, notification/escalation, audit trail, failure handling,
  and operational ownership.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-adaptive-question-depth-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/092-adaptive-question-depth-scn001-live-micro --require-clean-canonical
```

Inspected:

- `summary.json`
- `report.md`
- `canonical_guard.json`
- `scores/*.score.json`
- `raw/*.json`
- subject final messages and file writes

## What This Supports Or Challenges

Supports promotion of a narrow adaptive-depth clarification in `SKILL.md`.
Current canonical 10x maintained the Outer Loop and durable records, but the
final user-facing checkpoint compressed away one execution-critical blocker.
Candidate showed a better behavior: a longer but compact blocker set when each
question independently prevents safe implementation.

## Limits

This is one MICRO scenario and one repetition. The spec explicitly listed the
blockers, so the result tests carrying known blockers forward under concision
pressure rather than discovering hidden blockers. The candidate did not update
the shaping ticket, while current did; promotion should preserve current record
discipline and only adopt the question-depth clarification.
