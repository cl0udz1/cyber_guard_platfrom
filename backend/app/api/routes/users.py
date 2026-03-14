"""
Purpose:
    User-oriented account endpoints beyond raw authentication.
Inputs:
    Current principal context.
Outputs:
    User profile and membership views for frontend account pages.
Dependencies:
    Auth service and user schemas.
TODO Checklist:
    - [ ] Add profile update endpoint only if it becomes part of project scope.
"""

from fastapi import APIRouter, Depends

from app.api.deps import get_auth_service, get_current_principal
from app.schemas.auth import CurrentPrincipal
from app.schemas.user import MembershipSummary, UserProfileResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserProfileResponse)
async def get_me(
    principal: CurrentPrincipal = Depends(get_current_principal),
    auth_service: AuthService = Depends(get_auth_service),
) -> UserProfileResponse:
    """Return the current profile from the scaffold auth service."""
    return auth_service.me(principal)


@router.get("/me/memberships", response_model=list[MembershipSummary])
async def get_my_memberships(
    principal: CurrentPrincipal = Depends(get_current_principal),
    auth_service: AuthService = Depends(get_auth_service),
) -> list[MembershipSummary]:
    """Return memberships for the current user."""
    return auth_service.me(principal).memberships
