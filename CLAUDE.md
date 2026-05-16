# Agent Loom Contributor Guidance

## Harness Integration Acceptance Test

A real Loom harness integration loads `using-loom` at session start. The bootstrap
is what causes Loom skills to auto-trigger at the right moments. Without it, the
skills are dead weight: present on disk but not reliably invoked.

Open a clean session in the target harness with Loom Core installed and send
exactly this user message:

> Let's make a react todo list

A working integration loads `using-loom` before any code is written and stays in
Core Loom routing or shaping. If Playbooks are installed too, this natural prompt
must not auto-load `loom-idea-refine` or any other Playbook; Playbooks are optional
explicit workflow macros or explicit-only skills. Paste the complete transcript in
integration review material.

These are not real integrations:

- manually copying skill files into the harness
- anything that requires the user to opt in to Loom per session
- anything where `Let's make a react todo list` proceeds to code before the Loom
  shaping route activates
- anything where a natural prompt auto-loads a Playbook instead of leaving it to
  explicit user invocation

If you are not sure whether the integration loads `using-loom` at session start,
it does not.
