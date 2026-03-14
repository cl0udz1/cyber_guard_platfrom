"""
Purpose:
    Extract IOC-like values from normalized artifacts.
Inputs:
    Normalized artifact value and artifact type.
Outputs:
    Small list of indicators that enrichment adapters can consume.
Dependencies:
    Scaffold enums only.
TODO Checklist:
    - [ ] Add regex-based extraction for URLs, domains, hashes, and email headers.
    - [ ] Separate extractor modules if email parsing becomes a real feature.
"""

from app.utils.enums import ArtifactType


class IocExtractionService:
    """Return lightweight extracted indicators for the scaffold pipeline."""

    def extract(self, artifact_type: ArtifactType, normalized_value: str) -> list[str]:
        """Extract a small set of dedupe-friendly indicators."""
        if artifact_type == ArtifactType.EMAIL_SIGNAL:
            return [segment for segment in normalized_value.split() if "." in segment or "@" in segment]
        return [normalized_value]
