"""
Purpose:
    API v1 router that bundles all endpoint groups.
Inputs:
    Endpoint routers for auth, scan, IoC, dashboard.
Outputs:
    One `APIRouter` included by the main FastAPI app.
Dependencies:
    FastAPI routing.
TODO Checklist:
    - [ ] Add route-level rate limiting/middleware as needed.
    - [ ] Version endpoints carefully when breaking changes occur.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, dashboard, ioc, scan

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(scan.router)
api_router.include_router(ioc.router)
api_router.include_router(dashboard.router)
