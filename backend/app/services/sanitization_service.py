"""
Purpose:
    Enforce the public/private data separation rule for shared threat content.
Inputs:
    Private report metadata and proposed public payloads.
Outputs:
    Sanitized public-safe payloads with obvious identity fields removed.
Dependencies:
    Standard library string helpers.
TODO Checklist:
    - [ ] Add stronger content scanning for names, emails, and internal IDs.
    - [ ] Add unit tests for organization/workspace leakage scenarios.
"""

from fastapi import HTTPException, status


FORBIDDEN_PUBLIC_KEYS = {
    "organization_id",
    "workspace_id",
    "user_id",
    "email",
    "owner_name",
    "private_report_id",
}


class SanitizationService:
    """Guardrail service for Disconnect by Design publication rules."""

    def assert_identity_safe(self, payload: dict[str, object]) -> None:
        """Reject payloads that include direct identity or workspace link fields."""
        forbidden = FORBIDDEN_PUBLIC_KEYS.intersection(payload.keys())
        if forbidden:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Public payload contains forbidden identity fields: {sorted(forbidden)}",
            )

    def sanitize_summary(self, summary: str) -> str:
        """Apply a lightweight text sanitization pass for scaffold demos."""
        sanitized = summary.replace("workspace", "private scope").replace("organization", "publisher")
        return sanitized
