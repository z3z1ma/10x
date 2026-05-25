# Audit Lenses

Audit lenses focus adversarial attention. Use the lenses that fit the target; add
another when the risk is not listed.

## Core Questions

- What claim is weaker than it sounds?
- What evidence is missing, stale, partial, or overclaimed?
- What assumption is hidden?
- What scenario breaks this?
- What changed outside scope?
- What record, evidence, or follow-through was forgotten?
- What would mislead the next agent?
- What must happen before acceptance, closure, or reuse is honest?

## Common Lenses

- claim and evidence: exact support for the claim
- scope: whether the target stayed inside boundary
- acceptance: whether `ACC-*` or equivalent criteria are satisfied
- implementation: correctness, simplicity, maintainability, integration, edges
- surface boundary: whether durable claims live in the right Loom surface
- security and trust boundary: secrets, auth, authorization, injection, unsafe
  commands, and instruction/data confusion
- performance: measured bottlenecks, representative data, before/after evidence
- data and migration: schema drift, idempotency, loss, compatibility, repeatability
- dependency and tooling: package, runtime, build, lint, typecheck, lockfile,
  generated-file, or automation drift
- product and UX: task clarity, flow, edge states, usefulness, real problem fit
- visual design and accessibility: hierarchy, affordance, density, responsiveness,
  keyboard path, names, labels, contrast, landmarks, reduced motion
- AI-artifact cleanup: debug leftovers, placeholders, TODOs, dead code,
  over-explaining comments, premature abstractions, local hardcoding
- follow-through: whether findings, worker output, evidence gaps, and residual
  risks were dispositioned

## Review Order

For implementation or behavior changes, review claim/scope/acceptance first,
evidence second, implementation quality third, risks fourth, and follow-through
last. A polished implementation of the wrong behavior is still a finding.

Split passes when one review would blur different judgments: acceptance vs code
quality, evidence sufficiency vs implementation polish, security or migration vs
ordinary maintainability, product/UX vs visual/accessibility, protocol boundary vs
code review, or research-source quality vs recommendation.

If the same finding repeats, fixes expose new scope gaps, feedback is being applied
mechanically, or the ticket cannot disposition findings without changing another
surface, route the blocker to the owner surface.
