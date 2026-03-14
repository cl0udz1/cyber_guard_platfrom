"""
Purpose:
    Organization and membership contract shapes for scaffold planning.
Inputs:
    Organization creation/update flows and membership listings.
Outputs:
    Typed org route payloads.
Dependencies:
    Pydantic models.
TODO Checklist:
    - [ ] Add invitation requests and acceptance flow in a later phase.
    - [ ] Add organization settings schemas if governance rules become configurable.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class OrganizationCreateRequest(BaseModel):
    """Create organization payload."""

    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=2, max_length=160)
    slug: str = Field(..., min_length=2, max_length=160)
    sector: str | None = Field(default=None, max_length=80)


class OrganizationResponse(BaseModel):
    """Organization summary response."""

    id: str
    name: str
    slug: str
    sector: str | None = None
    created_at: datetime


class MembershipResponse(BaseModel):
    """Membership summary for organization views."""

    user_id: str
    workspace_id: str | None = None
    role: str
