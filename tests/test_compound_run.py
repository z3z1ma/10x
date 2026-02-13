from __future__ import annotations

import contextlib
import json
import os
import subprocess
import tempfile
from pathlib import Path
import sys

from agent_loom.compound.engine import run_instincts_update
from agent_loom.compound.install import install_opencode
from agent_loom.compound.paths import compound_paths
from agent_loom.compound.state import load_state


def _git(args: list[str], *, cwd: Path, env: dict[str, str], check: bool = True) -> str:
    p = subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=check,
    )
    return (p.stdout or "").strip()


def _configure_mock_derivation_command(*, root: Path, payload: dict) -> None:
    script = root / ".mock_instincts_llm.py"
    script.write_text(
        "import json\n"
        "from pathlib import Path\n"
        + f"payload = {json.dumps(payload)}\n"
        + "base = Path('.loom/compound/instincts/local')\n"
        + "base.mkdir(parents=True, exist_ok=True)\n"
        + "for inst in payload.get('instincts', []):\n"
        + "    instinct_id = str(inst.get('id') or '').strip()\n"
        + "    if not instinct_id:\n"
        + "        continue\n"
        + "    tags = [str(t).strip() for t in list(inst.get('tags') or []) if str(t).strip()]\n"
        + "    domain = str(inst.get('domain') or '').strip() or (tags[0] if tags else 'general')\n"
        + "    notes = str(inst.get('notes') or '').strip()\n"
        + "    confidence = float(inst.get('confidence') or 0.5)\n"
        + "    content = '\\n'.join([\n"
        + "        '---',\n"
        + "        f\"id: {instinct_id}\",\n"
        + "        f\"title: {str(inst.get('title') or '').strip()}\",\n"
        + "        f\"trigger: {str(inst.get('trigger') or '').strip()}\",\n"
        + "        f\"confidence: {confidence:.4f}\",\n"
        + "        'status: active',\n"
        + "        f\"domain: {domain}\",\n"
        + "        'source: local',\n"
        + "        'created_at: 2026-02-12T00:00:00Z',\n"
        + "        'updated_at: 2026-02-12T00:00:00Z',\n"
        + "        f\"tags: {', '.join(tags)}\",\n"
        + "        f\"notes: {notes}\",\n"
        + "        '---',\n"
        + "        '',\n"
        + "        '## Action',\n"
        + "        str(inst.get('action') or '').strip(),\n"
        + "        '',\n"
        + "        '## Evidence',\n"
        + "        f\"- ts=2026-02-12T00:00:00Z source_id=seed-{instinct_id} source_hash=seed\",\n"
        + "        '',\n"
        + "        '## Notes',\n"
        + "        notes or '- _(none)_',\n"
        + "        '',\n"
        + "    ])\n"
        + "    (base / f\"{instinct_id}.md\").write_text(content, encoding='utf-8')\n",
        encoding="utf-8",
    )
    cfg = root / ".loom" / "compound" / "config.json"
    cfg.parent.mkdir(parents=True, exist_ok=True)
    cfg.write_text(
        json.dumps(
            {
                "version": 1,
                "instincts": {
                    "derive_command": [sys.executable, str(script)],
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


@contextlib.contextmanager
def _temp_git_repo():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        env = os.environ.copy()
        env.update(
            {
                "GIT_AUTHOR_NAME": "Test",
                "GIT_AUTHOR_EMAIL": "test@example.com",
                "GIT_COMMITTER_NAME": "Test",
                "GIT_COMMITTER_EMAIL": "test@example.com",
            }
        )
        _git(["init"], cwd=root, env=env)
        yield root, env


def test_instincts_update_creates_candidates_from_repeated_observations() -> None:
    with _temp_git_repo() as (root, env):
        install_opencode(dest=root, dry_run=False)
        _git(["add", "-A"], cwd=root, env=env)
        _git(["commit", "-m", "init"], cwd=root, env=env)

        paths = compound_paths(root)
        paths.observations_file.parent.mkdir(parents=True, exist_ok=True)
        rows = [
            {
                "id": "1",
                "ts": "2026-02-12T00:00:00Z",
                "event": "tool_complete",
                "tool": "grep",
                "command": "git status --porcelain",
            },
            {
                "id": "2",
                "ts": "2026-02-12T00:01:00Z",
                "event": "tool_complete",
                "tool": "read",
                "command": "git status --porcelain",
            },
            {
                "id": "3",
                "ts": "2026-02-12T00:02:00Z",
                "event": "tool_complete",
                "tool": "edit",
                "command": "git status --porcelain",
            },
            {
                "id": "4",
                "ts": "2026-02-12T00:03:00Z",
                "event": "tool_complete",
                "tool": "read",
            },
            {
                "id": "5",
                "ts": "2026-02-12T00:04:00Z",
                "event": "tool_complete",
                "tool": "edit",
            },
            {
                "id": "6",
                "ts": "2026-02-12T00:05:00Z",
                "event": "tool_complete",
                "tool": "read",
            },
        ]
        paths.observations_file.write_text(
            "\n".join([json.dumps(r) for r in rows]) + "\n",
            encoding="utf-8",
        )

        _configure_mock_derivation_command(
            root=root,
            payload={
                "instincts": [
                    {
                        "id": "reuse-git-status-porcelain",
                        "title": "Reuse git status porcelain checks",
                        "trigger": "When iterating on code changes and verifying repo cleanliness.",
                        "action": "Use `git status --porcelain` early and repeatedly before/after edits.",
                        "confidence": 0.84,
                        "tags": ["compound", "git", "workflow"],
                        "notes": "Observed repeated command usage in recent tool events.",
                    }
                ]
            },
        )
        res = run_instincts_update(
            root=root,
            auto=False,
            min_occurrences=2,
            max_candidates=8,
        )

        assert res.ok is True
        assert res.skipped is False
        assert res.observations_ingested == 6
        assert res.instincts_candidates >= 1
        assert res.instincts_created >= 1
        assert res.state_updated is True
        assert (
            root
            / ".loom"
            / "compound"
            / "instincts"
            / "local"
            / "reuse-git-status-porcelain.md"
        ).exists()
        assert (root / ".loom" / "compound" / "INSTINCTS.md").exists()


def test_instincts_update_auto_threshold_skips_without_state_writes() -> None:
    with _temp_git_repo() as (root, env):
        install_opencode(dest=root, dry_run=False)
        _git(["add", "-A"], cwd=root, env=env)
        _git(["commit", "-m", "init"], cwd=root, env=env)

        paths = compound_paths(root)
        paths.observations_file.parent.mkdir(parents=True, exist_ok=True)
        paths.observations_file.write_text(
            json.dumps(
                {
                    "id": "1",
                    "ts": "2026-02-12T00:00:00Z",
                    "event": "tool_complete",
                    "tool": "read",
                    "command": "git status --porcelain",
                }
            )
            + "\n",
            encoding="utf-8",
        )

        res = run_instincts_update(
            root=root,
            auto=True,
            min_new_observations=5,
            min_occurrences=2,
        )

        assert res.ok is True
        assert res.skipped is True
        assert res.skip_reason == "insufficient_new_observations"
        assert res.state_updated is False
        assert res.wrote_instincts_md is True
        assert (paths.loom_compound_dir / "INSTINCTS.md").exists()
        assert not (paths.loom_compound_dir / "state.json").exists()


def test_instincts_update_handles_observation_rotation() -> None:
    with _temp_git_repo() as (root, env):
        install_opencode(dest=root, dry_run=False)
        _git(["add", "-A"], cwd=root, env=env)
        _git(["commit", "-m", "init"], cwd=root, env=env)

        paths = compound_paths(root)
        paths.observations_file.parent.mkdir(parents=True, exist_ok=True)
        paths.observations_file.write_text(
            "\n".join(
                [
                    json.dumps({"id": "1", "ts": "2026-02-12T00:00:00Z", "tool": "read"}),
                    json.dumps({"id": "2", "ts": "2026-02-12T00:01:00Z", "tool": "edit"}),
                    "",
                ]
            ),
            encoding="utf-8",
        )
        _configure_mock_derivation_command(
            root=root,
            payload={
                "instincts": [
                    {
                        "id": "prefer-read-before-edit",
                        "title": "Prefer read before edit",
                        "trigger": "When changing a file based on fresh observations.",
                        "action": "Read target context before issuing edits.",
                        "confidence": 0.76,
                        "tags": ["compound", "tools"],
                        "notes": "Derived from recurrent read/edit transitions.",
                    }
                ]
            },
        )

        r1 = run_instincts_update(root=root, auto=False, min_occurrences=1)
        assert r1.ok is True
        assert r1.observations_ingested == 2

        rotated = paths.observations_file.with_name(paths.observations_file.name + ".bak")
        paths.observations_file.rename(rotated)
        paths.observations_file.write_text(
            json.dumps(
                {
                    "id": "3",
                    "ts": "2026-02-12T00:02:00Z",
                    "tool": "read",
                    "command": "git status --porcelain",
                }
            )
            + "\n",
            encoding="utf-8",
        )

        r2 = run_instincts_update(root=root, auto=False, min_occurrences=1)
        assert r2.ok is True
        assert r2.observations_reset_detected is True
        assert r2.observations_ingested == 1

        st = load_state(paths.loom_compound_dir / "state.json")
        assert st.observations_count == 1
