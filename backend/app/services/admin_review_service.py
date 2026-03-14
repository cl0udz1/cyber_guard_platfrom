"""
Purpose:
    Maintain the scaffold moderation queue for publish requests and external uploads.
Inputs:
    Review creation requests and reviewer decisions.
Outputs:
    Queue items and decision echoes used by admin routes.
Dependencies:
    Admin review schemas.
TODO Checklist:
    - [ ] Replace in-memory queue with DB persistence.
    - [ ] Add audit history and reviewer identity tracking.
"""

from datetime import datetime, timezone
from uuid import uuid4

from app.schemas.admin_review import (
    AdminReviewDecisionRequest,
    AdminReviewDecisionResponse,
    AdminReviewQueueItem,
)


class AdminReviewService:
    """In-memory moderation queue placeholder."""

    def __init__(self) -> None:
        self._queue: dict[str, AdminReviewQueueItem] = {}
        self.create_review("external_report_upload", "Review external report upload before public release.")

    def create_review(self, review_type: str, summary: str) -> AdminReviewQueueItem:
        """Add a scaffold queue item and return it."""
        item = AdminReviewQueueItem(
            review_id=str(uuid4()),
            review_type=review_type,
            status="pending",
            requested_action="publish",
            summary=summary,
            created_at=datetime.now(timezone.utc),
        )
        self._queue[item.review_id] = item
        return item

    def list_queue(self) -> list[AdminReviewQueueItem]:
        """Return review items in insertion order."""
        return list(self._queue.values())

    def decide(
        self,
        review_id: str,
        payload: AdminReviewDecisionRequest,
    ) -> AdminReviewDecisionResponse:
        """Apply a decision to a review queue item."""
        item = self._queue.get(review_id)
        if item is None:
            item = self.create_review("missing_reference", "Generated placeholder review item for missing ID.")
        item.status = "approved" if payload.decision == "approve" else "rejected"
        self._queue[item.review_id] = item
        return AdminReviewDecisionResponse(
            review_id=item.review_id,
            decision=payload.decision,
            status=item.status,
        )
