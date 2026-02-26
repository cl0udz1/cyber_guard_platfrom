"""
Purpose:
    Organization user model for authenticated portal features.
Inputs:
    Insert/update operations from auth/user management services.
Outputs:
    Persisted user rows used by future real authentication flow.
Dependencies:
    SQLAlchemy Base and model column types.
TODO Checklist:
    - [ ] Add registration/invitation flow for organization admins.
    - [ ] Add password reset metadata and audit fields.
    - [ ] Add role enum table/permission mapping if RBAC grows.
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class User(Base):
    """
    Basic user table.

    NOTE:
        IoC submissions intentionally must NOT reference this table to preserve
        "Disconnect by Design" anonymity rules.
    """

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(32), default="org_user")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
