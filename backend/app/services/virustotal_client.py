"""
Purpose:
    Minimal VirusTotal API integration wrapper using httpx.
Inputs:
    URL/hash values from scan service.
Outputs:
    Raw JSON payloads from VirusTotal (or controlled stub responses).
Dependencies:
    httpx, retry/backoff helper utilities.
TODO Checklist:
    - [ ] Implement full VT workflow (submit URL/file, poll analysis status).
    - [ ] Add strict response schema validation.
    - [ ] Add telemetry for request latency and error rates.
"""

import asyncio
from typing import Any

import httpx

from app.utils.rate_limit import get_backoff_seconds


class VirusTotalError(Exception):
    """Base class for VirusTotal client errors."""


class VirusTotalRateLimitError(VirusTotalError):
    """Raised when API keeps returning 429 after retries."""


class VirusTotalTimeoutError(VirusTotalError):
    """Raised on repeated timeout failures."""


class VirusTotalApiError(VirusTotalError):
    """Raised for non-retriable HTTP errors."""


class VirusTotalClient:
    """
    Lightweight async VT client.

    NOTE:
        For student skeleton simplicity, this wrapper is intentionally small.
    """

    def __init__(self, api_key: str, base_url: str, timeout_seconds: int = 20) -> None:
        self.api_key = api_key.strip()
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds

    @property
    def _headers(self) -> dict[str, str]:
        return {"x-apikey": self.api_key} if self.api_key else {}

    async def _request_with_retry(
        self,
        method: str,
        path: str,
        *,
        max_attempts: int = 3,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Perform VT request with simple 429/timeout retry strategy.

        TODO:
            - Respect `Retry-After` header when present.
            - Add circuit breaker when service repeatedly fails.
        """
        url = f"{self.base_url}{path}"
        timeout = httpx.Timeout(self.timeout_seconds)

        for attempt in range(1, max_attempts + 1):
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.request(
                        method=method,
                        url=url,
                        headers=self._headers,
                        **kwargs,
                    )

                if response.status_code == 429:
                    if attempt == max_attempts:
                        raise VirusTotalRateLimitError("VirusTotal rate limit exceeded.")
                    await asyncio.sleep(get_backoff_seconds(attempt))
                    continue

                response.raise_for_status()
                return response.json()

            except httpx.TimeoutException as exc:
                if attempt == max_attempts:
                    raise VirusTotalTimeoutError("VirusTotal request timed out.") from exc
                await asyncio.sleep(get_backoff_seconds(attempt))

            except httpx.HTTPStatusError as exc:
                # Non-429 HTTP errors are treated as non-retriable in this skeleton.
                raise VirusTotalApiError(
                    f"VirusTotal HTTP error {exc.response.status_code}: {exc.response.text}"
                ) from exc

        # Defensive fallback (should not normally be reached).
        raise VirusTotalApiError("VirusTotal request failed unexpectedly.")

    async def scan_url(self, normalized_url: str) -> dict[str, Any]:
        """
        Submit URL for analysis lookup.

        If API key is missing, return a deterministic stub payload.
        """
        if not self.api_key:
            return {
                "source": "stub_no_api_key",
                "stats": {"malicious": 0, "suspicious": 1, "harmless": 0, "undetected": 0},
                "url": normalized_url,
            }

        return await self._request_with_retry(
            "POST",
            "/urls",
            data={"url": normalized_url},
        )

    async def scan_file_hash(self, sha256_hash: str) -> dict[str, Any]:
        """
        Lookup file report by SHA-256 hash.

        Note:
            This does not upload or execute a file; it performs hash lookup only.
        """
        if not self.api_key:
            return {
                "source": "stub_no_api_key",
                "stats": {"malicious": 0, "suspicious": 0, "harmless": 1, "undetected": 0},
                "sha256": sha256_hash,
            }

        return await self._request_with_retry("GET", f"/files/{sha256_hash}")
