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
    - [ ] Add async engine support if the team moves long-running orchestration off-thread.
    - [ ] Add separate storage/schema handling for public threat data if needed later.
    - [ ] Tune connection pooling before deployment beyond classroom demos.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

settings = get_settings()

connect_args: dict[str, object] = {}
if settings.database_url.startswith("sqlite"):
    connect_args["check_same_thread"] = False

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    future=True,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)


def get_db() -> Generator[Session, None, None]:
    """Yield one database session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
