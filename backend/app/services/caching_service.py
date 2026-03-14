"""
Purpose:
    In-memory cache placeholder for duplicate scan submission behavior.
Inputs:
    Cache keys from normalized artifacts and AI mode selections.
Outputs:
    Previously generated scan job responses.
Dependencies:
    Standard library dictionaries.
TODO Checklist:
    - [ ] Replace in-memory cache with Redis or DB-backed cache if needed.
    - [ ] Add cache invalidation and freshness rules once real enrichment is live.
"""

from app.schemas.scan import ScanJobResponse


class CachingService:
    """Simple process-local cache for scaffold demonstrations and tests."""

    def __init__(self) -> None:
        self._scan_cache: dict[str, ScanJobResponse] = {}

    def get_scan(self, key: str) -> ScanJobResponse | None:
        """Return cached scan response if present."""
        return self._scan_cache.get(key)

    def set_scan(self, key: str, response: ScanJobResponse) -> None:
        """Store a scan response by cache key."""
        self._scan_cache[key] = response
