from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.ticket import Ticket
from backend.tools.ticket_tools import create_support_ticket


router = APIRouter()


class TicketCreateRequest(BaseModel):
    customer_id: str
    issue: str
    category: str
    priority: str


@router.post("/tickets")
def create_ticket(
    request: TicketCreateRequest,
    db: Session = Depends(get_db)
):
    result = create_support_ticket(
        customer_id=request.customer_id,
        issue=request.issue,
        category=request.category,
        priority=request.priority,
        db=db
    )

    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail="Could not create support ticket."
        )

    return result


@router.get("/tickets/{ticket_id}")
def get_ticket(
    ticket_id: str,
    db: Session = Depends(get_db)
):
    ticket = (
        db.query(Ticket)
        .filter(Ticket.ticket_id == ticket_id)
        .first()
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail=f"Ticket {ticket_id} was not found."
        )

    return {
        "success": True,
        "ticket_id": ticket.ticket_id,
        "customer_id": ticket.customer_id,
        "issue": ticket.issue,
        "category": ticket.category,
        "priority": ticket.priority,
        "status": ticket.status,
        "created_at": ticket.created_at.isoformat()
    }