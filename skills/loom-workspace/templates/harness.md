---
id: workspace:harness
kind: workspace-support
status: active
created_at: <UTC timestamp>
updated_at: <UTC timestamp>
scope:
  kind: workspace
links: {}
---

# Loom Harness Profiles

Use this file to document how fresh-context packet work should be launched in this repository.

The protocol does not require one transport.
It only requires a fresh worker and a faithful packet handoff.

This is a workspace support record. `kind: workspace-support` and
`id: workspace:harness` are support-local grammar for documenting harness
transport mechanics; they do not create a canonical owner layer. The `status`
field is support-local lifecycle only (`active`, `superseded`, or `retired`) and
does not own objective state, live ticket state, acceptance, evidence
sufficiency, critique verdicts, wiki truth, canonical truth, or packet lifecycle.

## Profile: default

- mode: `subagent | headless-cli | manual`
- use_when: default packet execution path
- packet_argument_style: how the packet file is attached or referenced
- prompt_template: the short instruction wrapped around the packet
- notes: any constraints, limits, or quirks

### Example shape

```md
## Profile: default

- mode: headless-cli
- use_when: normal Ralph, critique, and wiki packet work
- command_template: `my-harness run --file "{{ packet_path }}" --prompt "{{ prompt }}"`
- notes: prefer fresh workers; do not reuse saturated sessions for packet-consuming work
```

## Profile: critique

Use when critique packets need a different model, different safety posture, or different temperature.

## Profile: wiki

Use when wiki compilation benefits from a more synthesis-oriented worker.

## Guidance

- keep this file short
- document only patterns the operator actually wants reused
- do not turn it into a shell script
- the packet remains the contract; this file only documents the transport
- update canonical owner records first if harness notes ever disagree with Loom
  tickets, packets, evidence, critique, or wiki pages
