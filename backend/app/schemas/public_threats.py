"""
Purpose:
    Public threats feed schemas for anonymized sharing outputs.
Inputs:
    Public sharing service outputs.
Outputs:
    Typed public list/detail responses with no private linkage fields.
Dependencies:
    Pydantic models and scaffold enums.
TODO Checklist:
    - [ ] Add pagination and search filters once the public feed grows.
    - [ ] Keep this schema identity-safe as the private platform evolves.
"""

from datetime import datetime

from pydantic import BaseModel

from app.utils.enums import ThreatSeverity


class PublicThreatSummary(BaseModel):
    """Public feed item summary."""

    public_report_id: str
    public_slug: str
    title: str
    summary: str
    severity: ThreatSeverity
    indicator_count: int
    source_kind: str
    published_at: datetime


class PublicThreatListResponse(BaseModel):
    """Collection response for public feed endpoints."""

    items: list[PublicThreatSummary]
    next_cursor: str | None = None
