from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="customer")

    # Relationships
    orders = relationship("Order", back_populates="user")
    reviews = relationship("Review", back_populates="user")