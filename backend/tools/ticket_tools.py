from datetime import datetime
import uuid

from sqlalchemy.orm import Session

from backend.models.ticket import Ticket


def create_support_ticket(
    customer_id: str,
    issue: str,
    category: str,
    priority: str,
    db: Session
):
    if not customer_id:
        raise ValueError("Customer ID is required.")

    if not issue:
        raise ValueError("Issue is required.")

    if not category:
        raise ValueError("Category is required.")

    if not priority:
        raise ValueError("Priority is required.")

    ticket_id = str(uuid.uuid4())

    ticket = Ticket(
        ticket_id=ticket_id,
        customer_id=customer_id,
        issue=issue,
        category=category,
        priority=priority,
        status="OPEN",
        created_at=datetime.utcnow()
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

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