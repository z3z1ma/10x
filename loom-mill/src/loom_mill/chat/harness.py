from __future__ import annotations

import asyncio
import os
import shlex
from collections.abc import Awaitable, Callable


async def run_harness(
    command: str,
    prompt: str,
    session_id: str,
    broadcast_fn: Callable[[dict], Awaitable[None]],
    *,
    user_message: str | None = None,
) -> str:
    """Spawn harness, stream output via broadcast_fn, and return the full response."""
    args = shlex.split(command)
    if not args:
        raise ValueError("harness command is required")

    # Special echo test mode - no subprocess needed
    if args[0] == "echo":
        response = user_message or "No message provided"
        await broadcast_fn(
            {"event": "chat_stream", "data": {"session_id": session_id, "delta": response, "done": False}}
        )
        await broadcast_fn(
            {
                "event": "chat_complete",
                "data": {"session_id": session_id, "message": {"role": "assistant", "content": response}},
            }
        )
        return response

    # For all real harness commands: pipe prompt to stdin, read stdout
    proc = await asyncio.create_subprocess_exec(
        *args,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=os.getcwd(),
    )

    # Write prompt to stdin and close
    assert proc.stdin is not None
    proc.stdin.write(prompt.encode("utf-8"))
    await proc.stdin.drain()
    proc.stdin.close()

    # Stream stdout line by line
    full_response: list[str] = []
    assert proc.stdout is not None
    async for line in proc.stdout:
        text = line.decode("utf-8", errors="replace")
        full_response.append(text)
        await broadcast_fn(
            {
                "event": "chat_stream",
                "data": {"session_id": session_id, "delta": text, "done": False},
            }
        )

    # Collect stderr and wait for exit
    stderr_data = b""
    if proc.stderr is not None:
        stderr_data = await proc.stderr.read()
    await proc.wait()

    if proc.returncode != 0:
        stderr_text = stderr_data.decode("utf-8", errors="replace").strip()
        error_msg = stderr_text[:300] if stderr_text else f"Harness exited with code {proc.returncode}"
        await broadcast_fn({"event": "chat_error", "data": {"session_id": session_id, "error": error_msg}})
        raise RuntimeError(error_msg)

    response_text = "".join(full_response)
    await broadcast_fn(
        {
            "event": "chat_complete",
            "data": {"session_id": session_id, "message": {"role": "assistant", "content": response_text}},
        }
    )
    return response_text
