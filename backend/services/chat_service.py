import re

from sqlalchemy.orm import Session

from backend.agent.agent import process_message
from backend.memory.conversation_memory import (
    get_or_create_conversation,
    add_message,
    get_context,
    update_context,
)
from backend.rag.retrieval import retrieve_documents
from backend.tools.order_tools import (
    check_order_status,
    get_delivery_status,
)
from backend.tools.payment_tools import check_payment_status
from backend.tools.ticket_tools import create_support_ticket
from backend.tools.escalation_tools import escalate_to_human


def handle_chat(
    message: str,
    conversation_id: str,
    customer_id: str,
    db: Session
):
    if not message:
        raise ValueError("Message is required.")

    if not conversation_id:
        raise ValueError("Conversation ID is required.")

    if not customer_id:
        raise ValueError("Customer ID is required.")

    conversation = get_or_create_conversation(
        conversation_id=conversation_id,
        customer_id=customer_id,
        db=db
    )

    add_message(
        conversation=conversation,
        role="user",
        content=message,
        db=db
    )

    agent_result = process_message(message)
    intent = agent_result["intent"]

    update_context(
        conversation=conversation,
        key="last_intent",
        value=intent,
        db=db
    )

    order_match = re.search(r"\b\d{5}\b", message)

    if order_match:
        order_id = order_match.group()

        update_context(
            conversation=conversation,
            key="order_id",
            value=order_id,
            db=db
        )

    context = get_context(conversation)

    remembered_order_id = context.get("order_id")

    if intent == "order_status" and remembered_order_id:
        order_result = check_order_status(
            order_id=remembered_order_id,
            db=db
        )

        if order_result["success"]:
            answer = (
                f"Order {order_result['order_id']} is currently "
                f"{order_result['status']}. "
                f"Product: {order_result['product']}. "
                f"Estimated delivery: "
                f"{order_result['estimated_delivery']}. "
                f"Tracking number: "
                f"{order_result['tracking_number']}."
            )
            source = "order_database"
        else:
            answer = order_result["message"]
            source = "order_database"

    elif intent == "delivery_status" and remembered_order_id:
        delivery_result = get_delivery_status(
            order_id=remembered_order_id,
            db=db
        )

        if delivery_result["success"]:
            answer = (
                f"Order {delivery_result['order_id']} is currently "
                f"{delivery_result['status']}. "
                f"Estimated delivery: "
                f"{delivery_result['estimated_delivery']}. "
                f"Tracking number: "
                f"{delivery_result['tracking_number']}."
            )
            source = "order_database"
        else:
            answer = delivery_result["message"]
            source = "order_database"

    elif intent == "payment_status" and remembered_order_id:
        payment_result = check_payment_status(
            order_id=remembered_order_id,
            db=db
        )

        if payment_result["success"]:
            answer = (
                f"Payment for order "
                f"{payment_result['order_id']} was "
                f"{payment_result['status']}. "
                f"Amount: Rs. {payment_result['amount']}. "
                f"Payment method: "
                f"{payment_result['payment_method']}. "
                f"Transaction reference: "
                f"{payment_result['transaction_reference']}."
            )
            source = "payment_database"
        else:
            answer = payment_result["message"]
            source = "payment_database"

    elif intent == "support_request":
        category = "GENERAL_SUPPORT"
        priority = "MEDIUM"

        ticket_result = create_support_ticket(
            customer_id=customer_id,
            issue=message,
            category=category,
            priority=priority,
            db=db
        )

        if ticket_result["success"]:
            answer = (
                "Your support ticket has been created successfully. "
                f"Ticket ID: {ticket_result['ticket_id']}. "
                f"Status: {ticket_result['status']}."
            )
            source = "ticket_database"
        else:
            answer = (
                "I could not create your support ticket. "
                "Please try again."
            )
            source = "ticket_database"

    elif intent == "human_escalation":
        escalation_result = escalate_to_human(
            conversation_id=conversation_id,
            reason=message,
            db=db
        )

        if escalation_result["success"]:
            answer = (
                "Your conversation has been escalated to a human "
                "support representative. "
                "Reason: "
                f"{escalation_result['reason']}"
            )
            source = "escalation_database"
        else:
            answer = (
                "I could not escalate the conversation to human support. "
                "Please try again."
            )
            source = "escalation_database"

    else:
        retrieval_results = retrieve_documents(
            query=message,
            top_k=3
        )

        documents = retrieval_results.get("documents", [[]])[0]
        metadatas = retrieval_results.get("metadatas", [[]])[0]

        if documents:
            answer = documents[0]
            source = metadatas[0].get(
                "source",
                "knowledge_base"
            )
        else:
            answer = (
                "I could not find relevant information "
                "in the knowledge base."
            )
            source = None

    add_message(
        conversation=conversation,
        role="assistant",
        content=answer,
        db=db
    )

    context = get_context(conversation)

    return {
        "conversation_id": conversation.conversation_id,
        "customer_id": conversation.customer_id,
        "message": message,
        "intent": intent,
        "answer": answer,
        "source": source,
        "context": context
    }