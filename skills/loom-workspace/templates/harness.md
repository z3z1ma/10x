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
