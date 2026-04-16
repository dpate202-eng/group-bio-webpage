from pydantic import BaseModel

class OrderItemBase(BaseModel):
    order_id: int
    item_id: int
    quantity: int = 1

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    order_item_id: int

    class Config:
        orm_mode = True