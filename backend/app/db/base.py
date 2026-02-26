"""
Purpose:
    SQLAlchemy Declarative Base class shared by all ORM models.
Inputs:
    ORM model declarations import this base and inherit from it.
Outputs:
    Base metadata used for table creation and migrations.
Dependencies:
    SQLAlchemy ORM.
TODO Checklist:
    - [ ] Add naming conventions for constraints/indexes for Alembic stability.
    - [ ] Split models into bounded contexts as project grows.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Common declarative base for all tables."""
