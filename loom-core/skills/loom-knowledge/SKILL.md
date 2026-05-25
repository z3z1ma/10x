---
name: loom-knowledge
description: "Use when reusable understanding, preferences, procedures, concepts, references, troubleshooting notes, atlases, entities, or task-relevant recall should remain available beyond the current session."
---

# loom-knowledge

Knowledge is Loom's reusable understanding and retrieval station: current
preferences, procedures, concepts, references, troubleshooting, atlases, entities,
and notes future agents should find and apply quickly.

## Use This Skill When

Use this skill when any of these should survive the session:

- a preference should shape future collaboration, execution, or review
- a repeatable procedure, accepted explanation, troubleshooting path, atlas,
  reference, entity note, or retrieval cue should survive the session
- a future agent will likely search by task, path, tool, error, workflow, domain
  term, or record ID
- existing knowledge is stale, duplicated, misleading, too broad, badly named, or
  no longer useful

Knowledge must improve future retrieval, reuse, orientation, diagnosis, or
collaboration. Do not store one-off notes, chat residue, live state, unresolved
investigation, raw evidence, audit verdicts, behavior contracts, or secrets here.

## Dispatch

Create or materially update:

- read `references/knowledge-shape.md`
- read `references/retrieval-and-loading.md`
- read `references/maintaining-knowledge.md`
- search existing knowledge before creating a new record
- choose a keyword-rich slug, title, and `Triggers:` future agents are likely to
  search
- choose the narrowest useful `Type: Knowledge <Subtype>`
- include `Applies To:` when path, domain, tool, workflow, or context scope matters
- use the matching template from `templates/`

Load:

- after `using-loom` doctrine, eagerly load active `Type: Knowledge Preference`
  records; this type label is the loading signal
- for task work, search slugs, titles, `Triggers:`, `Applies To:`, and body text
  using words from the task, ticket, paths, tools, errors, and domain concepts
- read likely hits only when they can change the work
- follow related records or code paths when they are needed to apply the knowledge
  safely

Maintain:

- update in place when the same topic remains useful
- rename when the slug hurts retrieval, then repair refs with grep
- merge records that serve the same retrieval job
- split records that serve unrelated retrieval jobs
- delete obsolete, misleading, duplicate, unverifiable, or low-value records

Find or summarize:

- inspect `.loom/knowledge/`
- report what the knowledge record says
- preserve the scope and limits the knowledge record states

## Finding

Knowledge records live flat under `.loom/knowledge/`. Useful queries:

```bash
find .loom/knowledge -maxdepth 1 -name '*.md' -print 2>/dev/null | sort
grep -R '^ID: knowledge:' .loom/knowledge 2>/dev/null || true
grep -R '^Type: Knowledge' .loom/knowledge 2>/dev/null || true
grep -R '^Type: Knowledge Preference' .loom/knowledge 2>/dev/null || true
grep -R '^Triggers:' .loom/knowledge 2>/dev/null || true
grep -R '^Applies To:' .loom/knowledge 2>/dev/null || true
```

Search with slugs, titles, triggers, path names, domain terms, tool names, error
text, and record IDs.

## IDs And Shape

Use stable, keyword-rich IDs and matching filenames:

```text
knowledge:<keyword-rich-slug>
.loom/knowledge/<keyword-rich-slug>.md
```

Slugs are retrieval tools. Prefer likely search words, not `notes`, `misc`,
`workflow`, `person-name`, or `new-thing`. Top labels:

```text
ID: knowledge:<keyword-rich-slug>
Type: Knowledge Preference
Status: active
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Triggers: comma-separated retrieval words and task cues
Applies To: optional paths, domains, tools, workflows, or contexts
```

Use only `Status: active`; otherwise update, rename with refs repaired, merge,
split, or delete. Starter types: `Knowledge Preference`, `Knowledge Procedure`,
`Knowledge Concept`, `Knowledge Reference`, `Knowledge Troubleshooting`,
`Knowledge Atlas`, `Knowledge Entity`, and `Knowledge Note`. New subtypes are
allowed only when they improve retrieval or use.

## Invariants

Every record should be:

- current enough to use
- topic-sized rather than sprawling
- keyword-rich slug, title, and `Triggers:` for retrieval
- `Type:` specific enough to guide loading and use
- optional `Applies To:` when path, domain, tool, or workflow scope matters
- provenance, boundary, or related-record notes when they make use safer
- free of secrets, credentials, private keys, tokens, passwords, and sensitive
  personal data

Preferences are the eager-loaded knowledge type. Other knowledge is retrieved when
the task, path, tool, error, record, or domain makes it relevant.

## Stop Conditions

Stop or route elsewhere when the proposed record would really change:

- policy, principle, decision, or hard constraint -> constitution
- intended behavior, requirement, scenario, interface, or invariant -> specs
- live execution state, blocker, finding disposition, or closure -> tickets
- multi-ticket sequencing, rollout, or recovery strategy -> plans
- observation, output, reproduction, log, screenshot, or validation result -> evidence
- Ralph review finding or verdict -> audit
- investigation, tradeoff, source synthesis, rejected path, or null result -> research

If knowledge conflicts with source reality or another active record, inspect enough
context to identify the stale artifact. Do not smooth over the conflict.

## Done Means

Knowledge work is done when:

- the record can be found by likely task words
- the slug, title, type, `Triggers:`, and `Applies To:` make retrieval cheaper
- the prose is useful on its own
- applicability and limits are clear enough to prevent overclaiming
- outdated or duplicate knowledge was updated, merged, renamed with refs repaired,
  or deleted
