"""
Purpose:
    Organization model for team-owned accounts and workspaces.
Inputs:
    Organization setup and management workflows.
Outputs:
    Private organization records that own workspaces and memberships.
Dependencies:
    SQLAlchemy Base and model column types.
TODO Checklist:
    - [ ] Add billing/contact fields only if they become relevant to the project scope.
    - [ ] Add organization-level settings for retention and sharing policy later.
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Organization(Base):
    """Private organization account container."""

    __tablename__ = "organizations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(160), unique=True)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    sector: Mapped[str | None] = mapped_column(String(80), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
