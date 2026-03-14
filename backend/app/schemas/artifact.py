"""
Purpose:
    Artifact submission schemas covering file/hash/URL/email-signal inputs.
Inputs:
    Scan submission requests from authenticated users or organizations.
Outputs:
    Typed artifact payloads used by scan job routes and services.
Dependencies:
    Pydantic models and scaffold enums.
TODO Checklist:
    - [ ] Split file upload metadata from pasted values if multipart support is added.
    - [ ] Add stronger validation per artifact type once validators are implemented.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.utils.enums import ArtifactType


class ArtifactSubmissionRequest(BaseModel):
    """Create a private artifact submission."""

    model_config = ConfigDict(extra="forbid")

    workspace_id: str
    artifact_type: ArtifactType
    artifact_value: str = Field(..., min_length=2, max_length=10000)
    file_name: str | None = Field(default=None, max_length=255)
    notes: str | None = Field(default=None, max_length=500)


class ArtifactSubmissionResponse(BaseModel):
    """Echo of the accepted artifact submission."""

    submission_id: str
    workspace_id: str
    artifact_type: ArtifactType
    normalized_value: str
    created_at: datetime
