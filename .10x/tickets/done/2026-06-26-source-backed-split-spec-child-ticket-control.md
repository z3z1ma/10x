Status: done
Created: 2026-06-26
Updated: 2026-06-26
Parent: None
Depends-On: .10x/research/2026-06-26-multi-surface-spec-splitting-live-micro.md

# Source-Backed Split-Spec Child-Ticket Control

## Scope

Run the next autoresearch MICRO for multi-surface spec splitting with an
explicit implementation substrate, so current `SKILL.md` can be evaluated for
creating focused specs and bounded child tickets rather than only a blocked
parent plan.

Included:

- Seed or reuse a fixture that contains enough source authority for stack,
  persistence, auth/role model, mail adapter/retry mechanism, audit storage,
  and test runner.
- Use a ratified multi-surface prompt where UI, lifecycle/delivery, and audit
  behavior should become separate focused specs.
- Expect current `SKILL.md` to create focused specs, a parent plan, and child
  tickets when executable decomposition is safe.
- Verify that current still writes no implementation files in the same turn as
  creating the governing specs and first tickets.

Excluded:

- Broad rewrite of `SKILL.md`.
- Lower-cue prompt variant unless this source-backed positive control passes.
- App-harness real subagent execution.

## Acceptance criteria

- Experiment record exists with a live Codex runner definition.
- Manual inspection determines whether current creates focused specs and child
  tickets when implementation substrate blockers are removed.
- Evidence records the result and any residual gap.
- No `SKILL.md` mutation is promoted unless current fails and a candidate passes
  without weakening existing invariants.

## Progress and notes

- 2026-06-26: Opened from residual risk in
  `.10x/evidence/2026-06-26-multi-surface-spec-splitting-promotion.md` and
  `.10x/reviews/2026-06-26-promote-multi-surface-spec-splitting.md`.
- 2026-06-26: Registered and ran
  `.10x/research/2026-06-26-source-backed-split-spec-child-ticket-live-micro.md`.
  Current-10x failed by creating one suite-wide spec and one broad executable
  ticket. Candidate-variant passed with focused specs, a parent plan, bounded
  child tickets, and no implementation mutation.
- 2026-06-26: Promoted the narrow source-backed child-ticket rule into
  `SKILL.md`. Evidence:
  `.10x/evidence/2026-06-26-source-backed-split-spec-child-ticket-result.md`.
  Review:
  `.10x/reviews/2026-06-26-promote-source-backed-child-ticket-gate.md`.

## Blockers

None.
