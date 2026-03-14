"""
Purpose:
    Shared interface for threat-intel enrichment adapter placeholders.
Inputs:
    Extracted indicators and normalized artifact values.
Outputs:
    Consistent dictionaries that can become `SourceHit` models.
Dependencies:
    Standard library typing only.
TODO Checklist:
    - [ ] Replace loose dicts with richer typed adapter responses if needed.
    - [ ] Add standardized error/result metadata before real adapter implementation.
"""

from typing import Protocol


class EnrichmentAdapter(Protocol):
    """Protocol for scaffold enrichment clients."""

    name: str

    async def enrich(self, indicators: list[str], artifact_value: str) -> dict[str, object]:
        """Return source summary data for a scan request."""
