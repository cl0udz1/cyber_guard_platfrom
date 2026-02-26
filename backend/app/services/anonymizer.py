"""
Purpose:
    Enforce "Disconnect by Design" anonymization rules for IoC submissions.
Inputs:
    Raw IoC payload dictionary.
Outputs:
    Sanitized IoC dictionary with only allowed non-identity fields.
Dependencies:
    Standard library typing.
TODO Checklist:
    - [ ] Add heuristic detection for hidden identity leaks in free-text values.
    - [ ] Add configurable blocklist/allowlist from policy file.
    - [ ] Emit privacy audit metrics without storing private data.
"""

from datetime import datetime
from typing import Any, Mapping

ALLOWED_KEYS = {"type", "value", "confidence", "tags", "first_seen"}
FORBIDDEN_IDENTITY_KEYS = {
    "user_id",
    "org_id",
    "organization_id",
    "ip",
    "ip_address",
    "email",
    "username",
    "submitter",
    "submitted_by",
    "source_ip",
    "client_ip",
}


def anonymize_ioc_payload(payload: Mapping[str, Any]) -> dict[str, Any]:
    """
    Sanitize incoming IoC payload.

    Rules:
        1) Reject identity-like fields.
        2) Reject unknown extra fields.
        3) Return only allowed IoC fields.
    """
    incoming_keys = {key for key in payload.keys()}
    lowered_keys = {key.lower() for key in incoming_keys}
    forbidden_present = lowered_keys & FORBIDDEN_IDENTITY_KEYS
    if forbidden_present:
        blocked = ", ".join(sorted(forbidden_present))
        raise ValueError(f"Identity-related fields are not allowed: {blocked}")

    unknown_keys = incoming_keys - ALLOWED_KEYS
    if unknown_keys:
        unknown = ", ".join(sorted(unknown_keys))
        raise ValueError(f"Unexpected fields are not allowed: {unknown}")

    # Build sanitized payload explicitly to prevent accidental passthrough.
    cleaned: dict[str, Any] = {
        "type": payload["type"],
        "value": str(payload["value"]).strip(),
        "confidence": int(payload["confidence"]),
        "tags": [str(tag).strip() for tag in payload.get("tags", []) if str(tag).strip()],
    }

    first_seen = payload.get("first_seen")
    if first_seen is not None:
        # Keep datetime object if provided by schema layer; parse string fallback.
        cleaned["first_seen"] = (
            datetime.fromisoformat(first_seen) if isinstance(first_seen, str) else first_seen
        )

    return cleaned
