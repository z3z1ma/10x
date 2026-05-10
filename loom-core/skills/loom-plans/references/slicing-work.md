# Slicing Work

Plans exist to produce child tickets.

Use this question repeatedly:

> What is the next smallest ticket-ready slice that makes meaningful progress
> without widening scope?

A slice is ticket-ready when it has an outcome, boundary, evidence target, and
stop condition.

## Good Slices

A good execution unit is:

- independently legible
- small enough to become one ticket
- vertical enough to produce observable value when possible
- grounded in a source record, code path, interface, migration, or clear operator
  goal
- explicit about the likely scope boundary
- clear about the order reason or dependency
- clear about validation and evidence expectations
- able to stop cleanly if a behavior, evidence, policy, or sequencing question
  appears

Each execution unit should have a concrete child ticket ID once the plan is saved.

## Prefer Vertical Slices

Prefer a narrow path through real behavior, interface, data, validation, and user
or operator value.

A vertical slice can be smaller than the whole feature. It should produce a real,
observable step through the system.

Examples:

- prove one end-to-end path before broadening coverage
- migrate one representative case before generalizing the migration
- implement one contract-backed behavior before expanding variants
- wire one adapter path before adding every integration

## Use Horizontal Slices Carefully

Horizontal slices are useful when the layer itself is valuable or is a bounded
prerequisite.

Good horizontal slices include:

- migration preparation
- compatibility support
- shared validation harness
- adapter seam
- behavior-preserving refactor prerequisite
- contract or interface tightening before multiple tickets rely on it

A horizontal slice still needs an outcome, boundary, evidence target, and stop
condition.

## Common Slicing Modes

Use these when they help explain the route:

- tracer bullet: one narrow end-to-end path through the real system
- contract-first: define or tighten a shared behavior or interface before other
  tickets rely on it
- risk-first: prove the riskiest assumption or integration early
- migration-first: establish compatibility or data movement before dependent
  changes
- evidence-first: create or repair validation before implementation would be hard
  to trust
- cleanup-only: isolate behavior-preserving simplification so review can separate
  it from feature work

Use the mode only when it clarifies the strategy.

## Bad Slices

These are usually not ticket-ready:

- backend work
- frontend work
- integration
- polish
- cleanup
- finish remaining items
- add tests later
- handle edge cases
- update docs
- wire everything together

They become ticket-ready when they name an outcome, boundary, evidence target, and
stop condition.

## Slice Integrity

Keep feature work, bug fixes, refactors, dependency changes, generated-file
churn, and formatting-only cleanup separate unless the plan explains why bundling
them is still reviewable.

If one slice needs several independent children, split it.

If a slice cannot be verified independently, make it smaller, change the evidence
plan, or route back to shaping.

If a slice cannot be executed from its child ticket and linked records, it is not
ready.
