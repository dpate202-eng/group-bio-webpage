from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PromoCodeBase(BaseModel):
    code: str
    discount: float
    expiry: Optional[datetime] = None

class PromoCodeCreate(PromoCodeBase):
    pass

class PromoCodeResponse(PromoCodeBase):
    promo_id: int

    class Config:
        orm_mode = True