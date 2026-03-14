"""
Purpose:
    SQLAlchemy declarative base shared by the refreshed scaffold models.
Inputs:
    ORM model declarations from `app.models`.
Outputs:
    Metadata object used by tests and future Alembic migrations.
Dependencies:
    SQLAlchemy ORM.
TODO Checklist:
    - [ ] Add naming conventions for stable Alembic diffs.
    - [ ] Split metadata if the public-share schema becomes physically separate.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Common declarative base for Cyber Guard ORM tables."""
