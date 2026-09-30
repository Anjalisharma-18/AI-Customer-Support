from sqlalchemy.orm import Session

from backend.models.order import Order


def check_order_status(order_id: str, db: Session):
    if not order_id:
        raise ValueError("Order ID is required.")

    order = db.query(Order).filter(Order.order_id == order_id).first()

    if not order:
        return {
            "success": False,
            "message": f"Order {order_id} was not found."
        }

    return {
        "success": True,
        "order_id": order.order_id,
        "customer_id": order.customer_id,
        "product": order.product,
        "status": order.status,
        "order_date": str(order.order_date),
        "estimated_delivery": (
            str(order.estimated_delivery)
            if order.estimated_delivery
            else None
        ),
        "tracking_number": order.tracking_number
    }


def get_delivery_status(order_id: str, db: Session):
    if not order_id:
        raise ValueError("Order ID is required.")

    order = db.query(Order).filter(Order.order_id == order_id).first()

    if not order:
        return {
            "success": False,
            "message": f"Order {order_id} was not found."
        }

    return {
        "success": True,
        "order_id": order.order_id,
        "status": order.status,
        "estimated_delivery": (
            str(order.estimated_delivery)
            if order.estimated_delivery
            else None
        ),
        "tracking_number": order.tracking_number
    }