from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("menu_items.item_id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String)

    # Relationships
    user = relationship("User", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")