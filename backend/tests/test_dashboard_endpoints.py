"""
Purpose:
    Validate dashboard summary endpoint shape and auth requirement.
Inputs:
    Seeded IoC/scan rows in test DB.
Outputs:
    Assertions for counts and recent lists.
Dependencies:
    pytest fixtures, ORM models.
TODO Checklist:
    - [ ] Add trend/date range tests after trend fields are implemented.
"""

from datetime import datetime, timezone

from app.models.ioc import Ioc
from app.models.scan_result import ScanResult


def test_dashboard_summary_requires_auth(client) -> None:
    response = client.get("/api/v1/dashboard/summary")
    assert response.status_code == 401


def test_dashboard_summary_returns_counts_and_recent(client, db_session, auth_header) -> None:
    db_session.add_all(
        [
            Ioc(type="domain", value="bad.example", confidence=80, tags=["phishing"]),
            Ioc(type="ip", value="8.8.8.8", confidence=10, tags=["benign-ish"]),
            ScanResult(
                scan_type="url",
                scan_key="https://bad.example",
                original_input="https://bad.example",
                status="MALICIOUS",
                score=95,
                summary="Flagged malicious",
                reasons=["test reason"],
                raw_vt_json={"stats": {"malicious": 2, "suspicious": 0}},
                created_at=datetime.now(timezone.utc),
            ),
        ]
    )
    db_session.commit()

    response = client.get("/api/v1/dashboard/summary", headers=auth_header)
    assert response.status_code == 200
    payload = response.json()

    assert "counts_by_type" in payload
    assert payload["counts_by_type"]["domain"] >= 1
    assert payload["counts_by_type"]["ip"] >= 1
    assert isinstance(payload["recent_iocs"], list)
    assert isinstance(payload["recent_scans"], list)
