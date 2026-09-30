from enum import Enum


class Intent(str, Enum):
    GENERAL_FAQ = "general_faq"
    KNOWLEDGE_BASE_QUERY = "knowledge_base_query"
    REFUND_REQUEST = "refund_request"
    ORDER_STATUS = "order_status"
    PAYMENT_STATUS = "payment_status"
    DELIVERY_STATUS = "delivery_status"
    SUPPORT_REQUEST = "support_request"
    HUMAN_ESCALATION = "human_escalation"
    UNKNOWN = "unknown"


def detect_intent(message: str) -> Intent:
    text = message.lower()

    if "human" in text or "agent" in text or "speak to someone" in text:
        return Intent.HUMAN_ESCALATION

    if "refund" in text or "money back" in text:
        return Intent.REFUND_REQUEST

    if "payment" in text or "paid" in text:
        return Intent.PAYMENT_STATUS

    if "delivery" in text or "arrive" in text or "when will it come" in text:
        return Intent.DELIVERY_STATUS

    if "order" in text and ("status" in text or "where" in text):
        return Intent.ORDER_STATUS

    if "ticket" in text or "complaint" in text or "problem" in text:
        return Intent.SUPPORT_REQUEST

    if "shipping" in text or "cancel" in text or "policy" in text:
        return Intent.KNOWLEDGE_BASE_QUERY

    if "hello" in text or "hi" in text or "help" in text:
        return Intent.GENERAL_FAQ

    return Intent.UNKNOWN