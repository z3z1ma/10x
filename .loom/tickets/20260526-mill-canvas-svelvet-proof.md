# Svelvet Svelte 5 Compatibility Proof

ID: ticket:20260526-mill-canvas-svelvet-proof
Type: Ticket
Status: open
Created: 2026-05-26
Updated: 2026-05-26
Risk: high - Svelvet declares peer dep svelte >=3.59.2 || ^4.0.0; our frontend uses Svelte 5. If incompatible, entire canvas plan pivots.

Priority: high - blocks all other canvas tickets

## Summary

Install Svelvet and prove it works with Svelte 5. The published package declares
peer deps for Svelte 3/4 only. Svelte 5 has backward compatibility with Svelte 4
component patterns, so it may work despite the peer dep warning. We need concrete
proof before investing in the rest of the canvas implementation.

Single closure claim: Svelvet renders a custom Svelte 5 component node on an
interactive (zoom/pan/drag) canvas without errors.

## Related Records

- `spec:mill-shaping-canvas` — governs the canvas UX; Svelvet is the chosen
  rendering technology per resolved decisions
- `plan:20260526-mill-shaping-canvas` — parent plan; this is Unit 1 (risk-first)
- `loom-mill/frontend/package.json` — target for the dependency addition
- `loom-mill/frontend/src/lib/design/GraphView.svelte` — existing SVG graph
  implementation; fallback patterns if Svelvet fails

## Scope

**What changes:**
- `loom-mill/frontend/package.json`: add `svelvet` dependency
- Create `loom-mill/frontend/src/lib/design/SvelvetProof.svelte`: minimal test
  component that renders a Svelvet canvas with one custom node
- Optionally create a test route or modify an existing page to mount the proof

**What must NOT change:**
- Existing ShapingTimeline, ShapingBlock, or other components
- Backend code
- Any production functionality

**Likely read scope:** Svelvet docs/source for Svelte 5 compatibility, our
existing Svelte 5 component patterns, GraphView.svelte for fallback reference.

**Likely write scope:** package.json, one new proof component, possibly
vite.config or svelte.config if Svelvet needs special config.

**Stop conditions:**
- If Svelvet installs but throws runtime errors on mount → document the error,
  check if there's a Svelte 5 fork or canary version
- If Svelvet renders but custom component nodes don't work → document which
  features work and which don't
- If Svelvet is fundamentally incompatible → stop, document findings, update the
  plan to pivot to custom SVG canvas

**Evidence posture:** Playwright screenshot of the rendered canvas + console log
showing no errors.

**Review posture:** Generalist verifies the proof is honest (not a partial render
that would fail under real usage).

## Acceptance

- ACC-001: Svelvet package installs without blocking errors (peer dep warnings are
  acceptable; hard install failures are not)
  - Evidence: `npm install` output showing success; `npm ls svelvet` showing
    installed version
  - Audit: Verify no patching, no fork, no version pinning tricks that hide
    incompatibility

- ACC-002: A Svelvet canvas mounts and renders at least one custom Svelte 5
  component node (using runes/`$state`/`$props` syntax, not legacy Svelte 4 syntax)
  - Evidence: Playwright screenshot showing the rendered canvas with a visible
    custom node containing reactive content
  - Audit: Verify the component uses Svelte 5 idioms, not Svelte 4 compatibility
    mode

- ACC-003: Zoom, pan, and node drag work without errors
  - Evidence: Playwright interaction test: zoom in → zoom out → pan → drag node →
    verify no console errors
  - Audit: Check browser console for warnings/errors during interaction

- ACC-004: Multiple nodes with edges render correctly
  - Evidence: Render 3+ nodes connected by edges; Playwright screenshot showing
    correct layout
  - Audit: Verify edges connect to correct nodes, no visual artifacts

## Current State

Ready to start. First Ralph run: install Svelvet, create proof component, run
Playwright verification.

## Journal

- 2026-05-26: Created ticket with Status `open`. Risk-first gate for canvas plan.
  If this fails, plan pivots to custom SVG before other tickets proceed.
