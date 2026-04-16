from sqlalchemy import Column, Integer, String, Float, DateTime
from db import Base

class PromoCode(Base):
    __tablename__ = "promo_codes"

    promo_id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
    discount = Column(Float, nullable=False)
    expiry = Column(DateTime)