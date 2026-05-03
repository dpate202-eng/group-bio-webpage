from sqlalchemy import Column, Integer, String, Float, Boolean
from db import Base

class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
    discount_percent = Column(Float, nullable=False)
    active = Column(Boolean, default=True)