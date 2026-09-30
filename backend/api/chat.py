from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.services.chat_service import handle_chat


router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    conversation_id: str
    customer_id: str


@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    return handle_chat(
        message=request.message,
        conversation_id=request.conversation_id,
        customer_id=request.customer_id,
        db=db
    )