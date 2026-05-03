from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from db import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    method = Column(Enum("cash", "credit_card", "debit_card", "online", name="payment_method"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum("pending", "completed", "failed", "refunded", name="payment_status"), default="pending")