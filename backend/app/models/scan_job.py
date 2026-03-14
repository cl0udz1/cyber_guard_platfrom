"""
Purpose:
    Async scan job model representing the orchestration lifecycle.
Inputs:
    Artifact submissions and scan orchestration status updates.
Outputs:
    Job rows that can be polled by the frontend and dashboard.
Dependencies:
    SQLAlchemy Base and model column types.
TODO Checklist:
    - [ ] Add retry metadata and worker assignment fields if background jobs are implemented.
    - [ ] Add progress percentages only if the UI really needs them.
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ScanJob(Base):
    """Asynchronous scan orchestration record."""

    __tablename__ = "scan_jobs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    artifact_submission_id: Mapped[str] = mapped_column(
        ForeignKey("artifact_submissions.id"),
        index=True,
    )
    workspace_id: Mapped[str] = mapped_column(ForeignKey("workspaces.id"), index=True)
    status: Mapped[str] = mapped_column(String(32), default="queued")
    ai_mode: Mapped[str] = mapped_column(String(16), default="local")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
