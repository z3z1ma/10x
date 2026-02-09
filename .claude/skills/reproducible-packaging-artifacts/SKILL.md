---
name: reproducible-packaging-artifacts
description: Checklist for making pack/archive outputs deterministic across runs.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-09T19:02:04.864649Z"
  source_episode_ids: "6b4f92dcfe0b292c1545e85c5c8d5eb0751c41108b80b557a74a4c6539245fd9"
  source_instinct_ids: "reproducible-pack-outputs"
  tags: "cli,determinism,packaging,python"
  updated_at: "2026-02-09T19:02:04.864649Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
# Reproducible Packaging Artifacts

Make `pack`/bundle/archive outputs deterministic so repeated runs produce identical artifacts.

## Procedure
1. Sort inputs deterministically (paths, entries, manifest rows).
2. Normalize paths:
   - Use `/` separators in archive/internal manifests.
   - Strip leading `./`.
3. Normalize text serialization:
   - Explicit encoding (UTF-8).
   - Consistent newline (`\n`).
4. If producing archives (tar/zip):
   - Fix timestamps (e.g. epoch or a passed-in build time).
   - Normalize uid/gid, owner/group names.
   - Normalize file modes when feasible.
5. Document any intentional nondeterminism (e.g. embed build id) and gate it behind an explicit flag.

## Verification
- Run the pack command twice on identical input and compare hashes.
- Add a regression test that asserts stable ordering and stable metadata for a small fixture.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
