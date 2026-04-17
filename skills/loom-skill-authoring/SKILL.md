---
name: loom-skill-authoring
description: "Create or refine Loom-compatible skills that are scoped, durable, discoverable, and template-backed. Use when adding a new subsystem skill, tightening a skill description, extending references/templates, or auditing a skill for overlap, ambiguity, or anti-patterns."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  loom_layer: authoring
  protocol_version: "2.0"
---

# loom-skill-authoring

Use this skill to author skills in the same style this package uses.

## What Good Loom Skills Do

A good Loom skill:

- has a clear activation description
- owns one subsystem or one coherent capability
- tells the agent what it governs and what it does not
- teaches a practical procedure
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

## Read In This Order

1. `references/principles.md`
2. `references/structure.md`
3. `references/anti-patterns.md`
4. the template you need
