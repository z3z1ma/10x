Status: recorded
Created: 2026-06-26
Updated: 2026-06-26
Target: SKILL.md, .10x/evidence/2026-06-26-multi-surface-spec-splitting-promotion.md
Verdict: pass

# Review: Promote Multi-Surface Spec Splitting

## Target

Promotion of focused specification splitting into `SKILL.md`, supported by
`EXP-20260626-741-multi-surface-spec-splitting-live-micro`.

## Findings

- Pass: The targeted failure mode is real. Pre-promotion current created a
  single broad `team-onboarding-suite.md` covering independent UI, lifecycle,
  delivery retry, and audit behavior.
- Pass: The promoted change is narrow. It changes where specifications are
  created and how their boundaries are chosen; it does not relax Outer Loop
  closure, assumption provenance, ticket ownership, evidence, or review gates.
- Pass: Post-promotion current created focused active specs and no
  implementation files. The post-promotion canonical guard reports no canonical
  file drift during the run.
- Pass: The mutation preserves minimalism by allowing one specification when
  the behavior is one cohesive surface and by exempting mechanical edits,
  no-code/reuse answers, and work already governed by active specs.
- Concern: The promoted wording may encourage more specs for tightly coupled
  features. The new text mitigates this by anchoring one spec to one coherent
  surface whose acceptance criteria are normally verified together.
- Concern: The post-promotion current run did not create child tickets because
  the empty seed lacked implementation substrate authority. This is safer than
  inventing stack assumptions, but it means child-ticket decomposition after
  focused specs still needs a source-backed positive control.

## Semantic Behavior Review

Failure mode targeted:

- Agents satisfy the spec-first gate by creating one god spec that hides
  independent actors, workflows, lifecycles, side effects, or verification
  paths.

Invariant preserved:

- No implementation before Inner Loop entry; no semantic defaults; tickets
  derive from specifications; parent tickets remain orchestration records.

New behavior intended:

- For net-new multi-surface behavior, create the minimal focused specification
  set first, then coordinate implementation through a parent plan and bounded
  child tickets when execution is authorized and unblocked.

Behavior accidentally permitted:

- Oversplitting a cohesive behavior into unnecessary records. The wording limits
  this by allowing one spec for one cohesive surface and using normal
  verification-together boundaries.

Eval cases expected to improve:

- Multi-surface greenfield requests where UI, lifecycle, notification/delivery,
  audit, permissions, or operational side effects are bundled in one user ask.

Regression cases that must not move:

- Existing active specification reuse.
- No-code/reuse answers.
- Exact trivial edits.
- Single-surface net-new behavior where one focused spec is the right record.

## Verdict

Pass. Promote and keep. The change addresses a reproduced current failure and
post-promotion current behavior passes the core target. The next experiment
should test focused specs plus child-ticket decomposition with a concrete
implementation substrate, not weaken this promotion.

## Residual Risk

Manual inspection remains authoritative. The live scenario had explicit numbered
surfaces; later lower-cue scenarios should verify that the agent can infer
split boundaries when the user does not enumerate them.
