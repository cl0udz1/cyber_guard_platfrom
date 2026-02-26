"""
Purpose:
    Store scan results for URL/file lookups, including cache keys.
Inputs:
    New scan results from `scan_service`, cached lookups by scan key.
Outputs:
    Persisted safety report data and raw VirusTotal JSON.
Dependencies:
    SQLAlchemy Base and JSON-capable columns.
TODO Checklist:
    - [ ] Add dedicated table for large raw VT payloads if size grows.
    - [ ] Add indexes for reporting queries (status/date).
    - [ ] Add retention policy job for old scan data.
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ScanResult(Base):
    """
    Cached scan record.

    Cache policy:
        - URL scans: `scan_key` = normalized URL.
        - File scans: `scan_key` = SHA-256 hash.
    """

    __tablename__ = "scan_results"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    scan_type: Mapped[str] = mapped_column(String(16), index=True)  # "url" or "file"
    scan_key: Mapped[str] = mapped_column(String(512), index=True, unique=True)
    original_input: Mapped[str | None] = mapped_column(Text, nullable=True)

    status: Mapped[str] = mapped_column(String(16), index=True)  # SAFE | SUSPICIOUS | MALICIOUS
    score: Mapped[int] = mapped_column(Integer, default=0)
    summary: Mapped[str] = mapped_column(Text, default="")
    reasons: Mapped[list[str]] = mapped_column(JSON, default=list)
    raw_vt_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )
