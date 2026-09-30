import json

from sqlalchemy.orm import Session

from backend.models.conversation import Conversation


def get_or_create_conversation(
    conversation_id: str,
    customer_id: str,
    db: Session
):
    conversation = (
        db.query(Conversation)
        .filter(Conversation.conversation_id == conversation_id)
        .first()
    )

    if conversation:
        return conversation

    conversation = Conversation(
        conversation_id=conversation_id,
        customer_id=customer_id,
        messages=json.dumps([]),
        context=json.dumps({}),
        status="ACTIVE"
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def add_message(
    conversation: Conversation,
    role: str,
    content: str,
    db: Session
):
    if not role:
        raise ValueError("Message role is required.")

    if not content:
        raise ValueError("Message content is required.")

    messages = json.loads(conversation.messages or "[]")

    messages.append({
        "role": role,
        "content": content
    })

    conversation.messages = json.dumps(messages)

    db.commit()
    db.refresh(conversation)

    return conversation


def get_messages(conversation: Conversation):
    return json.loads(conversation.messages or "[]")


def update_context(
    conversation: Conversation,
    key: str,
    value: str,
    db: Session
):
    if not key:
        raise ValueError("Context key is required.")

    context = json.loads(conversation.context or "{}")

    context[key] = value

    conversation.context = json.dumps(context)

    db.commit()
    db.refresh(conversation)

    return conversation


def get_context(conversation: Conversation):
    return json.loads(conversation.context or "{}")