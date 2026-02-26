"""
Purpose:
    Pydantic schemas for scan request/response payloads.
Inputs:
    URL/file scan endpoint payloads.
Outputs:
    API contract-compliant scan results.
Dependencies:
    Pydantic, datetime typing.
TODO Checklist:
    - [ ] Add richer scan reason taxonomy.
    - [ ] Add confidence explanations for score generation.
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

ScanStatus = Literal["SAFE", "SUSPICIOUS", "MALICIOUS"]


class ScanUrlRequest(BaseModel):
    """Request body for `POST /api/v1/scan/url`."""

    model_config = ConfigDict(extra="forbid")
    url: str = Field(..., examples=["https://example.org/login"])


class ScanResponse(BaseModel):
    """Shared response body for URL/file scan endpoints."""

    scan_id: str
    status: ScanStatus
    score: int = Field(..., ge=0, le=100)
    summary: str
    reasons: list[str]
    created_at: datetime
