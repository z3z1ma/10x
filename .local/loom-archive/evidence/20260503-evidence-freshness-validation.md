---
id: evidence:evidence-freshness-validation
kind: evidence
status: recorded
created_at: 2026-05-03T02:47:50Z
updated_at: 2026-05-03T02:47:50Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:evfresh8
  packet:
    - packet:ralph-ticket-evfresh8-20260503T024435Z
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
  critique:
    - critique:evidence-freshness-review
external_refs: {}
---

# Summary

Observation-first validation for `ticket:evfresh8`: the evidence template now asks
for observed-at/source-state/procedure verdict metadata, and evidence guidance now
contains a concrete challenging-evidence example.

# Procedure

Observed at: 2026-05-03T02:47:50Z
Source state: baseline commit `a5b37b176f4a45159f155d41f7070ba6efcf2736` plus
uncommitted Ralph child diff
Procedure: reviewed the child product diff, ran baseline/current targeted
searches, and ran `git diff --check`
Procedure verdict / exit code: pass; `git diff --check` exited 0 with no output

# Artifacts

Changed files:

- `skills/loom-evidence/templates/evidence.md`
- `skills/loom-evidence/SKILL.md`
- `skills/loom-evidence/references/evidence-quality.md`

Baseline search at `a5b37b1`:

```text
a5b37b1:skills/loom-evidence/SKILL.md:28:Evidence does not own intended behavior, live execution state, review verdicts,
a5b37b1:skills/loom-evidence/SKILL.md:44:- the fact is an adversarial finding or verdict; use `loom-critique`
a5b37b1:skills/loom-evidence/references/evidence-quality.md:5:verdicts, intended behavior, or closure.
a5b37b1:skills/loom-evidence/references/evidence-quality.md:67:- `Challenges Claims` lists claim IDs the observation weakens, falsifies, or
a5b37b1:skills/loom-evidence/references/evidence-quality.md:90:- newer evidence records the same procedure from a later source state
a5b37b1:skills/loom-evidence/references/evidence-quality.md:106:define intended behavior, or replace critique verdicts.
a5b37b1:skills/loom-evidence/templates/evidence.md:18:Do not claim acceptance, closure, critique verdicts, or intended behavior here.
a5b37b1:skills/loom-evidence/templates/evidence.md:37:# Challenges Claims
a5b37b1:skills/loom-evidence/templates/evidence.md:54:Fresh enough for:
a5b37b1:skills/loom-evidence/templates/evidence.md:56:Invalidated by:
```

Current search after implementation:

```text
skills/loom-evidence/SKILL.md:26:- observed-at, source-state, procedure verdict, freshness, invalidation, and
skills/loom-evidence/SKILL.md:66:2. record when it was observed, the source state observed, and the exact
skills/loom-evidence/SKILL.md:69:4. record the observed procedure verdict and exit code when applicable
skills/loom-evidence/SKILL.md:78:- observed-at, source-state, and procedure verdict details are explicit enough
skills/loom-evidence/references/evidence-quality.md:10:2. how, when, where, and from which source state it was observed
skills/loom-evidence/references/evidence-quality.md:36:  procedure, procedure verdict or exit code when applicable, and environment observed
skills/loom-evidence/references/evidence-quality.md:79:# Challenges Claims
skills/loom-evidence/references/evidence-quality.md:81:- ticket:abc12345#ACC-002 — `git diff --check` returned exit code 1 at
skills/loom-evidence/templates/evidence.md:22:Observed at: <UTC timestamp>
skills/loom-evidence/templates/evidence.md:23:Source state: <commit / branch / relevant record versions / external source version>
skills/loom-evidence/templates/evidence.md:25:Procedure verdict / exit code: <observed pass/fail/mixed/inconclusive and exit code when applicable>
skills/loom-evidence/templates/evidence.md:43:# Challenges Claims
skills/loom-evidence/templates/evidence.md:60:Fresh enough for: <claims or review questions; not acceptance or closure>
skills/loom-evidence/templates/evidence.md:62:Invalidated by: <conditions that would make this observation unreliable for the cited claims>
```

Whitespace check:

```text
$ git diff --check
<passed with no output>
```

# Supports Claims

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-010`
- `ticket:evfresh8#ACC-001`
- `ticket:evfresh8#ACC-002`
- `ticket:evfresh8#ACC-003`
- `ticket:evfresh8#ACC-004`

# Challenges Claims

None.

# Environment

Commit: `a5b37b176f4a45159f155d41f7070ba6efcf2736` plus uncommitted Ralph child diff
Branch: `main`
Runtime: none; Markdown protocol corpus only
OS: darwin
Relevant config: no app runtime or automated test suite in this repository

# Validity

Valid for: working tree after Ralph child output for `ticket:evfresh8` and before
oracle critique.
Fresh enough for: structural validation of `ticket:evfresh8#ACC-001` through
`ticket:evfresh8#ACC-004`.
Recheck when: evidence template, evidence skill, evidence-quality guidance, claim
coverage challenge guidance, or ticket acceptance criteria change again.
Invalidated by: newer edits that remove the observed metadata fields, freshness
prompts, challenge example, or evidence owner-boundary wording.
Supersedes / superseded by: None.

# Limitations

This evidence records structural searches, diff review, and whitespace validation
only. It does not establish oracle critique sufficiency, ticket acceptance, or
closure by itself.

# Result

The evidence template now asks for observed-at, source-state, procedure, and
procedure verdict / exit code metadata. The template makes freshness,
invalidation, and recheck triggers explicit. Evidence-quality guidance includes a
concrete failed `git diff --check` challenge example. `git diff --check` passed.

# Interpretation

The structural observations support `ACC-001` through `ACC-004`. `ACC-005`
requires the mandatory oracle critique to pass with no unresolved findings.

# Related Records

- `ticket:evfresh8`
- `packet:ralph-ticket-evfresh8-20260503T024435Z`
- `critique:evidence-freshness-review`
