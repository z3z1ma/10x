import sys
import tempfile
import unittest
from pathlib import Path


from agent_loom.core import concurrent as core_concurrent
from agent_loom.core import exec as core_exec
from agent_loom.core import fs as core_fs
from agent_loom.core import time as core_time


class TestCoreTime(unittest.TestCase):
    def test_parse_iso_accepts_z_suffix(self) -> None:
        dt = core_time.parse_iso("2026-01-02T03:04:05Z")
        self.assertIsNotNone(dt)
        assert dt is not None
        self.assertIsNotNone(dt.tzinfo)
        off = dt.utcoffset()
        self.assertIsNotNone(off)
        assert off is not None
        self.assertEqual(int(off.total_seconds()), 0)

    def test_parse_iso_z_alias(self) -> None:
        dt = core_time.parse_iso_z("2026-01-02T03:04:05Z")
        self.assertIsNotNone(dt)

    def test_parse_duration_seconds_supports_weeks(self) -> None:
        self.assertEqual(core_time.parse_duration_seconds("1w"), 7 * 86400)
        self.assertEqual(
            core_time.parse_duration_seconds("1w2d"), 7 * 86400 + 2 * 86400
        )


class TestCoreFs(unittest.TestCase):
    def test_fs_escape_is_reversible(self) -> None:
        raw = "feature/one"
        esc = core_fs.fs_escape(raw)
        self.assertNotEqual(esc, raw)
        self.assertIn("%2F", esc)
        self.assertEqual(core_fs.fs_unescape(esc), raw)

    def test_ensure_dir_creates_parents(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "a" / "b" / "c"
            self.assertFalse(p.exists())
            core_fs.ensure_dir(p)
            self.assertTrue(p.exists())


class TestCoreConcurrent(unittest.TestCase):
    def test_parallel_map_preserves_order(self) -> None:
        out = core_concurrent.parallel_map(lambda x: x * 2, [3, 2, 1], jobs=4)
        self.assertEqual(out, [6, 4, 2])


class TestCoreExec(unittest.TestCase):
    def test_run_captures_stdout_and_stderr(self) -> None:
        cmd = [
            sys.executable,
            "-c",
            "import sys; print('hi'); sys.stderr.write('err');",
        ]
        p = core_exec.run(cmd, cwd=Path.cwd())
        self.assertEqual(p.returncode, 0)
        self.assertIn("hi", p.stdout)
        self.assertIn("err", p.stderr)

    def test_run_raises_exec_error_with_output(self) -> None:
        cmd = [
            sys.executable,
            "-c",
            "import sys; print('out'); sys.stderr.write('bad'); sys.exit(2)",
        ]
        with self.assertRaises(core_exec.ExecError) as ctx:
            core_exec.run(cmd, cwd=Path.cwd(), check=True)
        e = ctx.exception
        self.assertEqual(e.returncode, 2)
        self.assertIn("out", e.stdout)
        self.assertIn("bad", e.stderr)
        # __str__ should be human-friendly and include cwd.
        self.assertIn(str(Path.cwd()), str(e))


if __name__ == "__main__":
    unittest.main()
