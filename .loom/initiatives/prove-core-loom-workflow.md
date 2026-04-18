---
id: initiative:prove-core-loom-workflow
kind: initiative
status: active
created_at: 2026-04-04T23:57:48Z
updated_at: 2026-04-17T23:58:42Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  plan:
    - plan:bootstrap-core-workflow-backlog
  spec:
    - spec:minimum-proven-core-workflow-surface
  ticket:
    - ticket:1ypcbj0m
    - ticket:zomng8h3
    - ticket:vyypge85
---

# Objective

Establish a proven, package-local Loom maintainer path from canonical record
framing through one fresh-context proof run, plus the live-record and wrapper
reconciliation that should follow from that proof.

# Why Now

The repository now has strong doctrine, skill playbooks, templates, and a
clearer constitutional frame, but parts of the dogfooded execution graph and
repo instruction surfaces still mix the old script-era model with the current
template-first rewrite.

The next highest-value work is therefore to prove the main protocol path and
reconcile the active workflow surfaces to that rewrite instead of adding more
disconnected surfaces.

# In Scope

- maintain one explicit initiative/spec/plan/ticket chain for the repository's
  next workflow slice
- execute one real root-repository Ralph -> critique -> wiki proof flow on a
  small shipped change
- reconcile the active workflow chain and repo instruction surfaces to YAML
  frontmatter and `wiki`/`packets`/`evidence` vocabulary
- decide whether a small optional harness-wrapper command surface is still worth
  keeping after the proof slice
- tighten validation and query guidance where the exercised path exposes
  rule-backed gaps

# Out of Scope

- a monolithic `loom` CLI or long-running orchestration service
- making command wrappers part of the protocol core
- speculative multi-repository automation beyond fail-closed scope rules
- hidden runtime behavior outside the visible Markdown bundle
- validation rules that invent policy not already visible in doctrine

# Success Metrics

- a future agent can read the initiative, spec, plan, and three tickets and
  understand the intended sequence without transcript context
- one bounded proof slice lands through execution, critique, wiki/evidence
  follow-through, and ticket reconciliation
- the core operator path is understandable from rules, skills, templates, and
  canonical records without depending on wrapper commands or helper scripts
- any retained wrapper command surface is clearly optional and consistent with
  the owning skills
- validation and query guidance catch the main structural failures surfaced by
  the proof slice

# Milestones

1. Keep the durable record chain truthful and current for the next workflow
   slice.
2. Prove one end-to-end Ralph -> critique -> wiki path on a small repo-local
   target.
3. Reconcile the active repo instruction surfaces and optional wrapper posture
   to the proved path.
4. Harden validation and query guidance around the exercised path.

# Dependencies

- current doctrine and `constitution:main` remain the governing source of truth
- the existing workspace, Ralph, critique, wiki, records, plans, specs, and
  tickets skills remain package-local and self-contained
- optional wrappers stay secondary to the owning rules and skills

# Risks

- overdesigning wrapper surfaces before one small workflow slice is proven
- reconciling prose without enough execution evidence from a real proof run
- tightening validation or query guidance faster than the written doctrine can
  support
- choosing a proof target that is too large to run cleanly in one bounded fresh
  context

# Linked Specs, Plans, and Tickets

- Spec: `spec:minimum-proven-core-workflow-surface`
- Plan: `plan:bootstrap-core-workflow-backlog`
- Ticket: `ticket:1ypcbj0m` - prove one end-to-end flow
- Ticket: `ticket:zomng8h3` - evaluate optional wrapper commands
- Ticket: `ticket:vyypge85` - harden structural validation and query guidance

# Status Summary

This initiative owns the next three increments for the repository's workflow
maturation. `ticket:1ypcbj0m` remains the first ready execution slice.
`ticket:zomng8h3` is now an optional-wrapper follow-up that should remain
secondary to the core protocol surfaces. `ticket:vyypge85` is the follow-up
hardening slice for validation and query guidance once the proof run exposes
what actually needs tightening.
