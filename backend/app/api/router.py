"""
Purpose:
    Bundle all refreshed route groups into one API router.
Inputs:
    Route modules under `app.api.routes`.
Outputs:
    One FastAPI router mounted at the API prefix by `app.main`.
Dependencies:
    FastAPI routing and route modules.
TODO Checklist:
    - [ ] Add versioned include/exclude strategy if a v2 contract is introduced.
    - [ ] Add route-level tags or dependency groups if auth/rate limits get richer.
"""

from fastapi import APIRouter

from app.api.routes import (
    admin_reviews,
    auth,
    dashboard,
    integrations,
    orgs,
    public_threats,
    reports,
    scan_jobs,
    users,
    workspaces,
)

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(orgs.router)
api_router.include_router(workspaces.router)
api_router.include_router(scan_jobs.router)
api_router.include_router(reports.router)
api_router.include_router(public_threats.router)
api_router.include_router(admin_reviews.router)
api_router.include_router(dashboard.router)
api_router.include_router(integrations.router)
