from backend.agent.intent import detect_intent


def process_message(text: str):
    if not text:
        raise ValueError("Message is required.")

    intent = detect_intent(text)

    decisions = {
        "order_status": "check_order_status",
        "payment_status": "check_payment_status",
        "delivery_status": "get_delivery_status",
        "support_request": "create_support_ticket",
        "human_escalation": "escalate_to_human",
        "refund_request": "search_knowledge_base",
        "knowledge_base_query": "search_knowledge_base",
        "general_faq": "search_knowledge_base",
        "unknown": "search_knowledge_base",
    }

    action = decisions.get(
        intent.value,
        "search_knowledge_base"
    )

    return {
        "message": text,
        "intent": intent.value,
        "action": action
    }