# Constitution Schema Reference

## Purpose

Use the constitution layer when the repository needs durable policy, identity, principle, doctrine, roadmap, or decision truth.

Constitution records are where Loom says what the project is, what it values, what constraints it accepts, and what durable strategic direction should survive beyond the current wave of execution.

## Which Constitutional Record To Use

- use the main constitution record for project identity, durable principles, constraints, and stable strategic direction
- use a decision record for one bounded architectural or policy choice that needs durable history
- use a roadmap record for longer-horizon strategic direction, milestone framing, or focus areas that should remain visible over time

If you are unsure, prefer the narrowest record that still preserves the durable truth without scattering it across multiple places.

## A Strong Constitutional Record Answers

1. what durable truth is being established or changed
2. why that truth matters to later work
3. what principles or constraints follow from it
4. what downstream artifacts or workflows it affects
5. what a future agent should now assume unless superseded later

It should help a later reader judge whether a proposed change aligns with durable project intent or conflicts with it.

## Frontmatter Expectations

Constitution-layer records should preserve at least:

- a stable `id`
- `kind` that matches the record family
- truthful `status`
- `repository_scope`
- typed `links` to affected downstream artifacts when relevant, except for `constitution:main`
- `created_at` and `updated_at`

Do not use frontmatter links as a substitute for prose. The body should explain the actual meaning of the change.

The main constitution record is the exception to normal downstream-link practice: `constitution:main` is implicitly authoritative for the whole workspace and should keep `links: {}`.

The constitution layer currently uses these first-class kinds:

- main constitution: `kind: constitution`
- decision records: `kind: decision`
- roadmap records: `kind: roadmap`

## Body Expectations By Record Type

### Main Constitution

The main constitution should usually make these areas explicit:

- vision or identity
- principles
- constraints
- strategic direction
- current focus
- open constitutional questions
- change history when durable policy changes matter later

Its downstream impact should be explained in prose rather than through outbound frontmatter links.

### Decision Record

A decision record should normally use these headings:

- Decision
- Why This Decision Exists
- Alternatives Considered
- Consequences
- Supersession

A decision record should usually make these areas explicit:

- the decision itself in plain language
- why the decision was made now
- what alternatives were rejected or left open
- what downstream artifacts or workflows are constrained by the choice
- whether the decision supersedes or narrows earlier assumptions

### Roadmap Record

A roadmap record should normally use these headings:

- Strategic Theme
- Why Now
- Focus Areas
- Milestones
- Sequencing Assumptions
- Downstream Work
- Status Summary

A roadmap record should usually make these areas explicit:

- the strategic direction being pursued
- why now is the right time
- focus areas or milestones
- sequencing or ordering assumptions at a strategic level
- what downstream initiative, spec, plan, or ticket work should exist beneath it

## Writing Standard

Good constitutional writing is:

- durable rather than reactive
- strategic rather than operational
- explicit about constraints and principles
- useful as a judgment frame for later work
- self-contained enough that a later reader does not need transcript archaeology

Good constitutional writing says what future work is allowed, encouraged, constrained, or ruled out.

## Relationship To Neighboring Layers

- initiatives inherit strategic direction from constitutional records
- specs should align with constitutional constraints instead of redefining them silently
- plans should implement constitutional strategy rather than inventing conflicting policy
- tickets should not carry durable policy that belongs here
- docs may explain accepted constitutional ideas, but docs do not define policy authority

## Review Checklist

Before accepting a constitutional change, check:

1. is the record family correct
2. does the record establish durable truth rather than temporary execution state
3. are principles, constraints, or strategic consequences explicit
4. does `constitution:main` stay link-free while decision and roadmap records link downstream work when that materially helps
5. would a future agent know how this record should influence later work

## Failure Cases To Avoid

- turning the constitution into a day-to-day project diary
- recording execution truth here instead of in tickets or plans
- making the main constitution enumerate downstream records instead of acting as implicitly authoritative context
- writing vague philosophy that does not actually constrain later work
- creating a decision record that never explains why the decision matters

## Good Constitutional Writing

Good constitutional writing makes later work easier because it tells a fresh reader how to judge proposed changes against durable project intent.

## Done Means

- the right constitutional artifact owns the truth change
- the body preserves durable meaning rather than transient context
- affected downstream work is visible where relevant
- a later agent can use the record as a judgment frame without guessing
