"""
Purpose:
    Workspace management endpoints for organization-scoped analysis areas.
Inputs:
    Workspace payloads and authenticated principal context.
Outputs:
    Workspace summaries and list responses.
Dependencies:
    Workspace schemas and auth dependencies.
TODO Checklist:
    - [ ] Add DB-backed workspace ownership and permission checks.
    - [ ] Add archive/delete flows only if they become necessary for the team.
"""

from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends

from app.api.deps import get_current_principal
from app.schemas.auth import CurrentPrincipal
from app.schemas.workspace import WorkspaceCreateRequest, WorkspaceResponse

router = APIRouter(prefix="/workspaces", tags=["workspaces"])


@router.post("", response_model=WorkspaceResponse)
async def create_workspace(
    payload: WorkspaceCreateRequest,
    _: CurrentPrincipal = Depends(get_current_principal),
) -> WorkspaceResponse:
    """Create a workspace placeholder response."""
    return WorkspaceResponse(
        id=str(uuid4()),
        organization_id=payload.organization_id,
        name=payload.name,
        slug=payload.slug,
        created_at=datetime.now(timezone.utc),
    )


@router.get("", response_model=list[WorkspaceResponse])
async def list_workspaces(
    principal: CurrentPrincipal = Depends(get_current_principal),
) -> list[WorkspaceResponse]:
    """Return scaffold workspace list for the current principal."""
    return [
        WorkspaceResponse(
            id=principal.workspace_id or "demo-workspace",
            organization_id=principal.organization_id or "demo-org",
            name="Threat Research Workspace",
            slug="threat-research",
            created_at=datetime.now(timezone.utc),
        )
    ]


@router.get("/{workspace_id}", response_model=WorkspaceResponse)
async def get_workspace(
    workspace_id: str,
    principal: CurrentPrincipal = Depends(get_current_principal),
) -> WorkspaceResponse:
    """Return a single workspace placeholder summary."""
    return WorkspaceResponse(
        id=workspace_id,
        organization_id=principal.organization_id or "demo-org",
        name="Threat Research Workspace",
        slug="threat-research",
        created_at=datetime.now(timezone.utc),
    )
