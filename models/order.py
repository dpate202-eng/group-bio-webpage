from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from db import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    customer_phone = Column(String, nullable=False)
    customer_address = Column(String, nullable=True)
    order_type = Column(Enum("delivery", "takeout", name="order_type"), default="takeout")
    status = Column(Enum("pending", "preparing", "ready", "delivered", "cancelled", name="order_status"), default="pending")
    total_price = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    promo_code_id = Column(Integer, ForeignKey("promo_codes.id"), nullable=True)