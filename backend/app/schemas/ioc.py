"""
Purpose:
    Pydantic schemas for anonymous IoC submission and display.
Inputs:
    JSON payloads from `/api/v1/ioc/submit`.
Outputs:
    Validated IoC objects with strict field filtering.
Dependencies:
    Pydantic model validation.
TODO Checklist:
    - [ ] Add stricter per-type validators (IP/domain/hash formats).
    - [ ] Add optional source confidence rationale field.
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

IocType = Literal["ip", "domain", "url", "hash", "email", "file_name", "other"]


class IocSubmitRequest(BaseModel):
    """
    Request body for anonymous IoC submission.

    Security:
        `extra="forbid"` blocks unrecognized keys before service handling.
    """

    model_config = ConfigDict(extra="forbid")

    type: IocType
    value: str = Field(..., min_length=1)
    confidence: int = Field(..., ge=0, le=100)
    tags: list[str] = Field(default_factory=list)
    first_seen: datetime | None = None

    @field_validator("value")
    @classmethod
    def value_must_not_be_blank(cls, value: str) -> str:
        """Guard against whitespace-only IoC values."""
        normalized = value.strip()
        if not normalized:
            raise ValueError("IoC value cannot be blank.")
        return normalized


class IocSubmitResponse(BaseModel):
    """Response body for successful IoC submission."""

    ioc_id: str
    stored: bool = True


class IocPublicRecord(BaseModel):
    """Public IoC shape returned by dashboard endpoints."""

    ioc_id: str
    type: IocType
    value: str
    confidence: int
    tags: list[str]
    first_seen: datetime | None
    created_at: datetime
