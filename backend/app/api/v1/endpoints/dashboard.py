"""
Purpose:
    Dashboard endpoints for threat feed overview and trends starter data.
Inputs:
    Authenticated request context and DB aggregation queries.
Outputs:
    Counts by IoC type, recent IoCs, and recent scans.
Dependencies:
    SQLAlchemy aggregation, auth dependency, dashboard schemas.
TODO Checklist:
    - [ ] Add date-range query parameters for trend filtering.
    - [ ] Add graph-ready daily buckets.
    - [ ] Add pagination for recent lists when data grows.
"""

from fastapi import APIRouter, Depends
from sqlalchemy import desc, func, select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.ioc import Ioc
from app.models.scan_result import ScanResult
from app.schemas.auth import UserMeResponse
from app.schemas.dashboard import DashboardRecentScan, DashboardSummaryResponse
from app.schemas.ioc import IocPublicRecord

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary", response_model=DashboardSummaryResponse)
async def get_dashboard_summary(
    db: Session = Depends(get_db),
    current_user: UserMeResponse = Depends(get_current_user),
) -> DashboardSummaryResponse:
    """
    Return lightweight dashboard summary.

    TODO:
        - Add role checks if different org roles get different visibility.
    """
    _ = current_user

    count_rows = db.execute(
        select(Ioc.type, func.count(Ioc.id)).group_by(Ioc.type)
    ).all()
    counts_by_type = {ioc_type: int(total) for ioc_type, total in count_rows}

    recent_ioc_rows = db.execute(
        select(Ioc).order_by(desc(Ioc.created_at)).limit(10)
    ).scalars()
    recent_iocs = [
        IocPublicRecord(
            ioc_id=row.id,
            type=row.type,  # type: ignore[arg-type]
            value=row.value,
            confidence=row.confidence,
            tags=row.tags or [],
            first_seen=row.first_seen,
            created_at=row.created_at,
        )
        for row in recent_ioc_rows
    ]

    recent_scan_rows = db.execute(
        select(ScanResult).order_by(desc(ScanResult.created_at)).limit(10)
    ).scalars()
    recent_scans = [
        DashboardRecentScan(
            scan_id=row.id,
            status=row.status,  # type: ignore[arg-type]
            score=row.score,
            summary=row.summary,
            created_at=row.created_at,
        )
        for row in recent_scan_rows
    ]

    return DashboardSummaryResponse(
        counts_by_type=counts_by_type,
        recent_iocs=recent_iocs,
        recent_scans=recent_scans,
    )
