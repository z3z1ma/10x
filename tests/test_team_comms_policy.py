import contextlib
import unittest
from pathlib import Path
from unittest import mock

from agent_loom.team import core as team
from agent_loom.team.errors import TeamError
from agent_loom.team.run_state import RunPaths


class TestTeamCommsPolicy(unittest.TestCase):
    def test_forbidden_route_worker_to_workers_is_rejected(self) -> None:
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
                "w9": {
                    "worker_id": "w9",
                    "role": "worker",
                    "ticket_id": "tk-9",
                    "pane_id": "%9",
                    "window": "w9",
                    "worktree_key": "tk-9",
                    "retired": False,
                },
            },
            "composition": {
                "spec": {
                    "communication": {
                        "routes": [
                            {"from_role": "worker", "to": ["manager"]},
                            {"from_role": "manager", "to": ["all"]},
                        ]
                    }
                }
            },
        }

        @contextlib.contextmanager
        def fake_locked_run(_paths: RunPaths, *, save: bool = True):
            _ = save
            yield run

        with (
            mock.patch.object(team, "_paths_for", return_value=paths),
            mock.patch.object(team, "locked_run", fake_locked_run),
            mock.patch.object(team, "_inbox_write_and_maybe_nudge"),
            mock.patch.object(team, "write_event"),
            mock.patch.dict(
                "os.environ",
                {"TEAM_ROLE": "worker", "TEAM_WORKER_ID": "w9"},
                clear=False,
            ),
        ):
            with self.assertRaises(TeamError) as ctx:
                team.send(team="CobraKai", target="workers", message="ping")

        self.assertEqual(str(ctx.exception.code), "PERMISSION")
        self.assertIn("Communication route forbidden", str(ctx.exception))

    def test_worker_escalate_resolves_via_policy(self) -> None:
        paths = RunPaths(repo_root=Path("/repo"), team="CobraKai")
        run = {
            "team": "CobraKai",
            "run_id": "1234567890abcdef",
            "session": "team-cobrakai",
            "manager": {"pane_id": "%1"},
            "workers": {
                "w9": {
                    "worker_id": "w9",
                    "role": "worker",
                    "ticket_id": "tk-9",
                    "pane_id": "%9",
                    "window": "w9",
                    "worktree_key": "tk-9",
                    "retired": False,
                }
            },
            "composition": {
                "spec": {
                    "communication": {
                        "escalation": {"target_role": "manager", "timeout_seconds": 60},
                        "routes": [
                            {"from_role": "worker", "to": ["escalate"]},
                            {"from_role": "manager", "to": ["all"]},
                        ],
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
            return ({"id": "m-1"}, target, True, "", {"role": "manager"})

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
                {"TEAM_ROLE": "worker", "TEAM_WORKER_ID": "w9"},
                clear=False,
            ),
        ):
            result = team.send(team="CobraKai", target="escalate", message="need assist")

        self.assertEqual(calls, ["manager"])
        self.assertTrue(result.delivered)
        self.assertEqual(result.target.get("resolved"), 1)

    def test_manager_escalate_is_rejected(self) -> None:
        paths = RunPaths(repo_root=Path("/repo"), team="CobraKai")
        run = {
            "team": "CobraKai",
            "run_id": "1234567890abcdef",
            "session": "team-cobrakai",
            "manager": {"pane_id": "%1"},
            "workers": {},
        }

        @contextlib.contextmanager
        def fake_locked_run(_paths: RunPaths, *, save: bool = True):
            _ = save
            yield run

        with (
            mock.patch.object(team, "_paths_for", return_value=paths),
            mock.patch.object(team, "locked_run", fake_locked_run),
            mock.patch.object(team, "_inbox_write_and_maybe_nudge"),
            mock.patch.object(team, "write_event"),
            mock.patch.dict(
                "os.environ",
                {"TEAM_ROLE": "manager"},
                clear=False,
            ),
        ):
            with self.assertRaises(TeamError) as ctx:
                team.send(team="CobraKai", target="escalate", message="nope")

        self.assertEqual(str(ctx.exception.code), "PERMISSION")
        self.assertIn("Escalation target is only allowed", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
