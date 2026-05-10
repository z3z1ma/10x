# How Loom Thinks

Loom turns AI engineering work into a shared human-agent control plane with clear
judgment, bounded execution slices, evidence, audit, reusable knowledge, and
recoverable records.

Loom works when the agent treats the `.loom` directory as the durable shape of the
work, not as notes beside the work.

## Truth Lives In The Right Surface

Do not let the newest artifact, loudest artifact, or current chat message win by
default.

Ask which surface can maintain the truth:

- constitution owns durable project judgment, policy, principles, constraints,
  ADRs, and roadmap direction
- tickets own executable work units, live execution state, acceptance, and closure
  posture
- research owns investigation, tradeoffs, rejected paths, synthesis, and
  conclusions
- specs own intended behavior, requirements, scenarios, interfaces, and invariants
- plans own operator-shaped strategy for complex changes spanning multiple
  tickets or execution units
- evidence owns observations, outputs, reproductions, screenshots, logs, and
  validation
- audit owns fresh-context review of claims, risks, evidence, and implementation
  shape
- knowledge owns preferences, procedures, accepted explanation, reusable
  understanding, and retrieval cues
- packets own bounded worker contracts for fresh or separate execution context

When truth is in the wrong place, move the durable version to the appropriate
surface and simplify the accidental one.

## Keep The Graph Coherent

A Loom surface is authoritative for the kind of truth it owns.

A ticket can describe live execution state, but it should not silently rewrite a
spec. A packet can bound worker execution, but it should not outrank the records
it was compiled from. Evidence can prove an observation, but it does not decide
intent. Audit can identify risk, but it does not itself change the product
contract.

When surfaces disagree, do not average them. Find the surface responsible for the
claim, preserve the correct version there, and make the conflict visible.

## The Recovery Graph

The `.loom` directory is the recovery graph.

Its records should be easy to find with `find`, reduce with `grep`, and
understand by reading the Markdown.

Use stable words, IDs, labels, headings, statuses, dates, and refs to keep the
graph searchable. Records should link to other records in prose when the connection
matters.

The prose remains the record. Structure helps retrieval, but the writing carries
the reasoning.

A record should help a future agent reason, recover, verify, or act.

## Record When It Helps

Always route work through Loom. Create records when they help.

Create or update records when doing so materially improves recovery, judgment,
execution, verification, review, or future reuse.

Skip record creation when the work is tiny, obvious, low-risk, and leaves no
durable truth behind.

Do not preserve every intermediate thought. Preserve the durable truth where a
future agent will know to look for it.

## Common Routes

If a task needs a bounded executable work unit, use tickets.

If it changes durable project judgment, policy, principle, constraint, precedent,
ADR shape, or roadmap direction, use constitution.

If it changes intended behavior, requirements, scenarios, interface expectations,
or invariants, use specs.

If it needs investigation, comparison, synthesis, rejected paths, or null results,
use research.

If it needs operator-shaped strategy across more than one bounded ticket or
execution unit, use plans.

If it makes or checks an observation, use evidence.

If it needs fresh-context review, use audit.

If it creates reusable accepted understanding, preference, procedure, or retrieval
cue, use knowledge.

If it delegates bounded work to a fresh or separate worker, use a Ralph packet.
