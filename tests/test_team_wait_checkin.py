import contextlib
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from agent_loom.team import core as team
from agent_loom.team import waiting
from agent_loom.team.run_state import RunPaths


class TestManagerWaitCheckin(unittest.TestCase):
    def test_checkins_after_two_timeouts_with_cooldown(self) -> None:
        paths = RunPaths(repo_root=Path("/repo"), team="CobraKai")
        run = {
            "team": "CobraKai",
            "run_id": "1234567890abcdef",
            "session": "team-cobrakai",
            "workers": {
                "w1": {"worker_id": "w1", "role": "worker", "retired": False},
                "w2": {"worker_id": "w2", "role": "worker", "retired": False},
                "w3": {"worker_id": "w3", "role": "worker", "retired": False},
            },
        }

        @contextlib.contextmanager
        def fake_locked_run(_paths: RunPaths, *, _save: bool = True):
            yield run

        sent: list[str] = []

        def fake_inbox_write_and_maybe_nudge(**kwargs):
            self.assertEqual(str(kwargs.get("sender") or ""), "manager")
            self.assertEqual(str(kwargs.get("kind") or ""), "checkin")
            self.assertTrue(str(kwargs.get("message") or ""))
            target = str(kwargs.get("target") or "")
            sent.append(target)
            return ({"id": "m-1"}, target, True, "", {})

        with (
            mock.patch.object(team, "_paths_for", return_value=paths),
            mock.patch.object(team, "load_run", return_value=run),
            mock.patch.object(team, "locked_run", fake_locked_run),
            mock.patch.object(team, "safe_write_event"),
            mock.patch.object(team, "write_event"),
            mock.patch.object(team, "tmux_available", return_value=True),
            mock.patch.object(team, "tmux_has_session", return_value=True),
            mock.patch.object(team, "tmux_wait_for", return_value=False),
            mock.patch.object(
                team, "_inbox_write_and_maybe_nudge", fake_inbox_write_and_maybe_nudge
            ),
            mock.patch.object(team.time, "time", return_value=1000.0),
            mock.patch.dict(os.environ, {"TMUX": ""}, clear=False),
        ):
            # 1st timeout: record streak only.
            team.wait(team="CobraKai", duration="5m")
            self.assertEqual(sent, [])

            # 2nd consecutive timeout: check in with max_targets=2.
            team.wait(team="CobraKai", duration="5m")
            self.assertEqual(sent, ["w1", "w2"])

            # Two more consecutive timeouts: cooldown blocks w1/w2, so w3 is nudged.
            team.wait(team="CobraKai", duration="5m")
            team.wait(team="CobraKai", duration="5m")
            self.assertEqual(sent, ["w1", "w2", "w3"])

    def test_signal_resets_streak(self) -> None:
        paths = RunPaths(repo_root=Path("/repo"), team="CobraKai")
        run = {
            "team": "CobraKai",
            "run_id": "1234567890abcdef",
            "session": "team-cobrakai",
            "workers": {
                "w1": {"worker_id": "w1", "role": "worker", "retired": False},
            },
            "ops": {"manager": {"checkin": {"timeout_streak": 1}}},
        }

        @contextlib.contextmanager
        def fake_locked_run(_paths: RunPaths, *, _save: bool = True):
            yield run

        sent: list[str] = []

        def fake_inbox_write_and_maybe_nudge(**kwargs):
            sent.append(str(kwargs.get("target") or ""))
            return ({"id": "m-1"}, str(kwargs.get("target") or ""), True, "", {})

        with (
            mock.patch.object(team, "_paths_for", return_value=paths),
            mock.patch.object(team, "load_run", return_value=run),
            mock.patch.object(team, "locked_run", fake_locked_run),
            mock.patch.object(team, "safe_write_event"),
            mock.patch.object(team, "write_event"),
            mock.patch.object(team, "tmux_available", return_value=True),
            mock.patch.object(team, "tmux_has_session", return_value=True),
            mock.patch.object(team, "tmux_wait_for", return_value=True),
            mock.patch.object(
                team, "_inbox_write_and_maybe_nudge", fake_inbox_write_and_maybe_nudge
            ),
            mock.patch.object(team.time, "time", return_value=1000.0),
            mock.patch.dict(os.environ, {"TMUX": ""}, clear=False),
        ):
            res = team.wait(team="CobraKai", duration="5m")
            self.assertEqual(res.wake_reason, "signal")

        self.assertEqual(sent, [])
        streak = (
            ((run.get("ops") or {}).get("manager") or {}).get("checkin") or {}
        ).get("timeout_streak") or 0
        self.assertEqual(int(streak), 0)


class TestWaitingHelpers(unittest.TestCase):
    def test_wait_for_wake_times_out_when_tmux_wait_not_signaled(self) -> None:
        with (
            mock.patch.object(waiting, "tmux_available", return_value=True),
            mock.patch.object(waiting, "tmux_has_session", return_value=True),
            mock.patch.object(waiting, "tmux_wait_for", return_value=False),
        ):
            wake_reason, signaled = waiting.wait_for_wake(
                session="team-cobrakai",
                channel="ch",
                seconds=300,
            )

        self.assertEqual(wake_reason, "timeout")
        self.assertFalse(signaled)

    def test_capture_pane_and_persist_writes_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            paths = RunPaths(repo_root=Path(td), team="CobraKai")
            run = {"team": "CobraKai", "run_id": "run-123"}
            event_calls: list[dict[str, object]] = []

            with (
                mock.patch.object(waiting, "_iso_z", return_value="2026-02-16T12:00:00Z"),
                mock.patch.object(
                    waiting,
                    "tmux_capture",
                    return_value="pane output",
                ),
                mock.patch.object(
                    waiting.uuid,
                    "uuid4",
                    return_value=type("U", (), {"hex": "1234567890abcdef1234567890abcdef"})(),
                ),
                mock.patch.object(
                    waiting,
                    "safe_write_event",
                    side_effect=lambda *args, **kwargs: event_calls.append(kwargs),
                ),
            ):
                cap = waiting.capture_pane_and_persist(
                    paths,
                    run=run,
                    pane_id="%1",
                    target_key="manager",
                    target_meta={"role": "manager", "pane_id": "%1"},
                    pane={"pane_id": "%1"},
                    lines=120,
                    no_join=False,
                    summary="Captured manager lines=120",
                )

            output_file = Path(str(cap.get("output_file") or ""))
            meta_file = Path(str(cap.get("meta_file") or ""))
            self.assertTrue(output_file.exists())
            self.assertTrue(meta_file.exists())
            self.assertEqual(output_file.read_text(encoding="utf-8"), "pane output")

            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            self.assertEqual(meta["id"], "1234567890ab")
            self.assertEqual(meta["team"], "CobraKai")
            self.assertEqual(meta["run_id"], "run-123")
            self.assertEqual(int(meta["lines"]), 120)
            self.assertEqual(int(meta["bytes"]), len("pane output".encode("utf-8")))
            self.assertEqual(len(event_calls), 1)
            self.assertEqual(
                str(event_calls[0].get("event_type") or ""), "capture.saved"
            )


if __name__ == "__main__":
    unittest.main()
