from fastapi import HTTPException

from app.services.sanitization_service import SanitizationService


def test_sanitizer_rejects_identity_fields() -> None:
    service = SanitizationService()

    try:
        service.assert_identity_safe({"title": "safe", "organization_id": "demo-org"})
    except HTTPException as exc:
        assert exc.status_code == 400
    else:
        raise AssertionError("Expected identity-safe validation to fail.")


def test_sanitizer_rewrites_sensitive_summary_terms() -> None:
    service = SanitizationService()
    result = service.sanitize_summary("Share workspace findings with the organization.")

    assert "workspace" not in result
    assert "organization" not in result
