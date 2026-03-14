"""
Purpose:
    Scan job schemas describing orchestration state and source outputs.
Inputs:
    Scan submission routes and job polling endpoints.
Outputs:
    Typed async scan responses.
Dependencies:
    Pydantic models and scaffold enums.
TODO Checklist:
    - [ ] Add pagination/filter support for job history routes later.
    - [ ] Add richer worker/progress metadata only if the UI really needs it.
"""

from datetime import datetime

from pydantic import BaseModel

from app.schemas.artifact import ArtifactSubmissionRequest, ArtifactSubmissionResponse
from app.utils.enums import AiMode, ScanJobStatus


class SourceHit(BaseModel):
    """Compact per-source enrichment result."""

    source_name: str
    verdict: str
    confidence_score: int
    summary: str


class ScanJobCreateRequest(BaseModel):
    """Create scan job payload."""

    artifact: ArtifactSubmissionRequest
    ai_mode: AiMode = AiMode.LOCAL


class ScanJobResponse(BaseModel):
    """Scan job status response."""

    scan_job_id: str
    status: ScanJobStatus
    artifact: ArtifactSubmissionResponse
    ai_mode: AiMode
    sources: list[SourceHit]
    report_id: str | None = None
    created_at: datetime
    completed_at: datetime | None = None
