"""
Purpose:
    Shared interface for optional AI analysis adapters.
Inputs:
    Artifact value, extracted indicators, and source hit summaries.
Outputs:
    Optional analyst-friendly narrative text.
Dependencies:
    Standard library typing only.
TODO Checklist:
    - [ ] Add token budgeting and privacy guardrails before real integration.
"""

from typing import Protocol

from app.schemas.scan import SourceHit


class AiAnalysisAdapter(Protocol):
    """Protocol for scaffold AI analysis services."""

    async def analyze(
        self,
        artifact_value: str,
        indicators: list[str],
        source_hits: list[SourceHit],
    ) -> str | None:
        """Return optional AI-generated narrative text."""
