# Docs Schema Reference

## Purpose

Docs records explain accepted system shape to an audience.

They should help another agent or operator understand what exists, why it exists, how it is used, and what evidence supports the claims being made.

## A Strong Docs Record Answers

1. who the document is for
2. what problem or workflow the document explains
3. what system shape is already accepted
4. what examples make the explanation concrete
5. what evidence supports the explanation
6. what would make the document stale later

It should also answer why this explanation belongs in durable docs rather than in a ticket, plan, or transient chat summary.

## Frontmatter Expectations

Docs records should preserve:

- stable `id`
- `kind: doc`
- truthful `status`
- `repository_scope`
- links to truth sources such as constitution, spec, plan, ticket, critique, and verification records when relevant
- timestamps that show when the explanation changed materially

## Section Guidance

- `Overview`: summarize the document's purpose in plain language
- `Audience`: name the intended reader clearly
- `Problem Framing`: explain why the document exists
- `Accepted System Shape`: describe the accepted behavior or architecture, not aspirational future state
- `Workflow / Operations Details`: give the reader a usable procedure or mental model
- `Rationale`: explain why the accepted shape works this way
- `Examples`: make the workflow or shape concrete
- `Verification Source`: show what evidence supports the claims
- `Related Artifacts`: link nearby specs, plans, tickets, or other docs
- `Supersession / History`: explain whether the doc replaces an earlier explanation or is itself likely to be replaced later

The body should make it easy for a future reader to distinguish accepted reality from motivation, rationale, examples, and known stale triggers.

## Strong Documentation Characteristics

Good Loom docs are:

- detail-first rather than blurb-first
- self-contained for future human and AI readers
- dense with architecture, workflow, and rationale context
- explicit about scope, assumptions, dependencies, and evidence
- careful not to duplicate live execution logs or ticket state unnecessarily

## Relationship To Neighboring Layers

- tickets tell what is happening right now
- docs explain what a future operator should understand after the work is accepted
- plans may motivate the explanation, but plans do not define accepted reality
- critique may shape whether the explanation is trustworthy enough to publish

## Evidence Discipline

If a doc claims accepted system reality, it should preserve enough truth-source and verification context that a later reader can understand why those claims are trustworthy.

## Failure Cases To Avoid

- explaining proposed future state as if it were already accepted
- writing for people who were present instead of future readers
- duplicating a ticket journal instead of teaching the workflow or architecture
- omitting the evidence basis behind strong claims

## Done Means

- the intended audience is obvious
- the accepted system shape is clear
- rationale, examples, and evidence basis make the explanation trustworthy
- the doc can stand on its own for a future reader
