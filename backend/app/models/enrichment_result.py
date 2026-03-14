"""
Purpose:
    Enrichment adapter output model for storing source-by-source findings.
Inputs:
    Threat-intel source queries executed by the scan engine.
Outputs:
    One row per source response per scan job.
Dependencies:
    SQLAlchemy Base and model column types.
TODO Checklist:
    - [ ] Add evidence blob references instead of raw excerpts if payloads become large.
    - [ ] Add source latency/error fields when operational metrics matter.
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class EnrichmentResult(Base):
    """Threat-intel source result for a scan job."""

    __tablename__ = "enrichment_results"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    scan_job_id: Mapped[str] = mapped_column(ForeignKey("scan_jobs.id"), index=True)
    source_name: Mapped[str] = mapped_column(String(64), index=True)
    verdict: Mapped[str] = mapped_column(String(32), default="unknown")
    confidence_score: Mapped[int] = mapped_column(default=0)
    summary: Mapped[str] = mapped_column(Text)
    raw_excerpt: Mapped[dict[str, object]] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
