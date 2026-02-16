import unittest
from unittest import mock

from agent_loom.team import targets
from agent_loom.team.errors import TeamError


class TestTeamTargets(unittest.TestCase):
    def test_resolve_target_by_worktree_key(self) -> None:
        run = {
            "manager": {"pane_id": "%1"},
            "workers": {
                "integrator": {
                    "worker_id": "integrator",
                    "role": "integrator",
                    "ticket_id": "",
                    "pane_id": "%71",
                    "window": "integrator",
                    "worktree_key": "merge-queue",
                    "retired": False,
                }
            },
        }

        pane_id, meta = targets._resolve_target(run, "merge-queue")
        self.assertEqual(pane_id, "%71")
        self.assertEqual(str(meta.get("worker_id") or ""), "integrator")

    def test_resolve_target_by_window_name(self) -> None:
        run = {
            "manager": {"pane_id": "%1"},
            "workers": {
                "w1": {
                    "worker_id": "w1",
                    "role": "worker",
                    "ticket_id": "tk-1",
                    "pane_id": "%3",
                    "window": "alpha",
                    "worktree_key": "tk-1",
                    "retired": False,
                }
            },
        }

        pane_id, meta = targets._resolve_target(run, "alpha")
        self.assertEqual(pane_id, "%3")
        self.assertEqual(str(meta.get("worker_id") or ""), "w1")

    def test_worktree_key_ignores_retired_workers(self) -> None:
        run = {
            "manager": {"pane_id": "%1"},
            "workers": {
                "w1": {
                    "worker_id": "w1",
                    "role": "worker",
                    "ticket_id": "",
                    "pane_id": "%2",
                    "window": "alpha",
                    "worktree_key": "merge-queue",
                    "retired": True,
                },
                "w2": {
                    "worker_id": "w2",
                    "role": "worker",
                    "ticket_id": "",
                    "pane_id": "%3",
                    "window": "beta",
                    "worktree_key": "merge-queue",
                    "retired": False,
                },
            },
        }

        pane_id, meta = targets._resolve_target(run, "merge-queue")
        self.assertEqual(pane_id, "%3")
        self.assertEqual(str(meta.get("worker_id") or ""), "w2")

    def test_ambiguous_worktree_key_raises(self) -> None:
        run = {
            "manager": {"pane_id": "%1"},
            "workers": {
                "w1": {
                    "worker_id": "w1",
                    "role": "worker",
                    "ticket_id": "",
                    "pane_id": "%2",
                    "window": "alpha",
                    "worktree_key": "merge-queue",
                    "retired": False,
                },
                "w2": {
                    "worker_id": "w2",
                    "role": "worker",
                    "ticket_id": "",
                    "pane_id": "%3",
                    "window": "beta",
                    "worktree_key": "merge-queue",
                    "retired": False,
                },
            },
        }

        with self.assertRaises(TeamError) as ctx:
            targets._resolve_target(run, "merge-queue")
        self.assertEqual(str(getattr(ctx.exception, "code", "")), "AMBIGUOUS")

    def test_best_effort_tmux_nudge_uses_ctrl_enter_for_omp(self) -> None:
        run = {"harness": "omp", "manager": {"pane_id": "%1"}, "workers": {}}

        with (
            mock.patch.object(targets, "tmux_available", return_value=True),
            mock.patch.object(targets, "tmux_has_session", return_value=True),
            mock.patch.object(targets, "_resolve_target", return_value=("%3", {"pane_id": "%3"})),
            mock.patch.object(
                targets,
                "tmux_list_panes",
                return_value={"%3": {"current_command": "omp", "dead": "0"}},
            ),
            mock.patch.object(targets, "tmux_send_text") as send_text,
        ):
            ok, reason, _meta = targets._best_effort_tmux_nudge(
                run=run,
                session="team-cobra",
                target="manager",
                line="TEAM inbox id=abc",
                force=False,
            )

        self.assertTrue(ok)
        self.assertEqual(reason, "")
        send_text.assert_called_once_with("%3", "TEAM inbox id=abc", enter=True, ctrl_enter=True)

    def test_best_effort_tmux_nudge_uses_enter_for_non_omp(self) -> None:
        run = {"harness": "opencode", "manager": {"pane_id": "%1"}, "workers": {}}

        with (
            mock.patch.object(targets, "tmux_available", return_value=True),
            mock.patch.object(targets, "tmux_has_session", return_value=True),
            mock.patch.object(targets, "_resolve_target", return_value=("%3", {"pane_id": "%3"})),
            mock.patch.object(
                targets,
                "tmux_list_panes",
                return_value={"%3": {"current_command": "opencode", "dead": "0"}},
            ),
            mock.patch.object(targets, "tmux_send_text") as send_text,
        ):
            ok, reason, _meta = targets._best_effort_tmux_nudge(
                run=run,
                session="team-cobra",
                target="manager",
                line="TEAM inbox id=abc",
                force=False,
            )

        self.assertTrue(ok)
        self.assertEqual(reason, "")
        send_text.assert_called_once_with("%3", "TEAM inbox id=abc", enter=True, ctrl_enter=False)

    def test_resolve_targets_workers_group(self) -> None:
        run = {
            "manager": {"pane_id": "%1"},
            "workers": {
                "w1": {
                    "worker_id": "w1",
                    "role": "worker",
                    "ticket_id": "tk-1",
                    "pane_id": "%3",
                    "window": "alpha",
                    "worktree_key": "tk-1",
                    "retired": False,
                },
                "w2": {
                    "worker_id": "w2",
                    "role": "worker",
                    "ticket_id": "tk-2",
                    "pane_id": "%4",
                    "window": "beta",
                    "worktree_key": "tk-2",
                    "retired": False,
                },
                "w3": {
                    "worker_id": "w3",
                    "role": "investigator",
                    "ticket_id": "tk-3",
                    "pane_id": "%5",
                    "window": "gamma",
                    "worktree_key": "tk-3",
                    "retired": False,
                },
            },
        }

        resolved = targets._resolve_targets(run, "workers")
        self.assertEqual([str(x.get("worker_id") or "") for x in resolved], ["w1", "w2"])

    def test_resolve_targets_policy_group(self) -> None:
        run = {
            "manager": {"pane_id": "%1"},
            "workers": {
                "w1": {
                    "worker_id": "w1",
                    "role": "worker",
                    "ticket_id": "tk-1",
                    "pane_id": "%3",
                    "window": "alpha",
                    "worktree_key": "tk-1",
                    "retired": False,
                },
                "w2": {
                    "worker_id": "w2",
                    "role": "integrator",
                    "ticket_id": "",
                    "pane_id": "%7",
                    "window": "integrator",
                    "worktree_key": "merge-queue",
                    "retired": False,
                },
            },
            "composition": {
                "spec": {
                    "communication": {
                        "broadcast_groups": {
                            "ops": ["workers", "integrators"],
                        }
                    }
                }
            },
        }

        resolved = targets._resolve_targets(run, "group:ops")
        self.assertEqual([str(x.get("worker_id") or "") for x in resolved], ["w1", "w2"])

    def test_resolve_targets_unknown_policy_group_raises(self) -> None:
        run = {
            "manager": {"pane_id": "%1"},
            "workers": {},
            "composition": {"spec": {"communication": {"broadcast_groups": {"ops": ["manager"]}}}},
        }

        with self.assertRaises(TeamError) as ctx:
            targets._resolve_targets(run, "group:missing")
        self.assertIn("Unknown broadcast group", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
