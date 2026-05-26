import hashlib
from pathlib import Path

from starlette.responses import JSONResponse, Response

from loom_mill.state import MillStateStore


async def get_record_content(request):
    record_id = request.path_params["record_id"]
    store: MillStateStore = request.app.state.store
    snapshot = await store.snapshot()

    record = next((item for item in snapshot.records if item.metadata.id == record_id or item.path == record_id), None)
    if record is None:
        return JSONResponse({"detail": "Record not found"}, status_code=404)

    path = Path(request.app.state.workspace_root) / ".loom" / record.path
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return JSONResponse({"detail": "Record not found"}, status_code=404)

    content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
    if_none_match = getattr(request, "headers", {}).get("if-none-match")
    if if_none_match and if_none_match.strip('"') == content_hash:
        return Response(status_code=304)

    return JSONResponse(
        {"id": record_id, "path": record.path, "content": content, "hash": content_hash},
        headers={"ETag": f'"{content_hash}"'},
    )
