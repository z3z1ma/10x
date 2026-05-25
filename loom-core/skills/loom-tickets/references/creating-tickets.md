# Creating Tickets

Ticket creation is outer-loop work. Create one only when a meaningful executable
slice can start without inventing scope.

## Readiness Standard

Before saving a ticket, prove:

- the executable boundary is small and concrete
- scope-selection, exclusions, system-shape, data/state implications, and
  coherence constraints are settled or owned by linked records
- the ticket produces engineering value, not process activity
- `ACC-*` criteria are observable and auditable
- the first Ralph run can launch from the ticket and linked records without chat
  history
- likely read/write scope, stop conditions, evidence posture, review posture, and
  output reconciliation are known enough for handoff

If any item is missing, keep shaping or route to specs, plans, research,
constitution, evidence, audit, knowledge, or the operator.

## Single Closure Claim

One ticket closes around one coherent claim. Say the closure claim in one sentence
before writing the ticket. If that sentence combines independent results, split the
work or create a plan with child tickets.

Ticket-sized claims usually have one primary write boundary, one evidence posture,
and one audit lens. Do not make a ticket choose architecture, change dependencies,
implement behavior, migrate paths, and perform final verification as independent
outcomes under one closure story.

## Creation Procedure

Use this sequence:

1. Identify the concrete outcome.
2. Inspect constraining records and source.
3. Define the smallest useful executable slice.
4. State what is explicitly out of scope.
5. Name relevant system-shape, data-model, state, abstraction, or coherence
   constraints.
6. Identify likely write boundaries.
7. Define observable `ACC-*` criteria.
8. Name evidence needed for the important claims.
9. Name the audit target or lens before closure.
10. Name the first likely Ralph run boundary.
11. Assign risk with a reason.
12. Add related records only when an acting agent should read them.
13. Create the ticket from `templates/ticket.md`.

## Route Elsewhere When

Do not force non-executable work into a ticket.

- unclear intended behavior -> specs
- ordering, decomposition, or rollout -> plans
- feasibility, evidence, alternatives, or tradeoffs -> research
- durable rules or operating principles -> constitution
- observations -> evidence
- adversarial review -> audit
- accepted reusable explanation -> knowledge

## Shaping Prompts

Useful questions are concrete: what artifact changes, what is out of scope, what
smallest slice matters, which seam or state relationship constrains it, what first
Ralph run acts, what evidence proves it, what audit should challenge, and what
would make it blocked.

Do not copy the interview into the ticket. Preserve only decisions, constraints,
evidence requirements, and boundaries that change execution.

Tickets are not drafts. If material questions remain, keep the conversation in the
outer loop or create the record that can resolve the ambiguity.
