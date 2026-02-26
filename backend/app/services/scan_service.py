"""
Purpose:
    Scan orchestration service: cache lookup, VT query, report persistence.
Inputs:
    URL/file scan requests from API endpoints plus DB session.
Outputs:
    `ScanResult` ORM rows representing cached or newly created scan reports.
Dependencies:
    Scan model, VT client, report builder, hashing utility.
TODO Checklist:
    - [ ] Add TTL policy for cache freshness.
    - [ ] Store intermediate analysis IDs for async VT polling.
    - [ ] Add richer error mapping for frontend UX messages.
"""

from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.scan_result import ScanResult
from app.services.report_service import build_safety_report
from app.services.virustotal_client import VirusTotalClient
from app.utils.hashing import sha256_bytes


class ScanService:
    """Encapsulates scan/caching behavior for both URL and file flows."""

    def __init__(self, vt_client: VirusTotalClient) -> None:
        self.vt_client = vt_client

    async def scan_url(self, db: Session, original_url: str, normalized_url: str) -> ScanResult:
        """
        Scan a URL with cache-by-normalized-URL policy.

        Returns existing cached row if found.
        """
        existing = db.execute(
            select(ScanResult).where(
                ScanResult.scan_type == "url",
                ScanResult.scan_key == normalized_url,
            )
        ).scalar_one_or_none()
        if existing is not None:
            return existing

        raw_vt = await self.vt_client.scan_url(normalized_url)
        scan_id = str(uuid4())
        report = build_safety_report(scan_id=scan_id, vt_payload=raw_vt)

        row = ScanResult(
            id=scan_id,
            scan_type="url",
            scan_key=normalized_url,
            original_input=original_url,
            status=report["status"],
            score=report["score"],
            summary=report["summary"],
            reasons=report["reasons"],
            raw_vt_json=raw_vt,
        )
        db.add(row)
        db.commit()
        db.refresh(row)
        return row

    async def scan_file(self, db: Session, filename: str, file_bytes: bytes) -> ScanResult:
        """
        Scan a file by SHA-256 hash lookup with caching.

        Critical safety rule:
            Never execute uploaded file content.
        """
        file_hash = sha256_bytes(file_bytes)

        existing = db.execute(
            select(ScanResult).where(
                ScanResult.scan_type == "file",
                ScanResult.scan_key == file_hash,
            )
        ).scalar_one_or_none()
        if existing is not None:
            return existing

        raw_vt = await self.vt_client.scan_file_hash(file_hash)
        scan_id = str(uuid4())
        report = build_safety_report(scan_id=scan_id, vt_payload=raw_vt)

        row = ScanResult(
            id=scan_id,
            scan_type="file",
            scan_key=file_hash,
            original_input=filename,
            status=report["status"],
            score=report["score"],
            summary=report["summary"],
            reasons=report["reasons"],
            raw_vt_json=raw_vt,
        )
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
