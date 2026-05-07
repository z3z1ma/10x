# Spec Shape

## Core sections

- Summary
- Problem
- Problem Pressure Check
- Desired Behavior
- Quality Bar
- Options Considered
- Not Doing
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
current implementation behavior, comparable workflow pages, accepted patterns,
anti-patterns, or short prose examples. Non-examples are especially useful for
preventing safe-but-generic agent output.

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

## Decision Points

Surface assumptions whose answer would materially change behavior, UX,
architecture, acceptance, risk, or scope. Low-risk reversible assumptions may be
recorded as accepted. Material or irreversible assumptions should block execution
until the user or the owning record resolves them.

## Anti-patterns

Avoid:

- implementation journals
- strategic roadmap language
- research dumps with no contract
- hand-wavy acceptance language
- solution attachment accepted as intended behavior before the problem is checked
- quality claims without examples, non-examples, or evidence plan
- silently accepted product or UX assumptions that would change the result
- one-path specs for fuzzy product or workflow requests where divergent options
  were never considered
- specs with no explicit `Not Doing` boundary when implementation could easily
  grow beyond the smallest valuable shape

## Good linking

Specs commonly link to:

- initiative
- research
- plan
- ticket
- critique
- wiki
