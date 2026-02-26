"""
Purpose:
    Utility helpers for SHA-256 hashing.
Inputs:
    File bytes or byte chunks.
Outputs:
    Hex digest strings used for cache keys and safe file identification.
Dependencies:
    Standard library `hashlib`.
TODO Checklist:
    - [ ] Add unit tests for stream/file object hashing helper.
    - [ ] Support additional hash algorithms if needed for research.
"""

import hashlib
from collections.abc import Iterable


def sha256_bytes(data: bytes) -> str:
    """Return SHA-256 hex digest for a byte sequence."""
    return hashlib.sha256(data).hexdigest()


def sha256_chunks(chunks: Iterable[bytes]) -> str:
    """
    Hash a stream of byte chunks.

    Useful for large-file processing without loading all bytes in memory.
    """
    digest = hashlib.sha256()
    for chunk in chunks:
        digest.update(chunk)
    return digest.hexdigest()
