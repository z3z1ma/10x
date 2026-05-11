# Evidence Quality

Good evidence makes claims harder to overstate.

It records what was observed, how it was observed, which stable claims it supports
or challenges when applicable, and what the observation does not establish.

## Observation Before Inference

Write the observation first:

- command output
- test result
- file diff or structural scan
- screenshot or visual artifact
- log excerpt
- reproduction result
- manual inspection result
- external artifact

Then write only the bounded support or challenge justified by that observation.

Evidence may say an observation supports or challenges a claim. It does not say
the ticket is accepted, audit passes, behavior changed, or policy is decided.

## Claim Scope

Evidence is claim-scoped.

A passing unit test supports the behavior covered by that test. A successful
manual reproduction supports that reproduction. A clean typecheck supports type
correctness. A screenshot supports what is visible in that screenshot.

Good evidence names the boundary of support rather than letting a future agent
infer it.

## What This Shows

Use stable IDs when evidence supports or challenges claims.

Good entries say:

- the claim ID
- what part of the claim was observed
- whether the observation supports, challenges, or partially supports it
- which artifact or procedure produced that support or challenge

If no stable claim ID exists, omit claim language or state that the record is a
standalone observation.

## What This Does Not Show

Limitations are part of evidence quality.

Name what was not checked, what the procedure cannot prove, which environments or
scenarios are absent, and what would require rechecking.

When the expected result or claim scope is unclear, record that limitation rather
than inventing a cleaner conclusion.

## Freshness

Freshness is relationship to the source, records, environment, dependency state,
and procedure observed.

For claim-linked evidence, name enough source state and procedure detail that a
future agent can decide whether the observation still applies.

Common recheck triggers:

- source files or records cited by the evidence changed
- dependencies, environment, or harness behavior changed
- ticket, spec, audit, or acceptance scope changed
- newer evidence observed the same claim from a later source state
- audit challenged the observation or its interpretation

Avoid rerunning successful checks when nothing relevant has changed. Duplicate
output is not fresher evidence.

## Dossiers

An Evidence Dossier composes multiple observations.

The dossier should keep mixed results visible. If one observation supports a claim
and another challenges or limits it, say both.

The consuming ticket, audit, review, or other surface decides sufficiency.

Use dossiers for validation stories, not live progress logs.

## Sensitive Data

Do not place secrets, credentials, tokens, private keys, passwords, sensitive
personal data, or raw customer data into evidence records or artifact stores.

When sensitive material matters, record the non-sensitive fact and omit or redact
the value.

Good examples:

- `credential-dependent behavior reproduced; secret value redacted`
- `API key was present in local environment; value not persisted`
- `customer-specific value omitted from artifact excerpt`
- `raw customer payload excluded; structural property summarized`

## Quality Checks

Before relying on evidence, ask:

- Is the observation clearly separated from inference?
- Is the artifact path or excerpt enough to interpret it?
- Are claim links stable when support or challenge is claimed?
- Does `## What This Does Not Show` prevent overclaiming?
- Is the source or procedure detail strong enough for the claim risk?
- Would a future agent know when to recheck it?
