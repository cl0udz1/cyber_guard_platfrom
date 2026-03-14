def test_login_returns_token(client) -> None:
    response = client.post(
        "/api/v1/auth/login",
        json={"email": "admin@example.edu", "password": "org-admin-demo"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert body["principal_role"] == "org_admin"


def test_me_returns_current_profile(client, org_auth_header) -> None:
    response = client.get("/api/v1/auth/me", headers=org_auth_header)

    assert response.status_code == 200
    body = response.json()
    assert body["platform_role"] == "org_admin"
    assert body["memberships"][0]["workspace_id"] == "demo-workspace"
