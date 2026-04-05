# Specs Schema Reference

## Purpose

Specs describe behavior, requirements, scenarios, and acceptance.

Use a spec when intended behavior needs a durable contract that plans, tickets, critique, and docs can all refer to without redefining the behavior each time.

## What A Spec Owns

A spec owns:

- the problem framing
- the intended behavior
- the constraints that materially shape the solution space
- the requirements and scenarios that make the behavior concrete
- the acceptance language that later verification and critique can judge against

It does not own live execution state.

## A Strong Spec Answers

1. what behavior is wanted
2. why that behavior matters
3. what constraints shape the design space
4. which scenarios the behavior must satisfy
5. what evidence will count as acceptance

It should make it possible for plans, tickets, critique, and docs to talk about the same intended behavior without redefining it each time.

## Frontmatter Expectations

Spec records should preserve:

- stable `id`
- `kind: spec`
- truthful `status`
- `repository_scope`
- links to governing constitution, research, initiative, plan, tickets, critique, or docs where relevant
- timestamps that show when the contract changed materially

## Body Expectations

The body should usually make these sections meaningful:

- `Summary`
- `Problem Framing`
- `Desired Behavior`
- `Constraints`
- `Capabilities`
- `Requirements`
- `Scenarios`
- `Acceptance`
- `Design Notes`
- `Open Questions`

The contract should remain visible even if some implementation-oriented notes are present.

## Core Rule

Specs do not function as execution ledgers. They define expected behavior for downstream plans, tickets, critique, and docs work.

## Writing Standard

Good specs:

- describe intended behavior before implementation detail
- make constraints and acceptance concrete
- separate what is normative from what is informative when necessary
- help critique test the real contract rather than a loose summary
- define enough behavior that another agent knows what must remain true even if the implementation changes

## Relationship To Neighboring Layers

- research can justify the contract or compare options before the contract hardens
- plans turn the contract into sequencing and rollout strategy
- tickets track what is actually being done to realize the contract
- critique tests whether the implementation or docs actually satisfy the contract
- docs explain the accepted reality after the contract has landed

## Review Checklist

Before treating a spec as ready, check:

1. is the problem framing clear
2. is the desired behavior explicit
3. are constraints and scenarios concrete
4. is acceptance strong enough to test or review later
5. does the spec still read like a contract instead of a design diary or status report

## Failure Cases To Avoid

- using the spec as a progress report
- leaving acceptance too vague for later verification
- burying the main behavior contract inside design-note prose
- mixing aspirational future work into the normative contract without saying so

## Done Means

- intended behavior has one clear durable owner
- constraints, scenarios, and acceptance are explicit
- downstream layers can rely on the contract without reinterpretation
