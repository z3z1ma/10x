# Creating Tickets

Ticket creation is outer-loop work.

Create a ticket when a meaningful executable work unit has been shaped enough that
an agent can start without inventing scope.

## Shaping Standard

Before writing the ticket, prove three things:

- executable boundary: the work is small and concrete enough to execute without
  inventing scope
- engineering value: the ticket produces a real engineering outcome, not activity
  or process compliance
- acceptance clarity: `ACC-*` criteria are specific enough that evidence can
  observe them and audit can challenge them

If any of those are missing, keep shaping. Ask the operator, inspect the codebase,
or route to research, specs, plans, or constitution before creating the ticket.

## Single Closure Claim

One ticket should close around one coherent claim.

Before saving the ticket, say the closure claim in one sentence. If the sentence
needs several independent outcomes, split or route to a plan.

Ticket-sized claims name one result and one proof path. They usually have one
primary write boundary and one evidence posture.

Claims that usually need a plan or split combine independent results, such as
choosing an architecture, changing dependencies, implementing user-visible
behavior, adding broad variants, migrating old paths, and performing final
verification in the same work unit.

Use the ticket only after the result, boundary, evidence, and audit lens all belong
to the same closure story.

## Create A Ticket Only When

Create a ticket when all of these are true:

- the work has an executable change boundary
- the smallest useful slice is identifiable
- the ticket has one coherent closure claim
- likely affected files, records, systems, or artifacts are known enough to begin
- acceptance can be written as observable criteria
- the initial status can honestly be `open`
- unresolved questions do not materially change the scope or acceptance

Do not create a ticket as a placeholder for unresolved thought.

## Route Elsewhere When

Do not force non-executable work into a ticket.

Route instead:

- unclear intended behavior to specs
- ordering, decomposition, or rollout strategy to plans
- feasibility, evidence, alternatives, or tradeoffs to research
- durable rules or operating principles to constitution
- accepted reusable explanation to knowledge
- adversarial review to audit

A ticket can depend on those records. It should not pretend to replace them.

## Engineering Discipline

Ground the ticket before writing it.

- Inspect relevant source, tests, records, and prior decisions before asking the
  operator to restate facts.
- Prefer a small vertical slice that creates observable value over vague phases or
  horizontal chores.
- Name the likely write boundary, validation target, risk, and escalation triggers.
- Challenge fuzzy verbs like improve, clean up, support, handle, align, simplify,
  refactor, finish, and polish until they imply concrete change and evidence.
- Ask one material question at a time when operator input is needed.
- Offer a recommended answer when the choice has a clear engineering tradeoff.
- Preserve only answers that change execution.

## Shaping Procedure

Use this sequence:

1. Identify the concrete outcome.
2. Inspect existing records and source that constrain the work.
3. Define the smallest useful executable slice.
4. State what is explicitly out of scope.
5. Identify likely write boundaries.
6. Define acceptance criteria with `ACC-*` IDs.
7. Name evidence needed for each important closure claim.
8. Name the audit target or lens expected before closure.
9. Assign risk with a reason.
10. Add related records only when an acting agent should read them.
11. Create the ticket using `templates/ticket.md`.

## Creation Questions

Good ticket-shaping questions include:

- What code-facing or artifact-facing change will exist when this is done?
- What is the smallest useful slice?
- What is explicitly out of scope?
- What existing record constrains this work?
- What source, test, or artifact path is likely involved?
- What would count as evidence that the work succeeded?
- What should audit challenge before this closes?
- What would make this ticket blocked instead of executable?
- What decision would materially change acceptance?

Do not copy the whole interview into the ticket. Preserve the decisions,
constraints, evidence requirements, and boundary facts that change execution.

## Do Not Create Draft Tickets

Tickets are born ready enough to start. The default status is `open`.

If material questions remain, do not save a draft ticket as a placeholder. Keep the
conversation in the outer loop or create the record that can resolve the
ambiguity.

If the work is important but not executable yet, say what is missing and recommend
the next Loom surface.
