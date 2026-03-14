"""
Purpose:
    Moderation endpoints for public sharing governance.
Inputs:
    Review queue queries and reviewer decisions.
Outputs:
    Queue state and decision acknowledgements.
Dependencies:
    Admin review service and admin auth dependency.
TODO Checklist:
    - [ ] Add reviewer notes history and audit logs.
    - [ ] Separate external-upload rules from publish-review rules if they diverge.
"""

from fastapi import APIRouter, Depends

from app.api.deps import get_admin_review_service, require_admin
from app.schemas.admin_review import (
    AdminReviewDecisionRequest,
    AdminReviewDecisionResponse,
    AdminReviewQueueItem,
)
from app.schemas.auth import CurrentPrincipal
from app.services.admin_review_service import AdminReviewService

router = APIRouter(prefix="/admin-reviews", tags=["admin-reviews"])


@router.get("/queue", response_model=list[AdminReviewQueueItem])
async def get_review_queue(
    _: CurrentPrincipal = Depends(require_admin),
    admin_review_service: AdminReviewService = Depends(get_admin_review_service),
) -> list[AdminReviewQueueItem]:
    """Return the current moderation queue."""
    return admin_review_service.list_queue()


@router.post("/{review_id}/decision", response_model=AdminReviewDecisionResponse)
async def submit_review_decision(
    review_id: str,
    payload: AdminReviewDecisionRequest,
    _: CurrentPrincipal = Depends(require_admin),
    admin_review_service: AdminReviewService = Depends(get_admin_review_service),
) -> AdminReviewDecisionResponse:
    """Apply a reviewer decision to a queued item."""
    return admin_review_service.decide(review_id, payload)
