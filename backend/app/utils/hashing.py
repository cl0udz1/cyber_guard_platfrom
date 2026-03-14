"""
Purpose:
    Hashing helpers for artifact normalization, cache keys, and report fingerprints.
Inputs:
    File bytes, byte chunks, or normalized text values.
Outputs:
    Hex digest strings safe to use as identifiers and dedupe keys.
Dependencies:
    Standard library `hashlib`.
TODO Checklist:
    - [ ] Add tests for stream/file object hashing helper.
    - [ ] Add alternate algorithms only if a real requirement appears.
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


def sha256_text(value: str) -> str:
    """Hash normalized text values such as URLs or pasted email signals."""
    return sha256_bytes(value.encode("utf-8"))
