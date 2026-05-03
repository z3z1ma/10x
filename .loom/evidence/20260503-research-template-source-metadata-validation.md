---
id: evidence:research-template-source-metadata-validation
kind: evidence
status: recorded
created_at: 2026-05-03T07:25:10Z
updated_at: 2026-05-03T07:28:48Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:rsrcmt18
  packet:
    - packet:ralph-ticket-rsrcmt18-20260503T072340Z
  critique:
    - critique:research-template-source-metadata-review
external_refs: {}
---

# Summary

Validation observations for `ticket:rsrcmt18`, checking that the research template
now prompts for reusable source metadata while preserving research as evidence
synthesis rather than external-source authority.

# Procedure

- Inspected the scoped diff for `ticket:rsrcmt18`.
- Searched the research template for source metadata fields.
- Searched source-handling guidance for alignment wording covering type,
  observed time, version/date/commit, freshness risk, recheck trigger, and trust
  rationale.
- Searched the template and source-handling reference for research/external-source
  authority boundary wording.
- Searched the template and source-handling reference for forbidden additions:
  source-fetching automation, external-source validators, rigid citation schema,
  canonical external-source authority, or required full raw source dumps.
- Ran `git add -N .loom/packets/ralph/20260503T072340Z-ticket-rsrcmt18-iter-01.md .loom/evidence/20260503-research-template-source-metadata-validation.md`.
- Ran `git diff --check -- .loom/tickets/20260503-rsrcmt18-add-research-source-metadata-fields.md .loom/packets/ralph/20260503T072340Z-ticket-rsrcmt18-iter-01.md .loom/evidence/20260503-research-template-source-metadata-validation.md .loom/critique/research-template-source-metadata-review.md skills/loom-research/templates/research.md skills/loom-research/references/source-handling.md`.

# Artifacts

Scoped changed tracked files:

- `.loom/tickets/20260503-rsrcmt18-add-research-source-metadata-fields.md`
- `skills/loom-research/templates/research.md`
- `skills/loom-research/references/source-handling.md`

Scoped new Loom record files:

- `.loom/packets/ralph/20260503T072340Z-ticket-rsrcmt18-iter-01.md`
- `.loom/evidence/20260503-research-template-source-metadata-validation.md`
- `.loom/critique/research-template-source-metadata-review.md`

Targeted observations:

- `skills/loom-research/templates/research.md:41-48` prompts for source title or
  description, type, URL or path, observed time, version/date/commit, freshness
  risk, recheck trigger, and trust rationale.
- `skills/loom-research/references/source-handling.md:37-48` aligns with those
  fields through source title/description, source type, provenance, URL/local
  path, observed time/access date, version/publication date/repository ref/commit,
  freshness risk, recheck/invalidation trigger, and trust rationale/source-quality
  note.
- `skills/loom-research/templates/research.md:50-52` and
  `skills/loom-research/references/source-handling.md:12-17` preserve the boundary
  that sources support research synthesis and do not become instruction authority
  or canonical project truth merely because research cites them.
- Search for `source-fetching automation|external-source validators|rigid citation schema|canonical external-source authority|required full raw source dumps`
  returned no matches in the edited template and source-handling reference.
- `git diff --check` result: passed with no output.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-019`
- `ticket:rsrcmt18#ACC-001`
- `ticket:rsrcmt18#ACC-002`
- `ticket:rsrcmt18#ACC-003`
- `ticket:rsrcmt18#ACC-004`

# Challenges Claims

None - the observations did not weaken the scoped claims.

# Environment

Commit: `bbe01ec0f5e74a95d07076a394f1ece19c13aa41` plus uncommitted scoped
`ticket:rsrcmt18` changes.
Branch: `main`
Runtime: Markdown/static repository; no app runtime.
OS: macOS/Darwin
Relevant config: no generated files, lockfiles, raw source dump requirement,
source-fetching automation, external-source validator, rigid citation schema, or
external-source truth authority observed in the scoped diff.

# Validity

Valid for: the scoped `ticket:rsrcmt18` diff at 2026-05-03T07:28:48Z.
Recheck when: any scoped file changes before closure or before the commit is
created.

# Limitations

This evidence is structural and textual. It confirms prompts and owner-boundary
wording, not whether future research records will fill the metadata well.

# Result

The research template now includes copyable source metadata prompts, and the
source-handling reference is aligned with the same fields. Research remains the
evidence-synthesis layer, not external-source authority. The scoped diff passes
`git diff --check`.

# Interpretation

The evidence supports the ticket's source-metadata claims. It does not close the
ticket; mandatory critique and the ticket-owned acceptance decision remain
separate gates.

# Related Records

- `ticket:rsrcmt18`
- `packet:ralph-ticket-rsrcmt18-20260503T072340Z`
