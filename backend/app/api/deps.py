"""
Purpose:
    Shared FastAPI dependencies for DB sessions, auth context, and scaffold services.
Inputs:
    Request auth headers, DB session factory, and runtime settings.
Outputs:
    Reusable dependency providers for route modules.
Dependencies:
    FastAPI Depends, SQLAlchemy session, JWT helpers, scaffold services.
TODO Checklist:
    - [ ] Replace token-only principal resolution with DB-backed account loading.
    - [ ] Add workspace membership lookups once workspace switching is implemented.
    - [ ] Move service wiring to a DI container only if the team outgrows simple factories.
"""

from functools import lru_cache

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.permissions import can_review_public_content
from app.core.security import decode_access_token, oauth2_scheme
from app.db.session import get_db
from app.schemas.auth import CurrentPrincipal
from app.services.admin_review_service import AdminReviewService
from app.services.ai.api_ai_service import ApiAiService
from app.services.ai.local_ai_service import LocalAiService
from app.services.artifact_service import ArtifactService
from app.services.auth_service import AuthService
from app.services.caching_service import CachingService
from app.services.dashboard_service import DashboardService
from app.services.enrichment.source_a_client import SourceAClient
from app.services.enrichment.source_b_client import SourceBClient
from app.services.enrichment.source_c_client import SourceCClient
from app.services.enrichment.virustotal_client import VirusTotalClient
from app.services.ioc_extraction_service import IocExtractionService
from app.services.normalization_service import NormalizationService
from app.services.public_sharing_service import PublicSharingService
from app.services.report_service import ReportService
from app.services.sanitization_service import SanitizationService
from app.services.scan_orchestrator import ScanOrchestrator


@lru_cache
def _build_report_service() -> ReportService:
    """Build shared in-memory report service."""
    return ReportService()


@lru_cache
def _build_scan_orchestrator() -> ScanOrchestrator:
    """Build the shared scan orchestrator and its adapters."""
    settings = get_settings()
    enrichment_adapters = []
    if settings.virustotal_enabled:
        enrichment_adapters.append(
            VirusTotalClient(
                api_key=settings.virustotal_api_key,
                base_url=settings.virustotal_base_url,
                timeout_seconds=settings.http_timeout_seconds,
            )
        )
    if settings.source_a_enabled:
        enrichment_adapters.append(SourceAClient())
    if settings.source_b_enabled:
        enrichment_adapters.append(SourceBClient())
    if settings.source_c_enabled:
        enrichment_adapters.append(SourceCClient())

    ai_services = {
        "local": LocalAiService(enabled=settings.local_ai_enabled),
        "api": ApiAiService(
            enabled=settings.api_ai_enabled,
            provider_name=settings.api_ai_provider_name,
        ),
    }

    return ScanOrchestrator(
        artifact_service=ArtifactService(),
        normalization_service=NormalizationService(),
        ioc_extraction_service=IocExtractionService(),
        caching_service=CachingService(),
        enrichment_adapters=enrichment_adapters,
        ai_services=ai_services,
        report_service=_build_report_service(),
    )


@lru_cache
def _build_public_sharing_service() -> PublicSharingService:
    """Build public sharing service with sanitizer dependency."""
    settings = get_settings()
    return PublicSharingService(
        sanitization_service=SanitizationService(),
        admin_review_required=settings.admin_review_required_for_external_reports,
    )


@lru_cache
def _build_dashboard_service() -> DashboardService:
    """Build lightweight dashboard service used by overview endpoints."""
    return DashboardService()


@lru_cache
def _build_admin_review_service() -> AdminReviewService:
    """Build admin review workflow service."""
    return AdminReviewService()


@lru_cache
def _build_auth_service() -> AuthService:
    """Build auth service for demo registration and login flows."""
    return AuthService()


def get_auth_service() -> AuthService:
    """Dependency wrapper for auth service access."""
    return _build_auth_service()


def get_scan_orchestrator() -> ScanOrchestrator:
    """Dependency wrapper for scan orchestration access."""
    return _build_scan_orchestrator()


def get_public_sharing_service() -> PublicSharingService:
    """Dependency wrapper for public sharing service access."""
    return _build_public_sharing_service()


def get_dashboard_service() -> DashboardService:
    """Dependency wrapper for dashboard service access."""
    return _build_dashboard_service()


def get_report_service() -> ReportService:
    """Dependency wrapper for report retrieval."""
    return _build_report_service()


def get_admin_review_service() -> AdminReviewService:
    """Dependency wrapper for admin review service access."""
    return _build_admin_review_service()


def get_current_principal(token: str = Depends(oauth2_scheme)) -> CurrentPrincipal:
    """Decode bearer token and return the lightweight scaffold principal."""
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    subject = payload.get("sub")
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing subject.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return CurrentPrincipal(
        subject=subject,
        email=payload.get("email", subject),
        role=payload.get("role", "analyst"),
        organization_id=payload.get("organization_id", "demo-org"),
        workspace_id=payload.get("workspace_id", "demo-workspace"),
    )


def require_admin(principal: CurrentPrincipal = Depends(get_current_principal)) -> CurrentPrincipal:
    """Ensure the caller has a platform-level review/admin role."""
    if not can_review_public_content(principal.role):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin or reviewer privileges are required for this route.",
        )
    return principal


DbSessionDep = Depends(get_db)
PrincipalDep = Depends(get_current_principal)
AdminDep = Depends(require_admin)
SessionType = Session
