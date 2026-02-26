"""
Purpose:
    Shared pytest fixtures for backend tests.
Inputs:
    FastAPI app, SQLAlchemy metadata, dependency overrides.
Outputs:
    Test client, isolated DB session, and auth header fixtures.
Dependencies:
    pytest, fastapi.testclient, SQLAlchemy in-memory SQLite.
TODO Checklist:
    - [ ] Add factory fixtures for common model records.
    - [ ] Add async client fixture for fully async endpoint tests.
"""

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    # Ensure local `backend/app` package wins over any globally installed `app` package.
    sys.path.insert(0, str(BACKEND_ROOT))

from app.api import deps
from app.core.security import create_access_token
from app.db.base import Base
from app.main import app
from app.models.ioc import Ioc  # noqa: F401  # Ensure table models are imported.
from app.models.scan_result import ScanResult  # noqa: F401
from app.models.user import User  # noqa: F401

TEST_DATABASE_URL = "sqlite+pysqlite:///:memory:"
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=Session)


@pytest.fixture(scope="session", autouse=True)
def create_test_tables() -> None:
    """Create/drop all tables once for test session."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db_session() -> Session:
    """
    Provide transactional DB session per test.

    The transaction rollback keeps tests isolated.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture()
def client(db_session: Session):
    """FastAPI TestClient with dependency override for DB session."""

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    deps._build_scan_service.cache_clear()
    app.dependency_overrides[deps.get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture()
def auth_header() -> dict[str, str]:
    """Reusable bearer token fixture for organization endpoints."""
    token = create_access_token({"sub": "student@example.edu", "role": "org_user"})
    return {"Authorization": f"Bearer {token}"}
