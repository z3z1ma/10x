from __future__ import annotations

import asyncio
import json
import os
import shlex
import sys
from dataclasses import asdict
from pathlib import Path

from starlette.requests import Request
from starlette.responses import JSONResponse

from loom_mill.state import WorkstationStateChanged
from loom_mill.workstation import FactoryConfig, HarnessConfig, WorkstationState, WorkstationStatus
from loom_mill.workstation.manager import WorkstationManager


DEFAULT_CONFIG = FactoryConfig()


def _workspace_root(request: Request) -> Path:
    return Path(request.app.state.workspace_root)


def _config_path(request: Request) -> Path:
    return _workspace_root(request) / ".mill" / "config.json"


def _ticket_path(request: Request, ticket_id: str) -> Path:
    slug = ticket_id.removeprefix("ticket:")
    return _workspace_root(request) / ".loom" / "tickets" / f"{slug}.md"


def _manager(request: Request) -> WorkstationManager:
    return request.app.state.workstation_manager


def _state_payload(state: WorkstationState) -> dict:
    payload = asdict(state)
    if state.worktree_path is not None:
        payload["worktree_path"] = str(state.worktree_path)
    return payload


def _harness_payload(config: HarnessConfig) -> dict:
    return {
        "command": config.command,
        "args": config.args,
        "env": config.env or {},
        "cwd": config.cwd,
    }


def _config_payload(config: FactoryConfig) -> dict:
    return {
        "max_workstations": config.max_workstations,
        "harness": _harness_payload(config.harness),
    }


def _parse_config(data: dict) -> HarnessConfig:
    command = str(data.get("command") or "").strip()
    if not command:
        raise ValueError("command is required")

    args_value = data.get("args", [])
    if not isinstance(args_value, list):
        raise ValueError("args must be a list")
    args = [str(arg) for arg in args_value]

    env_value = data.get("env") or {}
    if not isinstance(env_value, dict):
        raise ValueError("env must be an object")
    env = {str(key): str(value) for key, value in env_value.items() if str(key).strip()}

    cwd_value = data.get("cwd")
    cwd = str(cwd_value).strip() if cwd_value else None
    return HarnessConfig(command=command, args=args, env=env, cwd=cwd)


def load_factory_config(config_path: Path) -> FactoryConfig:
    if not config_path.exists():
        return DEFAULT_CONFIG
    data = json.loads(config_path.read_text(encoding="utf-8"))
    harness = _parse_config(data.get("harness", data))
    max_workstations = int(data.get("max_workstations", 1))
    if max_workstations < 1:
        raise ValueError("max_workstations must be at least 1")
    return FactoryConfig(max_workstations=max_workstations, harness=harness)


def load_harness_config(config_path: Path) -> HarnessConfig:
    return load_factory_config(config_path).harness


def save_factory_config(config_path: Path, config: FactoryConfig) -> None:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(_config_payload(config), indent=2) + "\n", encoding="utf-8")


def save_harness_config(config_path: Path, config: HarnessConfig) -> None:
    existing = load_factory_config(config_path)
    save_factory_config(config_path, FactoryConfig(max_workstations=existing.max_workstations, harness=config))


async def get_harness_config(request: Request) -> JSONResponse:
    return JSONResponse(_harness_payload(load_harness_config(_config_path(request))))


async def put_harness_config(request: Request) -> JSONResponse:
    try:
        config = _parse_config(await request.json())
    except (json.JSONDecodeError, ValueError) as error:
        return JSONResponse({"error": str(error)}, status_code=400)
    save_harness_config(_config_path(request), config)
    _manager(request).update_config(load_factory_config(_config_path(request)))
    return JSONResponse(_harness_payload(config))


async def get_config(request: Request) -> JSONResponse:
    return JSONResponse(_config_payload(load_factory_config(_config_path(request))))


async def put_config(request: Request) -> JSONResponse:
    try:
        data = await request.json()
        existing = load_factory_config(_config_path(request))
        harness = _parse_config(data["harness"]) if isinstance(data.get("harness"), dict) else existing.harness
        max_workstations = int(data.get("max_workstations", existing.max_workstations))
        if max_workstations < 1:
            raise ValueError("max_workstations must be at least 1")
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        return JSONResponse({"error": str(error)}, status_code=400)
    config = FactoryConfig(max_workstations=max_workstations, harness=harness)
    save_factory_config(_config_path(request), config)
    _manager(request).update_config(config)
    return JSONResponse(_config_payload(config))


async def start_workstation(request: Request) -> JSONResponse:
    data = await request.json()
    ticket_id = str(data.get("ticket_id") or "").removeprefix("ticket:")
    if not ticket_id:
        return JSONResponse({"error": "ticket_id is required"}, status_code=400)

    ticket_path = _ticket_path(request, ticket_id)
    if not ticket_path.exists():
        return JSONResponse({"error": "ticket not found"}, status_code=404)

    try:
        harness = _parse_config(data["harness"]) if isinstance(data.get("harness"), dict) else None
        engine = await _manager(request).start(ticket_path, ticket_id, harness=harness)
    except (RuntimeError, ValueError) as error:
        return JSONResponse({"error": str(error)}, status_code=409)
    state = engine.state
    return JSONResponse(_state_payload(state))


async def list_workstations(request: Request) -> JSONResponse:
    return JSONResponse([_state_payload(state) for state in _manager(request).list()])


async def get_workstation(request: Request) -> JSONResponse:
    engine = _manager(request).get(request.path_params["workstation_id"])
    if engine is None:
        return JSONResponse({"error": "workstation not found"}, status_code=404)
    return JSONResponse(_state_payload(engine.state))


async def delete_workstation(request: Request) -> JSONResponse:
    workstation_id = request.path_params["workstation_id"]
    try:
        state = await _manager(request).stop(workstation_id, remove=True)
    except KeyError:
        return JSONResponse({"error": "workstation not found"}, status_code=404)
    return JSONResponse(_state_payload(state))


async def pause_workstation(request: Request) -> JSONResponse:
    return await _control_workstation(request, request.path_params.get("workstation_id") or request.path_params["ticket_id"], WorkstationStatus.PAUSED)


async def resume_workstation(request: Request) -> JSONResponse:
    workstation_id = request.path_params.get("workstation_id") or request.path_params["ticket_id"]
    engine = _get_engine_by_route_param(request, workstation_id)
    if engine is None:
        return JSONResponse({"error": "workstation not found"}, status_code=404)
    if engine.state.status != WorkstationStatus.PAUSED:
        return JSONResponse({"error": "workstation is not paused"}, status_code=409)

    try:
        state = await _manager(request).resume(engine.workstation_id)
    except RuntimeError as error:
        return JSONResponse({"error": str(error)}, status_code=409)
    return JSONResponse(_state_payload(state))


async def acknowledge_andon(request: Request) -> JSONResponse:
    ticket_id = request.path_params["ticket_id"].removeprefix("ticket:")
    engine = _manager(request).get_by_ticket(ticket_id)
    if engine is None:
        return JSONResponse({"error": "workstation not found"}, status_code=404)

    state = engine.acknowledge_andon()
    await request.app.state.store.replace_workstation_state(engine.workstation_id, state)
    await request.app.state.store.publish(WorkstationStateChanged(workstation_id=engine.workstation_id, workstation=state))
    return JSONResponse(_state_payload(state))


async def stop_workstation(request: Request) -> JSONResponse:
    return await _control_workstation(request, request.path_params.get("workstation_id") or request.path_params["ticket_id"], WorkstationStatus.STOPPED)


async def edit_workstation_ticket(request: Request) -> JSONResponse:
    ticket_id = request.path_params["ticket_id"].removeprefix("ticket:")
    ticket_path = _ticket_path(request, ticket_id)
    if not ticket_path.exists():
        return JSONResponse({"error": "ticket not found"}, status_code=404)

    editor = os.environ.get("EDITOR")
    if editor:
        command = [*shlex.split(editor), str(ticket_path)]
    elif sys.platform == "darwin":
        command = ["open", str(ticket_path)]
    else:
        return JSONResponse({"error": "EDITOR is not configured"}, status_code=409)

    try:
        await asyncio.create_subprocess_exec(
            *command,
            cwd=_workspace_root(request),
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
    except OSError as error:
        return JSONResponse({"error": f"failed to open editor: {error}"}, status_code=500)

    return JSONResponse({"path": str(ticket_path)})


async def _control_workstation(request: Request, ticket_id: str, target_status: WorkstationStatus) -> JSONResponse:
    engine = _get_engine_by_route_param(request, ticket_id)
    if engine is None:
        return JSONResponse({"error": "workstation not found"}, status_code=404)

    try:
        state = await (
            _manager(request).pause(engine.workstation_id)
            if target_status == WorkstationStatus.PAUSED
            else _manager(request).stop(engine.workstation_id, remove=target_status == WorkstationStatus.STOPPED)
        )
    except RuntimeError as error:
        return JSONResponse({"error": str(error)}, status_code=409)
    return JSONResponse(_state_payload(state))


def _get_engine_by_route_param(request: Request, value: str):
    manager = _manager(request)
    return manager.get(value) or manager.get_by_ticket(value)
