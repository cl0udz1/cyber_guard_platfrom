"""
Purpose:
    Authentication endpoints for organization area access.
Inputs:
    Login credentials and bearer tokens.
Outputs:
    JWT token (`/login`) and current user identity (`/me`).
Dependencies:
    FastAPI router, auth schemas, security helpers.
TODO Checklist:
    - [ ] Replace demo-password logic with real DB-backed auth.
    - [ ] Add login attempt throttling and audit logging.
    - [ ] Add password reset and org onboarding endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_current_user
from app.core.config import get_settings
from app.core.security import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse, UserMeResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest) -> TokenResponse:
    """
    Minimal login endpoint.

    Skeleton behavior:
        Any email is accepted if password matches `DEMO_ORG_USER_PASSWORD`.
    """
    settings = get_settings()
    if payload.password != settings.demo_org_user_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    token = create_access_token({"sub": payload.email, "role": "org_user"})
    return TokenResponse(access_token=token, token_type="bearer")


@router.get("/me", response_model=UserMeResponse)
async def me(current_user: UserMeResponse = Depends(get_current_user)) -> UserMeResponse:
    """Return caller identity from JWT claims."""
    return current_user
