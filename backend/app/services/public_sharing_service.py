"""
Purpose:
    Prepare anonymized public threat outputs from private reports or external uploads.
Inputs:
    Private report details, publish requests, and external report metadata.
Outputs:
    Public-safe summaries and publication workflow status.
Dependencies:
    Sanitization service and public threat schemas.
TODO Checklist:
    - [ ] Add stronger anonymization checks before production use.
    - [ ] Add DB persistence and public slug uniqueness rules.
"""

from datetime import datetime, timezone
from uuid import uuid4

from app.schemas.public_threats import PublicThreatListResponse, PublicThreatSummary
from app.schemas.report import ExternalReportUploadRequest, PublishRequest, ThreatReportResponse
from app.services.sanitization_service import SanitizationService
from app.utils.enums import ThreatSeverity


class PublicSharingService:
    """Scaffold service for anonymized sharing workflows."""

    def __init__(self, sanitization_service: SanitizationService, admin_review_required: bool) -> None:
        self.sanitization_service = sanitization_service
        self.admin_review_required = admin_review_required
        self._public_reports: dict[str, PublicThreatSummary] = {}

    def create_publish_request(
        self,
        report: ThreatReportResponse,
        payload: PublishRequest,
    ) -> dict[str, object]:
        """Return a scaffold publish request preview."""
        public_summary = self.sanitization_service.sanitize_summary(report.executive_summary)
        public_payload = {
            "title": f"Anonymized threat report {report.report_id[:8]}",
            "summary": public_summary,
            "severity": report.severity.value,
            "indicator_count": len(report.source_summary),
            "notes_for_reviewer": payload.notes_for_reviewer,
        }
        self.sanitization_service.assert_identity_safe(public_payload)
        return {
            "report_id": report.report_id,
            "status": "pending_review" if self.admin_review_required else "publish_ready",
            "public_payload_preview": public_payload,
        }

    def accept_external_upload(self, payload: ExternalReportUploadRequest) -> dict[str, object]:
        """Return scaffold metadata for an external upload review request."""
        reference = str(uuid4())
        return {
            "upload_reference": reference,
            "status": "pending_review",
            "title": payload.title,
        }

    def publish_public_report(self, title: str, summary: str, severity: ThreatSeverity) -> PublicThreatSummary:
        """Create a public-safe feed entry with no private link fields."""
        public_report = PublicThreatSummary(
            public_report_id=str(uuid4()),
            public_slug=f"threat-{uuid4().hex[:10]}",
            title=title,
            summary=self.sanitization_service.sanitize_summary(summary),
            severity=severity,
            indicator_count=3,
            source_kind="workspace_publish",
            published_at=datetime.now(timezone.utc),
        )
        self._public_reports[public_report.public_report_id] = public_report
        return public_report

    def list_public_reports(self) -> PublicThreatListResponse:
        """Return the current public feed placeholder items."""
        if not self._public_reports:
            seed = self.publish_public_report(
                title="Credential phishing kit indicators",
                summary="Sanitized community-facing report showing phishing infrastructure indicators.",
                severity=ThreatSeverity.MEDIUM,
            )
            self._public_reports[seed.public_report_id] = seed
        return PublicThreatListResponse(items=list(self._public_reports.values()))

    def get_public_report(self, public_report_id: str) -> PublicThreatSummary | None:
        """Return a single public report if present."""
        return self._public_reports.get(public_report_id)
