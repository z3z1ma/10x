from __future__ import annotations

from pathlib import Path

from agent_loom.compound.prime import prime_rules


def test_compound_prime_writes_rules_files(tmp_path: Path) -> None:
    root = tmp_path
    res = prime_rules(root=root)
    assert res.ok is True
    # smoke check that we wrote at least the expected subsystem files
    expected = {
        root / ".opencode" / "rules" / "memory.md",
        root / ".opencode" / "rules" / "team.md",
        root / ".opencode" / "rules" / "ticket.md",
        root / ".opencode" / "rules" / "workspace.md",
    }
    for p in expected:
        assert p.exists(), str(p)
        assert p.read_text(encoding="utf-8").strip(), str(p)
