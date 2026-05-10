# Spec Shape

A spec is a durable behavior contract.

It should be as small as the behavior allows and as precise as downstream work
needs.

## Required Shape

A useful spec says:

- what behavior or interface it defines
- what problem, ambiguity, or shared contract requires a spec
- what the desired behavior is
- what is out of scope
- which requirements must hold
- which scenarios exercise those requirements
- what evidence could show the behavior works
- what questions or assumptions remain

Use optional sections when they clarify downstream work: quality bar, interface
contract, examples and non-examples, constraints, amendment notes, or related
records.

## Requirements

Requirements are durable behavior claims.

Use `REQ-*` IDs, starting at `REQ-001`.

Good requirements:

- state one behavior, invariant, interface guarantee, error semantic, permission
  rule, compatibility promise, or quality constraint
- name the actor, system, API, workflow, or record surface when it matters
- name the condition or trigger when it matters
- name the observable outcome
- avoid implementation steps unless the interface, command, or file shape is the
  behavior being specified

Prefer precise language. Use `MUST` for hard requirements and `SHOULD` only when
exceptions are legitimate and named.

Do not reuse a requirement ID for different behavior. If meaning changes enough to
mislead existing references, supersede the old ID and create a new one.

## Scenarios

Scenarios are concrete probes for requirements.

Use `SCN-*` IDs, starting at `SCN-001`.

Each scenario should cite the requirements it exercises.

Use GIVEN, WHEN, THEN, and AND steps when that structure clarifies state, trigger,
and outcome.

Include the smallest happy path plus material edge, failure, permission,
compatibility, empty-state, and idempotency cases when they affect behavior.

Remove or sharpen scenarios that cannot plausibly be tested, observed, or reviewed.

## Evidence Plan

The evidence plan says how downstream work could prove the requirements and
scenarios.

Evidence can be tests, command output, screenshots, logs, manual observations,
diff review, trace output, generated artifacts, or another durable observation.

Specs define expected evidence. Evidence records store observed artifacts.

Good evidence expectations are claim-scoped. They say which requirement or scenario
the evidence should support and what observation would be sufficient.

## Quality Bar

Use a quality bar when the intended behavior includes quality beyond existence.

For UI, UX, product, operator workflow, API ergonomics, developer experience,
agent workflow, or record quality, name observable probes such as:

- task clarity
- before/after comparison
- discoverability
- error clarity
- density
- affordance quality
- compatibility
- examples and non-examples
- reduced ambiguity for downstream agents

Quality bars should be observable enough for tickets and audit to evaluate.

## Interface Contract

Use an interface contract for public APIs, module interfaces, component props,
commands, data shapes, file formats, packets, records, or cross-worker contracts.

Name inputs, outputs, side effects, ordering, idempotency, error semantics,
validation boundary, compatibility, and deprecation expectations when they matter.

When the interface is versioned or compatibility-sensitive, state which versions,
callers, files, or consumers are in scope.

## Examples And Non-Examples

Examples make fuzzy quality concrete.

Use examples, non-examples, screenshots, comparable flows, short prose examples,
or anti-patterns when they prevent generic or ambiguous implementation.

Good examples show the boundary of the behavior. Good non-examples prevent nearby
wrong implementations.

## Boundaries And Non-Goals

A spec should make scope boundaries visible.

Useful boundaries include:

- behaviors intentionally excluded
- interfaces or callers not covered
- environments, versions, or data shapes not covered
- quality claims not being made
- compatibility promises not being extended
- implementation choices intentionally left to tickets

Use non-goals to prevent likely scope creep or downstream misinterpretation.

## Shaping Behavior

Before writing or accepting a spec, shape the behavior until four things are true:

- behavior question: the spec names the behavior, interface, invariant, workflow,
  or record shape being defined
- bounded scope: the spec can say what is covered, what is excluded, and where the
  contract stops
- observable scenarios: the behavior can be probed through concrete scenarios,
  examples, commands, UI states, API calls, records, or review checks
- downstream use: tickets, packets, evidence, audit, or future agents can cite the
  requirements and scenarios without redefining them

Inspect existing specs, tickets, plans, research, constitution, evidence,
knowledge, and source files that already constrain the behavior.

When operator input is needed:

- ask one material question at a time
- recommend an answer when the repository, records, risk, or product shape supports
  one path
- challenge vague or overloaded terms before they become requirements
- test proposed wording against concrete scenarios
- surface assumptions whose answer would change behavior, UX, architecture,
  evidence expectations, risk, or scope

Good shaping questions include:

- What smallest valuable behavior should exist?
- What is explicitly not being done?
- What current behavior, workaround, failure, or baseline matters?
- Which actor, workflow, API, command, record, or interface is affected?
- Which success, edge, failure, permission, empty-state, compatibility, or
  idempotency scenario would reveal the boundary?
- What evidence would show the behavior works?

Record settled answers in the spec. Route unsettled questions to the surface that
can answer them.

Stop shaping when remaining questions no longer change intended behavior or can be
recorded as open questions with clear downstream limits.

## Amending A Spec

Classify meaningful changes before editing:

- added: new behavior or scenario that does not change an existing claim
- modified: changed behavior for an existing requirement or scenario
- removed: behavior is no longer intended
- renamed: terminology changed while behavior remains stable
- superseded: old IDs no longer describe the active contract and have named
  successors

Search for inbound references before changing cited IDs.

If a requirement or scenario splits, narrows, or changes enough that reuse would
mislead, mark the old ID as superseded in prose and add successor IDs.

When amending, update related requirements, scenarios, evidence expectations, open
questions, and status together so the spec remains coherent.

## Routing

Route truth to the owning surface:

- execution sequencing or complex multi-ticket strategy to plans
- live scoped work, blockers, acceptance, and closure to tickets
- investigation, tradeoffs, source synthesis, rejected paths, or null results to
  research
- durable judgment, policy, principles, or architectural precedent to constitution
- observations, logs, screenshots, reproductions, or validation outputs to evidence
- fresh-context adversarial review to audit
- accepted reusable explanation to knowledge

## Contract Review

Before downstream work relies on a spec, check:

- completeness: material behavior, edge states, non-goals, constraints, scenarios,
  and evidence expectations are covered or explicitly out of scope
- correctness: requirements describe intended behavior, not only current
  implementation or a preferred solution shape
- coherence: requirements, scenarios, examples, constraints, and open questions do
  not contradict one another
- citability: `REQ-*` and `SCN-*` IDs can be cited without requiring chat history

This is a spec-quality pass. Audit is the fresh-context challenge when a claim
needs adversarial review.
