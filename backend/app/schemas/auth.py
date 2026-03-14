"""
Purpose:
    Authentication and principal schemas for the refreshed scaffold.
Inputs:
    Auth route payloads and dependency-resolved principal state.
Outputs:
    Typed request/response models used across backend and tests.
Dependencies:
    Pydantic models and validation helpers.
TODO Checklist:
    - [ ] Add invitation acceptance and password reset schemas later.
    - [ ] Replace demo fields with real registration data once auth is implemented.
"""

from pydantic import BaseModel, ConfigDict, Field


class RegisterRequest(BaseModel):
    """Scaffold registration payload for individual or organization-linked users."""

    model_config = ConfigDict(extra="forbid")

    display_name: str = Field(..., min_length=2, max_length=120)
    email: str
    password: str = Field(..., min_length=8, max_length=128)
    account_type: str = Field(default="user")


class LoginRequest(BaseModel):
    """Scaffold login payload."""

    model_config = ConfigDict(extra="forbid")

    email: str
    password: str = Field(..., min_length=8, max_length=128)


class TokenResponse(BaseModel):
    """Bearer token response used by the scaffold frontend."""

    access_token: str
    token_type: str = "bearer"
    principal_role: str


class CurrentPrincipal(BaseModel):
    """Lightweight current-user context resolved from JWT claims."""

    subject: str
    email: str
    role: str
    organization_id: str | None = None
    workspace_id: str | None = None
