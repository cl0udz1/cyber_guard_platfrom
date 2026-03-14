"""
Purpose:
    Schemas for integration catalog views and planned public API metadata.
Inputs:
    Integration planning routes.
Outputs:
    Typed responses for adapters and phase-2 public API visibility.
Dependencies:
    Pydantic models.
TODO Checklist:
    - [ ] Add per-source credential schemas only when admin configuration is implemented.
"""

from pydantic import BaseModel


class IntegrationCatalogEntry(BaseModel):
    """Threat-intel or AI integration summary."""

    name: str
    category: str
    mode: str
    enabled: bool
    notes: str


class PublicApiStatusResponse(BaseModel):
    """Status response for the planned public threats API surface."""

    enabled: bool
    phase: str
    notes: list[str]
