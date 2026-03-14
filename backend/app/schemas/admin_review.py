"""
Purpose:
    Admin review queue schemas for moderated sharing workflows.
Inputs:
    Review queue service outputs and decision submissions.
Outputs:
    Typed moderation request and response payloads.
Dependencies:
    Pydantic models.
TODO Checklist:
    - [ ] Add reviewer identity/audit schemas once platform accounts are implemented.
    - [ ] Split external-upload review from publish review if the rules diverge.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class AdminReviewQueueItem(BaseModel):
    """Review queue entry returned to reviewers."""

    review_id: str
    review_type: str
    status: str
    requested_action: str
    summary: str
    created_at: datetime


class AdminReviewDecisionRequest(BaseModel):
    """Decision payload for admin review queue routes."""

    model_config = ConfigDict(extra="forbid")

    decision: str = Field(..., pattern="^(approve|reject|needs_changes)$")
    reviewer_notes: str | None = Field(default=None, max_length=1000)


class AdminReviewDecisionResponse(BaseModel):
    """Decision response echo."""

    review_id: str
    decision: str
    status: str
