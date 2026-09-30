from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime

from backend.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    conversation_id = Column(String, primary_key=True, index=True)
    customer_id = Column(String, nullable=False)
    messages = Column(Text, nullable=True)
    context = Column(Text, nullable=True)
    status = Column(String, nullable=False, default="ACTIVE")
    escalation_reason = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )