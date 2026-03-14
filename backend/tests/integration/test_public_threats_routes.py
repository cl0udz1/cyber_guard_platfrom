def test_public_feed_is_accessible(client) -> None:
    response = client.get("/api/v1/public-threats")

    assert response.status_code == 200
    assert len(response.json()["items"]) >= 1


def test_admin_review_requires_admin(client, org_auth_header, admin_auth_header) -> None:
    forbidden = client.get("/api/v1/admin-reviews/queue", headers=org_auth_header)
    allowed = client.get("/api/v1/admin-reviews/queue", headers=admin_auth_header)

    assert forbidden.status_code == 403
    assert allowed.status_code == 200
    assert len(allowed.json()) >= 1
