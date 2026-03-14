"""
Purpose:
    Threat report and sharing workflow schemas.
Inputs:
    Report detail routes, publish requests, and external upload requests.
Outputs:
    Typed report payloads for private and public flows.
Dependencies:
    Pydantic models and scaffold enums.
TODO Checklist:
    - [ ] Add versioning or analyst-notes schemas if report editing becomes part of scope.
    - [ ] Add external upload attachment metadata if file ingestion is implemented.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.utils.enums import PublicShareStatus, ThreatSeverity


class ThreatReportResponse(BaseModel):
    """Private report detail response."""

    report_id: str
    scan_job_id: str
    severity: ThreatSeverity
    confidence: int
    executive_summary: str
    recommended_actions: list[str]
    source_summary: list[str]
    ai_summary: str | None = None
    publish_status: PublicShareStatus
    created_at: datetime


class PublishRequest(BaseModel):
    """Request to publish a private report to the public feed."""

    model_config = ConfigDict(extra="forbid")

    include_in_public_feed: bool = True
    notes_for_reviewer: str | None = Field(default=None, max_length=500)


class ExternalReportUploadRequest(BaseModel):
    """Organization-provided external report upload placeholder payload."""

    model_config = ConfigDict(extra="forbid")

    organization_id: str
    title: str = Field(..., min_length=4, max_length=180)
    summary: str = Field(..., min_length=20, max_length=5000)
    source_url: str | None = Field(default=None, max_length=500)
    requested_visibility: str = Field(default="public_after_review")
