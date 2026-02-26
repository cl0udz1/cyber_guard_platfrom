"""
Purpose:
    Validate anonymization rules for IoC submissions.
Inputs:
    Sample payload dictionaries.
Outputs:
    Assertions proving forbidden identity fields are blocked.
Dependencies:
    pytest and `app.services.anonymizer`.
TODO Checklist:
    - [ ] Add tests for disguised identity data inside `value`/`tags`.
"""

import pytest

from app.services.anonymizer import anonymize_ioc_payload


def test_anonymizer_accepts_allowed_fields() -> None:
    payload = {
        "type": "domain",
        "value": "evil.example",
        "confidence": 70,
        "tags": ["phishing", "credential-theft"],
    }
    result = anonymize_ioc_payload(payload)
    assert result["type"] == "domain"
    assert result["value"] == "evil.example"
    assert result["confidence"] == 70
    assert result["tags"] == ["phishing", "credential-theft"]


def test_anonymizer_rejects_identity_keys() -> None:
    payload = {
        "type": "ip",
        "value": "1.2.3.4",
        "confidence": 80,
        "tags": [],
        "user_id": "abc123",
    }
    with pytest.raises(ValueError, match="Identity-related fields"):
        anonymize_ioc_payload(payload)


def test_anonymizer_rejects_unknown_extra_keys() -> None:
    payload = {
        "type": "url",
        "value": "https://bad.example",
        "confidence": 50,
        "tags": [],
        "notes": "unexpected field",
    }
    with pytest.raises(ValueError, match="Unexpected fields"):
        anonymize_ioc_payload(payload)
