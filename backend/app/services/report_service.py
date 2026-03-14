"""
Purpose:
    Build and store private threat report placeholders from completed scan jobs.
Inputs:
    Scan job metadata, enrichment hits, and optional AI summary text.
Outputs:
    Typed threat report responses retrievable by report ID.
Dependencies:
    Report schemas and threat severity rules.
TODO Checklist:
    - [ ] Replace in-memory storage with DB persistence.
    - [ ] Add section versioning only if analyst editing becomes part of scope.
"""

from datetime import datetime, timezone
from uuid import uuid4

from app.schemas.artifact import ArtifactSubmissionResponse
from app.schemas.report import ThreatReportResponse
from app.schemas.scan import SourceHit
from app.utils.enums import PublicShareStatus, ThreatSeverity


class ReportService:
    """Create and retain scaffold threat reports in memory."""

    def __init__(self) -> None:
        self._reports: dict[str, ThreatReportResponse] = {}

    async def build_report(
        self,
        scan_job_id: str,
        artifact: ArtifactSubmissionResponse,
        source_hits: list[SourceHit],
        ai_summary: str | None,
    ) -> ThreatReportResponse:
        """Build a private threat report from source hits and optional AI output."""
        max_score = max((hit.confidence_score for hit in source_hits), default=20)
        severity = ThreatSeverity.MEDIUM
        if max_score >= 80:
            severity = ThreatSeverity.HIGH
        elif max_score < 35:
            severity = ThreatSeverity.LOW

        report = ThreatReportResponse(
            report_id=str(uuid4()),
            scan_job_id=scan_job_id,
            severity=severity,
            confidence=max_score,
            executive_summary=f"Scaffold report for {artifact.artifact_type.value} artifact submission.",
            recommended_actions=[
                "Review source findings in the private workspace.",
                "Decide whether anonymized publication is appropriate.",
                "Track duplicate submissions before escalating externally.",
            ],
            source_summary=[hit.summary for hit in source_hits],
            ai_summary=ai_summary,
            publish_status=PublicShareStatus.PRIVATE,
            created_at=datetime.now(timezone.utc),
        )
        self._reports[report.report_id] = report
        return report

    def get_report(self, report_id: str) -> ThreatReportResponse | None:
        """Return a previously built report if it exists."""
        return self._reports.get(report_id)
