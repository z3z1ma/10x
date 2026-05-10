# Creating Plans

Plan creation is outer-loop work.

Create a plan when complex codebase work needs more than one bounded ticket, or
when sequencing, dependencies, coordination, validation, or audit posture matter
across multiple execution units.

A plan should make the route executable. It should preserve the decisions,
constraints, decomposition, and child ticket links that shape execution.

## Shaping Standard

Before writing the plan, shape the work until four things are true:

- decomposition need: the work genuinely exceeds one bounded ticket
- execution route: the route through the work is understandable and justified
- ticket set: the child tickets can be created now
- proof posture: validation, evidence, audit, risk, and loopback expectations are
  clear enough for downstream tickets

Resolve ambiguity before saving the plan. Inspect the codebase, read governing
records, ask the operator, or route unknowns to research, specs, or constitution.

Ask one material question at a time when operator input is needed. Offer a
recommended route when the tradeoff is clear.

Do not copy the whole shaping conversation into the plan. Preserve the route,
decomposition, decisions, constraints, risks, validation posture, and child ticket
links that change execution.

## Create A Plan Only When

Create a plan when all of these are true:

- the overall outcome is clear
- the work genuinely exceeds one bounded ticket
- intended behavior is clear enough or owned by a spec
- major tradeoffs or feasibility questions are resolved or owned by research
- durable policy, precedent, or architectural judgment is resolved or owned by
  constitution
- the route through the work is understandable
- the work can be sliced into ticket-ready execution units
- each execution unit can become a child ticket with concrete scope and `ACC-*`
  acceptance
- validation, evidence, audit, risk, and loopback expectations are clear enough
  for downstream tickets
- the plan's initial status can honestly be `open`

If the plan cannot yet produce ticket-ready units, keep shaping, inspect the
codebase, ask the operator, or route the unknowns to the owning Loom surface.

## Before Writing

Ground the plan before writing it.

Inspect relevant records and source reality before asking the operator to repeat
facts. Depending on the work, this may include specs, research, constitution
records, prior tickets, evidence, source paths, tests, interfaces, migrations, or
external references.

Then shape the route until these are clear:

- why the work needs a plan instead of one ticket
- what outcome the plan is driving toward
- what records constrain the work
- what decomposition makes sense
- what order matters and why
- what can run independently
- what must be sequential
- what validation and evidence child tickets should inherit
- what risks should be handled early
- what should trigger replanning

## Slicing Standard

Prefer thin execution units that leave the codebase in a working, testable state.

A strong slice does one meaningful thing completely enough to verify before the
next slice expands the change. It should produce observable progress without
requiring the acting agent to implement the whole feature in one pass.

Prefer slices that:

- follow a narrow path through real behavior
- can be tested or inspected independently
- keep unrelated changes separate
- make risk visible early
- let later tickets build on verified ground
- stop cleanly when behavior, evidence, policy, or sequencing questions appear

Use horizontal slices when the layer itself is valuable or is a bounded
prerequisite, such as migration preparation, a compatibility seam, a validation
harness, an adapter boundary, or a behavior-preserving refactor.

## Useful Slicing Routes

Use these routes when they clarify the plan:

- vertical-first: prove one narrow end-to-end path, then broaden coverage
- contract-first: define or tighten a shared interface before multiple tickets
  depend on it
- risk-first: prove the riskiest assumption or integration early
- evidence-first: create or repair validation before implementation would be hard
  to trust
- migration-first: establish the safe data or compatibility path before dependent
  changes
- cleanup-first: isolate behavior-preserving simplification when it makes later
  work easier to review

Use the route that best explains the sequence.

## Scope Discipline

Each execution unit should change one logical thing.

Keep feature work, bug fixes, refactors, dependency changes, generated-file churn,
and formatting-only cleanup separate unless bundling them is necessary and still
reviewable.

If an adjacent improvement is worth doing, give it its own ticket or leave it out.

## Creation Procedure

Use this sequence as the default path, not as a form:

1. Identify the overall outcome.
2. Inspect governing records and relevant source reality.
3. Shape the work until decomposition need, execution route, ticket set, and proof
   posture are clear.
4. Decide why this needs a plan rather than one ticket.
5. Write the strategy in prose.
6. Slice the work into ticket-ready execution units.
7. Create the child tickets.
8. Put each child ticket ID under the corresponding execution unit.
9. Add the plan to each child ticket's `## Related Records`.
10. Define milestones that group meaningful execution outcomes.
11. Name validation, evidence, audit, risk, and loopback posture.
12. Save the plan using `templates/plan.md`.

If a child ticket cannot be written yet, the execution unit is not ticket-ready.
Keep shaping or route the missing truth to the appropriate surface.

## Creation Questions

Good plan-shaping questions include:

- Why is this more than one ticket?
- What is the smallest useful sequence of child tickets?
- Which slice should produce the first observable value?
- Which slice should prove the riskiest assumption?
- Which shared contract or interface must be settled before parallel work begins?
- Which validation should exist before implementation expands?
- Which work must be sequential?
- Which work can run independently later?
- Which files, records, interfaces, or systems create coordination risk?
- What validation should child tickets inherit?
- What evidence would make downstream closure honest?
- What should cause the plan to change?

Preserve the route, decomposition, decisions, constraints, risks, validation
posture, and child ticket links that change execution.
