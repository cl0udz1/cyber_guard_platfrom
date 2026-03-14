"""
Purpose:
    User and membership schemas for workspace-aware account views.
Inputs:
    User profile and membership data from auth and user routes.
Outputs:
    Typed responses for frontend account/workspace context.
Dependencies:
    Pydantic models.
TODO Checklist:
    - [ ] Add invitation status once org onboarding is implemented.
    - [ ] Add profile editing request schemas if needed later.
"""

from datetime import datetime

from pydantic import BaseModel


class MembershipSummary(BaseModel):
    """Compact membership view for account and workspace pages."""

    organization_id: str
    workspace_id: str | None = None
    role: str


class UserProfileResponse(BaseModel):
    """Current user profile response."""

    id: str
    display_name: str
    email: str
    platform_role: str
    memberships: list[MembershipSummary]
    created_at: datetime
