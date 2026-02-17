from __future__ import annotations

from typing import Final

CAPABILITY_ENDPOINTS: Final[list[dict[str, str]]] = [
    {"method": "GET", "path": "/api/v1/health"},
    {"method": "GET", "path": "/api/v1/capabilities"},
    {"method": "GET", "path": "/api/v1/introspect/<subsystem>"},
    {"method": "GET", "path": "/api/v1/tickets"},
    {"method": "GET", "path": "/api/v1/tickets/<id>"},
    {"method": "GET", "path": "/api/v1/tickets/<id>/view"},
    {"method": "GET", "path": "/api/v1/tickets/<id>/dep"},
    {"method": "GET", "path": "/api/v1/tickets/swarm"},
    {"method": "POST", "path": "/api/v1/tickets"},
    {"method": "PATCH", "path": "/api/v1/tickets/<id>"},
    {"method": "GET", "path": "/api/v1/teams"},
    {"method": "GET", "path": "/api/v1/teams/<team>/status"},
    {"method": "GET", "path": "/api/v1/teams/<team>/run"},
    {"method": "GET", "path": "/api/v1/teams/<team>/events"},
    {"method": "GET", "path": "/api/v1/teams/<team>/inbox"},
    {"method": "GET", "path": "/api/v1/teams/<team>/captures"},
    {"method": "GET", "path": "/api/v1/teams/<team>/captures/text"},
    {"method": "GET", "path": "/api/v1/memory/recall"},
    {"method": "GET", "path": "/api/v1/memory/notes/<id>"},
    {"method": "GET", "path": "/api/v1/workspace/meta"},
    {"method": "GET", "path": "/api/v1/workspace/worktrees"},
    {"method": "GET", "path": "/api/v1/workspace/worktree/diff"},
    {"method": "GET", "path": "/api/v1/workspace/components/index"},
    {"method": "GET", "path": "/api/v1/workspace/services/index"},
    {"method": "GET", "path": "/api/v1/compound/skills"},
    {"method": "GET", "path": "/api/v1/compound/skills/<name>"},
    {"method": "GET", "path": "/api/v1/compound/instincts"},
]
