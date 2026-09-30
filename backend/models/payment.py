from sqlalchemy import Column, String, Float

from backend.database import Base


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(String, primary_key=True, index=True)
    order_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    payment_method = Column(String, nullable=False)
    transaction_reference = Column(String, nullable=True)