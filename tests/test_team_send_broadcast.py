import contextlib
import unittest
from pathlib import Path
from unittest import mock

from agent_loom.team import core as team
from agent_loom.team.run_state import RunPaths


class TestTeamSendBroadcast(unittest.TestCase):
    def test_send_group_fanout_deduplicates_and_reports_partial_delivery(self) -> None:
        paths = RunPaths(repo_root=Path("/repo"), team="CobraKai")
        run = {
            "team": "CobraKai",
            "run_id": "1234567890abcdef",
            "session": "team-cobrakai",
            "workers": {
                "w1": {
                    "worker_id": "w1",
                    "role": "worker",
                    "ticket_id": "tk-1",
                    "pane_id": "%3",
                    "window": "w1",
                    "worktree_key": "tk-1",
                    "retired": False,
                },
                "w2": {
                    "worker_id": "w2",
                    "role": "worker",
                    "ticket_id": "tk-2",
                    "pane_id": "%4",
                    "window": "w2",
                    "worktree_key": "tk-2",
                    "retired": False,
                },
            },
            "roster": {
                "spec": {
                    "communication": {
                        "broadcast_groups": {
                            "ops": ["workers", "w1"],
                        }
                    }
                }
            },
        }

        @contextlib.contextmanager
        def fake_locked_run(_paths: RunPaths, *, save: bool = True):
            _ = save
            yield run

        calls: list[str] = []

        def fake_inbox_write_and_maybe_nudge(**kwargs):
            target = str(kwargs.get("target") or "")
            calls.append(target)
            if target == "w1":
                return ({"id": "m-1"}, target, True, "", {"worker_id": "w1", "role": "worker"})
            return (
                {"id": "m-2"},
                target,
                False,
                "pane_missing",
                {"worker_id": "w2", "role": "worker"},
            )

        with (
            mock.patch.object(team, "_paths_for", return_value=paths),
            mock.patch.object(team, "locked_run", fake_locked_run),
            mock.patch.object(
                team,
                "_inbox_write_and_maybe_nudge",
                side_effect=fake_inbox_write_and_maybe_nudge,
            ),
            mock.patch.object(team, "write_event"),
            mock.patch.dict(
                "os.environ",
                {"TEAM_ROLE": "manager"},
                clear=False,
            ),
        ):
            result = team.send(
                team="CobraKai",
                target="group:ops",
                message="status check",
            )

        self.assertEqual(calls, ["w1", "w2"])
        self.assertFalse(result.delivered)
        self.assertEqual(result.delivery_reason, "partial_delivery")
        self.assertEqual(len(result.deliveries), 2)
        self.assertEqual(result.inbox.get("count"), 2)
        self.assertIn("loom team status CobraKai --show-dead", result.suggestions)


if __name__ == "__main__":
    unittest.main()
