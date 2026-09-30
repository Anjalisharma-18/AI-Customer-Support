from sqlalchemy.orm import Session

from backend.models.payment import Payment


def check_payment_status(order_id: str = None, payment_id: str = None, db: Session = None):
    if not order_id and not payment_id:
        raise ValueError("Order ID or Payment ID is required.")

    query = db.query(Payment)

    if payment_id:
        payment = query.filter(Payment.payment_id == payment_id).first()
    else:
        payment = query.filter(Payment.order_id == order_id).first()

    if not payment:
        return {
            "success": False,
            "message": "Payment information was not found."
        }

    return {
        "success": True,
        "payment_id": payment.payment_id,
        "order_id": payment.order_id,
        "amount": payment.amount,
        "status": payment.status,
        "payment_method": payment.payment_method,
        "transaction_reference": payment.transaction_reference
    }