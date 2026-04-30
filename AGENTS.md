# AGENTS.md

## What This Repo Is

This repository develops a distributable Markdown-native Loom bundle.

The protocol core is the top-level `skills/` directory, especially the mandatory
`skills/loom-bootstrap` entry skill and its ordered references.

There is no app runtime, build pipeline, or test suite. The durable product asset
is the skills corpus itself: skills, bootstrap doctrine references, templates,
and references.

Loom should be treated as a control plane for AI knowledge work: a
source-of-truth type system plus a transaction protocol for bounded
fresh-context mutations. Do not reduce it to "docs for agents" or expand it
into a required runtime.

## Agent Boundary

The agent is the primary operator in a Loom workspace.

This core package ships no Python helper scripts. Record creation, packet
authoring, validation, and graph inspection are taught as visible protocol
behaviors using Markdown guidance, templates, and ordinary file tools.

Ad hoc local automation is acceptable when it is clearly helpful, but it stays
derivative. It must not become the real source of Loom behavior or a hidden
second ontology.

Harnesses, external issue trackers, generated context files, dashboards, and MCPs
may transport or mirror Loom work. They must not own Loom truth unless a future
constitutional record explicitly changes that boundary.

## Repo Structure

### Product surface

The product surface is `skills/` only:

- `skills/loom-bootstrap/` -- mandatory first-use bootstrap doctrine and ordered
  references
- `skills/` -- self-contained skill directories with `SKILL.md`, references,
  and templates

**Isolation rule**: content inside `skills/` must stay self-contained, use generic
`.loom/...` runtime paths, and avoid source-repo-only assumptions.

### Internal Review Fixtures

- `examples/` -- internal golden protocol fixtures and traces used to visualize
  workflow routes and review drift. They are not loaded into normal installed
  agent context, not a product surface, and not a truth owner.
- `optional-utilities/` -- local utility skills excluded from the default
  protocol install.

### Dogfooding artifacts

This repo uses its own product. `.opencode/` is a consumption surface for the
bundle. `.loom/` contains Loom records created while using the product on this
repo.

Neither `.opencode/` nor `.loom/` is the source of truth for how the product is
designed. Use `skills/`, especially `skills/loom-bootstrap`, for that.

## Verification

There is no automated test suite.

Verification is structural and manual. Use the smallest honest checks that fit
the claim being made, such as:

- diff review
- targeted `rg` queries for links, IDs, or status fields
- manual comparison against the owning template or skill reference
- spot-checks of canonical path, scope, and cross-record consistency

## Markdown And Record Guidelines

- Loom records use YAML frontmatter between `---` fences
- required sections, statuses, and naming guidance live in the owning skill's
  templates and references
- `SKILL.md` frontmatter must include `name` and `description`
- this repository does not ship a top-level command-wrapper product surface

## Editing Guidance

- prefer the smallest correct change
- keep bootstrap doctrine and `skills/` aligned when a change crosses their
  boundaries
- when changing bootstrap references or a skill, check related templates and
  references; check `examples/` only for internal fixture consistency
- do not add hidden runtimes, helper-dependent instructions, or monolithic CLI
  assumptions
- express new workflows as routes through existing owner layers before adding
  new artifact kinds
- keep traceability grep-friendly with stable IDs, typed links, explicit
  coverage, evidence, and critique references
- path-local instruction files may point to Loom owner records, but they must
  not define independent project truth

### Cross-surface review checklist

If a change touches multiple surfaces, verify:

- `skills/loom-bootstrap/references/` doctrine wording
- `PROTOCOL.md`, `README.md`, and `ARCHITECTURE.md` when package framing changes
- `skills/*/SKILL.md` instructions
- `skills/*/references/` docs
- `skills/*/templates/` artifacts
- `examples/` fixtures when behavior or workflow routing changes, for internal
  review consistency only
- dogfood `.loom/` records when they are relevant project truth for this repo,
  not as product-surface teaching fixtures

## Key Architecture Facts

- bootstrap doctrine is mandatory before work, either through `loom-bootstrap` or
  an adapter preloading the same ordered references
- the layer model is Loom's source-of-truth type system
- Ralph is Loom's bounded implementation handoff loop
- skills own behavior through `SKILL.md`, references, and templates rather than
  shipped scripts or command wrappers
- tickets are the sole live execution ledger
- packets are bounded execution contracts
- wiki is the persistent explanation layer
- evidence stores observed artifacts without becoming project-truth ownership
- native harness adapters may preload bootstrap references, but `skills/` remains
  the product surface

## Current Product Direction

The next phase is protocol sharpening rather than platform expansion. Prioritize:

- product-surface consistency across README, install docs, architecture notes,
  AGENTS guidance, bootstrap doctrine, skills, and templates
- shared non-ticket status lifecycle grammar in `skills/loom-records/references/status-lifecycle.md`
- claim-level coverage across specs, tickets, packets, evidence, and critique
- packet freshness and context-budget guidance
- named critique risk profiles
- codebase atlas, debug, spike, sketch, execution-wave, external-reference,
  ship, retrospective-prevention, and internal golden-example workflows as routes
  through the existing owner graph

Do not borrow external-system complexity as protocol core. A new workflow is a
good Loom workflow when it makes ownership, evidence, review, and recovery more
regular without creating a second ledger.
