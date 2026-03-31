# Memory Context Scripts

## `scripts/scan_memory_l0.py`

Use this script when you need a compact summary of memory files before deciding what to read.

Examples:

```bash
python3 scripts/scan_memory_l0.py
python3 scripts/scan_memory_l0.py --domain user
python3 scripts/scan_memory_l0.py --json
```

## `scripts/validate_memory_module.py`

Use this script before relying on the memory module after structural edits or when the module may be incomplete.

Examples:

```bash
python3 scripts/validate_memory_module.py
python3 scripts/validate_memory_module.py --json
```
