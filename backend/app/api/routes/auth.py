"""
Purpose:
    Account registration and login endpoints for user and organization access.
Inputs:
    Registration/login payloads and authenticated principal context.
Outputs:
    Tokens and current-user profile responses.
Dependencies:
    Auth service, route dependencies, and auth schemas.
TODO Checklist:
    - [ ] Replace demo auth rules with DB-backed identity management.
    - [ ] Add invitation and password reset endpoints later.
"""

from fastapi import APIRouter, Depends

from app.api.deps import get_auth_service, get_current_principal
from app.schemas.auth import CurrentPrincipal, LoginRequest, RegisterRequest, TokenResponse
from app.schemas.user import UserProfileResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserProfileResponse)
async def register(
    payload: RegisterRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> UserProfileResponse:
    """Register a new scaffold user profile."""
    return auth_service.register(payload)


@router.post("/login", response_model=TokenResponse)
async def login(
    payload: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenResponse:
    """Return a demo bearer token for the scaffold UI."""
    return auth_service.login(payload)


@router.get("/me", response_model=UserProfileResponse)
async def me(
    principal: CurrentPrincipal = Depends(get_current_principal),
    auth_service: AuthService = Depends(get_auth_service),
) -> UserProfileResponse:
    """Return the current scaffold user profile."""
    return auth_service.me(principal)
