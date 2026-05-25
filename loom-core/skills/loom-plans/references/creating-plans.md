# Creating Plans

Plan creation is outer-loop work. Create a plan only when complex work needs more
than one bounded ticket or shared sequencing, dependency, coordination,
validation, evidence, or audit posture.

The saved plan should already name the child tickets agents are expected to run.
Execution starts from those tickets.

## Readiness

Create a plan when all are true:

- overall outcome is clear
- work genuinely exceeds one bounded ticket
- intended behavior is clear or owned by a spec
- tradeoffs and feasibility questions are resolved or owned by research
- system-shape, data-model, state-model, abstraction, and coherence constraints are resolved or linked
- durable policy or precedent is resolved or owned by constitution
- route and order are understandable
- work can be sliced into child tickets with concrete scope and `ACC-*` acceptance
- validation, evidence, audit, risk, and loopback expectations can guide child tickets
- initial status can honestly be `open`

If not, keep shaping or route the missing truth to the owning Loom surface.

## Grounding

Before writing, inspect relevant specs, research, constitution records, tickets,
evidence, source paths, tests, interfaces, migrations, and external references.

Shape until these are clear:

- why one ticket is not enough
- what outcome the plan drives toward
- what is intentionally left out
- what records constrain the work
- what system-shape, data, state, abstraction, or coherence constraints shape the route
- what decomposition and order make sense
- what can run independently and what must be sequential
- what validation and evidence child tickets inherit
- what risks should be handled early
- what should trigger replanning

## Procedure

1. Identify the outcome and governing records.
2. Shape route, decomposition, ticket set, and proof posture.
3. Name scope-selection decisions and design constraints.
4. Write strategy in prose.
5. Slice into ticket-ready execution units.
6. Create child tickets.
7. Put each child ticket ID under its execution unit.
8. Add the plan to each child ticket's `## Related Records`.
9. Define meaningful milestones.
10. Name validation, evidence, audit, risk, and loopback posture.
11. Save with `templates/plan.md`.

If a child ticket cannot be written yet, the execution unit is not ticket-ready.

Test each unit with the single-closure-claim rule: one child ticket should produce
one bounded result with one coherent evidence and closure story. Split units that
combine independent stack, data, UI, migration, feature, review, or verification
claims.

## Useful Questions

- Why is this more than one ticket?
- What belongs here and what is left out?
- What is the smallest useful sequence of child tickets?
- Which system seam, data model, state relationship, or abstraction shapes the route?
- Which slice gives first observable value or proves the riskiest assumption?
- Which shared contract must be settled before parallel work?
- Which work must be sequential, and which can run independently?
- What evidence would make downstream closure honest?
- What should cause replanning?
