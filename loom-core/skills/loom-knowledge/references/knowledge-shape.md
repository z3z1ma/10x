# Knowledge Shape

Knowledge is current reusable context, not an archive.

The record should help a future agent retrieve and apply the right understanding.

## Fit Test

Create or update knowledge when all of these are true:

- the content should remain available beyond the current session
- a future agent is likely to search for it
- the content helps orientation, collaboration, execution, diagnosis, or reuse
- the content is current enough to rely on as knowledge

Route elsewhere only when the content is actually changing another surface, such
as ticket state, ticket acceptance, raw evidence, audit findings, plan strategy,
spec behavior, research conclusions, or constitutional judgment.

## Types

Use `Type: Knowledge <Subtype>`.

Starter types:

- `Knowledge Preference`: collaboration or operator preferences future agents
  should load eagerly
- `Knowledge Procedure`: repeatable steps or operating patterns
- `Knowledge Concept`: reusable explanation of a concept or mental model
- `Knowledge Reference`: compact lookup for fields, commands, conventions, or
  facts
- `Knowledge Troubleshooting`: symptoms, checks, causes, and fixes
- `Knowledge Atlas`: accepted map of a codebase, module, system, or area
- `Knowledge Entity`: compact note for a recurring person, system, service,
  package, tool, topic, or alias cluster
- `Knowledge Note`: useful current knowledge that does not fit a sharper type

Add a new subtype when the type will improve retrieval or use. Otherwise use
`Knowledge Note`.

## Granularity

Prefer one focused topic per file.

Good topics are small enough that the slug, title, and triggers all point to the
same thing:

- one operator preference cluster
- one repeatable procedure
- one reusable concept
- one troubleshooting pattern
- one package, service, module, or recurring entity
- one codebase area atlas

Split when a record starts serving unrelated retrieval jobs.

A compact operator-preferences record can cover several closely related
collaboration preferences. Keep it short; split when separate preference clusters
need different triggers or applicability.

## Top Labels

Use these labels near the top:

```text
ID: knowledge:<keyword-rich-slug>
Type: Knowledge <Subtype>
Status: active
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Triggers: comma-separated retrieval words and task cues
Applies To: optional paths, domains, tools, workflows, or contexts
```

Remove `Applies To:` only when it adds no retrieval value.

Do not add a load label. `Type: Knowledge Preference` is the eager-loading signal.

## Slugs

Slugs are retrieval design.

A good slug includes the words a future agent would use to prune search results.

Prefer:

- `operator-preferences-review-final-summary`
- `ticket-closure-audit-procedure`
- `react-query-cache-invalidation-reference`
- `checkout-timeout-troubleshooting`

Avoid:

- `notes`
- `misc`
- `workflow`
- `alex`
- `new-thing`

Rename when the slug is misleading, then repair refs with grep.

## Triggers

`Triggers:` are retrieval cues.

Use words likely to appear in future tasks, tickets, paths, errors, tools, or
domain language.

Good triggers include:

- task verbs
- domain nouns
- tool or framework names
- error phrases
- aliases
- related record IDs
- paths or path fragments
- workflow names

Do not stuff every synonym into `Triggers:`. Use enough cues to make retrieval
cheap.

## Sections

Use the template for the type, but keep the writing prose-forward.

Most knowledge records should answer:

- what future agents should know
- when it applies
- how to use it
- what should not be inferred from it
- where related records, code, tools, or examples are useful

Sources are optional. Include provenance or boundary notes when the knowledge
could be misapplied, contested, stale, or hard to re-derive.

## Provenance And Boundaries

Knowledge may be original, derived, synthesized, or preference-shaped.

Use provenance or boundary notes when helpful:

- `Source:` where the understanding came from, if worth preserving
- `Related:` records, code paths, tools, examples, or artifacts that help apply it
- `Boundary:` where the knowledge stops applying
- `Check:` what to inspect before relying on it for high-risk work

Use these notes when they make the knowledge easier to apply or maintain.
