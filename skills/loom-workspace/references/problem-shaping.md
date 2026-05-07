# Problem Shaping

Problem shaping is the divergent pre-planning posture for fuzzy requests.

It should make the request legible enough to route, without prematurely
creating initiatives, specs, plans, or tickets.

## Use When

- the request is fuzzy
- assumptions are hidden
- precedent may already answer the question
- the honest next move is questions rather than records

## Procedure

1. Orient without committing.
2. Restate the request in one or two sentences.
3. Name what is unclear.
4. Ask a small number of sharp clarifying questions. For creative, product,
   behavior, architecture, or workflow-shaping requests, run the pressure check
   below before durable records or implementation depend on the answer.
5. If a question can be answered by inspecting the workspace, inspect first
   instead of asking the operator to restate available facts.
6. Check constitution, decisions, wiki, and prior research for precedent.
7. Check accepted shared language and relevant source/code paths when terminology,
   behavior, or architecture claims could conflict with reality.
8. Surface assumptions as accepted, to-be-confirmed, or contested.
9. When source, records, or accepted language disagree, state the conflict and the
   owner that can resolve it instead of normalizing it away in chat.
10. When the work is creative or behavior-shaping, present two or three viable
    approaches with tradeoffs and a recommendation before narrowing.
11. Route to the next owner layer or workflow.

Ask one material question at a time when operator input is needed. A bundle of
questions is acceptable only when every answer is independent and low-friction;
otherwise it hides which decision actually blocks the route.

## Creative Shaping

Use creative shaping when the request could reasonably produce different valid
designs, behaviors, architectures, UI shapes, or rollout paths.

The goal is not to create a new design-doc ledger. The goal is to make the next
owner-layer mutation safe.

Do this:

- ask one question at a time when the operator needs to choose or clarify
- prefer multiple-choice questions when that lowers friction without hiding nuance
- name purpose, constraints, success criteria, and non-goals before proposing work
- open the space before narrowing it: generate a small set of meaningfully
  different approaches, cluster them into the real options, then converge on a
  recommendation
- propose two or three approaches with tradeoffs when alternatives matter
- surface hidden assumptions and how each could be validated or invalidated
- write a `Not Doing` list when focus or MVP shape is the important decision
- separate accepted assumptions from contested or unconfirmed assumptions
- keep large multi-subsystem ideas decomposed before creating one oversized plan
- route accepted intended behavior to spec and sequencing to plan

## Pressure Check

Before turning a fuzzy request into a spec, plan, ticket, packet, or code change,
scan for the gaps that would make the agent silently invent direction:

- evidence gap: what observed user, operator, system, or maintenance pain shows
  this matters now?
- specificity gap: who or what exact surface benefits, and what changes for them?
- counterfactual gap: what happens today if nothing ships, and what workaround or
  cost exists now?
- attachment gap: is the request attached to one solution shape before the value
  has been clarified; what is the smallest valuable shape?
- durability gap: what near-term change in the product, market, dependency,
  harness, or team would make this direction wrong?

Do not turn this into a questionnaire. Ask only the material gaps that are
actually present, one question at a time when operator input is needed. If a
material answer is unavailable, route it as a blocking question, research need,
spec decision point, plan risk, or ticket assumption instead of hiding it in chat.
Low-risk reversible assumptions may proceed only when recorded in the owner layer.

For visual, spatial, or product-shape questions, a sketch route may be better
than more prose. Use `loom-spike` sketch flow when mockups, diagrams, screenshots,
or side-by-side variants would make the choice clearer. Evidence owns the
observed artifacts; specs and wiki own accepted behavior or explanation.

## Decision Capture Threshold

Do not create a durable decision record for every preference. Route to
constitution decisions when the choice is hard to reverse, surprising without
context, and the result of a real tradeoff. If only one or two of those are true,
the decision may belong in a spec, plan, research note, ticket assumption, or wiki
explanation instead.

When a rejected option is likely to recur, preserve the durable reason in the
owner that can maintain it: research for rejected options and null results,
constitution for durable policy, wiki for accepted explanation, or a ticket for a
ticket-local cancellation / wontfix disposition. Do not create a separate
out-of-scope ledger unless the constitution later defines one.

## Routes

- clear enough to sequence -> plan
- evidence missing -> research
- behavior unclear -> spec
- design alternatives need artifacts -> spike/sketch evidence, then spec or wiki
- durable choice needed -> constitution decision
- already answered -> cite the existing owner record
- still too fuzzy but worth preserving -> research with `status: deferred_questions`

## Guardrails

- Do not draft execution records from a still-fuzzy request.
- Do not answer with code.
- Do not silently choose between materially ambiguous readings. Ask the user when
  proceeding would invent authority, accept material risk, change owner-record
  truth, or make an irreversible or high-risk decision.
- Do not ask the user to answer questions the repository can answer through
  direct inspection.
- Do not hide a code/record/terminology conflict by choosing the side that makes
  implementation easiest.
- Do not turn the first plausible approach into a spec or ticket before hidden
  assumptions, alternatives, and the smallest valuable shape have been checked
  when those facts would change the result.
- If an assumption is low risk, reversible, and inside delegated authority,
  record it in the owning record before continuing through the appropriate
  route.
- Do not bypass constitutional conflicts.
- Do not let an approved-sounding chat or transcript summary replace spec,
  plan, ticket, or other owner-record ownership when the decision or assumption
  needs to persist.
