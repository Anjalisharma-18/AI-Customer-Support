from datetime import datetime

from sqlalchemy.orm import Session

from backend.models.conversation import Conversation


def escalate_to_human(
    conversation_id: str,
    reason: str,
    db: Session
):
    if not conversation_id:
        raise ValueError("Conversation ID is required.")

    if not reason:
        raise ValueError("Escalation reason is required.")

    conversation = (
        db.query(Conversation)
        .filter(Conversation.conversation_id == conversation_id)
        .first()
    )

    if not conversation:
        return {
            "success": False,
            "message": f"Conversation {conversation_id} was not found."
        }

    conversation.status = "ESCALATED"
    conversation.escalation_reason = reason
    conversation.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(conversation)

    return {
        "success": True,
        "conversation_id": conversation.conversation_id,
        "status": conversation.status,
        "reason": conversation.escalation_reason
    }