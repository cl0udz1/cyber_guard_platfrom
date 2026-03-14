"""
Purpose:
    Integration planning endpoints for threat sources and planned public API exposure.
Inputs:
    Runtime settings and feature flags.
Outputs:
    Lists of enabled sources and future public API status.
Dependencies:
    Config settings, feature flags, and integration schemas.
TODO Checklist:
    - [ ] Add org/workspace-level integration settings once admin configuration is real.
"""

from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings
from app.core.feature_flags import public_threats_api_enabled
from app.schemas.integrations import IntegrationCatalogEntry, PublicApiStatusResponse

router = APIRouter(prefix="/integrations", tags=["integrations"])


@router.get("/catalog", response_model=list[IntegrationCatalogEntry])
async def get_integration_catalog(
    settings: Settings = Depends(get_settings),
) -> list[IntegrationCatalogEntry]:
    """Return scaffold integration metadata for planning and UI wiring."""
    return [
        IntegrationCatalogEntry(
            name="virustotal",
            category="threat_intel",
            mode="adapter",
            enabled=settings.virustotal_enabled,
            notes="Legacy source retained as one adapter among many.",
        ),
        IntegrationCatalogEntry(
            name="source_a",
            category="threat_intel",
            mode="adapter",
            enabled=settings.source_a_enabled,
            notes="Placeholder slot for team-selected enrichment source.",
        ),
        IntegrationCatalogEntry(
            name="source_b",
            category="threat_intel",
            mode="adapter",
            enabled=settings.source_b_enabled,
            notes="Placeholder slot for secondary enrichment source.",
        ),
        IntegrationCatalogEntry(
            name="local_ai",
            category="ai",
            mode="local",
            enabled=settings.local_ai_enabled,
            notes="Privacy-preserving AI analysis mode.",
        ),
        IntegrationCatalogEntry(
            name="api_ai",
            category="ai",
            mode="api",
            enabled=settings.api_ai_enabled,
            notes="Convenience-focused remote AI analysis mode.",
        ),
    ]


@router.get("/public-threats-api", response_model=PublicApiStatusResponse)
async def get_public_api_status(
    settings: Settings = Depends(get_settings),
) -> PublicApiStatusResponse:
    """Return phase information for the planned public threats API."""
    enabled = public_threats_api_enabled(settings)
    return PublicApiStatusResponse(
        enabled=enabled,
        phase="Phase 2" if enabled else "Planned",
        notes=[
            "Public threats API is intentionally separate from private identity/workspace data.",
            "Keep this disabled during MVP unless the team explicitly enters phase 2 work.",
        ],
    )
