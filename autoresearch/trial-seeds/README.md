# Trial Seeds

`autoresearch/trial-seeds/` contains clean-room starting states for live
subject-agent trials. Seeds are not answer keys. They create conditions for the
scientist to test against a registered hypothesis.

Use `index.json` as the selection surface. Each entry records:

- scenario and target rubric IDs;
- condition summary and experiment use;
- suggested prompt family;
- expected high-quality and failure behavior;
- known traps and quality-floor signals;
- material `.10x` records and source files to inspect;
- `raw_path`, `workspace_manifest_path`, and `workspace_procedure` for runner
  definitions.

For "all seed-backed scenarios", use exactly `index.json` `seeds[]`.
Historical live research definitions that are not replayable from tracked seed
packages are documented in `baseline-exclusions.json`; they are not deleted, but
they are outside the deterministic seed-backed baseline until promoted into
tracked seeds.

After adding, removing, or materially changing a seed, regenerate the index:

```bash
python3 autoresearch/build_trial_seed_index.py
```

Then validate from the repository root:

```bash
python3 autoresearch/validate.py
```
