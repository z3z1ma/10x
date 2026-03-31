# Memory Reflection Scripts

Reflection uses the same structural helpers as ordinary memory work.

## `scripts/scan_memory_l0.py`

Use this script before a broad reflection pass so file selection stays deliberate.

```bash
python3 scripts/scan_memory_l0.py
python3 scripts/scan_memory_l0.py --domain system
```

## `scripts/validate_memory_module.py`

Use this script before and after a substantial reflection pass.

```bash
python3 scripts/validate_memory_module.py
```
