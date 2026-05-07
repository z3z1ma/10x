---
name: loom-skill-authoring
description: "Maintain Loom-compatible skills. Use when adding, tightening, reviewing, or auditing skill boundaries, activation descriptions, common triggers, templates, references, routing, or anti-rationalization guidance."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  skill_kind: authoring
---

# loom-skill-authoring

Use this skill to author Loom-compatible skills.

## Core Dependency

This playbook requires `loom-core`. If `using-loom` and the core owner-layer
skills are not installed or preloaded, stop and load/install `loom-core` instead
of treating this playbook as a substitute for Loom doctrine or record grammar.

## What This Skill Owns

- skill activation descriptions
- skill frontmatter and metadata conventions
- skill boundaries and overlap review
- skill review and pressure-scenario validation
- skill directory structure
- reference/template placement
- anti-pattern review for hidden runtimes or vague ownership

## What Good Loom Skills Do

A good Loom skill:

- has a broad activation description that names ordinary user/task triggers and
  owner boundaries
- uses frontmatter metadata consistently with the skill boundary
- owns one subsystem or one coherent capability
- tells the agent what it governs and what it does not
- teaches a practical procedure
- names common rationalizations when agents are likely to skip the discipline
- names red flags that show the skill is being violated
- ends with evidence-backed verification, not a vibe check
- provides references for nuanced judgment
- provides templates when artifact creation is part of the workflow

## Use This Skill When

- you are adding a new skill
- you are collapsing duplicate skills
- you are tightening a vague skill description
- you are deciding whether a subsystem should exist as its own skill

## Do Not Use This Skill When

- the work really belongs to a canonical project record
- the "new skill" is just a one-off task
- you are trying to hide core rules inside a skill that should really be always-on doctrine

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The skill reads well, so it is done." | Skill edits change future operator behavior; validation must check activation, boundaries, references, templates, and proportional evidence. |
| "This rule can live in the new skill only." | Always-on doctrine belongs in using-Loom; owner truth belongs in owner records. Skills coordinate behavior without hiding core policy. |
| "A broad description means the skill owns all related truth." | Broad activation improves discovery. Durable truth still routes to the owning Loom layer. |

## Red Flags

- activation is too vague for an agent to know when to load the skill
- the skill duplicates another owner or creates a shadow owner layer
- required references are a bare index instead of immediate versus conditional reads
- templates introduce placeholder IDs, vague completion claims, or hidden runtime assumptions
- verification is only the author's confidence that the prose sounds right

## Verification

- [ ] Frontmatter names `name`, `description`, `compatibility`, and appropriate `metadata`.
- [ ] The description names ordinary activation triggers without becoming the workflow shortcut.
- [ ] Ownership boundaries and non-owners are clear enough to prevent overlap.
- [ ] References are immediate or conditional for a stated reason.
- [ ] Templates exist only for artifact shapes the skill owns.
- [ ] Behavior-changing edits have structural checks, pressure scenarios, critique, or evidence proportional to risk.

## Done Means

- the skill has a broad activation description with ordinary triggers, aliases,
  and owner boundaries where relevant
- frontmatter names `name`, `description`, `compatibility`, and appropriate
  `metadata` fields
- the skill states what it owns and what it does not own
- the skill teaches process over reference knowledge
- common rationalizations, red flags, and verification are present when they would
  change agent behavior
- references and templates are placed only where they serve the skill boundary
- the skill does not duplicate another owner or create a hidden runtime

## Read In This Order

Read immediately for skill authoring:

1. `references/principles.md` when deciding whether a skill should exist and
   what it should own.
2. `references/structure.md` when laying out files, references, and templates.

Then read conditionally:

3. `references/anti-patterns.md` when checking overlap, hidden runtime
   dependency, or vague activation.
4. `references/skill-review.md` when a skill changes operator behavior,
   discipline, routing, or protocol authority and needs pressure-testing or
   critique before acceptance.
5. `templates/simple-skill.md` when creating an owner-layer, workflow, support,
   shared-grammar, inner-loop, control-plane, entry-doctrine, or authoring skill with a
   single coherent boundary.
6. `templates/router-skill.md` when creating a workflow coordinator that routes
   among multiple owner layers without owning a new truth layer.
