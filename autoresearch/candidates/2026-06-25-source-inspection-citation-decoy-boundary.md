# Candidate: Source Inspection Citation Decoy Boundary

Candidate ID: `candidate-source-inspection-citation-decoy-boundary-v1`
Created: 2026-06-25
Canonical target: `SKILL.md`
Status: promoted
Promotion: manual-only

## Target Behavior

For read-only source-authority questions, the agent should not open
non-authoritative decoy files merely to produce clickable path links or line
citations. If active records, search results, filenames, or imports already
establish that a file is non-authoritative, cite the path plainly and keep the
inspection focused on the authority path.

## Motivation

EXP-713 showed the source-inspection target-precision promotion improved
canonical current behavior, but current still read three decoy files in full
before line-citing them as non-authority. The no-op arm regressed further and
read broad decoys in full.

The prior promotion correctly says not to read every plausible decoy. The
remaining gap is citation pressure: models may open decoys just to produce
line-linked citations, even when those files cannot change the answer.

## Proposed Instruction Overlay

Add to `## Mechanical Tool Economy`, immediately after the promoted
source-authority decoy paragraph:

```text
Do not open non-authoritative files merely to create clickable links, line
citations, or more polished ignored-source callouts. Plain path citations are
enough for decoys whose non-authority is already established by active records,
search results, filenames, or imports. Spend detailed reads on authority files
and on suspicious files that could reveal drift, contradict records, or change
the answer.
```

## Expected Score Movement

- Source-inspection decoy-pressure operation quality should improve further.
- S003 should hold because record-backed answers remain intact.
- S001/S002 should hold because this is read-only inspection guidance.
- SCN-006 drift handling should hold because suspicious files remain inspectable.

## Scenario Coverage

Primary:

- SCN-003 source-inspection decoy pressure post-promotion replay.

Regressions:

- SCN-006 multi-surface source/record drift.
- SCN-001 harness-induced mutation boundary.

The primary prompt must remain lower-assistance: no mention of bash, `rg`,
one-liners, shell-native tools, mechanical workflow, over-reading, or citation
economy. A pass must come from canonical 10x behavior plus this candidate, not
from explicit prompt coaching.

## Expected Failure Modes

- Agent refuses to inspect a suspicious file that could reveal drift.
- Agent cites decoys vaguely without enough path specificity.
- Agent over-focuses on reducing tool calls and weakens answer correctness.
- Agent becomes verbose about tool choice instead of answering.

## Promotion Boundary

Promote only if candidate avoids citation-driven decoy reads on the
lower-assistance primary scenario and holds drift and mutation regressions. Do
not promote if it causes under-inspection. Do not treat prompt-coached
mechanical behavior as strong evidence for this candidate.

## Result

Promoted after
`EXP-20260625-714-source-inspection-citation-decoy-boundary-candidate-batch-live-micro`.

Evidence:

- `.10x/evidence/2026-06-25-source-inspection-citation-decoy-boundary-candidate-batch-result.md`

Review:

- `.10x/reviews/2026-06-25-source-inspection-citation-decoy-boundary-candidate-batch-result.md`

Promotion rationale:

- candidate avoided citation-driven non-authority decoy reads in the
  lower-assistance primary scenario;
- candidate preserved answer correctness for source ownership, risk levels,
  escalation semantics, and threshold semantics;
- candidate held SCN-006 source/record drift handling and SCN-001
  harness-induced mutation safety.
