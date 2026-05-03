---
id: evidence:evidence-anti-theater-validation
kind: evidence
status: recorded
created_at: 2026-05-03T05:27:17Z
updated_at: 2026-05-03T05:27:17Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:evhard05
  packet:
    - packet:ralph-ticket-evhard05-20260503T052442Z
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
external_refs: {}
---

# Summary

Observed evidence anti-theater guidance for `ticket:evhard05` and checked
expected-vs-actual prompts, freshness/source-state/recheck wording,
support/challenge/partial-support/untested-limit wording, evidence authority
boundaries, absence of forbidden runtime or framework machinery, and
`git diff --check`.

# Procedure

Observed at: 2026-05-03T05:27:17Z

Source state: working tree on `main` based on commit
`88fcd76547688a74ec5eb28726eab63c2c494c2a`, after Ralph child output and before
mandatory critique.

Procedure:

- Ran targeted `rg` checks over the evidence skill, evidence-quality reference,
  evidence template, and claim-coverage reference.
- Added the new Ralph packet to the index with intent-to-add and ran
  `git diff --check` so the check covered new packet content and tracked edits.

Procedure verdict / exit code: pass; targeted positive searches returned expected
lines, forbidden machinery search returned no matches, and `git diff --check`
returned no output.

# Artifacts

## Expected Versus Actual Wording

Command:

```bash
rg -n 'expected result|actual observed result|Expected Versus Actual|expected-versus-actual' skills/loom-evidence/SKILL.md skills/loom-evidence/references/evidence-quality.md skills/loom-evidence/templates/evidence.md skills/loom-records/references/claim-coverage.md
```

Output:

```text
skills/loom-evidence/SKILL.md:66:- clear about expected result versus actual observed result when a claim names an
skills/loom-evidence/SKILL.md:81:3. record the expected result when applicable and the actual observed result
skills/loom-evidence/templates/evidence.md:49:If the actual observed result differs from the expected result, cite the claim it
skills/loom-evidence/templates/evidence.md:78:What the evidence actually showed, including expected-versus-actual mismatch when
skills/loom-evidence/references/evidence-quality.md:28:## Expected Versus Actual Results
skills/loom-evidence/references/evidence-quality.md:33:- **expected result** — the behavior, output, state, or artifact the owning
skills/loom-evidence/references/evidence-quality.md:35:- **actual observed result** — what the command, inspection, screenshot, log,
skills/loom-evidence/references/evidence-quality.md:38:Keep the actual result close to the artifact. If the expected result came from a
skills/loom-evidence/references/evidence-quality.md:42:If the actual result differs from the expected result, record the difference as a
skills/loom-evidence/references/evidence-quality.md:95:- **supports** — the actual observed result matches the expected result for the
skills/loom-evidence/references/evidence-quality.md:97:- **challenges** — the actual observed result conflicts with the expected result
skills/loom-records/references/claim-coverage.md:154:- spec:<slug>#ACC-001 — actual observed result matched the expected result for
skills/loom-records/references/claim-coverage.md:161:- spec:<slug>#ACC-002 — actual observed result differed from the expected result
```

## Freshness And Source-State Wording

Command:

```bash
rg -n 'Source state|source state|environment|Freshness|freshness|Recheck when|Invalidated by|invalidation|invalidated' skills/loom-evidence/SKILL.md skills/loom-evidence/references/evidence-quality.md skills/loom-evidence/templates/evidence.md skills/loom-records/references/claim-coverage.md
```

Output:

```text
skills/loom-evidence/SKILL.md:33:- procedure, artifact, environment, validity, and limitation sections
skills/loom-evidence/SKILL.md:37:- observed-at, source-state, procedure verdict, freshness, invalidation, and
skills/loom-evidence/SKILL.md:65:- specific about procedure and environment
skills/loom-evidence/SKILL.md:68:- freshness-aware about the source, record, dependency, and environment state it
skills/loom-evidence/SKILL.md:79:2. record when it was observed, the source state observed, and the exact
skills/loom-evidence/SKILL.md:85:7. state environment, freshness, validity, recheck trigger, invalidation or
skills/loom-evidence/SKILL.md:95:- freshness, invalidation, and supersession notes make the record's current value
skills/loom-evidence/references/evidence-quality.md:10:2. how, when, where, and from which source state it was observed
skills/loom-evidence/references/evidence-quality.md:45:## Freshness
skills/loom-evidence/references/evidence-quality.md:47:Freshness is evidence's relationship to the current source, records,
skills/loom-evidence/references/evidence-quality.md:48:dependencies, environment, and procedure.
skills/loom-evidence/references/evidence-quality.md:50:An evidence record should make freshness inspectable by naming:
skills/loom-evidence/references/evidence-quality.md:53:  procedure, procedure verdict or exit code when applicable, and environment observed
skills/loom-evidence/references/evidence-quality.md:96:  cited claim within the stated source state, environment, and limitations
skills/loom-evidence/references/evidence-quality.md:100:  environment, only one scenario, or only a weaker proxy for the claim
skills/loom-evidence/references/evidence-quality.md:102:  adjacent path, environment, scenario, or acceptance unit
skills/loom-evidence/references/evidence-quality.md:136:Use invalidation when an observation should no longer be relied on for a claim.
skills/loom-evidence/references/evidence-quality.md:142:- dependencies, environment, or harness behavior changed
skills/loom-evidence/references/evidence-quality.md:145:- newer evidence records the same procedure from a later source state
skills/loom-evidence/references/evidence-quality.md:157:should provide observed support, observed challenges, freshness notes, and
skills/loom-evidence/templates/evidence.md:23:Source state: <commit / branch / relevant record versions / external source version>
skills/loom-evidence/templates/evidence.md:29:Include enough context for a future agent to judge freshness without treating this
skills/loom-evidence/templates/evidence.md:65:Valid for: <claims, source state, and environment this observation can speak to>
skills/loom-evidence/templates/evidence.md:67:Recheck when: <source, records, dependencies, environment, procedure, or scope changes>
skills/loom-evidence/templates/evidence.md:68:Invalidated by: <conditions that would make this observation unreliable for the cited claims>
skills/loom-evidence/templates/evidence.md:74:environments, source states, adjacent claims, or critique questions.
skills/loom-records/references/claim-coverage.md:162:  in `<environment>`.
skills/loom-records/references/claim-coverage.md:166:- Untested: `<scenario or environment>` for `spec:<slug>#ACC-003`.
```

## Support, Challenge, Partial Support, And Untested Limits

Command:

```bash
rg -n 'partial support|untested|Supports Claims|Challenges Claims|Limitations|support|challenge' skills/loom-evidence/SKILL.md skills/loom-evidence/references/evidence-quality.md skills/loom-evidence/templates/evidence.md skills/loom-records/references/claim-coverage.md
```

Output:

```text
skills/loom-evidence/SKILL.md:15:supports or challenges, and what the evidence does not establish.
skills/loom-evidence/SKILL.md:70:- explicit about what it supports and what it does not establish
skills/loom-evidence/SKILL.md:71:- explicit when it challenges a claim or when limitations make support weak
skills/loom-evidence/SKILL.md:84:6. list supported claims, challenged claims, and weak or partial support separately
skills/loom-evidence/references/evidence-quality.md:62:## Limitations
skills/loom-evidence/references/evidence-quality.md:79:- "This manual inspection partially supports `ticket:abc123#ACC-001`; it did not
skills/loom-evidence/references/evidence-quality.md:80:  check the untested retry path named by `spec:example#ACC-003`."
skills/loom-evidence/references/evidence-quality.md:84:Use support and challenge links precisely:
skills/loom-evidence/references/evidence-quality.md:89:- Partial support should say which part of a claim was observed and which part
skills/loom-evidence/references/evidence-quality.md:90:  remains untested or limited.
skills/loom-evidence/references/evidence-quality.md:95:- **supports** — the actual observed result matches the expected result for the
skills/loom-evidence/references/evidence-quality.md:97:- **challenges** — the actual observed result conflicts with the expected result
skills/loom-evidence/references/evidence-quality.md:99:- **partial support** — the observation covers only part of the claim, only one
skills/loom-evidence/references/evidence-quality.md:101:- **untested limitation** — the observation says nothing reliable about an
skills/loom-evidence/references/evidence-quality.md:107:# Supports Claims
skills/loom-evidence/references/evidence-quality.md:111:# Challenges Claims
skills/loom-evidence/references/evidence-quality.md:117:# Limitations
skills/loom-evidence/references/evidence-quality.md:163:Evidence can strengthen or weaken the dossier, including with partial support or
skills/loom-evidence/references/evidence-quality.md:164:untested limitations. It cannot convert that dossier into acceptance by itself.
skills/loom-records/references/claim-coverage.md:148:Evidence should name claims it supports and distinguish challenges, partial
skills/loom-records/references/claim-coverage.md:149:support, and untested limits instead of turning an observation into acceptance:
skills/loom-records/references/claim-coverage.md:152:# Supports Claims
skills/loom-records/references/claim-coverage.md:156:- ticket:<token>#ACC-001 — partial support only; the observed structural check
skills/loom-records/references/claim-coverage.md:159:# Challenges Claims
skills/loom-records/references/claim-coverage.md:164:# Limitations
skills/loom-evidence/templates/evidence.md:39:# Supports Claims
skills/loom-evidence/templates/evidence.md:42:For partial support, name the observed portion and the untested or limited portion.
skills/loom-evidence/templates/evidence.md:46:# Challenges Claims
skills/loom-evidence/templates/evidence.md:71:# Limitations
skills/loom-evidence/templates/evidence.md:73:What this evidence does not establish, including untested scenarios,
```

Output omitted unchanged description/search-helper matches that do not affect the
claim.

## Evidence Authority Boundary

Command:

```bash
rg -n 'must not say "therefore the ticket is accepted"|does not own acceptance|Do not make evidence records close tickets|not an acceptance decision|ticket still owns|cannot convert.*acceptance|Evidence links make coverage inspectable' skills/loom-evidence/SKILL.md skills/loom-evidence/references/evidence-quality.md skills/loom-evidence/templates/evidence.md skills/loom-records/references/claim-coverage.md
```

Output:

```text
skills/loom-evidence/templates/evidence.md:79:applicable. This should be an observed result, not an acceptance decision.
skills/loom-evidence/references/evidence-quality.md:25:`spec:example#ACC-002`". It must not say "therefore the ticket is accepted",
skills/loom-evidence/references/evidence-quality.md:148:future agent can follow the chain. The ticket still owns whether evidence is
skills/loom-evidence/references/evidence-quality.md:160:Do not make evidence records close tickets, accept risks, withdraw findings,
skills/loom-evidence/references/evidence-quality.md:164:untested limitations. It cannot convert that dossier into acceptance by itself.
skills/loom-records/references/claim-coverage.md:169:Evidence links make coverage inspectable. The ticket still owns scoped coverage
```

## Forbidden Machinery Search

Command:

```bash
rg -n 'exhaustive|test framework|test-framework|runtime validation|schema|validator|new owner layer' skills/loom-evidence/SKILL.md skills/loom-evidence/references/evidence-quality.md skills/loom-evidence/templates/evidence.md skills/loom-records/references/claim-coverage.md
```

Output:

```text
```

Exit status: pass; no forbidden exhaustive-log/test-framework/runtime/schema/
validator/new-owner-layer wording was found.

## Full Diff Whitespace Check

Command:

```bash
git add -N ".loom/packets/ralph/20260503T052442Z-ticket-evhard05-iter-01.md" && git diff --check
```

Output:

```text
```

Exit status: pass; no whitespace errors were reported.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-006`
- `ticket:evhard05#ACC-001`
- `ticket:evhard05#ACC-002`
- `ticket:evhard05#ACC-003`
- `ticket:evhard05#ACC-004`

# Challenges Claims

None - no challenged claims were observed.

# Environment

Commit: `88fcd76547688a74ec5eb28726eab63c2c494c2a` plus uncommitted
ticket-scoped working-tree changes

Branch: `main`

Runtime: none; Markdown corpus only

OS: macOS / Darwin

Relevant config: no app runtime or automated test suite

# Validity

Valid for: the listed files observed at 2026-05-03T05:27:17Z.

Fresh enough for: mandatory critique and ticket acceptance review for
`ticket:evhard05`.

Recheck when: evidence skill guidance, evidence-quality reference, evidence
template, claim-coverage examples, ticket criteria, or critique findings change
before closure.

Invalidated by: later edits that remove expected-vs-actual prompts, weaken
source-state/freshness/recheck requirements, blur evidence with acceptance or
critique verdict authority, or introduce runtime/schema/validator/test-framework
requirements.

Supersedes / superseded by: None.

# Limitations

This evidence does not prove the guidance is sufficient or that operators will
apply it correctly; mandatory critique and ticket-owned acceptance decide that.

# Result

The observed evidence guidance changes are Markdown-only, make anti-overclaiming
prompts more explicit, and stay within the declared write scope.

# Interpretation

The observations support the ticket's structural claims, pending critique.

# Related Records

- `ticket:evhard05`
- `packet:ralph-ticket-evhard05-20260503T052442Z`
- `initiative:skills-corpus-context-integrity-hardening-pass`
