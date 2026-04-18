# AGENTS.md

## What This Repo Is

This repository develops a distributable Markdown-first Loom bundle.

The protocol core is the top-level `rules/` and `skills/` directories.
Top-level `commands/` files may exist as optional harness-wrapper prompt
surfaces, but they are not part of Loom core and the protocol must make sense
without them.

There is no app runtime, build pipeline, or test suite. The durable asset is
the protocol corpus itself: rules, skills, templates, references, and canonical
examples.

## Agent Boundary

The agent is the primary operator in a Loom workspace.

This core package ships no Python helper scripts. Record creation, packet
authoring, validation, and graph inspection are taught as visible protocol
behaviors using Markdown guidance, templates, and ordinary file tools.

Ad hoc local automation is acceptable when it is clearly helpful, but it stays
derivative. It must not become the real source of Loom behavior or a hidden
second ontology.

## Repo Structure

### Product source

Everything a user receives lives here:

- `rules/` -- always-on doctrine files
- `skills/` -- self-contained skill directories with `SKILL.md`, references,
  and templates
- `commands/` -- optional harness-wrapper prompt files when this repository
  wants to ship them

**Isolation rule**: content inside `rules/`, `skills/`, and any optional
`commands/` files must stay self-contained, use generic `.loom/...` runtime
paths, and avoid source-repo-only assumptions.

### Dogfooding artifacts

This repo uses its own product. `.opencode/` is a consumption surface for the
bundle. `.loom/` contains Loom records created while using the product on this
repo.

Neither `.opencode/` nor `.loom/` is the source of truth for how the product is
designed. Use `rules/`, `skills/`, and optional top-level wrapper prompts for
that.

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
- optional command-wrapper files are pure Markdown prompt definitions, not code

## Editing Guidance

- prefer the smallest correct change
- keep `rules/`, `skills/`, and optional `commands/` aligned when a change
  crosses their boundaries
- when changing a rule or skill, check related templates, references, and any
  canonical `.loom/` examples that teach the same concept
- do not add hidden runtimes, helper-dependent instructions, or monolithic CLI
  assumptions

### Cross-surface review checklist

If a change touches multiple surfaces, verify:

- `rules/` doctrine wording
- `skills/*/SKILL.md` instructions
- `skills/*/references/` docs
- `skills/*/templates/` artifacts
- optional `commands/` wrappers when they cover the same workflow
- canonical `.loom/` examples when they are meant to teach the product

## Key Architecture Facts

- rules are always on
- skills own behavior through `SKILL.md`, references, and templates rather than
  shipped scripts
- tickets are the sole live execution ledger
- packets are bounded execution contracts
- wiki is the persistent explanation layer
- evidence stores proof artifacts without becoming project-truth ownership
- optional wrapper commands remain convenience surfaces, not protocol core
