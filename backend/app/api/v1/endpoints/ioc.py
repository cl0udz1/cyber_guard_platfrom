"""
Purpose:
    Anonymous IoC submission endpoint for authenticated organization users.
Inputs:
    IoC JSON payload from logged-in user.
Outputs:
    IoC record ID with stored=true when accepted.
Dependencies:
    Auth dependency, anonymizer service, SQLAlchemy session.
TODO Checklist:
    - [ ] Add moderation/review queue for malicious spam IoCs.
    - [ ] Add duplicate IoC deduplication and merge strategy.
    - [ ] Add optional evidence/reference URL support (carefully sanitized).
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.ioc import Ioc
from app.schemas.auth import UserMeResponse
from app.schemas.ioc import IocSubmitRequest, IocSubmitResponse
from app.services.anonymizer import anonymize_ioc_payload

router = APIRouter(prefix="/ioc", tags=["ioc"])


@router.post("/submit", response_model=IocSubmitResponse)
async def submit_ioc(
    payload: IocSubmitRequest,
    db: Session = Depends(get_db),
    current_user: UserMeResponse = Depends(get_current_user),
) -> IocSubmitResponse:
    """
    Submit anonymized IoC.

    Privacy design:
        Caller must be authenticated to access organization area, but submitted
        IoC is stored without user/org/ip linkage.
    """
    # `current_user` is intentionally unused for persistence.
    _ = current_user

    try:
        cleaned = anonymize_ioc_payload(payload.model_dump(exclude_none=True))
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc

    row = Ioc(
        type=cleaned["type"],
        value=cleaned["value"],
        confidence=cleaned["confidence"],
        tags=cleaned.get("tags", []),
        first_seen=cleaned.get("first_seen"),
    )
    db.add(row)
    db.commit()
    db.refresh(row)

    return IocSubmitResponse(ioc_id=row.id, stored=True)
