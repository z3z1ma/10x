# Research Schema Reference

## Purpose

Research records capture reusable discovery.

Use research when the repository needs durable evidence, investigation, comparisons, experiments, or synthesis that later work should cite instead of rediscovering.

## What Research Owns

Research owns:

- the question being investigated
- the investigation method
- the evidence gathered
- the rejected paths and unresolved questions that still matter
- the conclusions and recommendations that later layers should inherit

Research does not own live execution state, accepted behavior contracts, or final explanatory docs.

## A Strong Research Record Answers

1. what question was being investigated
2. what decision or uncertainty motivated the investigation
3. what method was used
4. what evidence was gathered
5. what conclusions are justified
6. what downstream work should do next

It should make clear what is still unknown and what evidence would change the current conclusion.

## Frontmatter Expectations

Research records should preserve:

- stable `id`
- `kind: research`
- truthful `status`
- `repository_scope`
- links to downstream specs, plans, tickets, initiatives, critique, or docs when relevant
- timestamps that show when the note was created and revised

## Body Expectations

The body should usually make these sections meaningful, not decorative:

- `Question`
- `Objective`
- `Scope`
- `Non-goals`
- `Methodology`
- `Hypotheses`
- `Evidence`
- `Experiments`
- `Rejected Paths`
- `Conclusions`
- `Recommendations`
- `Open Questions`
- `Linked Downstream Artifacts`

The exact prose can vary, but a later reader should be able to audit the reasoning chain.

## Writing Standard

Good research records:

- capture evidence quality explicitly
- separate conclusions from hypotheses
- preserve rejected paths so later work does not repeat them blindly
- point downstream clearly into specs, plans, or tickets
- remain synthesis-oriented rather than conversational

The durable value is not the raw transcript. The durable value is curated understanding.

## Relationship To Neighboring Layers

- move intended behavior into specs when the note starts acting like a contract
- move sequencing and rollout thinking into plans when the note starts prescribing execution strategy
- move live progress and blockers into tickets when the note starts acting like a ledger
- move accepted explanation into docs when the investigation result is already settled enough to teach operators

## Review Checklist

Before relying on a research note, check:

1. is the question crisp
2. is the method explicit enough to audit later
3. is the evidence concrete rather than impressionistic
4. are conclusions bounded by what the evidence supports
5. are downstream implications explicit

## Failure Cases To Avoid

- dumping transcript fragments without synthesis
- leaving the downstream implication of the research unclear
- reporting conclusions without enough evidence context for later reuse
- using research as a parking lot for unresolved execution truth
- omitting rejected paths that later work is likely to rediscover

## Done Means

- the question, method, evidence, and conclusions are explicit
- uncertainty is visible instead of hidden by false confidence
- downstream consumers know what to do with the note
- another agent can reuse the investigation without replaying it
