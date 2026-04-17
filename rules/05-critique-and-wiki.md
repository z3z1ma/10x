# Critique And Wiki

Critique and Wiki are not side quests.
They are how Loom pressure-tests work and how Loom compounds understanding.

## Critique Is A Ralph Variant

Critique uses the same packetized fresh-context model as Ralph, but the goal is different.

Ralph asks:

- can this bounded step be executed safely and usefully

Critique asks:

- is the resulting shape actually good
- are the claims supported
- what residual risks remain
- what follow-up work is required before acceptance

A critique pass should feel adversarial in the healthy sense.
It should search for mismatches, hidden assumptions, weak evidence, brittle reasoning, and user-facing confusion.

## Default Critique Policy

Use this as the default until a project records something stricter.

### Low risk

Examples:

- small link fixes
- local wording cleanup
- minor ticket hygiene

Default: critique optional.

### Medium risk

Examples:

- meaningful workflow changes
- important packet changes
- behavior clarifications that could mislead operators

Default: critique recommended.

### High risk

Examples:

- scope model changes
- authority model changes
- changes to how completion is judged
- architecture changes with broad downstream impact

Default: critique mandatory.

## What Good Critique Produces

A good critique record makes these explicit:

- review target
- verdict
- findings
- severity
- confidence
- evidence reviewed
- residual risks
- required follow-up

A good critique does not merely say "looks good".
It leaves a durable review surface another agent can inspect later.

## Wiki Is Also A Ralph Variant

Wiki work is a packetized knowledge-compilation pass.

It happens after enough truth is accepted that the understanding should persist as a page instead of a chat answer.

Wiki is where Loom stores:

- architecture explanations
- workflow guides
- concept pages
- operator references
- troubleshooting notes
- synthesis pages that answer recurring questions

## What Makes Wiki Different From Old Docs

Wiki is not a dumping ground for prose.

Wiki is:

- interlinked
- maintained over time
- grounded in accepted truth
- designed for future retrieval and reuse
- allowed to grow page by page as understanding compounds

A strong wiki page should reduce the chance that a future agent needs to re-derive the same explanation from scratch.

## Promotion Rule

Promote something into the wiki when one or more of these are true:

- the same question will likely come up again
- the answer requires synthesis across multiple records
- the accepted workflow changed materially
- the project now has a concept or pattern worth naming explicitly
- another agent would benefit from reading the page before touching nearby work

## Wiki Source Rule

A wiki page should be grounded in:

- canonical records
- accepted critique outcomes
- evidence
- accepted external sources when the page is summarizing outside knowledge

Do not let a wiki page become authoritative by eloquence alone.
Its sources should be inspectable.

## Relationship To Tickets

Tickets remain the live execution ledger.
Wiki does not replace them.

The relationship is:

- tickets say what is happening
- critique says what is risky or weak
- wiki says what is now understood and worth preserving

## Relationship To Memory

Memory is optional support context.
Wiki is canonical explanation.

If a concept matters to the project as a whole, it belongs in the wiki rather than only in memory.

## Maintenance Rule

Wiki pages should age deliberately.

When accepted reality changes:

- update the page if it still describes the same concept
- mark it stale if the concept remains but the page is out of date
- supersede it if a better page replaces it
- link forward from the old page when practical

Good wiki maintenance makes the knowledge base compound instead of rot.
