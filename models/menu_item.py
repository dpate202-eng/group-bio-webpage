from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    category = Column(String)

    # Relationships
    order_items = relationship("OrderItem", back_populates="menu_item")
    reviews = relationship("Review", back_populates="menu_item")