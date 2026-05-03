# Evidence Quality

Evidence quality is the discipline that keeps observed artifacts useful for
acceptance and critique without making evidence own acceptance, critique
verdicts, intended behavior, or closure.

Good evidence answers four questions:

1. what was observed
2. how, when, where, and from which source state it was observed
3. which claims the observation supports or challenges
4. what the observation does not establish

## Observed Artifacts Before Inference

Record the observation first: command output, file diff, screenshot, log excerpt,
manual inspection result, reproduction step, test result, or external artifact.

Then record the limited interpretation that follows from that observation.
Inference is allowed only when it is labeled as interpretation and bounded by the
artifact actually observed.

Avoid writing evidence as if it directly decides project truth. Evidence may say
"this output supports `ticket:abc123#ACC-001`" or "this observation challenges
`spec:example#ACC-002`". It must not say "therefore the ticket is accepted",
"therefore critique passes", or "therefore intended behavior is changed".

## Expected Versus Actual Results

When a claim, procedure, test, reproduction, or manual check has an expected
outcome, record both sides:

- **expected result** — the behavior, output, state, or artifact the owning
  ticket, spec, packet, or procedure expected to observe
- **actual observed result** — what the command, inspection, screenshot, log,
  reproduction, or external artifact actually showed

Keep the actual result close to the artifact. If the expected result came from a
spec, ticket, packet, or command documentation, cite that owner instead of
restating it as evidence-owned intended behavior.

If the actual result differs from the expected result, record the difference as a
challenge or limitation. Do not smooth the mismatch into a passing summary.

## Freshness

Freshness is evidence's relationship to the current source, records,
dependencies, environment, and procedure.

An evidence record should make freshness inspectable by naming:

- the observed-at timestamp, commit, branch, relevant files or record versions,
  procedure, procedure verdict or exit code when applicable, and environment observed
- whether the observation is fresh enough for the claim it supports or challenges
- what would require rechecking the observation
- whether newer evidence supersedes it or invalidates part of it

`fresh enough` is proportional to the claim. A link-only cleanup may need only a
current structural search. A protocol-authority, security, data, migration, or
user-facing behavior change usually needs stronger current evidence and critique.

## Limitations

Limitations prevent overclaiming.

Every non-trivial evidence record should state what was not checked, what the
procedure cannot prove, and which adjacent claims remain unsupported. A useful
limitation is specific enough that a ticket or critique reviewer can decide
whether more evidence is required.

Examples:

- "This search shows the term appears in the edited guidance; it does not prove
  operators will follow it correctly."
- "This green test output covers the named scenario only; it does not cover the
  migration path."
- "This screenshot confirms the local UI state; it does not establish production
  behavior."
- "This manual inspection partially supports `ticket:abc123#ACC-001`; it did not
  check the untested retry path named by `spec:example#ACC-003`."

## Support And Challenge Strength

Use support and challenge links precisely:

- `Supports Claims` lists claim IDs the observation makes more credible.
- `Challenges Claims` lists claim IDs the observation weakens, falsifies, or
  leaves unexpectedly unsupported.
- Partial support should say which part of a claim was observed and which part
  remains untested or limited.
- Mixed evidence should list both sides instead of smoothing conflict away.

Common shapes:

- **supports** — the actual observed result matches the expected result for the
  cited claim within the stated source state, environment, and limitations
- **challenges** — the actual observed result conflicts with the expected result
  or exposes an unsupported assumption in the cited claim
- **partial support** — the observation covers only part of the claim, only one
  environment, only one scenario, or only a weaker proxy for the claim
- **untested limitation** — the observation says nothing reliable about an
  adjacent path, environment, scenario, or acceptance unit

Concrete challenging-evidence example:

```md
# Supports Claims

None - the observed command failed.

# Challenges Claims

- ticket:abc12345#ACC-002 — `git diff --check` returned exit code 1 at
  commit `abc1234`, so the observation challenges the claim that the edited
  Markdown passed structural whitespace validation.

# Limitations

- This does not test whether the edited guidance is complete or whether critique
  will accept the implementation shape.
```

This example records a challenge to a claim. It does not decide ticket
acceptance, critique verdict, intended behavior, or closure.

Evidence strength depends on the change class and risk class. Manual inspection
may be sufficient for small record hygiene. Behavioral, protocol-authority,
security-sensitive, or data-sensitive changes usually need direct observations,
fresh structural checks, relevant tests when available, and critique when policy
requires it.

## Invalidation And Supersession

Evidence ages deliberately.

Use invalidation when an observation should no longer be relied on for a claim.
Use supersession when newer evidence replaces older evidence for the same claim.

Common recheck triggers include:

- source files or records cited by the evidence changed
- dependencies, environment, or harness behavior changed
- a critique finding challenged the observation or interpretation
- the ticket, spec, or acceptance scope changed
- newer evidence records the same procedure from a later source state

When superseding or invalidating evidence, update the newer or owning record so a
future agent can follow the chain. The ticket still owns whether evidence is
sufficient for acceptance.

## Acceptance Boundary

Evidence feeds the ticket-owned acceptance dossier.

The ticket decides whether evidence is sufficient, fresh enough, and paired with
required critique and retrospective / promotion disposition. Evidence records
should provide observed support, observed challenges, freshness notes, and
limitations so the ticket can fail closed honestly.

Do not make evidence records close tickets, accept risks, withdraw findings,
define intended behavior, or replace critique verdicts.

Evidence can strengthen or weaken the dossier, including with partial support or
untested limitations. It cannot convert that dossier into acceptance by itself.
