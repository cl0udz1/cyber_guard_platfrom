def test_scan_job_flow_returns_report(client, org_auth_header) -> None:
    response = client.post(
        "/api/v1/scan-jobs",
        headers=org_auth_header,
        json={
            "artifact": {
                "workspace_id": "demo-workspace",
                "artifact_type": "url",
                "artifact_value": "https://example.org/login",
            },
            "ai_mode": "local",
        },
    )

    assert response.status_code == 200
    job = response.json()
    assert job["status"] == "completed"
    assert len(job["sources"]) >= 2

    report_response = client.get(f"/api/v1/reports/{job['report_id']}", headers=org_auth_header)
    assert report_response.status_code == 200
    assert report_response.json()["scan_job_id"] == job["scan_job_id"]


def test_duplicate_submission_returns_cached_job(client, org_auth_header) -> None:
    payload = {
        "artifact": {
            "workspace_id": "demo-workspace",
            "artifact_type": "url",
            "artifact_value": "https://example.org/login",
        },
        "ai_mode": "local",
    }

    first = client.post("/api/v1/scan-jobs", headers=org_auth_header, json=payload)
    second = client.post("/api/v1/scan-jobs", headers=org_auth_header, json=payload)

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json()["scan_job_id"] == second.json()["scan_job_id"]
