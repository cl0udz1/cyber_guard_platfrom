"""
Purpose:
    VirusTotal adapter placeholder kept as one threat-intel source among several.
Inputs:
    Extracted indicators and normalized artifact values.
Outputs:
    Simple per-source verdict summary for the scan orchestrator.
Dependencies:
    Adapter protocol and backend settings.
TODO Checklist:
    - [ ] Replace scaffold response with real HTTP requests and parsing.
    - [ ] Add timeout, rate limit, and retry handling once integrated.
"""


class VirusTotalClient:
    """Threat-intel adapter placeholder for VirusTotal."""

    name = "virustotal"

    def __init__(self, api_key: str, base_url: str, timeout_seconds: int) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.timeout_seconds = timeout_seconds

    async def enrich(self, indicators: list[str], artifact_value: str) -> dict[str, object]:
        """Return a deterministic scaffold response without calling the network."""
        return {
            "source_name": self.name,
            "verdict": "observed",
            "confidence_score": 65,
            "summary": f"VirusTotal placeholder hit count for {artifact_value[:40]}.",
        }
