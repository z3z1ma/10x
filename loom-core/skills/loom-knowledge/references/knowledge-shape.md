# Knowledge Shape

Knowledge records are current reusable context, not archives.

## Fit Test

Create or update knowledge when all are true:

- the content should remain available beyond the current session
- a future agent is likely to search for it
- the content helps orientation, collaboration, execution, diagnosis, or reuse
- the content is current enough to rely on as knowledge

Route elsewhere when the content changes another surface: ticket state or
acceptance, raw evidence, audit findings, plan strategy, spec behavior, research
conclusions, or constitutional judgment.

## Types

Use `Type: Knowledge <Subtype>`.

Starter types: `Knowledge Preference` for eager-loaded preferences,
`Knowledge Procedure` for repeatable steps, `Knowledge Concept` for reusable
explanation, `Knowledge Reference` for compact lookup, `Knowledge Troubleshooting`
for symptoms and fixes, `Knowledge Atlas` for maps, `Knowledge Entity` for
recurring entities, and `Knowledge Note` when no sharper type fits.

Add a new subtype when the type will improve retrieval or use. Otherwise use
`Knowledge Note`.

## Granularity

Prefer one focused topic per file. Good topics are small enough that slug, title,
and triggers point to the same thing: one preference cluster, procedure, concept,
troubleshooting pattern, package, service, module, recurring entity, or area atlas.

Split when a record starts serving unrelated retrieval jobs.

A compact preference record may cover closely related preferences. Split when
clusters need different triggers or applicability.

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

Slugs are retrieval design. Prefer search words like
`ticket-closure-audit-procedure` or `checkout-timeout-troubleshooting`; avoid
generic slugs like `notes`, `misc`, `workflow`, `person-name`, or `new-thing`.

Rename when the slug is misleading, then repair refs with grep.

## Triggers

`Triggers:` are retrieval cues. Use words likely to appear in future tasks,
tickets, paths, errors, tools, or domain language.

Good triggers include task verbs, domain nouns, tools, frameworks, error phrases,
aliases, related record IDs, paths, and workflow names.

Do not stuff every synonym into `Triggers:`. Use enough cues to make retrieval cheap.

## Sections

Use the type template, but keep the writing prose-forward. Most records answer what
future agents should know, when it applies, how to use it, what not to infer, and
where related records, code, tools, or examples help.

Sources are optional. Add provenance or boundaries when the knowledge could be
misapplied, contested, stale, or hard to re-derive.

## Provenance And Boundaries

Knowledge may be original, derived, synthesized, or preference-shaped.

Use provenance or boundary notes when helpful: `Source:`, `Related:`, `Boundary:`,
or `Check:` for high-risk use. Keep them only when they make the knowledge easier
to apply or maintain.
