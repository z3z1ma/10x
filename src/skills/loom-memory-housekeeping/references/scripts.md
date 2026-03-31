# Memory Housekeeping Scripts

## `scripts/validate_memory_module.py`

Use this script to validate the module before and after structural edits.

```bash
python3 scripts/validate_memory_module.py
python3 scripts/validate_memory_module.py --json
```

## `scripts/scan_memory_l0.py`

Use this script when you want a quick summary of regular memory files.

```bash
python3 scripts/scan_memory_l0.py
```

## `scripts/rebuild_memory_glacier_index.py`

Use this script after archive edits so the glacier catalog stays truthful.

```bash
python3 scripts/rebuild_memory_glacier_index.py
```

## `scripts/rebuild_memory_link_index.py`

Use this script after link-heavy edits so the backlink map stays truthful.

```bash
python3 scripts/rebuild_memory_link_index.py
```
