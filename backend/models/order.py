from sqlalchemy import Column, String, Date

from backend.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(String, primary_key=True, index=True)
    customer_id = Column(String, nullable=False)
    product = Column(String, nullable=False)
    order_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    estimated_delivery = Column(Date, nullable=True)
    tracking_number = Column(String, nullable=True)