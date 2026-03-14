EXPECTED_PATHS = {
    "/api/v1/auth/register",
    "/api/v1/auth/login",
    "/api/v1/auth/me",
    "/api/v1/users/me",
    "/api/v1/orgs",
    "/api/v1/workspaces",
    "/api/v1/scan-jobs",
    "/api/v1/reports/{report_id}",
    "/api/v1/public-threats",
    "/api/v1/admin-reviews/queue",
    "/api/v1/dashboard/overview",
    "/api/v1/integrations/public-threats-api",
}


def test_openapi_contains_expected_route_groups(client) -> None:
    schema = client.get("/openapi.json").json()
    paths = set(schema["paths"].keys())

    assert EXPECTED_PATHS.issubset(paths)
