from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

from agent_loom.compound.engine import run_instincts_update
from agent_loom.compound.evolve import evolve_instincts
from agent_loom.compound.hooks import run_claude_hook
from agent_loom.compound.import_export import export_instincts, instinct_import
from agent_loom.compound.install import install_opencode
from agent_loom.compound.instincts import load_instincts
from agent_loom.compound.paths import compound_paths


def _configure_mock_derivation_command(*, root: Path, payload: dict) -> None:
    script = root / ".mock_learning_v2_llm.py"
    script.write_text(
        "import json\n"
        "from pathlib import Path\n"
        + f"payload = {json.dumps(payload)}\n"
        + "base = Path('.loom/compound/instincts/personal')\n"
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
        + "        'source: personal',\n"
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


def test_claude_hook_rotation_and_observer_nudge() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        install_opencode(dest=root, dry_run=False)
        paths = compound_paths(root)

        prev = {
            "COMPOUND_OBSERVATIONS_MAX_BYTES": os.environ.get("COMPOUND_OBSERVATIONS_MAX_BYTES"),
            "COMPOUND_OBSERVATIONS_MAX_BACKUPS": os.environ.get("COMPOUND_OBSERVATIONS_MAX_BACKUPS"),
        }
        os.environ["COMPOUND_OBSERVATIONS_MAX_BYTES"] = "100"
        os.environ["COMPOUND_OBSERVATIONS_MAX_BACKUPS"] = "2"
        try:
            for idx in range(1, 8):
                payload = {
                    "hook_event_name": "PostToolUse",
                    "session_id": f"s-{idx}",
                    "tool_name": "Read",
                    "tool_input": {"file_path": f"/tmp/demo-{idx}.txt"},
                    "tool_response": {"output": "x" * 1800},
                }
                run_claude_hook(
                    repo=root,
                    stdin_text=json.dumps(payload),
                    payload_json="",
                    event="",
                )
        finally:
            for key, value in prev.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value

        assert paths.observations_file.exists()
        assert paths.observer_nudge_file.exists()
        assert paths.observations_file.with_name("observations.jsonl.1.bak").exists()


def test_instinct_markdown_roundtrip_and_import_export_merge() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        install_opencode(dest=root, dry_run=False)
        paths = compound_paths(root)
        paths.observations_file.parent.mkdir(parents=True, exist_ok=True)
        paths.observations_file.write_text(
            "\n".join(
                [
                    json.dumps({"id": "1", "ts": "2026-02-12T00:00:00Z", "event": "tool_complete", "tool": "read"}),
                    json.dumps({"id": "2", "ts": "2026-02-12T00:01:00Z", "event": "tool_complete", "tool": "edit"}),
                    json.dumps({"id": "3", "ts": "2026-02-12T00:02:00Z", "event": "tool_complete", "tool": "read"}),
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
                        "id": "read-before-edit",
                        "title": "Read before edit",
                        "trigger": "Before editing files",
                        "action": "Read target files first",
                        "confidence": 0.7,
                        "tags": ["workflow"],
                        "notes": "Repeated read/edit pattern",
                    }
                ]
            },
        )

        res = run_instincts_update(root=root)
        assert res.ok is True

        store = load_instincts(paths.instincts_file)
        assert any(i.id == "read-before-edit" for i in store.instincts)

        export_path = root / "instincts.bundle.json"
        exp = export_instincts(
            instincts_file=paths.instincts_file,
            out_file=export_path,
            min_confidence=0.0,
        )
        assert exp.exported >= 1

        bundle = json.loads(export_path.read_text(encoding="utf-8"))
        instincts = bundle.get("instincts") if isinstance(bundle.get("instincts"), list) else []
        assert instincts
        instincts[0]["confidence"] = 0.6
        export_path.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")

        imp1 = instinct_import(
            instincts_file=paths.instincts_file,
            source=str(export_path),
            force=False,
            min_confidence=0.0,
        )
        assert imp1.skipped >= 1

        instincts[0]["confidence"] = 0.95
        export_path.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")

        imp2 = instinct_import(
            instincts_file=paths.instincts_file,
            source=str(export_path),
            force=False,
            min_confidence=0.0,
        )
        assert imp2.updated >= 1


def test_evolve_is_deterministic_and_generates_harness_artifacts() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        install_opencode(dest=root, dry_run=False)
        personal = root / ".loom" / "compound" / "instincts" / "personal"
        personal.mkdir(parents=True, exist_ok=True)

        template = (
            "---\n"
            "id: {id}\n"
            "title: {title}\n"
            "trigger: {trigger}\n"
            "confidence: {confidence}\n"
            "status: active\n"
            "domain: workflow\n"
            "source: personal\n"
            "created_at: 2026-02-12T00:00:00Z\n"
            "updated_at: 2026-02-12T00:00:00Z\n"
            "tags: workflow\n"
            "notes: n\n"
            "---\n\n"
            "## Action\n"
            "{action}\n\n"
            "## Evidence\n"
            "- ts=2026-02-12T00:00:00Z source_id={source_id} source_hash={source_hash}\n\n"
            "## Notes\n"
            "n\n"
        )

        entries = [
            {
                "id": "workflow-a",
                "title": "Workflow A",
                "trigger": "when implementing auth flow",
                "confidence": "0.9000",
                "action": "Run checks before commit",
                "source_id": "obs-1",
                "source_hash": "abc",
            },
            {
                "id": "workflow-b",
                "title": "Workflow B",
                "trigger": "when implementing auth flow",
                "confidence": "0.8800",
                "action": "Inspect changed files first",
                "source_id": "obs-2",
                "source_hash": "def",
            },
            {
                "id": "workflow-c",
                "title": "Workflow C",
                "trigger": "when implementing auth flow",
                "confidence": "0.8600",
                "action": "Verify tests before push",
                "source_id": "obs-3",
                "source_hash": "ghi",
            },
        ]

        for entry in entries:
            personal.joinpath(f"{entry['id']}.md").write_text(
                template.format(**entry),
                encoding="utf-8",
            )

        r1 = evolve_instincts(root=root, threshold=0.75, generate=True)
        assert r1.ok is True
        assert r1.clusters >= 1

        skill_path = root / ".loom" / "compound" / "evolved" / "skills" / "auth-flow.md"
        assert skill_path.exists()
        before = skill_path.read_text(encoding="utf-8")

        r2 = evolve_instincts(root=root, threshold=0.75, generate=True)
        assert r2.ok is True
        after = skill_path.read_text(encoding="utf-8")
        assert before == after

        assert (root / ".claude" / "skills" / "learned" / "auth-flow" / "SKILL.md").exists()
        assert (root / ".opencode" / "commands" / "instinct-auth-flow.md").exists()
        assert (root / ".claude" / "agents" / "instinct-auth-flow-agent.md").exists()
