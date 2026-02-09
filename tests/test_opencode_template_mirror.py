from __future__ import annotations

from pathlib import Path


def test_compound_opencode_template_is_mirrored() -> None:
    root = Path(__file__).resolve().parents[1]

    pairs = [
        (
            root / ".opencode" / "plugins" / "compound_engineering.ts",
            root
            / "src"
            / "agent_loom"
            / "pack"
            / "packs"
            / "loom-compound-core"
            / "files"
            / ".opencode"
            / "plugins"
            / "compound_engineering.ts",
        ),
        (
            root / ".opencode" / "compound" / "prompts" / "autolearn.md",
            root
            / "src"
            / "agent_loom"
            / "pack"
            / "packs"
            / "loom-compound-core"
            / "files"
            / ".opencode"
            / "compound"
            / "prompts"
            / "autolearn.md",
        ),
    ]

    for a, b in pairs:
        assert a.exists(), str(a)
        assert b.exists(), str(b)
        assert a.read_text(encoding="utf-8") == b.read_text(encoding="utf-8"), (
            f"template drift: {a} != {b}"
        )
