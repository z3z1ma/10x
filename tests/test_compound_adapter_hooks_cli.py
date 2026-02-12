import contextlib
import importlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from collections.abc import Iterator
from pathlib import Path
from typing import Callable, cast


compound_mod = importlib.import_module("agent_loom.compound.cli")
compound_cli = cast(Callable[[list[str]], int], getattr(compound_mod, "main"))


def _run_text(argv: list[str], *, cwd: Path) -> tuple[int, str, str]:
    out = io.StringIO()
    err = io.StringIO()
    old = Path.cwd()
    try:
        os.chdir(cwd)
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = int(compound_cli(argv))
    finally:
        os.chdir(old)
    return rc, out.getvalue(), err.getvalue()


def _run_json(argv: list[str], *, cwd: Path) -> tuple[int, dict]:
    rc, out, _ = _run_text(argv, cwd=cwd)
    payload = out.strip()
    return rc, (json.loads(payload) if payload else {})


def _run_text_with_stdin(argv: list[str], *, cwd: Path, stdin: str) -> tuple[int, str, str]:
    out = io.StringIO()
    err = io.StringIO()
    old_cwd = Path.cwd()
    old_stdin = sys.stdin
    try:
        os.chdir(cwd)
        sys.stdin = io.StringIO(stdin)
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = int(compound_cli(argv))
    finally:
        sys.stdin = old_stdin
        os.chdir(old_cwd)
    return rc, out.getvalue(), err.getvalue()


def _git(args: list[str], *, cwd: Path, env: dict[str, str]) -> None:
    subprocess.run(["git", *args], cwd=str(cwd), env=env, check=True)


@contextlib.contextmanager
def _git_identity_env() -> Iterator[None]:
    before = os.environ.copy()
    os.environ.update(
        {
            "GIT_AUTHOR_NAME": "Test",
            "GIT_AUTHOR_EMAIL": "test@example.com",
            "GIT_COMMITTER_NAME": "Test",
            "GIT_COMMITTER_EMAIL": "test@example.com",
        }
    )
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(before)


def _configure_mock_derivation_command(*, root: Path, payload: dict) -> None:
    script = root / ".mock_cli_instincts_llm.py"
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


class TestCompoundHookAdapterCliUx(unittest.TestCase):
    def test_help_lists_only_expected_commands(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            rc, out, err = _run_text(["-h"], cwd=Path(td))
        self.assertEqual(rc, 0)
        self.assertTrue(out.strip() or err.strip())
        text = (out + "\n" + err).lower()

        for cmd in [
            "init",
            "instincts-update",
            "instinct-status",
            "instinct-export",
            "instinct-import",
            "evolve",
            "observer",
            "sync",
            "prime",
            "claude-hook",
            "opencode-hook",
            "omp-hook",
        ]:
            self.assertIn(cmd, text)

        self.assertIn(
            "{init,sync,instincts-update,instinct-status,instinct-export,instinct-import,evolve,observer,prime,claude-hook,opencode-hook,omp-hook}",
            text,
        )

        for gone in [
            "learn",
            "refresh",
            "skills-author",
            "doctor",
            "rebuild",
            "triage",
            "replay",
            "docblock",
            "changelog",
        ]:
            self.assertNotIn(gone, text)

    def test_prime_prints_cookbook(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            rc, out, _ = _run_text(["prime"], cwd=Path(td))
        self.assertEqual(rc, 0)
        self.assertIn("Compound Cookbook", out)
        self.assertIn("loom compound init", out)

    def test_removed_command_is_structured_json_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            rc, payload = _run_json(["rebuild", "--json"], cwd=Path(td))
        self.assertEqual(rc, 2)
        self.assertFalse(bool(payload.get("ok")))
        self.assertEqual(str(payload.get("code") or ""), "ARGPARSE")
        self.assertTrue(str(payload.get("hint") or ""))

    def test_init_instincts_sync_json_smoke(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            root.mkdir(parents=True, exist_ok=True)

            with _git_identity_env():
                env = os.environ.copy()
                _git(["init", "-b", "main"], cwd=root, env=env)
                (root / "README.txt").write_text("hi\n", encoding="utf-8")
                _git(["add", "-A"], cwd=root, env=env)
                _git(["commit", "-m", "init"], cwd=root, env=env)

                rc0, p0 = _run_json(["init", "--dest", str(root), "--json"], cwd=root)
                self.assertEqual(rc0, 0)
                self.assertTrue(bool(p0.get("ok")))

                obs = root / ".loom" / "compound" / "runtime" / "observations.jsonl"
                obs.parent.mkdir(parents=True, exist_ok=True)
                obs.write_text(
                    "\n".join(
                        [
                            '{"id":"1","ts":"2026-02-12T00:00:00Z","event":"tool_complete","tool":"read","command":"git status --porcelain"}',
                            '{"id":"2","ts":"2026-02-12T00:01:00Z","event":"tool_complete","tool":"edit","command":"git status --porcelain"}',
                            '{"id":"3","ts":"2026-02-12T00:02:00Z","event":"tool_complete","tool":"read","command":"git status --porcelain"}',
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
                                "id": "reuse-git-status-porcelain",
                                "title": "Reuse git status porcelain checks",
                                "trigger": "When iterating on repository changes.",
                                "action": "Use git status --porcelain before and after edits.",
                                "confidence": 0.82,
                                "tags": ["compound", "git"],
                                "notes": "Derived from repeated command/tool events.",
                            }
                        ]
                    },
                )
                rc2, p2 = _run_json(
                    [
                        "instincts-update",
                        "--repo",
                        str(root),
                        "--min-occurrences",
                        "2",
                        "--json",
                    ],
                    cwd=root,
                )
                self.assertEqual(rc2, 0)
                self.assertTrue(bool(p2.get("ok")))
                self.assertGreaterEqual(int(p2.get("instincts_created") or 0), 1)
                self.assertTrue(
                    (
                        root
                        / ".loom"
                        / "compound"
                        / "instincts"
                        / "personal"
                        / "reuse-git-status-porcelain.md"
                    ).exists()
                )

                ctx = root / "LOOM.md"
                ctx.write_text(
                    ctx.read_text(encoding="utf-8") + "\n# touched\n",
                    encoding="utf-8",
                )
                rc3, p3 = _run_json(
                    ["sync", "--repo", str(root), "--json", "-m", "chore: compound"],
                    cwd=root,
                )
                self.assertEqual(rc3, 0)
                self.assertTrue(bool(p3.get("ok")))
                self.assertIn("committed", p3)

    def test_hook_adapters_log_observation_json(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            root.mkdir(parents=True, exist_ok=True)

            with _git_identity_env():
                env = os.environ.copy()
                _git(["init", "-b", "main"], cwd=root, env=env)
                (root / "README.txt").write_text("hi\n", encoding="utf-8")
                _git(["add", "-A"], cwd=root, env=env)
                _git(["commit", "-m", "init"], cwd=root, env=env)

                rc0, p0 = _run_json(["init", "--dest", str(root), "--json"], cwd=root)
                self.assertEqual(rc0, 0)
                self.assertTrue(bool(p0.get("ok")))

                payload = {
                    "hook_event_name": "PostToolUse",
                    "session_id": "sess-1",
                    "tool_name": "Read",
                    "tool_input": {"file_path": "/tmp/demo.txt"},
                }
                rc1, out1, _ = _run_text(
                    [
                        "claude-hook",
                        "--repo",
                        str(root),
                        "--payload",
                        json.dumps(payload),
                    ],
                    cwd=root,
                )
                self.assertEqual(rc1, 0)
                self.assertEqual(json.loads(out1.strip()), payload)

                rc1b, p1b = _run_json(
                    [
                        "opencode-hook",
                        "--repo",
                        str(root),
                        "--event",
                        "tool.execute.before",
                        "--payload",
                        json.dumps(
                            {
                                "type": "tool.execute.before",
                                "session_id": "sess-1",
                                "tool_name": "Read",
                                "tool_input": {"file_path": "/tmp/demo2.txt"},
                            }
                        ),
                        "--json",
                    ],
                    cwd=root,
                )
                self.assertEqual(rc1b, 0)
                self.assertTrue(bool(p1b.get("ok")))
                self.assertEqual(str(p1b.get("harness") or ""), "opencode")

                rc1c, p1c = _run_json(
                    [
                        "omp-hook",
                        "--repo",
                        str(root),
                        "--event",
                        "tool_call",
                        "--payload",
                        json.dumps(
                            {
                                "event_name": "tool_call",
                                "session_id": "sess-omp-1",
                                "tool_name": "bash",
                                "tool_input": {"command": "git status --porcelain"},
                            }
                        ),
                        "--json",
                    ],
                    cwd=root,
                )
                self.assertEqual(rc1c, 0)
                self.assertTrue(bool(p1c.get("ok")))
                self.assertEqual(str(p1c.get("harness") or ""), "omp")

                obs = root / ".loom" / "compound" / "runtime" / "observations.jsonl"
                self.assertTrue(obs.exists())
                rows = [
                    ln
                    for ln in obs.read_text(encoding="utf-8").splitlines()
                    if ln.strip()
                ]
                self.assertTrue(rows)
                parsed = [json.loads(ln) for ln in rows]

                claude_obs = next(
                    x
                    for x in parsed
                    if str(x.get("harness") or "") == "claude"
                    and str(x.get("event") or "") == "tool_complete"
                )
                self.assertEqual(str(claude_obs.get("session_id") or ""), "sess-1")
                self.assertEqual(str(claude_obs.get("tool") or "").lower(), "read")

                opencode_obs = next(
                    x
                    for x in parsed
                    if str(x.get("harness") or "") == "opencode"
                    and str(x.get("event") or "") == "tool_start"
                )
                self.assertEqual(str(opencode_obs.get("session_id") or ""), "sess-1")

                omp_obs = next(
                    x
                    for x in parsed
                    if str(x.get("harness") or "") == "omp"
                    and str(x.get("event") or "") == "tool_start"
                )
                self.assertEqual(str(omp_obs.get("session_id") or ""), "sess-omp-1")

                rc2, out2, _ = _run_text(
                    [
                        "claude-hook",
                        "--repo",
                        str(root),
                        "--payload",
                        json.dumps(
                            {
                                "hook_event_name": "UserPromptSubmit",
                                "session_id": "sess-1",
                                "prompt": "Please add durable logging for compile failures",
                            }
                        ),
                    ],
                    cwd=root,
                )
                self.assertEqual(rc2, 0)
                self.assertTrue(out2.strip())

                rows2 = [
                    ln for ln in obs.read_text(encoding="utf-8").splitlines() if ln.strip()
                ]
                last2 = json.loads(rows2[-1])
                self.assertEqual(str(last2.get("event") or ""), "prompt_submit")
                metadata = (
                    last2.get("metadata")
                    if isinstance(last2.get("metadata"), dict)
                    else {}
                )
                self.assertTrue(str(metadata.get("prompt_excerpt") or ""))

    def test_claude_hook_echoes_stdin_payload(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            payload = {
                "hook_event_name": "PreToolUse",
                "session_id": "echo-1",
                "tool_name": "Bash",
                "tool_input": {"command": "echo hi"},
            }
            rc, out, _ = _run_text_with_stdin(
                ["claude-hook", "--repo", str(root)],
                cwd=root,
                stdin=json.dumps(payload),
            )
            self.assertEqual(rc, 0)
            self.assertEqual(json.loads(out.strip()), payload)

    def test_omp_hook_reads_stdin_payload_with_event(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            root.mkdir(parents=True, exist_ok=True)

            rc0, p0 = _run_json(["init", "--dest", str(root), "--json"], cwd=root)
            self.assertEqual(rc0, 0)
            self.assertTrue(bool(p0.get("ok")))

            payload = {
                "event_name": "tool_call",
                "session_id": "stdin-sess",
                "tool_name": "bash",
                "tool_input": {"command": "git status --porcelain"},
            }
            rc1, out, _ = _run_text_with_stdin(
                ["omp-hook", "--repo", str(root), "--event", "tool_call", "--json"],
                cwd=root,
                stdin=json.dumps(payload),
            )
            self.assertEqual(rc1, 0)
            data = json.loads(out.strip()) if out.strip() else {}
            self.assertEqual(str(data.get("harness") or ""), "omp")

            obs = root / ".loom" / "compound" / "runtime" / "observations.jsonl"
            rows = [ln for ln in obs.read_text(encoding="utf-8").splitlines() if ln.strip()]
            self.assertTrue(rows)
            last = json.loads(rows[-1])
            self.assertEqual(str(last.get("event") or ""), "tool_start")
            self.assertEqual(str(last.get("session_id") or ""), "stdin-sess")
            self.assertEqual(str(last.get("tool") or ""), "bash")


if __name__ == "__main__":
    unittest.main()
