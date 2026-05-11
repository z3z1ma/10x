---
id: spec:minimum-proven-core-workflow-surface
kind: spec
status: active
created_at: 2026-04-04T23:57:48Z
updated_at: 2026-04-17T23:58:42Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:prove-core-loom-workflow
  plan:
    - plan:bootstrap-core-workflow-backlog
  ticket:
    - ticket:1ypcbj0m
    - ticket:zomng8h3
    - ticket:vyypge85
---

# Summary

Define the minimum proven Loom workflow surface that this repository should
support next: a maintainer can enter cold, follow durable records, execute one
bounded fresh-context slice, reconcile critique/wiki/evidence outcomes, and
understand the operator path without depending on helper scripts or wrapper
commands.

# Problem Framing

The repository now proves that Loom's rules, skills, templates, and canonical
record grammar can ship, but it does not yet prove the main operator path end
to end. Parts of the active `.loom/` graph and repo instruction surfaces still
teach the old script-era model, which weakens Loom's claim that a future agent
can recover the method directly from the visible corpus.

# Desired Behavior

A capable maintainer should be able to start from canonical records, identify
one ready ticket, author the needed bounded packet from the shipped templates,
run one fresh execution slice inside root-repository scope, reconcile critique
and wiki follow-through, and leave the ticket ledger plus supporting artifacts
truthful.

Optional harness-wrapper commands may exist, but the core operator path must be
legible without them.

# Constraints

- no monolithic `loom` CLI
- protocol over hidden runtime or service orchestration
- no required command-wrapper surface for the core package
- scope and write authority must fail closed
- ticket truth must remain in tickets rather than in plans, wiki, packets, or
  evidence
- record creation, packet authoring, validation, and graph inspection should be
  taught in visible Markdown and ordinary file operations
- optional automation or wrappers remain derivative and must not become a shadow
  control plane

# Capabilities

- durable initiative/spec/plan/ticket framing for the next workflow slice
- one bounded Ralph -> critique -> wiki proof path in `repo:root`, driven by
  the agent using templates and standard tools
- truthful packet, critique, wiki, and evidence reconciliation after execution
- optional wrapper command entry points that remain clearly secondary when they
  are useful
- validation and query guidance for scope, packet shape, link integrity, and
  workspace readiness where doctrine already requires them

# Requirements

- maintain one explicit initiative/spec/plan/ticket chain for this workflow
  slice
- keep at least one ticket in `ready` state with enough detail to execute
  without relying on chat history
- the proof flow must declare repository scope, packet mode, source refs, trust
  boundary, output contract, and allowed write set before child execution
- execution outcomes must reconcile into the ticket plus linked critique,
  wiki, and evidence artifacts, or explain explicitly why a linked artifact was
  not created
- any retained wrapper command entry points must remain Markdown prompt
  definitions under top-level `commands/` and must stay obviously optional
- validation and query guidance must catch ambiguous scope, broken canonical
  links, and missing packet structure that doctrine already defines as required

# Scenarios

- a fresh maintainer reads the canonical records and can safely begin
  `ticket:1ypcbj0m`
- a proved workflow change needs wiki follow-through or an explicit
  wiki-not-required decision
- packet or scope information is incomplete and the visible guidance fails
  closed with a clear explanation
- the repository keeps a small wrapper command surface without letting that
  surface become the protocol core

# Acceptance

- the initiative, spec, plan, and three backlog tickets exist and are linked
  coherently
- `ticket:1ypcbj0m` is actionable without transcript archaeology
- later wrapper or validation changes can be judged against this contract
  without redefining what the workflow is supposed to do
- no accepted addition violates package-local isolation, the no-monolithic-CLI
  constraint, or the command-wrapper-as-optional principle

# Design Notes

- prove one small root-repository path before broadening coverage
- treat commands, when they exist, as harness sugar rather than runtime
  orchestrators
- let validation and query guidance follow doctrine rather than anticipating
  future policy
- prefer one real worked path over many speculative surfaces
- reconcile active examples to YAML frontmatter and the current
  `wiki`/`packets`/`evidence` vocabulary as part of proving the path honestly

# Open Questions

- which packet mode should become the default long-term posture for common runs
- when critique should become mandatory by risk class rather than recommendation
- how much packet freshness and acceptance logic should eventually move from
  prose into more standardized checks
- what, if any, optional wrapper command set is worth keeping after the proof
  slice
