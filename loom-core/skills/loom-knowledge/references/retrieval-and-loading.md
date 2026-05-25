# Retrieval And Loading

Knowledge records must be cheap to find. Search from the task shape, then load the
smallest useful set.

## Eager Preference Loading

At session start, after `using-loom` doctrine is loaded, read active records with:

```text
Type: Knowledge Preference
```

Preferences are the only eager-loaded knowledge type by default.

Keep preference records compact. If eager loading becomes noisy, split or delete
low-value preferences.

## Task Retrieval Heuristics

For task-specific retrieval, search with clues already present: task nouns and
verbs, record IDs, paths, modules, commands, tools, packages, services, file names,
error text, symptoms, synonyms, knowledge types, `Triggers:`, and `Applies To:`.

Use filenames and titles to prune quickly. Read likely hits only when they can
change the work.

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
troubleshooting, atlases, entities, and reusable understanding.

Follow related records or code paths when they materially affect the task. Do not
chase them mechanically.

Route to another surface when applying knowledge would change durable judgment,
behavior, live execution state, strategy, evidence, audit findings, or research
synthesis.

When knowledge conflicts with another active record or source reality, inspect
enough context to identify which artifact should change. Update or delete stale
knowledge when it is the stale piece.

## Loading Discipline

Load the smallest set of knowledge that can materially improve the task.

Search, prune, read likely hits, and continue. Do not read every knowledge record
for an ambiguous task.

When a record proves useful, follow related records or code paths only as needed.

Fix stale, misleading, duplicated, or hard-to-find knowledge when the operator
asked for maintenance or leaving it stale would materially harm the work.

## Retrieval Quality

Good knowledge is easy to find by slug, title, `Type:`, `Triggers:`, `Applies To:`,
related record IDs, and path, tool, framework, package, or domain words in the body.

If a record is useful but hard to find, fix the slug or triggers instead of
creating a duplicate.
