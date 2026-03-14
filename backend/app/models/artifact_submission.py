"""
Purpose:
    Private artifact submission model capturing the raw analysis request.
Inputs:
    File/hash/URL/email-signal submissions from users and organizations.
Outputs:
    Persisted submission rows that feed scan jobs and reports.
Dependencies:
    SQLAlchemy Base and model column types.
TODO Checklist:
    - [ ] Replace raw text storage with object storage references for uploaded files.
    - [ ] Add retention and deletion rules per workspace policy.
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ArtifactSubmission(Base):
    """Raw artifact submission record inside the private workspace boundary."""

    __tablename__ = "artifact_submissions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    workspace_id: Mapped[str] = mapped_column(ForeignKey("workspaces.id"), index=True)
    submitted_by_user_id: Mapped[str | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    artifact_type: Mapped[str] = mapped_column(String(32))
    raw_value: Mapped[str] = mapped_column(Text)
    normalized_value: Mapped[str] = mapped_column(Text)
    file_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    sha256: Mapped[str | None] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="queued")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
