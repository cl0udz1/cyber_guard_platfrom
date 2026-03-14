"""
Purpose:
    Private configuration model for workspace/organization integration settings.
Inputs:
    Admin-managed API keys or source enablement settings.
Outputs:
    Stored adapter configuration rows for future real enrichment clients.
Dependencies:
    SQLAlchemy Base and model column types.
TODO Checklist:
    - [ ] Move secrets out of the main DB before production.
    - [ ] Add per-source scopes and key rotation metadata if implemented.
"""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ApiClientConfig(Base):
    """Private source configuration per organization or workspace."""

    __tablename__ = "api_client_configs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), index=True)
    workspace_id: Mapped[str | None] = mapped_column(ForeignKey("workspaces.id"), nullable=True)
    provider_name: Mapped[str] = mapped_column(String(64))
    mode: Mapped[str] = mapped_column(String(16), default="shared")
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
