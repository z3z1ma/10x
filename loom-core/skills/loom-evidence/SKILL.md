---
name: loom-evidence
description: "Use when observations, validation outputs, reproductions, logs, screenshots, scans, command results, or artifact pointers should remain available for review or closure claims."
---

# loom-evidence

Evidence is Loom's observation surface.

It records what was seen, how it was seen, source or record state, which stable
claims the observation supports or challenges when applicable, and what the
observation does not show.

Evidence gives tickets, audit, research, specs, plans, and knowledge honest facts
to reason from. It does not decide acceptance, intended behavior, policy, audit
verdicts, or closure.

## Use This Skill When

Use this skill when an observation should survive the session: tests, command
results, inspections, reproductions, logs, screenshots, scans, artifact pointers,
validation outputs, or any fact a review or closure claim will depend on.

Small local checks can stay in a ticket journal when durable inspection is not
needed.

## Dispatch

If creating evidence:

- read `references/creating-evidence.md`
- read `references/evidence-quality.md`
- use `templates/observation.md` for one observation
- use `templates/dossier.md` when multiple observations compose one validation
  story
- link related records only when useful

If updating evidence:

- preserve the original observation for single-observation records
- add clarification, limits, freshness, supersession, or related-record notes
- create a new record for a new observation unless a dossier is meant to collect
  that validation story

If finding or summarizing evidence, inspect `.loom/evidence/` and keep observation,
inference, support, challenge, and acceptance distinct.

## Finding Evidence

Evidence records live under `.loom/evidence/`.

Useful searches:

```bash
find .loom/evidence -maxdepth 1 -name '*.md' -print 2>/dev/null | sort
grep -R '^ID: evidence:' .loom/evidence 2>/dev/null || true
grep -R '^Type: Evidence' .loom/evidence 2>/dev/null || true
grep -R '^Observed:' .loom/evidence 2>/dev/null || true
grep -R 'ACC-[0-9][0-9][0-9]' .loom/evidence 2>/dev/null || true
```

Raw artifacts may live under `.loom/evidence/artifacts/YYYYMMDD-<slug>/`, but the
Markdown record must still explain what the artifacts show and do not show.

## IDs And Shapes

Use `evidence:YYYYMMDD-<slug>` and `.loom/evidence/YYYYMMDD-<slug>.md`.

Shapes:

- `Type: Evidence Observation` for one check, artifact, reproduction, or result
- `Type: Evidence Dossier` for multiple observations that compose one validation
  story

Required labels:

```text
ID: evidence:YYYYMMDD-<slug>
Type: Evidence Observation
Status: recorded
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
Observed: YYYY-MM-DD or YYYY-MM-DD HH:MM UTC
```

For dossiers, `Observed:` may be a date range. Use only `Status: recorded`.
Freshness, invalidation, limitations, and supersession belong in prose.

## Evidence Invariants

Every evidence record keeps:

- observation before inference
- procedure and source state clear enough to interpret
- artifacts, paths, excerpts, or summaries sufficient for the claim risk
- stable claim IDs in `## What This Shows` when support or challenge is claimed
- explicit limits in `## What This Does Not Show`
- sensitive values redacted or omitted
- no acceptance, closure, policy, behavior, or audit verdict claimed by evidence
  itself

Standalone evidence is allowed when the observation matters but no stable claim ID
exists. Do not invent weak claim links.

## Done Means

Evidence work is done when the record says what was observed and how, its source
state and limits are clear, any claim support is bounded by stable IDs, freshness or
recheck triggers are visible, and consuming surfaces can cite it without treating
observation as acceptance or policy.
