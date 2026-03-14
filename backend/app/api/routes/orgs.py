"""
Purpose:
    Organization management endpoints for the scaffold contract.
Inputs:
    Organization payloads and authenticated principal context.
Outputs:
    Organization summaries and membership listings.
Dependencies:
    Auth dependencies and org schemas.
TODO Checklist:
    - [ ] Replace placeholder org creation with DB persistence and ownership rules.
    - [ ] Add invitation endpoints after workspace/membership work is in place.
"""

from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends

from app.api.deps import get_current_principal
from app.schemas.auth import CurrentPrincipal
from app.schemas.org import MembershipResponse, OrganizationCreateRequest, OrganizationResponse

router = APIRouter(prefix="/orgs", tags=["organizations"])


@router.post("", response_model=OrganizationResponse)
async def create_org(
    payload: OrganizationCreateRequest,
    _: CurrentPrincipal = Depends(get_current_principal),
) -> OrganizationResponse:
    """Create an organization placeholder response."""
    return OrganizationResponse(
        id=str(uuid4()),
        name=payload.name,
        slug=payload.slug,
        sector=payload.sector,
        created_at=datetime.now(timezone.utc),
    )


@router.get("/{org_id}", response_model=OrganizationResponse)
async def get_org(
    org_id: str,
    principal: CurrentPrincipal = Depends(get_current_principal),
) -> OrganizationResponse:
    """Return a scaffold organization summary."""
    return OrganizationResponse(
        id=org_id,
        name="Cyber Guard Demo Org",
        slug="cyber-guard-demo-org",
        sector="education",
        created_at=datetime.now(timezone.utc),
    )


@router.get("/{org_id}/memberships", response_model=list[MembershipResponse])
async def get_org_memberships(
    org_id: str,
    principal: CurrentPrincipal = Depends(get_current_principal),
) -> list[MembershipResponse]:
    """Return a small placeholder membership list for planning frontend work."""
    return [
        MembershipResponse(user_id=principal.subject, workspace_id=principal.workspace_id, role=principal.role),
        MembershipResponse(user_id="analyst-02", workspace_id=principal.workspace_id, role="analyst"),
    ]
