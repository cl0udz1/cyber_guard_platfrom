"""
Purpose:
    Placeholder for privacy-preserving local AI analysis mode.
Inputs:
    Artifact value, indicators, and source hits.
Outputs:
    Short local-mode AI summary text.
Dependencies:
    AI adapter protocol only.
TODO Checklist:
    - [ ] Replace stub with a real local model invocation if selected by the team.
"""

from app.schemas.scan import SourceHit


class LocalAiService:
    """Local AI placeholder that never leaves the environment."""

    def __init__(self, enabled: bool) -> None:
        self.enabled = enabled

    async def analyze(
        self,
        artifact_value: str,
        indicators: list[str],
        source_hits: list[SourceHit],
    ) -> str | None:
        if not self.enabled:
            return None
        return (
            "Local AI mode synthesized source overlap without sending artifact data to an external API. "
            f"Indicators reviewed: {len(indicators)}."
        )
