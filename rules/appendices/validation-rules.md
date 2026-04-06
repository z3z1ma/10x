# Appendix F — Validation Rules

## Purpose

Validation in this repository exists to keep the visible protocol trustworthy.

Validation is intentionally strict on structure and intentionally soft on prose.

That means validation should answer questions like:

- is the record structurally valid
- do the links resolve
- is the packet contract complete enough to trust
- is the scope explicit enough to avoid guessing
- is the skill bundle complete enough to operate locally

Validation should not answer questions like:

- is this prose elegant
- is this the best possible plan
- is this explanation beautifully written

## Validation Order

When the parent needs confidence in the repository state, run validation in this order:

1. record validation
2. link validation
3. scope validation
4. packet validation if packetized work is involved
5. skill validation if distribution or bundle completeness matters

This order is useful because later validation depends on earlier layers being trustworthy.

The parent usually reaches this point after reading and searching the relevant records directly with native tools. Validation confirms structural trust; it does not replace ordinary corpus reading.

## Record Validation

Record validation checks:

- frontmatter is present and parseable
- required common fields exist
- `kind` is known
- `status` is valid for the given kind
- required sections are present
- timestamps are parseable

Record validation should fail when structure is missing or contradictory.

Record validation should not fail merely because prose is brief, blunt, or stylistically uneven.

## Link Validation

Link validation checks:

- duplicate IDs
- missing target refs
- illegal self-links where prohibited
- `constitution:main` staying link-free
- suspicious plan/docs/ticket authority inversions

Link validation exists to keep the graph interpretable by a future agent.

If an important relationship exists only in prose and not in a typed link field, that should be treated as a quality gap even if the file is otherwise readable.

When validation follows a deletion, rename, or supersession, the parent should search `.loom/` directly for the affected canonical ID, reconcile those references with normal edits, and then rerun validation.

## Scope Validation

Scope validation checks:

- root repository is discoverable
- nested repositories are discoverable and normalized
- owning repository for a path can be determined when applicable
- ambiguous or out-of-scope targets are rejected rather than guessed

Good scope validation should produce one of two outcomes:

- one explicit owner
- one explicit failure

Silently choosing among multiple plausible owners is a validation failure.

## Packet Validation

Packet validation checks:

- required packet fields exist
- source refs are present
- scope fields are present
- trust boundary statements are present
- allowed write set is present when execution mode is true
- packet mode is coherent with the declared output contract

Packet validation matters because packets are the handoff contract for fresh child execution. A packet that is missing scope or output information is not merely incomplete. It is operationally unsafe.

## Skill Validation

Skill validation checks:

- `SKILL.md` is present
- required references are present
- required scripts are present
- documented packet command shapes exist for packet-consuming skills
- local examples exist and are useful enough to orient a fresh reader

Skill validation should prefer self-contained clarity.

If a loaded skill still forces the reader to infer its real workflow from unrelated files, the skill is structurally present but operationally weak.

Skill validation complements native work. It does not replace reading the skill, its references, and the owned records directly.

## Acceptance Use

Validation is not the whole acceptance model, but it is a gate for further trust.

The parent should usually treat validation failures as blockers for:

- packet compilation
- packet launch
- acceptance of a child result
- claims that a skill or record set is ready for reuse
