# Maintaining Knowledge

Knowledge should stay small, current, and useful.

The knowledge surface is for current retrieval, not historical accumulation.

## Maintenance Triggers

Update, rename, merge, split, or delete knowledge when:

- the record no longer reflects current practice, source reality, or useful
  understanding
- a preference changed or stopped mattering
- a procedure changed materially
- a record is hard to find by likely search words
- two records cover the same retrieval job
- one record serves unrelated retrieval jobs
- a ticket, plan, research record, audit, evidence record, spec, or constitution
  record changed context the knowledge depends on
- a record contains live state, raw observation, verdict, or behavior change that
  should be recorded elsewhere
- a record is too broad to scan cheaply
- a record is stale, duplicated, unverifiable, or no longer worth loading

## Update, Rename, Merge, Split, Delete

Use the smallest honest maintenance move:

- update in place when the topic is the same and the slug still helps retrieval
- rename when the slug is misleading, then grep and repair refs
- merge when two records serve the same retrieval job
- split when one record serves unrelated retrieval jobs
- delete when the record is obsolete, duplicated, unverifiable, misleading, or no
  longer worth scanning

A short redirect is only for rare cases where an external or hard-to-repair
reference would otherwise mislead future agents.

## Routing Boundaries

Keep knowledge focused on reusable understanding, preferences, procedures,
troubleshooting, references, atlases, entities, and notes.

Route content elsewhere when it is:

- policy, principle, durable decision, or hard constraint to constitution
- intended behavior, requirements, scenarios, or interface expectations to specs
- live execution state, blockers, finding disposition, or closure to tickets
- complex multi-ticket strategy or sequencing to plans
- observation, output, screenshot, reproduction, log, or validation result to
  evidence
- fresh-context review finding or verdict to audit
- investigation, tradeoff, source synthesis, rejected path, or null result to
  research

## Preference Maintenance

Preferences are eager-loaded, so they need extra pressure to stay compact.

A preference record should contain only preferences that materially change how
future agents collaborate, communicate, review, or execute.

When a preference becomes narrow to one task, path, or tool, move it into a more
specific knowledge record or delete it if it no longer helps.

When preferences conflict, preserve the current preference and remove or revise
the stale one.

## Atlases And References

Atlases and references are useful when they make orientation cheap.

Keep them compact. Prefer pointers, maps, and retrieval cues over copying large
chunks of source material.

Update atlases and references when names, paths, modules, ownership, APIs,
commands, or conventions change.

When a map becomes too large to scan, split it by area, workflow, package, or
retrieval job.

## Sensitive Data

Do not store secrets, credentials, API keys, tokens, private keys, passwords,
sensitive personal data, or raw customer data in knowledge records.

When sensitive material matters, record a safe retrieval cue and point to the
appropriate secure system, code path, or record without exposing the value.

## Quality Check

Before saving knowledge, ask:

- Would a future agent search for these slug or trigger words?
- Is the record current enough to use?
- Is the topic narrow enough to scan cheaply?
- Does it avoid becoming live state, raw evidence, verdict, or behavior contract?
- Should any provenance, boundary, code path, or related record be named?
- If this replaces another record, have refs been repaired or the duplicate
  deleted?
