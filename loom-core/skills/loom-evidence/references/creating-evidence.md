# Creating Evidence

Evidence can be created during shaping, execution, audit, research, or standalone
observation. The invariant is observation before inference.

## Choose Shape

Use an Evidence Observation for one command result, test run, screenshot,
reproduction attempt, manual inspection, scan, log excerpt, artifact capture, or
external artifact snapshot.

Use an Evidence Dossier when multiple observations compose one validation story,
such as final ticket acceptance evidence, migration validation, audit-support
evidence, or a linked chain of evidence records summarized for one review question.
A dossier is not a live progress log.

## Creation Procedure

1. Decide why the observation should remain available.
2. Choose Observation or Dossier.
3. Record source or record state.
4. Record the procedure that produced the observation.
5. Record what was observed before interpretation.
6. Capture artifact paths, key excerpts, or summaries.
7. Cite stable claim IDs when supporting or challenging a claim.
8. Record unclear expected results or claim limits.
9. Record what the evidence does not show.
10. Link related records only when useful.

Match detail to claim risk. Include ticket/spec/audit IDs, paths, commands,
working directory, test or inspection procedure, environment details, and timestamp
only when they affect interpretation.

## Claim-Linked Evidence

Claim-linked evidence names the stable claim, source state, procedure, actual
observation, support or challenge boundary, and what remains untested. Use IDs such
as `ticket:YYYYMMDD-<slug>#ACC-001`.

Standalone evidence is allowed when useful without a stable claim ID. Make it
legible on its own; do not pretend it supports a claim.

## Raw Artifacts

Use `.loom/evidence/artifacts/YYYYMMDD-<slug>/` for bulky logs, screenshots,
reports, fixtures, or command captures. The Markdown record must still stand on its
own with artifact pointers, key excerpts or summaries, what the artifacts show,
what they do not show, and what was omitted or redacted.
