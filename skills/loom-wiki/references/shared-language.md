# Shared Language Pages

Shared language is accepted terminology that helps future agents and humans use
the same project nouns. It is especially useful when domain words, architecture
terms, user-facing concepts, or workflow labels keep being re-explained in chat.

Wiki owns accepted explanation of terms. It does not own behavior contracts,
policy, live execution, or evidence.

## When To Create Or Update

Use a shared-language page when:

- terminology affects code names, specs, tickets, or critique findings;
- the same domain term is used inconsistently;
- a project has canonical terms and avoided synonyms;
- an architecture or product concept needs a short reusable definition;
- a future agent would otherwise burn context rediscovering vocabulary.

Route elsewhere when:

- the term defines intended behavior -> `loom-specs`;
- the term encodes durable policy or naming principle -> `loom-constitution`;
- the meaning is still disputed or evidence-light -> `loom-research`;
- the term is one-ticket scope only -> `loom-tickets`.

## Page Shape

A shared-language page may be a reference page or concept page. Keep entries
short and operational.

Useful entry shape:

```md
## <Term>

Meaning: <one or two sentences>

Use when: <where this term applies>

Avoid: <synonyms or confusing nearby terms, with reason>

Related: <other terms or owner records>

Source: <spec/research/wiki/decision/evidence refs>
```

## Discipline

- Prefer a small set of strong terms over a glossary dump.
- Include avoided terms when naming drift would make code, specs, or tickets worse.
- Cite owner records so the page does not become authoritative by eloquence.
- Update code/spec/wiki terminology deliberately when an accepted term changes.
- Mark contested, stale, or superseded terms instead of smoothing disagreement.

## Term Conflict Loop

When a user, ticket, spec, wiki page, or code path uses a term differently from an
accepted shared-language page, surface the conflict instead of normalizing it away:

```text
The accepted page uses <term> to mean <X>, but this request/code path appears to
mean <Y>. Which owner record should change, if any?
```

Then route the answer:

- accepted reusable meaning changed -> update the wiki page and linked owner records
- behavior meaning changed -> update the spec first
- code naming is misleading but behavior is unchanged -> ticket or refactor work
- disagreement remains unresolved -> research or ticket blocker

Do not put implementation details into shared language merely because a code file
uses a term. Shared language should name domain, architecture, product, or
workflow concepts future operators need.
