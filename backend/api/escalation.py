from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.tools.escalation_tools import escalate_to_human


router = APIRouter()


class EscalationRequest(BaseModel):
    conversation_id: str
    reason: str


@router.post("/escalate")
def escalate(
    request: EscalationRequest,
    db: Session = Depends(get_db)
):
    result = escalate_to_human(
        conversation_id=request.conversation_id,
        reason=request.reason,
        db=db
    )

    if not result["success"]:
        raise HTTPException(
            status_code=404,
            detail=result["message"]
        )

    return result