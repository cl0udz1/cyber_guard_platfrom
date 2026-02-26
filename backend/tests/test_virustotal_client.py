"""
Purpose:
    Unit tests for VirusTotal client using httpx mock transport (respx).
Inputs:
    Mocked HTTP routes and VT client method calls.
Outputs:
    Assertions for JSON parsing and retry logic on 429 rate limits.
Dependencies:
    pytest-asyncio, respx, httpx.
TODO Checklist:
    - [ ] Add timeout retry test with patched sleep.
    - [ ] Add tests for non-429 HTTP error mapping.
"""

import httpx
import pytest
import respx

from app.services.virustotal_client import VirusTotalClient


@pytest.mark.asyncio
async def test_scan_url_uses_httpx_and_returns_json() -> None:
    client = VirusTotalClient(
        api_key="demo-api-key",
        base_url="https://www.virustotal.com/api/v3",
        timeout_seconds=5,
    )

    with respx.mock(assert_all_called=True) as mock:
        mock.post("https://www.virustotal.com/api/v3/urls").respond(
            200,
            json={"data": {"id": "abc123"}, "stats": {"malicious": 0, "suspicious": 0}},
        )
        result = await client.scan_url("https://example.org")

    assert result["data"]["id"] == "abc123"


@pytest.mark.asyncio
async def test_request_retries_once_after_429(monkeypatch) -> None:
    client = VirusTotalClient(
        api_key="demo-api-key",
        base_url="https://www.virustotal.com/api/v3",
        timeout_seconds=5,
    )

    async def no_sleep(_: float) -> None:
        return None

    monkeypatch.setattr("app.services.virustotal_client.asyncio.sleep", no_sleep)

    with respx.mock(assert_all_called=True) as mock:
        route = mock.post("https://www.virustotal.com/api/v3/urls")
        route.mock(
            side_effect=[
                httpx.Response(429, json={"error": {"message": "rate limited"}}),
                httpx.Response(200, json={"data": {"id": "retry-ok"}, "stats": {}}),
            ]
        )
        result = await client.scan_url("https://retry.example")

    assert result["data"]["id"] == "retry-ok"
