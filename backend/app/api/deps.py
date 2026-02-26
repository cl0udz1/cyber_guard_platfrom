"""
Purpose:
    Shared FastAPI dependencies (DB session, auth user, services).
Inputs:
    Request auth header, DB session factory, service configuration.
Outputs:
    Reusable dependency providers for endpoint modules.
Dependencies:
    FastAPI Depends, SQLAlchemy session, JWT helpers.
TODO Checklist:
    - [ ] Load current user from DB once user table auth is implemented.
    - [ ] Add role/permission checks for admin-only endpoints.
    - [ ] Replace singleton service pattern if per-request state is needed.
"""

from functools import lru_cache

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.security import decode_access_token, oauth2_scheme
from app.db.session import get_db
from app.schemas.auth import UserMeResponse
from app.services.scan_service import ScanService
from app.services.virustotal_client import VirusTotalClient


@lru_cache
def _build_scan_service() -> ScanService:
    """
    Build a singleton scan service to reuse client configuration.

    TODO:
        - Move to dependency injection container if project scales.
    """
    settings = get_settings()
    vt_client = VirusTotalClient(
        api_key=settings.virustotal_api_key,
        base_url=settings.virustotal_base_url,
        timeout_seconds=settings.http_timeout_seconds,
    )
    return ScanService(vt_client=vt_client)


def get_scan_service() -> ScanService:
    """Dependency wrapper for scan service access."""
    return _build_scan_service()


def get_current_user(token: str = Depends(oauth2_scheme)) -> UserMeResponse:
    """
    Decode bearer token and return current user context.

    NOTE:
        This skeleton does not yet query user table for full account checks.
    """
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    email = payload.get("sub")
    role = payload.get("role", "org_user")
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing subject.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return UserMeResponse(email=email, role=role)


DbSessionDep = Depends(get_db)
CurrentUserDep = Depends(get_current_user)
ScanServiceDep = Depends(get_scan_service)
SessionType = Session
