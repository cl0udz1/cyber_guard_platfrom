"""
Purpose:
    Shared validation/normalization helpers for API inputs.
Inputs:
    Raw URL/IoC values from requests.
Outputs:
    Normalized strings or raised ValueError for invalid input.
Dependencies:
    Standard library URL parsing.
TODO Checklist:
    - [ ] Add robust domain/IP/hash validators per IoC type.
    - [ ] Add URL defanging/refanging helpers for safe UI rendering.
"""

from urllib.parse import urlparse, urlunparse


def normalize_url(url: str) -> str:
    """
    Normalize URL for cache key consistency.

    Current rules:
        - Trim whitespace.
        - Ensure scheme exists (default https).
        - Lowercase scheme + host.
        - Remove trailing slash from path root-only URLs.
    """
    raw = (url or "").strip()
    if not raw:
        raise ValueError("URL cannot be empty.")

    if "://" not in raw:
        raw = f"https://{raw}"

    parsed = urlparse(raw)
    if not parsed.netloc:
        raise ValueError("URL is invalid.")

    normalized_path = parsed.path or "/"
    if normalized_path == "/":
        normalized_path = ""

    return urlunparse(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            normalized_path,
            parsed.params,
            parsed.query,
            parsed.fragment,
        )
    )
