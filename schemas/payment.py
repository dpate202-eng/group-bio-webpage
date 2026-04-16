from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: int
    method: str
    status: str = "pending"
    amount: float

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    payment_id: int

    class Config:
        orm_mode = True