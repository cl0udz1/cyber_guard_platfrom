"""
Purpose:
    Placeholder for convenience-focused remote AI analysis mode.
Inputs:
    Artifact value, indicators, and source hits.
Outputs:
    Short API-mode AI summary text.
Dependencies:
    AI adapter protocol only.
TODO Checklist:
    - [ ] Add provider-specific request/response handling when implemented.
    - [ ] Add privacy redaction rules before sending data externally.
"""

from app.schemas.scan import SourceHit


class ApiAiService:
    """Remote AI placeholder intended for later provider integration."""

    def __init__(self, enabled: bool, provider_name: str) -> None:
        self.enabled = enabled
        self.provider_name = provider_name

    async def analyze(
        self,
        artifact_value: str,
        indicators: list[str],
        source_hits: list[SourceHit],
    ) -> str | None:
        if not self.enabled:
            return None
        return (
            f"API AI mode placeholder for provider '{self.provider_name}' summarized "
            f"{len(source_hits)} source results."
        )
