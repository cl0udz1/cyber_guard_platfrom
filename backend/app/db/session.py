"""
Purpose:
    Database engine and session factory setup for runtime and tests.
Inputs:
    Database URL from application settings.
Outputs:
    SQLAlchemy `SessionLocal` and `get_db` dependency generator.
Dependencies:
    SQLAlchemy, backend settings.
TODO Checklist:
    - [ ] Enable SQLAlchemy async engine if switching to async DB access.
    - [ ] Tune pool settings for production load.
    - [ ] Add automatic retry policy for transient DB failures.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

settings = get_settings()

connect_args: dict[str, object] = {}
if settings.database_url.startswith("sqlite"):
    # SQLite needs this flag when used in multi-threaded test client context.
    connect_args["check_same_thread"] = False

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    future=True,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a DB session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
