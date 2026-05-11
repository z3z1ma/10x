# Retrieval And Loading

Knowledge records must be cheap to find.

Use the shape of the task to search the knowledge surface intelligently.

## Eager Preference Loading

At session start, after `using-loom` doctrine is loaded, read active records with:

```text
Type: Knowledge Preference
```

Preferences are the only eager-loaded knowledge type by default.

Keep preference records compact. If eager loading becomes noisy, split or delete
low-value preferences.

## Task Retrieval Heuristics

For task-specific retrieval, search using the clues already present:

- task nouns and verbs from the operator request
- ticket, plan, spec, evidence, audit, research, or constitution IDs
- paths, modules, commands, tools, frameworks, packages, services, and file names
- error text, logs, symptoms, and user-facing terms
- likely synonyms and aliases
- knowledge types, such as `Knowledge Procedure` or `Knowledge Troubleshooting`
- `Triggers:` and `Applies To:` labels

Use filenames and titles to prune quickly.

Read likely hits only when they can change the work.

## Useful Queries

These are examples, not mandatory steps:

```bash
find .loom/knowledge -maxdepth 1 -name '*.md' -print 2>/dev/null | sort
grep -R '^Type: Knowledge Preference' .loom/knowledge 2>/dev/null || true
grep -R '^Type: Knowledge Procedure' .loom/knowledge 2>/dev/null || true
grep -R '^Type: Knowledge Troubleshooting' .loom/knowledge 2>/dev/null || true
grep -R '^Triggers:.*<term>' .loom/knowledge 2>/dev/null || true
grep -R '^Applies To:.*<path-or-tool>' .loom/knowledge 2>/dev/null || true
grep -R '<task-term-or-error>' .loom/knowledge 2>/dev/null || true
```

Retrieve knowledge when a preference, procedure, concept, atlas, entity,
troubleshooting pattern, or reference could materially change execution or
communication.

## Applying Knowledge

Use relevant knowledge directly for preferences, procedures, concepts, references,
troubleshooting, atlases, entities, and other reusable understanding.

Follow related records or code paths when they materially affect the task. Do not
chase them mechanically.

Route to another surface when applying the knowledge would actually change that
surface, such as:

- constitution for durable judgment, principles, constraints, and decisions
- specs for intended behavior, requirements, scenarios, and interfaces
- tickets for live execution state, finding disposition, and closure
- plans for complex multi-ticket strategy and sequencing
- evidence for observations
- audit for fresh-context review findings and verdicts
- research for investigation, tradeoffs, and source synthesis

When knowledge conflicts with another active record or with source reality, do not
smooth over the conflict. Inspect enough context to decide which artifact should
change, then update or delete stale knowledge when it is the stale piece.

## Loading Discipline

Load the smallest set of knowledge that can materially improve the task.

Search, prune, read likely hits, and continue. Do not read every knowledge record
for an ambiguous task.

When a knowledge record proves useful, follow related records or code paths only
as needed.

When a knowledge record is stale, misleading, duplicated, or hard to find, fix it
as part of knowledge maintenance when the operator asked for maintenance or when
leaving it stale would materially harm the work.

## Retrieval Quality

Good knowledge is easy to find by several routes:

- slug words
- title words
- `Type:`
- `Triggers:`
- `Applies To:`
- related record IDs
- path, tool, framework, package, or domain words in the body

If a record is useful but hard to find, fix the slug or triggers rather than
creating a duplicate.
