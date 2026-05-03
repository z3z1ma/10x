---
name: loom-evidence
description: "Maintain observed artifacts and outputs without turning evidence into project-truth ownership. Use when validation output, reproduction steps, test results, screenshots, logs, scan results, red/green output, or other observations need durable preservation with claim-level support or challenge links."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  skill_kind: owner-layer
  owns_layer: evidence
---

# loom-evidence

Evidence owns observed artifacts.

It records what was observed, how it was observed, what claims the observation
supports or challenges, and what the evidence does not establish.
The ticket, spec, critique, wiki, research, or constitution layer still owns the
truth decision that consumes the evidence.

## What This Skill Owns

- evidence records
- reproduction, red/green, validation, scan, screenshot, log, and observation artifacts
- procedure, artifact, environment, validity, and limitation sections
- claim support and challenge links
- provenance for external artifacts
- observed-at, source-state, procedure verdict, freshness, invalidation, and
  supersession notes for observed artifacts

Evidence does not own intended behavior, live execution state, review verdicts,
accepted explanation, or durable policy.

## Use This Skill When

- validation output should be preserved beyond the current transcript
- a reproduction, failing check, green check, scan result, screenshot, or log
  supports or challenges a claim
- ticket acceptance needs durable evidence rather than a summary assertion
- critique needs inspectable evidence to evaluate a claim
- a wiki or research conclusion needs sources that future agents can recheck

## Do Not Use This Skill When

- the fact is intended behavior; use `loom-specs`
- the fact is live execution state, acceptance disposition, or closure; use `loom-tickets`
- the fact is an adversarial finding or verdict; use `loom-critique`
- the fact is accepted explanation; use `loom-wiki`
- the fact is only support recall; use `loom-memory`

## Evidence Posture

Good evidence is:

- observed, not inferred
- specific about procedure and environment
- freshness-aware about the source, record, dependency, and environment state it
  was gathered from
- explicit about what it supports and what it does not establish
- explicit when it challenges a claim or when limitations make support weak
- linked to tickets, specs, packets, critiques, or wiki pages when useful
- recheckable enough that a future agent can judge its current value

## Default Procedure

1. identify the claim, acceptance ID, ticket, packet, or critique question the
   evidence bears on
2. record when it was observed, the source state observed, and the exact
   procedure or source of observation
3. record artifacts, outputs, screenshots, logs, commands, files, or observations
4. record the observed procedure verdict and exit code when applicable
5. list supported claims and challenged claims separately
6. state environment, freshness, validity, recheck trigger, invalidation or
   supersession conditions, and limitations
7. link the evidence back into the ticket or other owner record that needs it

## Done Means

- the evidence record says what was observed and how
- observed-at, source-state, and procedure verdict details are explicit enough
  to judge whether copied evidence is still current
- support and challenge links are explicit when claims are involved
- freshness, invalidation, and supersession notes make the record's current value
  inspectable
- limitations prevent overclaiming
- the owning ticket, critique, research, spec, or wiki page can cite the evidence
  without treating evidence as the owner of project truth

## Read In This Order

Read immediately for evidence work:

1. `templates/evidence.md` when creating an evidence record.
2. `references/evidence-quality.md` when deciding how strong, fresh, limited, or
   reusable the evidence needs to be.
3. `skills/loom-records/references/claim-coverage.md` when evidence supports or
   challenges spec acceptance IDs, ticket claims, or critique findings.

Then read conditionally:

4. `skills/loom-records/references/implementation-reality.md` when code, tests,
   specs, and observed outputs need their truth boundaries separated.
5. `skills/loom-records/references/query-and-linking.md` when linking evidence
   back to tickets, specs, critiques, packets, or wiki pages.
