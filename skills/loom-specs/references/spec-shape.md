# Spec Shape

## Core sections

- Summary
- Problem
- Problem Pressure Check
- Desired Behavior
- Quality Bar
- Options Considered
- Not Doing
- Boundary Tiers when operator or delivery authority matters
- Interface / API Contract when the behavior exposes a public or shared surface
- Examples / Non-Examples
- Constraints
- Requirements
- Scenarios
- Acceptance
- Evidence Plan
- Assumptions / Decision Points
- Open Questions

## Quality Bar

The quality bar prevents "it exists" from becoming "it is good." It names what
would make the result materially better than the current or baseline state.

For UI, UX, product, workflow, or operator-facing behavior, include observable
quality probes such as primary user task clarity, discoverability, affordance
quality, density, before/after comparison, or examples and non-examples.

## Options Considered And Not Doing

Use `# Options Considered` when several behaviors, APIs, UX flows, architecture
shapes, or workflow designs would satisfy the same rough request. Keep it compact:
two or three materially different directions, their tradeoffs, and why the chosen
direction best fits the problem pressure check.

Use `# Not Doing` when scope focus matters. A good non-goal says which attractive
idea was deliberately excluded and why excluding it keeps the contract sharper.
Do not bury product tradeoffs in prose enthusiasm.

If options remain evidence-light, route to research or spike. If one option would
change durable policy, route to constitution. If an assumption is unresolved and
material, keep it as a decision point instead of silently choosing.

## Examples And Non-Examples

Use examples to make fuzzy quality concrete. Sources can include screenshots,
comparable workflow pages, accepted patterns, anti-patterns, or short prose
examples. Non-examples are especially useful for preventing safe-but-generic agent
output.

## Problem Pressure Check

Use this section when product, UX, workflow, API, or behavior direction could be
invented by the agent. It keeps a spec from laundering an untested solution shape
into a behavior contract.

Check only the gaps that matter for the scope:

- evidence: what observed pain, workaround, request, failure, or baseline proves
  this problem exists?
- specificity: which user, operator, system, API consumer, or maintenance surface
  is affected?
- counterfactual: what happens today if nothing changes?
- attachment: what is the smallest valuable shape, and what larger solution shape
  is intentionally out of scope?
- durability: what predictable change would make this contract wrong or stale?

If an answer would materially change behavior, UX, architecture, acceptance, risk,
or scope, record it as a decision point. Do not hide it in prose confidence.

## Spec Grilling Procedure

Use this when creating or reshaping a spec from a fuzzy request, overloaded domain
language, a proposed solution, a disputed behavior, or a plan that would otherwise
make tickets guess.

The grilling pass is the behavior-contract equivalent of walking the design tree:
resolve one material branch at a time until the intended behavior is stable enough
for planning, ticketing, evidence, and critique.

Procedure:

- read relevant specs, wiki pages, research, decisions, and prior tickets when
  those owner records already carry behavior, domain language, constraints, or
  tradeoffs that shape the contract
- ask one material question at a time when operator input is needed; wait for the
  answer before moving to dependent branches
- provide a recommended answer for each material question, including the behavior,
  user, API, risk, or owner-record signal that makes that answer plausible
- challenge terminology conflicts immediately: if accepted language says one thing
  and the request appears to mean another, ask which term or concept should win
- sharpen fuzzy terms into canonical concepts, roles, states, and boundaries; do
  not let overloaded language become acceptance criteria
- invent concrete scenarios, including edge and failure scenarios, that force
  boundaries between concepts and reveal whether the proposed contract is too broad
  or too narrow
- capture resolved truth in the owner that can maintain it: spec for intended
  behavior, wiki for accepted shared language, research for rejected options or
  null results, plan for execution decomposition, ticket for live local assumptions,
  and constitution decision records only for choices that are hard to reverse,
  surprising without context, and tradeoff-backed

Do not import a project-specific glossary file layout as Loom ontology. The Loom
equivalent is owner-layer routing: wiki for accepted language, specs for behavior,
constitution decisions for durable precedent, and tickets for live execution truth.

If a grilling question blocks the contract, leave it as a blocking decision point.
If it merely shapes execution order after behavior is settled, route it to the plan.

## Decision Points

Surface assumptions whose answer would materially change behavior, UX,
architecture, acceptance, risk, or scope. Low-risk reversible assumptions may be
recorded as accepted. Material or irreversible assumptions should block execution
until the user or the owning record resolves them.

## Boundary Tiers

Use boundary tiers when the spec constrains what agents, builders, or users may do
around the behavior:

- **Always**: required invariants, validation, checks, compatibility, or safety
  behavior.
- **Ask first**: changes that need operator, product, security, data, or
  architecture approval before downstream work.
- **Never**: forbidden actions such as weakening security, deleting user data,
  disabling checks, or widening scope outside the accepted contract.

These tiers are behavior and authority boundaries for this spec. They do not
replace ticket state, critique disposition, or external approval workflows.

## Interface / API Contracts

For public APIs, module interfaces, component props, command surfaces, data
schemas, or cross-worker contracts, specify the observable contract before
downstream work depends on it:

- inputs, outputs, generated fields, side effects, ordering, and idempotency
- error semantics and status/result shapes
- validation boundary and trust assumptions for external data
- compatibility expectations, deprecation path, and additive vs breaking changes
- examples and non-examples that make misuse visible

## Anti-patterns

Avoid:

- delivery journals
- strategic roadmap language
- research dumps with no contract
- hand-wavy acceptance language
- public or shared interfaces with missing error, validation, compatibility, or
  deprecation semantics
- solution attachment accepted as intended behavior before the problem is checked
- spec creation that records a pressure-check table but skips the active grilling
  loop needed to resolve fuzzy terms, contract conflicts, or concrete scenarios
- quality claims without examples, non-examples, or evidence plan
- silently accepted product or UX assumptions that would change the result
- one-path specs for fuzzy product or workflow requests where divergent options
  were never considered
- specs with no explicit `Not Doing` boundary when delivery could easily grow
  beyond the smallest valuable shape

## Good linking

Specs commonly link to:

- initiative
- research
- plan
- ticket
- critique
- wiki
