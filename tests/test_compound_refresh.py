from __future__ import annotations

from pathlib import Path

from agent_loom.compound.docs import sync_docs
from agent_loom.compound.install import install_opencode


def test_compound_refresh_populates_agents_blocks(tmp_path: Path) -> None:
    dest = tmp_path
    install_opencode(dest=dest, dry_run=False)

    # run the refresh logic
    sync_docs(root=dest)

    agents = (dest / "AGENTS.md").read_text(encoding="utf-8")
    assert "<!-- BEGIN:compound:agents-ai-behavior -->" in agents
    assert "<!-- END:compound:agents-ai-behavior -->" in agents
    assert "Core loop" in agents
    assert "Plan -> Work -> Review -> Compound -> Repeat" in agents
