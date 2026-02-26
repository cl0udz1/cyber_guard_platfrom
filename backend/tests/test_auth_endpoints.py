"""
Purpose:
    Smoke tests for auth endpoint skeleton behavior.
Inputs:
    FastAPI test client fixture and sample login payloads.
Outputs:
    Assertions on token generation and `/me` response.
Dependencies:
    pytest + FastAPI TestClient fixtures from conftest.
TODO Checklist:
    - [ ] Add negative tests for expired/revoked tokens once implemented.
"""


def test_login_returns_bearer_token(client) -> None:
    response = client.post(
        "/api/v1/auth/login",
        json={"email": "orguser@example.edu", "password": "changeme123!"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["token_type"] == "bearer"
    assert isinstance(payload["access_token"], str)
    assert len(payload["access_token"]) > 10


def test_me_returns_claims_from_token(client) -> None:
    login = client.post(
        "/api/v1/auth/login",
        json={"email": "analyst@example.edu", "password": "changeme123!"},
    )
    token = login.json()["access_token"]
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json()["email"] == "analyst@example.edu"
    assert response.json()["role"] == "org_user"
