# Evidence Quality

Good evidence makes overclaiming harder. It records what was observed, how, what
stable claim it supports or challenges when applicable, and what it does not show.

## Observation Before Inference

Write the observation first: command output, test result, diff or structural scan,
screenshot, log excerpt, reproduction result, manual inspection, or artifact.

Then write only the bounded support or challenge justified by that observation.
Evidence may support or challenge a claim; it does not accept a ticket, pass audit,
decide behavior, or set policy.

## Claim Scope

Evidence is claim-scoped. A passing unit test supports the covered behavior. A
manual reproduction supports that reproduction. A clean typecheck supports type
correctness. A screenshot supports what is visible. Name the boundary.

Use stable IDs in `## What This Shows`. Say whether each claim is supported,
challenged, or partially supported and which observation produced that judgment. If
no stable claim exists, omit claim language or call it standalone.

## Limits And Freshness

`## What This Does Not Show` should name missing scenarios, environments,
unverified claims, unclear expected results, and recheck triggers.

Evidence freshness depends on the source, records, environment, dependency state,
and procedure observed. Recheck when cited source or record state changes,
environment or harness behavior changes, acceptance scope changes, newer evidence
exists, or audit challenges the observation.

## Dossiers

A dossier composes multiple observations and keeps mixed results visible. The
consuming ticket, audit, or review decides sufficiency.

## Sensitive Data

Do not put secrets, credentials, tokens, private keys, passwords, sensitive
personal data, or raw customer data in evidence or artifacts. Record the
non-sensitive fact and omit or redact the value.

## Quality Checks

Before relying on evidence, ask: is observation separate from inference; are
artifact paths or excerpts sufficient; are claim links stable; do limits prevent
overclaiming; is source/procedure detail proportional; would a future agent know
when to recheck?
