"""
Purpose:
    JWT and password helper utilities for authentication skeleton.
Inputs:
    Credentials/token data from auth endpoints and request dependencies.
Outputs:
    Signed JWT tokens and password verification results.
Dependencies:
    `python-jose`, `passlib`, backend settings.
TODO Checklist:
    - [ ] Rotate JWT secret and add key management strategy.
    - [ ] Add refresh token flow and token revocation list.
    - [ ] Enforce stronger password policy during registration.
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
    """Return True when plain password matches stored hash."""
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    """Hash a password for storage."""
    return pwd_context.hash(password)


def create_access_token(data: dict[str, Any], expires_minutes: int | None = None) -> str:
    """
    Create JWT access token.

    Required claim:
        `sub` - subject identifier (email in this scaffold).
    """
    settings = get_settings()
    to_encode = data.copy()
    expire_delta = timedelta(minutes=expires_minutes or settings.access_token_expire_minutes)
    to_encode["exp"] = datetime.now(timezone.utc) + expire_delta
    return jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict[str, Any] | None:
    """Decode JWT and return claims; return None on decode/validation errors."""
    settings = get_settings()
    try:
        return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    except JWTError:
        return None
