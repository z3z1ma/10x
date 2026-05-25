# Slicing Work

Plans exist to produce child tickets.

Ask repeatedly: what is the next smallest ticket-ready slice that makes meaningful
progress without widening scope?

A slice is ticket-ready when it has one outcome, one boundary, one evidence target,
one stop condition, and settled or linked design constraints.

## Good Slices

A good execution unit is independently legible, small enough to become one ticket,
grounded in a source record/code path/interface/migration/operator goal, explicit
about write boundary and design constraints, clear about order or dependency,
clear about validation and evidence, and able to stop cleanly when a behavior,
evidence, policy, or sequencing question appears.

Prefer vertical slices: one narrow path through real behavior, interface, data,
validation, and user or operator value. Examples include proving one end-to-end
path, migrating one representative case, implementing one contract-backed
behavior, or wiring one integration path.

Use horizontal slices only when the layer itself is valuable or a bounded
prerequisite: migration preparation, compatibility support, validation harness,
integration seam, behavior-preserving refactor, or contract tightening.

## Slicing Modes

Use a mode only when it clarifies strategy:

- tracer bullet: one narrow end-to-end path
- contract-first: define or tighten a shared behavior or interface
- risk-first: prove the riskiest assumption early
- migration-first: establish safe compatibility or data movement
- evidence-first: create or repair validation before expansion
- cleanup-only: isolate behavior-preserving simplification

## Bad Slices

These are not ticket-ready by themselves: backend work, frontend work,
integration, polish, cleanup, finish remaining items, add tests later, handle edge
cases, update docs, wire everything together.

They become ticket-ready only when they name outcome, boundary, evidence target,
stop condition, and design constraints.

## Integrity Check

Before creating or running a child ticket, answer:

- What single closure claim will this ticket make?
- What is excluded?
- What files, records, or surfaces form the likely write boundary?
- What system-shape, data-model, state, abstraction, or coherence constraint matters?
- What evidence verifies this slice without completing later slices?
- What stop condition returns to shaping, research, specs, or the operator?
- What later ticket can consume this result without chat history?

Split any slice whose answer points at multiple independent work products.
