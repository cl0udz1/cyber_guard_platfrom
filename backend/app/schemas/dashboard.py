"""
Purpose:
    Response schemas for dashboard analytics endpoints.
Inputs:
    Aggregated DB query results.
Outputs:
    Typed dashboard summary JSON payload.
Dependencies:
    Pydantic models, scan/ioc schema concepts.
TODO Checklist:
    - [ ] Add trend buckets by day/week.
    - [ ] Add top tags and top repeated IoCs.
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from app.schemas.ioc import IocPublicRecord

ScanStatus = Literal["SAFE", "SUSPICIOUS", "MALICIOUS"]


class DashboardRecentScan(BaseModel):
    """Compact scan shape used in dashboard recent list."""

    scan_id: str
    status: ScanStatus
    score: int
    summary: str
    created_at: datetime


class DashboardSummaryResponse(BaseModel):
    """Response model for `GET /api/v1/dashboard/summary`."""

    counts_by_type: dict[str, int]
    recent_iocs: list[IocPublicRecord]
    recent_scans: list[DashboardRecentScan]
