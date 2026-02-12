import contextlib
import importlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Callable, cast


memory_cli_mod = importlib.import_module("agent_loom.memory.cli")
memory_cli = cast(Callable[[list[str]], int], getattr(memory_cli_mod, "main"))


def _run_json(argv: list[str]) -> tuple[int, dict]:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = memory_cli(argv)
    payload = buf.getvalue().strip()
    return rc, (json.loads(payload) if payload else {})


def _run_text(argv: list[str]) -> tuple[int, str]:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = memory_cli(argv)
    return rc, buf.getvalue()


class TestMemoryCliUx(unittest.TestCase):
    def test_unknown_command_is_structured_json_error(self) -> None:
        rc, payload = _run_json(["nope"])
        self.assertEqual(rc, 2)
        self.assertFalse(payload.get("ok"))
        self.assertEqual(payload.get("code"), "ARGPARSE")
        self.assertTrue(str(payload.get("hint") or ""))

    def test_vault_missing_is_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc, payload = _run_json(["--vault", str(vault), "add", "Hello"])
        self.assertEqual(rc, 2)
        self.assertFalse(payload.get("ok"))
        self.assertEqual(payload.get("code"), "NOT_FOUND")
        self.assertIn("init", str(payload.get("hint") or "").lower())

    def test_add_positional_title_rewrites(self) -> None:
        norm = memory_cli_mod._normalize_argv(["add", "Hello"])
        args = memory_cli_mod.build_parser().parse_args(norm)
        self.assertEqual(str(getattr(args, "title", "") or ""), "Hello")

    def test_add_command_flag_parses(self) -> None:
        norm = memory_cli_mod._normalize_argv(
            ["add", "Hello", "--command", "uv run pytest"]
        )
        args = memory_cli_mod.build_parser().parse_args(norm)
        self.assertEqual(str(getattr(args, "command", "") or ""), "uv run pytest")

    def test_plural_flag_aliases_normalize(self) -> None:
        norm = memory_cli_mod._normalize_argv(
            [
                "add",
                "Hello",
                "--tags",
                "infra",
                "--aliases",
                "greeting",
                "--scopes",
                "file:src/app.py",
                "--links",
                "memory-foo",
                "--relateds",
                "memory-bar",
            ]
        )
        args = memory_cli_mod.build_parser().parse_args(norm)
        self.assertEqual(list(getattr(args, "tag", [])), ["infra"])
        self.assertEqual(list(getattr(args, "alias", [])), ["greeting"])
        self.assertEqual(list(getattr(args, "scope", [])), ["file:src/app.py"])
        self.assertEqual(list(getattr(args, "link", [])), ["memory-foo"])
        self.assertEqual(list(getattr(args, "related", [])), ["memory-bar"])

    def test_add_two_positional_args_become_title_and_body(self) -> None:
        norm = memory_cli_mod._normalize_argv(["add", "Hello", "Body"])
        args = memory_cli_mod.build_parser().parse_args(norm)
        self.assertEqual(str(getattr(args, "title", "") or ""), "Hello")
        self.assertEqual(str(getattr(args, "body", "") or ""), "Body")

    def test_edit_positional_text_becomes_append(self) -> None:
        norm = memory_cli_mod._normalize_argv(["edit", "note-1", "new findings"])
        args = memory_cli_mod.build_parser().parse_args(norm)
        self.assertEqual(str(getattr(args, "id", "") or ""), "note-1")
        self.assertEqual(str(getattr(args, "append", "") or ""), "new findings")

    def test_append_alias_normalizes(self) -> None:
        norm = memory_cli_mod._normalize_argv(["add-note", "note-1", "hello world"])
        args = memory_cli_mod.build_parser().parse_args(norm)
        self.assertEqual(str(getattr(args, "cmd", "") or ""), "append")
        self.assertEqual(str(getattr(args, "id", "") or ""), "note-1")
        self.assertEqual(str(getattr(args, "append", "") or ""), "hello world")

    def test_recall_alias_parses(self) -> None:
        args = memory_cli_mod.build_parser().parse_args(["get", "hello"])
        self.assertEqual(str(getattr(args, "cmd", "") or ""), "get")

    def test_empty_recall_returns_recent(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            rc1, payload1 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "add",
                    "--title",
                    "Hello",
                    "--body",
                    "Body",
                ]
            )
            self.assertEqual(rc1, 0)
            self.assertTrue(payload1.get("ok"))

            rc2, payload2 = _run_json(["--vault", str(vault), "recall", ""])
            self.assertEqual(rc2, 0)
            self.assertIsInstance(payload2, list)
            self.assertTrue(any(str(x.get("title") or "") == "Hello" for x in payload2))

    def test_forget_requires_filter(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            rc, payload = _run_json(["--vault", str(vault), "forget"])
            self.assertEqual(rc, 2)
            self.assertFalse(payload.get("ok"))
            self.assertEqual(payload.get("code"), "ARG")

    def test_grep_finds_regex_match(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            rc1, payload1 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "--format",
                    "json",
                    "add",
                    "--id",
                    "a",
                    "--title",
                    "Alpha",
                    "--body",
                    "Hello World",
                ]
            )
            self.assertEqual(rc1, 0)
            self.assertTrue(payload1.get("ok"))

            rc2, payload2 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "--format",
                    "json",
                    "grep",
                    "hello\\s+world",
                    "--ignore-case",
                    "--limit",
                    "10",
                ]
            )
            self.assertEqual(rc2, 0)
            self.assertTrue(payload2.get("ok"))
            items = list(payload2.get("items") or [])
            self.assertTrue(any(str(it.get("id") or "") == "a" for it in items))

    def test_link_suggest_returns_related(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            _rca, _pya = _run_json(
                [
                    "--vault",
                    str(vault),
                    "--format",
                    "json",
                    "add",
                    "--id",
                    "retry",
                    "--title",
                    "Retry",
                    "--tag",
                    "infra",
                    "--body",
                    "retry behavior",
                ]
            )
            _rcb, _pyb = _run_json(
                [
                    "--vault",
                    str(vault),
                    "--format",
                    "json",
                    "add",
                    "--id",
                    "backoff",
                    "--title",
                    "Backoff",
                    "--tag",
                    "infra",
                    "--body",
                    "backoff jitter",
                ]
            )

            rc2, payload2 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "--format",
                    "json",
                    "link",
                    "suggest",
                    "retry",
                    "--limit",
                    "10",
                ]
            )
            self.assertEqual(rc2, 0)
            self.assertIsInstance(payload2, list)
            self.assertTrue(
                any(str(it.get("id") or "") == "backoff" for it in payload2)
            )

    def test_link_suggest_accepts_title_reference(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            _run_json(
                [
                    "--vault",
                    str(vault),
                    "--format",
                    "json",
                    "add",
                    "--id",
                    "retry",
                    "--title",
                    "Retry Behavior",
                    "--tag",
                    "infra",
                    "--body",
                    "retry behavior",
                ]
            )
            _run_json(
                [
                    "--vault",
                    str(vault),
                    "--format",
                    "json",
                    "add",
                    "--id",
                    "backoff",
                    "--title",
                    "Backoff",
                    "--tag",
                    "infra",
                    "--body",
                    "backoff jitter",
                ]
            )

            rc2, payload2 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "--format",
                    "json",
                    "link",
                    "suggest",
                    "Retry Behavior",
                    "--limit",
                    "10",
                ]
            )
            self.assertEqual(rc2, 0)
            self.assertIsInstance(payload2, list)
            self.assertTrue(
                any(str(it.get("id") or "") == "backoff" for it in payload2)
            )

    def test_link_validate_positional_id_rewrites(self) -> None:
        norm = memory_cli_mod._normalize_argv(["link", "validate", "abc"])
        args = memory_cli_mod.build_parser().parse_args(norm)
        self.assertEqual(str(getattr(args, "id", "") or ""), "abc")

    def test_body_dash_requires_piped_stdin(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            # init vault so we get to the body '-' validation
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            class _TtyStdin(io.StringIO):
                def isatty(self) -> bool:  # type: ignore[override]
                    return True

            old_stdin = sys.stdin
            try:
                sys.stdin = _TtyStdin("")
                rc, payload = _run_json(
                    ["--vault", str(vault), "add", "Hello", "--body", "-"]
                )
            finally:
                sys.stdin = old_stdin
            self.assertEqual(rc, 2)
            self.assertFalse(payload.get("ok"))
            self.assertEqual(payload.get("code"), "ARG")
            self.assertIn("stdin", str(payload.get("error") or "").lower())

    def test_edit_piped_stdin_requires_explicit_mode(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            rc1, payload1 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "add",
                    "--id",
                    "n",
                    "--title",
                    "N",
                    "--body",
                    "x",
                ]
            )
            self.assertEqual(rc1, 0)
            self.assertTrue(payload1.get("ok"))

            old_stdin = sys.stdin
            try:
                sys.stdin = io.StringIO("new body")
                rc2, payload2 = _run_json(["--vault", str(vault), "edit", "n"])
            finally:
                sys.stdin = old_stdin

            self.assertEqual(rc2, 2)
            self.assertEqual(payload2.get("code"), "ARG")
            self.assertIn("stdin", str(payload2.get("error") or "").lower())

    def test_append_alias_updates_note_body(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            rc1, payload1 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "add",
                    "--id",
                    "n",
                    "--title",
                    "N",
                    "--body",
                    "base",
                ]
            )
            self.assertEqual(rc1, 0)
            self.assertTrue(payload1.get("ok"))

            rc2, payload2 = _run_json(["--vault", str(vault), "add-note", "n", "more"])
            self.assertEqual(rc2, 0)
            self.assertTrue(payload2.get("ok"))

            rc3, text = _run_text(["--vault", str(vault), "show", "n"])
            self.assertEqual(rc3, 0)
            self.assertIn("base", text)
            self.assertIn("more", text)

    def test_show_accepts_title_reference(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            _run_json(
                [
                    "--vault",
                    str(vault),
                    "add",
                    "--id",
                    "python-runtime",
                    "--title",
                    "Python",
                    "--alias",
                    "py",
                    "--body",
                    "initial",
                ]
            )

            rc1, text1 = _run_text(["--vault", str(vault), "show", "Python"])
            self.assertEqual(rc1, 0)
            self.assertIn("python-runtime", text1)

            rc2, payload2 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "edit",
                    "py",
                    "--append",
                    "updated",
                ]
            )
            self.assertEqual(rc2, 0)
            self.assertEqual(str(payload2.get("id") or ""), "python-runtime")

            rc3, text3 = _run_text(["--vault", str(vault), "show", "python-runtime"])
            self.assertEqual(rc3, 0)
            self.assertIn("updated", text3)

    def test_edit_reference_ambiguous_title_errors(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            _run_json(
                [
                    "--vault",
                    str(vault),
                    "add",
                    "--id",
                    "python-a",
                    "--title",
                    "Python",
                    "--body",
                    "a",
                ]
            )
            _run_json(
                [
                    "--vault",
                    str(vault),
                    "add",
                    "--id",
                    "python-b",
                    "--title",
                    "Python",
                    "--body",
                    "b",
                ]
            )

            rc1, payload1 = _run_json(
                ["--vault", str(vault), "edit", "Python", "--append", "x"]
            )
            self.assertEqual(rc1, 2)
            self.assertEqual(str(payload1.get("code") or ""), "ARG")
            self.assertIn("Ambiguous note reference", str(payload1.get("error") or ""))

    def test_around_accepts_title_reference(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / ".loom" / "memory"
            rc0, payload0 = _run_json(["--vault", str(vault), "init"])
            self.assertEqual(rc0, 0)
            self.assertTrue(payload0.get("ok"))

            _run_json(
                [
                    "--vault",
                    str(vault),
                    "add",
                    "--id",
                    "retry",
                    "--title",
                    "Retry Behavior",
                    "--body",
                    "r",
                ]
            )
            _run_json(
                [
                    "--vault",
                    str(vault),
                    "add",
                    "--id",
                    "backoff",
                    "--title",
                    "Backoff",
                    "--body",
                    "b",
                ]
            )

            rc1, payload1 = _run_json(
                [
                    "--vault",
                    str(vault),
                    "around",
                    "Retry Behavior",
                    "--k",
                    "5",
                    "--window-days",
                    "365",
                ]
            )
            self.assertEqual(rc1, 0)
            self.assertTrue(bool(payload1.get("ok")))
            items = list(payload1.get("items") or [])
            self.assertTrue(any(str(it.get("id") or "") == "backoff" for it in items))

    def test_prime_prints_cookbook(self) -> None:
        rc, text = _run_text(["prime"])
        self.assertEqual(rc, 0)
        self.assertIn("Memory Cookbook", text)
        self.assertIn("loom memory add", text)

    def test_prime_json_includes_markdown(self) -> None:
        rc, payload = _run_json(["prime", "--format", "json"])
        self.assertEqual(rc, 0)
        self.assertTrue(payload.get("ok"))
        content = str(payload.get("markdown") or "")
        self.assertIn("Memory Cookbook", content)
