"""
Purpose:
    Endpoint and cache behavior tests for URL/file scanning.
Inputs:
    FastAPI test client and stubbed VT client implementation.
Outputs:
    Assertions for API contract and cache hit/miss logic.
Dependencies:
    pytest fixtures and scan service singleton override.
TODO Checklist:
    - [ ] Add tests for VT timeout/rate-limit mapped user errors.
    - [ ] Add tests for max upload size handling edge cases.
"""

from app.api import deps


class CountingStubVTClient:
    """Tracks how many times VT lookup methods are called."""

    def __init__(self) -> None:
        self.url_calls = 0
        self.file_calls = 0

    async def scan_url(self, normalized_url: str) -> dict:
        self.url_calls += 1
        return {
            "stats": {"malicious": 0, "suspicious": 2, "harmless": 0, "undetected": 0},
            "url": normalized_url,
        }

    async def scan_file_hash(self, sha256_hash: str) -> dict:
        self.file_calls += 1
        return {
            "stats": {"malicious": 0, "suspicious": 0, "harmless": 1, "undetected": 0},
            "sha256": sha256_hash,
        }


def test_scan_url_cache_hit_skips_second_external_lookup(client) -> None:
    service = deps.get_scan_service()
    stub = CountingStubVTClient()
    service.vt_client = stub

    first = client.post("/api/v1/scan/url", json={"url": "https://Example.org/"})
    second = client.post("/api/v1/scan/url", json={"url": "https://example.org"})

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json()["scan_id"] == second.json()["scan_id"]
    assert stub.url_calls == 1


def test_scan_file_cache_hit_skips_second_external_lookup(client) -> None:
    service = deps.get_scan_service()
    stub = CountingStubVTClient()
    service.vt_client = stub

    file_payload = b"sample-bytes-for-hash"
    first = client.post(
        "/api/v1/scan/file",
        files={"file": ("sample.bin", file_payload, "application/octet-stream")},
    )
    second = client.post(
        "/api/v1/scan/file",
        files={"file": ("renamed.bin", file_payload, "application/octet-stream")},
    )

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json()["scan_id"] == second.json()["scan_id"]
    assert stub.file_calls == 1


def test_get_scan_by_id_returns_contract_shape(client) -> None:
    service = deps.get_scan_service()
    service.vt_client = CountingStubVTClient()

    created = client.post("/api/v1/scan/url", json={"url": "https://scan-id.example"})
    scan_id = created.json()["scan_id"]

    fetched = client.get(f"/api/v1/scan/{scan_id}")
    assert fetched.status_code == 200
    payload = fetched.json()
    assert payload["scan_id"] == scan_id
    assert payload["status"] in {"SAFE", "SUSPICIOUS", "MALICIOUS"}
    assert isinstance(payload["reasons"], list)
