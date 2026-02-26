"""
Purpose:
    Pydantic request/response schemas for authentication endpoints.
Inputs:
    Auth endpoint JSON payloads.
Outputs:
    Typed/validated API contract objects.
Dependencies:
    Pydantic models.
TODO Checklist:
    - [ ] Add stronger email/password validation.
    - [ ] Add refresh token schema when refresh flow is added.
"""

from pydantic import BaseModel, ConfigDict, Field


class LoginRequest(BaseModel):
    """Request body for `POST /api/v1/auth/login`."""

    model_config = ConfigDict(extra="forbid")

    email: str = Field(..., examples=["analyst@org.example"])
    password: str = Field(..., min_length=1)


class TokenResponse(BaseModel):
    """Access token response returned after successful login."""

    access_token: str
    token_type: str = "bearer"


class UserMeResponse(BaseModel):
    """Identity payload for `GET /api/v1/auth/me`."""

    email: str
    role: str = "org_user"
