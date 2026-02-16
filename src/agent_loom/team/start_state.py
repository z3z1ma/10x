from __future__ import annotations

import dataclasses
from typing import Any, Dict, Optional

from agent_loom.team.constants import (
    DEFAULT_ARCHITECT_AGENT,
    DEFAULT_INTEGRATOR_AGENT,
    DEFAULT_MANAGER_AGENT,
    DEFAULT_WORKER_AGENT,
    ROLE_ARCHITECT,
    ROLE_INTEGRATOR,
    ROLE_MANAGER,
    ROLE_WORKER,
)
from agent_loom.team.errors import TeamError
from agent_loom.team.merge_queue import _merge_state, merge_branch_for_run
from agent_loom.team.strings import sanitize

HARNESS_NAMES = ("opencode", "claude", "omp", "codex")
ROLE_MODEL_KEYS = (
    ROLE_MANAGER,
    ROLE_WORKER,
    ROLE_ARCHITECT,
    ROLE_INTEGRATOR,
)


def _trim(value: str) -> str:
    return str(value or "").strip()


@dataclasses.dataclass(frozen=True)
class StartModelOverrides:
    default_model: str = ""
    manager_model: str = ""
    architect_model: str = ""
    worker_model: str = ""
    integrator_model: str = ""

    @classmethod
    def from_inputs(
        cls,
        *,
        model: str,
        manager_model: str,
        architect_model: str,
        worker_model: str,
        integrator_model: str,
    ) -> "StartModelOverrides":
        return cls(
            default_model=_trim(model),
            manager_model=_trim(manager_model),
            architect_model=_trim(architect_model),
            worker_model=_trim(worker_model),
            integrator_model=_trim(integrator_model),
        )

    def role_map(self) -> Dict[str, str]:
        role_map: Dict[str, str] = {}
        if self.manager_model:
            role_map[ROLE_MANAGER] = self.manager_model
        if self.worker_model:
            role_map[ROLE_WORKER] = self.worker_model
        if self.architect_model:
            role_map[ROLE_ARCHITECT] = self.architect_model
        if self.integrator_model:
            role_map[ROLE_INTEGRATOR] = self.integrator_model
        return role_map


@dataclasses.dataclass(frozen=True)
class StartMergeOptions:
    target_branch: str = ""
    remote: str = ""
    push: Optional[bool] = None

    @classmethod
    def from_inputs(
        cls,
        *,
        target_branch: str,
        remote: str,
        push: Optional[bool],
    ) -> "StartMergeOptions":
        return cls(
            target_branch=_trim(target_branch),
            remote=_trim(remote),
            push=push,
        )


def build_default_harness_config(*, default_model: str) -> Dict[str, Any]:
    return {
        "model": default_model,
        "models": {role: "" for role in ROLE_MODEL_KEYS},
        "manager_agent": DEFAULT_MANAGER_AGENT,
        "worker_agent": DEFAULT_WORKER_AGENT,
        "architect_agent": DEFAULT_ARCHITECT_AGENT,
        "integrator_agent": DEFAULT_INTEGRATOR_AGENT,
        "bin": "",
    }


def initialize_harness_configs(run: Dict[str, Any], *, default_model: str) -> None:
    for harness in HARNESS_NAMES:
        run[harness] = build_default_harness_config(default_model=default_model)


def normalize_harness_configs(run: Dict[str, Any]) -> None:
    for harness in HARNESS_NAMES:
        raw_cfg = run.get(harness)
        cfg = dict(raw_cfg) if isinstance(raw_cfg, dict) else {}

        if "integrator_agent" not in cfg:
            if "merge_agent" in cfg:
                cfg["integrator_agent"] = cfg.pop("merge_agent")
            else:
                cfg["integrator_agent"] = DEFAULT_INTEGRATOR_AGENT

        cfg.setdefault("manager_agent", DEFAULT_MANAGER_AGENT)
        cfg.setdefault("worker_agent", DEFAULT_WORKER_AGENT)
        cfg.setdefault("architect_agent", DEFAULT_ARCHITECT_AGENT)
        cfg.setdefault("bin", str(cfg.get("bin") or ""))

        raw_models = cfg.get("models")
        models: Dict[str, str] = dict(raw_models) if isinstance(raw_models, dict) else {}
        for role in ROLE_MODEL_KEYS:
            models.setdefault(role, "")
        cfg["models"] = models
        cfg.setdefault("model", str(cfg.get("model") or "").strip())
        run[harness] = cfg


def apply_harness_bin_override(
    run: Dict[str, Any], *, harness: str, bin_override: str
) -> None:
    raw_cfg = run.get(harness)
    cfg = dict(raw_cfg) if isinstance(raw_cfg, dict) else {}
    cfg["bin"] = _trim(bin_override)
    run[harness] = cfg


def apply_model_overrides(
    run: Dict[str, Any], *, harness: str, overrides: StartModelOverrides
) -> None:
    raw_cfg = run.get(harness)
    cfg = dict(raw_cfg) if isinstance(raw_cfg, dict) else {}
    if overrides.default_model:
        cfg["model"] = overrides.default_model

    raw_models = cfg.get("models")
    models: Dict[str, str] = dict(raw_models) if isinstance(raw_models, dict) else {}
    for role, model in overrides.role_map().items():
        models[role] = model
    cfg["models"] = models
    run[harness] = cfg


def apply_max_headcount(run: Dict[str, Any], *, max_headcount: Optional[int]) -> None:
    if max_headcount is None:
        return
    raw_limits = run.get("limits")
    limits: Dict[str, Any] = dict(raw_limits) if isinstance(raw_limits, dict) else {}
    limits["max_headcount"] = max_headcount
    run["limits"] = limits


def apply_merge_options(
    run: Dict[str, Any], *, options: StartMergeOptions
) -> Dict[str, Any]:
    ms = _merge_state(run)
    cfg = dict(ms.get("config") or {})

    if options.target_branch:
        branch = sanitize(options.target_branch, allow=r"a-zA-Z0-9._/-", max_len=120)
        if not branch:
            raise TeamError(
                f"Invalid target branch: {options.target_branch}",
                code="ARG",
                exit_code=2,
            )
        cfg["target_branch"] = branch

    if options.remote:
        remote = sanitize(options.remote, allow=r"a-zA-Z0-9._/-", max_len=80)
        if not remote:
            raise TeamError(
                f"Invalid remote: {options.remote}",
                code="ARG",
                exit_code=2,
            )
        cfg["remote"] = remote

    if options.push is not None:
        cfg["push"] = bool(options.push)
    if options.push is None and bool(cfg.get("push")) is False:
        cfg["push"] = True
    if "push" not in cfg:
        cfg["push"] = True

    ms["config"] = cfg
    run["merge"] = ms
    ms["branch"] = merge_branch_for_run(run)
    run["merge"] = ms
    return cfg


def apply_defaults_from_merge(
    run: Dict[str, Any], *, merge_config: Dict[str, Any], target_branch_override: str
) -> None:
    raw_defaults = run.get("defaults")
    defaults: Dict[str, Any] = {}
    if isinstance(raw_defaults, dict):
        defaults.update(raw_defaults)
    if target_branch_override:
        defaults["base_ref"] = merge_config.get("target_branch")
    defaults.setdefault("base_ref", str(merge_config.get("target_branch") or "main"))
    run["defaults"] = defaults


def migrate_merge_role_workers(run: Dict[str, Any]) -> None:
    if not isinstance(run.get("workers"), dict):
        return
    workers = dict(run.get("workers") or {})
    changed = False
    for worker_id, worker in workers.items():
        if not isinstance(worker, dict):
            continue
        if str(worker.get("role") or "").strip().lower() != "merge":
            continue
        updated_worker = dict(worker)
        updated_worker["role"] = ROLE_INTEGRATOR
        workers[worker_id] = updated_worker
        changed = True
    if changed:
        run["workers"] = workers


def adopt_start_session(
    run: Dict[str, Any], *, session: str, session_provided: bool
) -> str:
    persisted = sanitize(str(run.get("session") or ""), max_len=120)
    if not session_provided and persisted:
        return persisted
    if session_provided:
        run["session"] = session
    return session


__all__ = [
    "HARNESS_NAMES",
    "ROLE_MODEL_KEYS",
    "StartMergeOptions",
    "StartModelOverrides",
    "adopt_start_session",
    "apply_defaults_from_merge",
    "apply_harness_bin_override",
    "apply_max_headcount",
    "apply_merge_options",
    "apply_model_overrides",
    "build_default_harness_config",
    "initialize_harness_configs",
    "migrate_merge_role_workers",
    "normalize_harness_configs",
]
