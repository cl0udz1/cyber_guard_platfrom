"""
Purpose:
    Guest scan endpoints for URL/file safety analysis.
Inputs:
    URL JSON body or uploaded file multipart payload.
Outputs:
    Safety report object with status, score, reasons, and timestamp.
Dependencies:
    Scan service, validators, SQLAlchemy session dependency.
TODO Checklist:
    - [ ] Add scan history pagination/search endpoint.
    - [ ] Add per-IP rate limiting for abuse protection.
    - [ ] Add asynchronous job queue for large file processing.
"""

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_scan_service
from app.core.config import get_settings
from app.models.scan_result import ScanResult
from app.schemas.scan import ScanResponse, ScanUrlRequest
from app.services.scan_service import ScanService
from app.utils.validators import normalize_url

router = APIRouter(prefix="/scan", tags=["scan"])


def _to_scan_response(row: ScanResult) -> ScanResponse:
    """Map ORM row into API response model."""
    return ScanResponse(
        scan_id=row.id,
        status=row.status,  # type: ignore[arg-type]
        score=row.score,
        summary=row.summary,
        reasons=row.reasons or [],
        created_at=row.created_at,
    )


@router.post("/url", response_model=ScanResponse)
async def scan_url(
    payload: ScanUrlRequest,
    db: Session = Depends(get_db),
    service: ScanService = Depends(get_scan_service),
) -> ScanResponse:
    """
    Scan a URL and return cached/new report.

    Caching:
        Uses normalized URL string as cache key.
    """
    normalized = normalize_url(payload.url)
    result = await service.scan_url(db, original_url=payload.url, normalized_url=normalized)
    return _to_scan_response(result)


@router.post("/file", response_model=ScanResponse)
async def scan_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    service: ScanService = Depends(get_scan_service),
) -> ScanResponse:
    """
    Scan file by hash lookup only.

    Critical safety rule:
        This endpoint never executes uploaded files.
    """
    settings = get_settings()
    contents = await file.read()
    if not contents:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty.",
        )

    max_size_bytes = settings.max_upload_size_mb * 1024 * 1024
    if len(contents) > max_size_bytes:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File exceeds {settings.max_upload_size_mb} MB limit.",
        )

    result = await service.scan_file(
        db=db,
        filename=file.filename or "uploaded_file",
        file_bytes=contents,
    )
    return _to_scan_response(result)


@router.get("/{scan_id}", response_model=ScanResponse)
async def get_scan_result(scan_id: str, db: Session = Depends(get_db)) -> ScanResponse:
    """
    Optional/recommended endpoint for fetching a prior scan by ID.

    TODO:
        - Add authorization if scan history becomes user-scoped in future.
    """
    row = db.execute(select(ScanResult).where(ScanResult.id == scan_id)).scalar_one_or_none()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scan not found.")
    return _to_scan_response(row)
