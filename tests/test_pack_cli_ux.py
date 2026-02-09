import contextlib
import importlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from typing import Callable, cast

from agent_loom.pack.core import install_pack


pack_mod = importlib.import_module("agent_loom.pack.cli")
pack_cli = cast(Callable[[list[str]], int], getattr(pack_mod, "main"))


def _run_text(argv: list[str], *, cwd: Path) -> tuple[int, str, str]:
    out = io.StringIO()
    err = io.StringIO()
    old = Path.cwd()
    try:
        os.chdir(cwd)
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = int(pack_cli(argv))
    finally:
        os.chdir(old)
    return rc, out.getvalue(), err.getvalue()


class TestPackCliUx(unittest.TestCase):
    def test_status_emits_note_when_drifted_without_diff(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            install_pack(repo_root=repo, pack_id="sample", dry_run=False)

            p = repo / ".opencode" / "commands" / "pack-sample.md"
            p.write_text("drift\n", encoding="utf-8")

            rc, out, err = _run_text(["status"], cwd=repo)
        self.assertEqual(rc, 0)
        self.assertEqual(err, "")
        self.assertIn('"drifted": 1', out)
        self.assertIn("rerun with --diff", out)

    def test_status_diff_prints_unified_diff_for_drifted_files(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            install_pack(repo_root=repo, pack_id="sample", dry_run=False)

            p = repo / ".opencode" / "commands" / "pack-sample.md"
            p.write_text("drift\n", encoding="utf-8")

            rc, out, err = _run_text(["status", "--diff"], cwd=repo)
        self.assertEqual(rc, 0)
        self.assertEqual(err, "")
        self.assertIn("diff (drifted): sample/.opencode/commands/pack-sample.md", out)
        self.assertIn("--- pack:sample/.opencode/commands/pack-sample.md", out)
        self.assertIn("+drift", out)

    def test_install_conflict_is_visible_in_status(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)

            p = repo / ".opencode" / "commands" / "pack-sample.md"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("preexisting drift\n", encoding="utf-8")

            install_pack(repo_root=repo, pack_id="sample", dry_run=False)

            rc, out, err = _run_text(["status", "--json"], cwd=repo)
        self.assertEqual(rc, 0)
        self.assertEqual(err, "")
        payload = json.loads(out.strip())
        self.assertEqual(int(payload.get("drifted") or 0), 1)


if __name__ == "__main__":
    unittest.main()
