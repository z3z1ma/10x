Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Target: SKILL.md, autoresearch/candidates/2026-06-23-upstream-gated-blockers.md
Verdict: pass

## Target

Canonical promotion of `candidate-upstream-gated-blockers-v1` into `SKILL.md`.

## Findings

- **Pass:** The promoted text is scoped to Outer Loop ambiguity resolution and
  does not alter record shapes, harness behavior, score definitions, or
  promotion gates.
- **Pass:** The instruction avoids the rejected one-question discipline. It
  explicitly permits several questions when independent answers change the next
  safe action.
- **Pass:** The rule addresses the observed failure mode: asking downstream
  product details before resolving missing target artifact, codebase, or product
  surface.
- **Concern accepted:** The promotion is based on a small number of live runs
  plus manual inspection, not a repeated FULL benchmark. The change is narrow,
  user-authorized, and reversible if future runs expose under-questioning.
- **Concern accepted:** The new bullet block adds prompt weight to `SKILL.md`.
  The text replaces a recurring behavioral gap with concise operational rules,
  so the token cost is justified for now.

## Verdict

Pass. Promote the upstream-gated blocker rule and continue autoresearch against
held-out ticket-boundary and repeated-run scenarios.

## Residual Risk

The highest residual risk is under-questioning when work is almost executable
and downstream details independently affect the next safe action. The skill now
allows multiple independent blockers, but future MICRO or FULL runs should still
test that boundary.
