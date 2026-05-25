# Maintaining Knowledge

Knowledge should stay small, current, and useful. It is for retrieval, not
historical accumulation.

## Maintenance Triggers

Update, rename, merge, split, or delete when a record no longer reflects current
practice or source reality, a preference or procedure changed, the slug or triggers
hurt retrieval, records duplicate a job, one record serves unrelated jobs, linked
records changed its context, it contains truth owned elsewhere, it is too broad to
scan, or it is stale, unverifiable, or no longer worth loading.

## Update, Rename, Merge, Split, Delete

Use the smallest honest move:

- update in place when the topic is the same and the slug still helps retrieval
- rename when the slug is misleading, then grep and repair refs
- merge when two records serve the same retrieval job
- split when one record serves unrelated retrieval jobs
- delete when obsolete, duplicated, unverifiable, misleading, or no longer worth
  scanning

A short redirect is only for rare external or hard-to-repair references.

## Routing Boundaries

Keep knowledge focused on reusable understanding, preferences, procedures,
troubleshooting, references, atlases, entities, and notes.

Route content elsewhere when it is policy or decision, intended behavior, live
execution state, multi-ticket strategy, observation or validation output, Ralph
review finding, investigation, tradeoff, rejected path, or null result.

## Preference Maintenance

Preferences are eager-loaded, so they need extra pressure to stay compact.

Preference records should contain only preferences that materially change how
future agents collaborate, communicate, review, or execute.

When a preference becomes narrow to one task, path, or tool, make it more specific
or delete it if it no longer helps.

When preferences conflict, preserve the current preference and remove or revise
the stale one.

## Atlases And References

Atlases and references are useful when they make orientation cheap. Prefer
pointers, maps, and retrieval cues over copied source material.

Update atlases and references when names, paths, modules, ownership, APIs,
commands, or conventions change.

When a map becomes too large to scan, split it by area, workflow, package, or job.

## Sensitive Data

Do not store secrets, credentials, API keys, tokens, private keys, passwords,
sensitive personal data, or raw customer data. When sensitive material matters,
record a safe cue and point to the secure system, code path, or record without the
value.

## Quality Check

Before saving knowledge, ask:

- Would a future agent search for these slug or trigger words?
- Is the record current enough to use?
- Is the topic narrow enough to scan cheaply?
- Does it avoid becoming live state, raw evidence, verdict, or behavior contract?
- Should any provenance, boundary, code path, or related record be named?
- If this replaces another record, have refs been repaired or the duplicate
  deleted?
