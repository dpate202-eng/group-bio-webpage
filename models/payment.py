from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    method = Column(String, nullable=False)
    status = Column(String, default="pending")
    amount = Column(Float, nullable=False)

    # Relationships
    order = relationship("Order", back_populates="payment")