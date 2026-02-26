"""
Purpose:
    Anonymous IoC storage model for shared threat feed.
Inputs:
    Sanitized IoC payload from `anonymizer.py`.
Outputs:
    Persisted IoC records with NO user identity linkage.
Dependencies:
    SQLAlchemy Base and common column types.
TODO Checklist:
    - [ ] Add DB-level checks for allowed IoC type values.
    - [ ] Add normalization per IoC type (e.g., lowercase domains).
    - [ ] Add data retention and archival strategy.
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Ioc(Base):
    """
    Anonymous IoC table.

    IMPORTANT:
        This table must not contain user/org/ip/email linkage fields.
    """

    __tablename__ = "iocs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    type: Mapped[str] = mapped_column(String(32), index=True)
    value: Mapped[str] = mapped_column(Text, index=True)
    confidence: Mapped[int] = mapped_column(Integer, default=50)
    tags: Mapped[list[str]] = mapped_column(JSON, default=list)
    first_seen: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )
