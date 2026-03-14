"""
Purpose:
    URL normalization helpers for scan submissions and dedupe keys.
Inputs:
    Raw URL strings from user or organization submissions.
Outputs:
    Safer normalized URL strings for caching and enrichment calls.
Dependencies:
    Standard library `urllib.parse`.
TODO Checklist:
    - [ ] Add defanging helpers for UI display if reused by frontend tooling.
    - [ ] Add stronger validation for IDNs and suspicious encodings.
"""

from urllib.parse import urlparse, urlunparse


def normalize_url(raw_url: str) -> str:
    """Normalize a URL enough for scaffold-level dedupe behavior."""
    parsed = urlparse(raw_url.strip())
    scheme = (parsed.scheme or "https").lower()
    netloc = parsed.netloc.lower()
    path = parsed.path or "/"
    normalized = parsed._replace(scheme=scheme, netloc=netloc, path=path, fragment="")
    return urlunparse(normalized)
