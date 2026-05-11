# Creating Evidence

Evidence can be created during shaping, execution, audit, research, or standalone
observation.

The invariant is observation before inference.

Record what was observed. If the observation reveals ambiguity, record the
limitation or route the ambiguity to the surface that can resolve it.

## Choose The Shape

Use an Evidence Observation when the record preserves one observation:

- one command result
- one test run
- one screenshot or screenshot pair
- one reproduction attempt
- one manual inspection
- one scan result
- one log excerpt or artifact capture
- one external artifact snapshot

Use an Evidence Dossier when multiple observations compose one validation story:

- final ticket acceptance evidence from several checks
- migration validation composed from multiple observations
- audit-support evidence that gathers several artifacts
- a linked chain of evidence records summarized for one review question

A dossier is a finite validation story, not a live progress log.

## Creation Procedure

Use this sequence as the default path, not as a form:

1. Decide why the observation should remain available.
2. Choose Evidence Observation or Evidence Dossier.
3. Record the source state or record state being observed.
4. Record the procedure that produced the observation.
5. Record what was observed before writing what it means.
6. Capture artifact paths and key excerpts or summaries.
7. If the evidence supports or challenges a claim, cite stable claim IDs.
8. If the expected result or claim scope is unclear, record that limitation.
9. Record what the evidence does not show.
10. Link related records only when useful.

Use enough detail for a future agent to understand the observation without chat
history.

## Source And Procedure Context

Evidence is easier to trust when the source and procedure are legible.

Include relevant context such as:

- ticket, spec, audit, research, plan, or knowledge IDs
- source paths, record paths, or artifact paths
- command run, working directory, and meaningful arguments
- test, scan, reproduction, or inspection procedure
- environment details when they affect interpretation
- timestamp or source state when freshness matters

Do not over-document routine checks. Match detail to claim risk.

## Claim-Linked Evidence

When evidence supports or challenges a ticket, spec, plan, audit, research, or
other stable claim, name the claim ID.

Claim-linked evidence should include enough source state and procedure detail for
a future agent to judge whether the observation is still useful.

Good claim-linked evidence answers:

- What claim was checked?
- What source or record state was observed?
- What procedure, command, inspection, or artifact produced the observation?
- What was actually seen?
- Which part of the claim is supported, challenged, or partially supported?
- What remains untested or uncertain?

Use stable IDs such as ticket acceptance IDs when they exist:

```text
ticket:YYYYMMDD-<slug>#ACC-001
```

## Standalone Evidence

Standalone evidence is allowed when an observation is worth preserving but is not
yet tied to a stable claim ID.

In that case, make the observation useful on its own. Describe what was observed,
how, where, and why the observation may matter.

Use `## Related Records` only when another record or path materially helps
interpretation.

## Dossiers

A dossier composes multiple observations into one validation story.

A good dossier names:

- the validation question
- the observations or artifacts included
- which claims each observation supports or challenges
- mixed results or limitations
- what still requires separate judgment by the consuming ticket, audit, or review

A dossier may link to separate evidence observation records or summarize multiple
observations directly when that is clearer.

## Raw Artifacts

Use `.loom/evidence/artifacts/YYYYMMDD-<slug>/` for bulky or numerous artifacts
such as full logs, traces, screenshots, generated reports, fixtures, or command
captures.

The Markdown record must still stand on its own enough for a future agent to know:

- which artifact path matters
- what key excerpt or summary matters
- what the artifacts show
- what they do not show
- whether anything was omitted or redacted

Prefer concise excerpts and artifact pointers over dumping raw logs into the
Markdown record.
