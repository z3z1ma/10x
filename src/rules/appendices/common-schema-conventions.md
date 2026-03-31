# Appendix A — Common Schema Conventions

## Frontmatter Format

Canonical records and packet artifacts in this repository use JSON-compatible frontmatter enclosed by `---` fences.

This keeps records human-readable while allowing deterministic parsing with the Python standard library.

## Required Common Fields

Every canonical record MUST declare:

- `id`
- `kind`
- `schema_version`
- `status`
- `repository_scope`
- `links`
- `created_at`
- `updated_at`

## Repository Scope Shapes

`repository_scope` tells future agents which repository boundary the record owns.

Use one of these shapes:

- single repository:

```json
{"kind": "repository", "repository_id": "repo:root"}
```

- multiple repositories:

```json
{"kind": "multi_repository", "repository_ids": ["repo:repos-admin-ui", "repo:repos-query-service"]}
```

- workspace-wide:

```json
{"kind": "workspace", "workspace_id": "workspace:main"}
```

Use `repository` when one repository clearly owns the work.

Use `multi_repository` when the work intentionally spans a bounded set of repositories inside one workspace.

Use `workspace` only when the work truly spans the whole Loom workspace or the bounded repository set is intentionally the whole workspace.

For practical record-writing:

- constitutions are usually `workspace` scoped, except for deliberately repository-local constitutional records
- initiatives are usually `workspace` or `multi_repository` scoped
- specs, plans, tickets, critique, docs, and verification should usually be `repository` scoped unless the work truly spans multiple repositories
- when a verification record supports linked records from different repositories, its scope should normally be inferred or declared as the merged `multi_repository` scope

All of these records still live in the one workspace `.loom/` tree. Scope tells you who owns the work, not where the Markdown file is stored.

## ID Conventions

- `constitution:main`
- `decision:0001`
- `roadmap:bootstrap-the-markdown-first-protocol-corpus`
- `research:evidence-synthesis`
- `initiative:improve-operator-workflows`
- `spec:packet-governance`
- `plan:execution-rollout`
- `ticket:0001`
- `packet:ticket-0001-2026-03-31T120000Z`

## Timestamp Format

Use UTC ISO-8601 timestamps with `Z` suffix.

## Links Shape

`links` is a mapping from typed relation names to arrays of record refs.

The point of the `links` object is not just cross-reference convenience. It is to make the record graph mechanically interpretable by helpers and by future agents.

`constitution:main` is the exception: it is implicitly linked to the whole workspace and SHOULD keep `links: {}` rather than enumerating downstream records.

## Common Link Keys By Kind

Typical keys include:

- constitution decision and roadmap records: `initiative`, `spec`, `plan`, `decision`, `roadmap`
- research records: `initiative`, `spec`, `plan`, `ticket`
- initiative records: `research`, `spec`, `plan`, `tickets`
- spec records: `constitution`, `initiative`, `plan`, `tickets`, `critique`
- plan records: `constitution`, `initiative`, `spec`, `tickets`
- ticket records: `plan`, `spec`, `initiative`, `research`, `ticket`, `verification`, `critique`, `docs`
- critique records: `spec`, `plan`, `tickets`, `verification`
- docs records: `constitution`, `spec`, `plan`, `tickets`, `verification`
- verification records: `packet`, `ticket`, `spec`, `critique`, `doc`, `plan`

## Per-Kind Extra Fields To Expect

The common required fields are only the baseline.

Common per-kind additions include:

- tickets: execution-mode-adjacent state, verification refs, docs disposition, blocker context
- docs: truth-source and staleness context
- critique: review completeness or finding disposition context
- verification: packet and evidence linkage
- packets: mode, target, scope, source refs, trust boundary, output contract, allowed write refs

These do not all need to be represented as one rigid universal schema yet, but the repository should document them explicitly enough that a future agent does not have to infer them from scattered examples.

## Common Status Sets By Kind

Use these as the normal status vocabularies for the current repository shape.

- constitution: `active`, `revised`, `superseded`
- decision: `active`, `revised`, `superseded`
- roadmap: `active`, `revised`, `superseded`
- research: `active`, `revised`, `superseded`
- initiative: `active`, `revised`, `superseded`
- spec: `active`, `revised`, `superseded`
- plan: `draft`, `active`, `revised`, `retired`
- ticket: `proposed`, `ready`, `active`, `blocked`, `review_required`, `complete_pending_acceptance`, `closed`, `cancelled`
- critique: `active`, `revised`, `superseded`
- doc: `draft`, `accepted`, `stale`, `superseded`
- verification: `recorded`, `superseded`
- packet: `compiled`, `launched`, `superseded`, `accepted`, `stale`, `failed`

## Per-Kind Frontmatter Matrix

These are the most important extra frontmatter expectations beyond the common baseline.

### Ticket records

Expect:

- links to plan/spec/initiative and often verification
- status that reflects current execution truth
- verification linkage strong enough to resume later
- journal/body content that explains execution changes over time

Required in normal use:

- at least one upstream execution-context link such as `plan`, `spec`, or `initiative`
- a status from the ticket status set
- body sections for acceptance, verification, journal, and docs disposition

### Docs records

Expect:

- links to truth sources and verification records
- status that reflects whether the explanation is draft, accepted, stale, or superseded
- body sections that explain audience and accepted system shape clearly

Required in normal use:

- at least one truth-source link such as `spec`, `constitution`, `plan`, or `ticket`
- verification linkage when the doc makes accepted-system claims

### Critique records

Expect:

- links to reviewed targets and any verification or follow-up work
- verdict and residual risk in the body
- findings that can be acted on later without reconstructing the whole review

Required in normal use:

- at least one reviewed-target link
- evidence-reviewed and verdict sections in the body

### Verification records

Expect:

- links to the packet and the canonical artifacts the evidence supports
- command and evidence sections that say what was actually checked
- outcome section that tells a future reader what confidence this verification supports

Required in normal use:

- at least one canonical artifact link or packet link that explains what this evidence supports
- explicit command and evidence sections

### Packet artifacts

Expect:

- mode, target, scope, source refs, trust boundary, output contract
- allowed repositories and worktrees
- allowed write refs for execution packets
- packet body that is usable as a local execution contract

Required in normal use:

- explicit mode, target, scope, and source refs
- explicit trust boundary
- explicit freshness or lineage context
- explicit write boundary for execution packets

## Legal And Suspicious Link Patterns

Link patterns are not all equally safe.

Healthy patterns:

- ticket -> plan/spec/research/verification
- critique -> ticket follow-up or reviewed artifact
- docs -> verification source and accepted truth source
- constitution:main -> no outbound frontmatter links

Suspicious patterns that deserve review:

- docs implicitly claiming ticket closure without the ticket being updated
- plan language or links that look like live execution truth
- run artifacts being referenced as if they outrank canonical records

## Common Illegal Or Weak Patterns

Treat these as quality failures or at least review triggers:

- a ticket with no explicit acceptance criteria
- a docs record that cites no verification source for important claims
- a critique record with a verdict but no evidence-reviewed section
- a verification record that reports success without saying what actually ran
- a packet that grants execution authority without an explicit write boundary
- `constitution:main` declaring outbound frontmatter links

## Normative Per-Kind Reminders

Use these as the current repository's strongest simple rules.

- tickets should not omit verification linkage when durable evidence exists
- docs should not claim accepted system shape without truth-source and verification support
- critique should not report a verdict without evidence-reviewed support
- verification should not exist as opaque success claims without command and evidence detail
- packets should not exist as execution contracts without scope, trust boundary, and output contract clarity

## Structural Validation Scope

The helper layer validates:

- frontmatter presence and parseability
- required fields
- known statuses by kind
- required sections by kind
- duplicate IDs
- link targets where applicable

The helper layer does not grade prose quality.

## Durable Verification Records

Verification artifacts that need to participate in the validated link graph SHOULD be stored as Markdown verification records under `.loom/verification/`.
