from __future__ import annotations

import argparse
import os
import signal
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from agent_loom.compound.engine import InstinctsUpdateResult, run_instincts_update
from agent_loom.compound.paths import compound_paths


def _pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except Exception:
        return False


def _read_pid(pid_file: Path) -> int:
    if not pid_file.exists():
        return 0
    try:
        return int((pid_file.read_text(encoding="utf-8") or "").strip() or 0)
    except Exception:
        return 0


def _write_pid(pid_file: Path, pid: int) -> None:
    pid_file.parent.mkdir(parents=True, exist_ok=True)
    pid_file.write_text(str(int(pid)) + "\n", encoding="utf-8")


def _poll_seconds() -> float:
    return max(1.0, float(os.environ.get("COMPOUND_OBSERVER_POLL_SECONDS", "5") or 5.0))


@dataclass(frozen=True)
class ObserverStartResult:
    ok: bool
    repo: str
    started: bool
    already_running: bool
    pid: int
    log_file: str


@dataclass(frozen=True)
class ObserverStopResult:
    ok: bool
    repo: str
    stopped: bool
    was_running: bool
    pid: int


@dataclass(frozen=True)
class ObserverStatusResult:
    ok: bool
    repo: str
    running: bool
    pid: int
    pid_file: str
    log_file: str
    nudge_file: str
    nudge_mtime: str


@dataclass(frozen=True)
class ObserverRunOnceResult:
    ok: bool
    repo: str
    ran: bool
    result: dict


def start_observer(*, repo: Path) -> ObserverStartResult:
    paths = compound_paths(repo)
    pid = _read_pid(paths.observer_pid_file)
    if pid and _pid_alive(pid):
        return ObserverStartResult(
            ok=True,
            repo=str(repo),
            started=False,
            already_running=True,
            pid=int(pid),
            log_file=str(paths.observer_log_file),
        )

    if pid and not _pid_alive(pid):
        paths.observer_pid_file.unlink(missing_ok=True)

    paths.runtime_dir.mkdir(parents=True, exist_ok=True)
    log_f = paths.observer_log_file.open("a", encoding="utf-8")
    cmd = [
        sys.executable,
        "-m",
        "agent_loom.compound.observer",
        "run-loop",
        "--repo",
        str(repo),
    ]
    proc = subprocess.Popen(
        cmd,
        cwd=str(repo),
        stdin=subprocess.DEVNULL,
        stdout=log_f,
        stderr=log_f,
        start_new_session=True,
    )
    log_f.close()

    _write_pid(paths.observer_pid_file, int(proc.pid))
    return ObserverStartResult(
        ok=True,
        repo=str(repo),
        started=True,
        already_running=False,
        pid=int(proc.pid),
        log_file=str(paths.observer_log_file),
    )


def stop_observer(*, repo: Path) -> ObserverStopResult:
    paths = compound_paths(repo)
    pid = _read_pid(paths.observer_pid_file)
    if pid <= 0:
        paths.observer_pid_file.unlink(missing_ok=True)
        return ObserverStopResult(
            ok=True,
            repo=str(repo),
            stopped=False,
            was_running=False,
            pid=0,
        )

    was_running = _pid_alive(pid)
    if was_running:
        try:
            os.kill(pid, signal.SIGTERM)
        except Exception:
            pass

        deadline = time.time() + 3.0
        while time.time() < deadline and _pid_alive(pid):
            time.sleep(0.1)

        if _pid_alive(pid):
            try:
                os.kill(pid, signal.SIGKILL)
            except Exception:
                pass

    paths.observer_pid_file.unlink(missing_ok=True)
    return ObserverStopResult(
        ok=True,
        repo=str(repo),
        stopped=was_running,
        was_running=was_running,
        pid=int(pid),
    )


def observer_status(*, repo: Path) -> ObserverStatusResult:
    paths = compound_paths(repo)
    pid = _read_pid(paths.observer_pid_file)
    running = _pid_alive(pid)
    nudge_mtime = ""
    if paths.observer_nudge_file.exists():
        try:
            nudge_mtime = (
                datetime.fromtimestamp(
                    paths.observer_nudge_file.stat().st_mtime, tz=timezone.utc
                )
                .isoformat()
                .replace("+00:00", "Z")
            )
        except Exception:
            nudge_mtime = ""

    return ObserverStatusResult(
        ok=True,
        repo=str(repo),
        running=running,
        pid=int(pid if running else 0),
        pid_file=str(paths.observer_pid_file),
        log_file=str(paths.observer_log_file),
        nudge_file=str(paths.observer_nudge_file),
        nudge_mtime=nudge_mtime,
    )


def run_observer_once(*, repo: Path) -> ObserverRunOnceResult:
    min_new = int(os.environ.get("COMPOUND_INSTINCTS_MIN_NEW_OBSERVATIONS", "12") or 12)
    res: InstinctsUpdateResult = run_instincts_update(
        root=repo,
        auto=True,
        dry_run=False,
        min_new_observations=min_new,
        min_occurrences=3,
        max_candidates=12,
    )
    return ObserverRunOnceResult(
        ok=True,
        repo=str(repo),
        ran=True,
        result=asdict(res),
    )


def run_observer_loop(*, repo: Path) -> int:
    paths = compound_paths(repo)
    current_pid = os.getpid()
    _write_pid(paths.observer_pid_file, current_pid)

    last_size = -1
    last_nudge = -1.0

    while True:
        owner_pid = _read_pid(paths.observer_pid_file)
        if owner_pid != current_pid:
            return 0

        obs_size = 0
        if paths.observations_file.exists():
            try:
                obs_size = int(paths.observations_file.stat().st_size)
            except Exception:
                obs_size = 0

        nudge_mtime = 0.0
        if paths.observer_nudge_file.exists():
            try:
                nudge_mtime = float(paths.observer_nudge_file.stat().st_mtime)
            except Exception:
                nudge_mtime = 0.0

        changed = obs_size != last_size or nudge_mtime != last_nudge
        if changed:
            result = run_observer_once(repo=repo)
            print(asdict(result), flush=True)
            last_size = obs_size
            last_nudge = nudge_mtime

        time.sleep(_poll_seconds())


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="observer")
    sub = p.add_subparsers(dest="cmd", required=True)

    run_loop = sub.add_parser("run-loop")
    run_loop.add_argument("--repo", required=True)

    return p


def main(argv: Optional[list[str]] = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.cmd == "run-loop":
        return run_observer_loop(repo=Path(str(args.repo)).expanduser().resolve())
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
