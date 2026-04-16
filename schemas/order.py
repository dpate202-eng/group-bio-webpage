from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    user_id: int
    status: str = "confirmed"
    delivery_method: str

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    order_id: int
    created_at: datetime

    class Config:
        orm_mode = True