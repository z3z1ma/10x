# Audit Lenses

Audit lenses are prompts for adversarial attention, not a required taxonomy.

Name the lenses that fit the target. Add a different lens when the actual risk is
not listed here.

## Core Questions

A good audit asks:

- What claim is weaker than it sounds?
- What evidence is missing, stale, partial, or overclaimed?
- What assumption is hidden?
- What scenario breaks this?
- What changed outside the declared scope?
- What did the implementer or record author forget to update?
- What would mislead the next agent?
- What must happen before acceptance, closure, or reuse is honest?

## Common Lenses

Use these when they help sharpen the review:

- claim and evidence: whether cited observations support the exact claim
- scope: whether the target stayed inside its declared boundary
- acceptance: whether `ACC-*` or equivalent acceptance claims are satisfied
- implementation: correctness, simplicity, maintainability, integration fit, and
  edge cases
- surface boundary: whether the target puts durable claims in the correct Loom surface
- security and trust boundary: secrets, auth, authorization, injection, unsafe
  commands, and instruction/data confusion
- performance: measured bottlenecks, hot paths, representative data, and
  before/after evidence
- data and migration: schema drift, idempotency, data loss, compatibility, and
  repeatability
- dependency and tooling: package, runtime, build, lint, typecheck, lockfile,
  generated-file, or local automation drift
- product and UX: primary task clarity, flow, edge states, usefulness, and whether
  the result solves the real problem
- visual design and accessibility: hierarchy, affordance, density, responsiveness,
  keyboard path, names, labels, contrast, landmarks, and reduced motion
- AI-artifact cleanup: debug leftovers, placeholders, TODOs, dead code,
  over-explaining comments, premature abstractions, and hardcoded local values
- follow-through: whether review comments, worker output, evidence gaps, and
  residual risks were dispositioned rather than hand-waved

## Review Order

For implementation or behavior changes, review in this order when practical:

1. Claim, scope, and acceptance: did the target build the right thing and stay in
   bounds?
2. Evidence: does the observed support match the exact claim?
3. Implementation quality: is the change correct, simple enough, maintainable,
   and consistent with the codebase?
4. Risk and failure modes: what breaks, leaks, regresses, or becomes hard to
   correct later?
5. Follow-through: can the next agent or ticket closure consume the result without
   reconstructing missing context?

A polished implementation of the wrong behavior is still an audit finding.

## Splitting Passes

Use multiple fresh-context audit passes when one pass would blur different kinds
of judgment.

Split when the target is broad, high risk, cross-surface, security-relevant,
user-facing, or likely to hide one class of risk behind another.

Useful splits include:

- acceptance and scope before code quality
- evidence sufficiency before implementation polish
- security or migration risk separate from ordinary maintainability
- product/UX separate from visual design or accessibility
- surface-boundary or protocol review separate from code review
- research-source quality separate from recommendation review

Each pass can create its own audit record, or one consolidated audit can clearly
separate the passes when that remains readable.

## Stalled Review Loops

A fix-review loop is stalling when:

- the same material finding returns after a fix attempt
- every fix exposes a new scope, behavior, evidence, or surface-boundary gap
- feedback is being implemented mechanically without resolving the challenged
  claim
- the ticket cannot disposition findings without changing spec, plan, research,
  scope, or operator intent

When the loop stalls, route the blocker to the surface that can resolve it.
