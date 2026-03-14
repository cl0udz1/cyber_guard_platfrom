"""
Purpose:
    Demo-friendly authentication service for the refreshed scaffold.
Inputs:
    Registration/login payloads from auth routes.
Outputs:
    Token responses and lightweight user profile data.
Dependencies:
    Backend settings, security helpers, and user schemas.
TODO Checklist:
    - [ ] Replace this demo service with DB-backed auth and password storage.
    - [ ] Add invitation and organization onboarding workflows.
"""

from datetime import datetime, timezone
from uuid import uuid4

from fastapi import HTTPException, status

from app.core.config import get_settings
from app.core.security import create_access_token
from app.schemas.auth import CurrentPrincipal, LoginRequest, RegisterRequest, TokenResponse
from app.schemas.user import MembershipSummary, UserProfileResponse
from app.utils.constants import DEFAULT_ORGANIZATION_ID, DEFAULT_WORKSPACE_ID


class AuthService:
    """Scaffold auth service backed by simple deterministic demo rules."""

    def __init__(self) -> None:
        self.settings = get_settings()

    def register(self, payload: RegisterRequest) -> UserProfileResponse:
        """Return a fake-but-typed registered user profile."""
        return UserProfileResponse(
            id=str(uuid4()),
            display_name=payload.display_name,
            email=payload.email,
            platform_role="analyst",
            memberships=[
                MembershipSummary(
                    organization_id=DEFAULT_ORGANIZATION_ID,
                    workspace_id=DEFAULT_WORKSPACE_ID,
                    role="analyst",
                )
            ],
            created_at=datetime.now(timezone.utc),
        )

    def login(self, payload: LoginRequest) -> TokenResponse:
        """Validate demo passwords and return a signed token."""
        role = "analyst"
        password_ok = payload.password == self.settings.demo_org_admin_password
        if payload.password == self.settings.demo_platform_admin_password:
            role = "platform_admin"
            password_ok = True
        elif payload.email.startswith("owner@"):
            role = "org_owner"
        elif payload.email.startswith("admin@"):
            role = "org_admin"

        if not password_ok:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid demo credentials for scaffold login.",
            )

        token = create_access_token(
            {
                "sub": payload.email,
                "email": payload.email,
                "role": role,
                "organization_id": DEFAULT_ORGANIZATION_ID,
                "workspace_id": DEFAULT_WORKSPACE_ID,
            }
        )
        return TokenResponse(access_token=token, principal_role=role)

    def me(self, principal: CurrentPrincipal) -> UserProfileResponse:
        """Convert principal context into a frontend-friendly profile response."""
        return UserProfileResponse(
            id="me-scaffold",
            display_name=principal.email.split("@")[0].replace(".", " ").title(),
            email=principal.email,
            platform_role=principal.role,
            memberships=[
                MembershipSummary(
                    organization_id=principal.organization_id or DEFAULT_ORGANIZATION_ID,
                    workspace_id=principal.workspace_id or DEFAULT_WORKSPACE_ID,
                    role=principal.role,
                )
            ],
            created_at=datetime.now(timezone.utc),
        )
