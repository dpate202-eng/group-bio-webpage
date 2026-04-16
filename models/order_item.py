from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("menu_items.item_id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    # Relationships
    order = relationship("Order", back_populates="order_items")
    menu_item = relationship("MenuItem", back_populates="order_items")