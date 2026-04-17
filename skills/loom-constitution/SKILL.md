---
name: loom-constitution
description: "Maintain durable project identity, principles, constraints, strategic direction, decision records, and roadmap records. Use when the work changes what the project is, what it values, what it refuses, or what long-lived direction it is committing to beyond current execution."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  loom_layer: constitution
  protocol_version: "2.0"
---

# loom-constitution

Constitution is Loom's highest project-facing owner layer.

Use it when the project needs to remember what it is and how it should judge future work.

## What This Skill Owns

- `constitution:main`
- constitutional decision records
- roadmap records
- durable principles and constraints

## Use This Skill When

- a principle should become durable policy
- an architectural constraint should become explicit
- a major choice should outlive the current ticket or plan
- the project's strategic direction changed materially
- a roadmap theme or milestone sequence deserves durable expression

## Do Not Use This Skill When

- you are tracking live progress
- you are describing one bounded implementation step
- the change belongs to a spec, plan, or ticket instead of durable policy
- you only need accepted explanation rather than policy authority

## Constitutional Posture

Good constitutional writing is:

- durable
- explicit
- constraining
- useful as a judgment frame
- not confused with day-to-day execution

A constitutional record should help a future agent decide, not merely admire the prose.

## Default Procedure

1. decide whether the work belongs in `constitution:main`, a decision record, or a roadmap record
2. copy the right template
3. fill in the policy truth, not just abstract philosophy
4. link downstream work where useful, except for `constitution:main`, which usually stays link-light
5. reconcile any plan/spec/wiki pages that are now out of date because the constitutional frame changed

## Done Means

- the durable principle or direction is explicit
- downstream work can now inherit the judgment
- the record reads as policy, not as a ticket
- a fresh agent would know how this should influence later work

## Read In This Order

1. `references/record-families.md`
2. `references/writing-standard.md`
3. `templates/constitution.md`
4. `templates/decision.md`
5. `templates/roadmap.md`
