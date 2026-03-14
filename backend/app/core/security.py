"""
Purpose:
    JWT and password helpers for scaffold authentication flows.
Inputs:
    Credentials and identity payloads from auth services and route dependencies.
Outputs:
    Signed tokens and lightweight password hashing helpers.
Dependencies:
    `python-jose`, `passlib`, backend settings.
TODO Checklist:
    - [ ] Add invitation tokens and password reset helpers.
    - [ ] Add refresh token or session revocation support if the team needs it.
    - [ ] Replace demo account assumptions with DB-backed authentication.
"""

from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Return True when a plain password matches a stored hash."""
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    """Create a password hash for future DB-backed auth."""
    return pwd_context.hash(password)


def create_access_token(data: dict[str, Any], expires_minutes: int | None = None) -> str:
    """Create a signed access token with a short-lived expiration."""
    settings = get_settings()
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(
        minutes=expires_minutes or settings.access_token_expire_minutes
    )
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict[str, Any] | None:
    """Decode a token and return claims or None when invalid."""
    settings = get_settings()
    try:
        return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    except JWTError:
        return None
