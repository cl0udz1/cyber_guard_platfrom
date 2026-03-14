"""
Purpose:
    Workspace request and response schemas.
Inputs:
    Workspace creation, selection, and listing routes.
Outputs:
    Typed workspace payloads for backend/frontend coordination.
Dependencies:
    Pydantic models.
TODO Checklist:
    - [ ] Add retention and sharing-policy settings once those controls are implemented.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class WorkspaceCreateRequest(BaseModel):
    """Create workspace payload."""

    model_config = ConfigDict(extra="forbid")

    organization_id: str
    name: str = Field(..., min_length=2, max_length=160)
    slug: str = Field(..., min_length=2, max_length=160)


class WorkspaceResponse(BaseModel):
    """Workspace summary response."""

    id: str
    organization_id: str
    name: str
    slug: str
    created_at: datetime
