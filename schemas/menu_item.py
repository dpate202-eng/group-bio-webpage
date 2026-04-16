from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemResponse(MenuItemBase):
    item_id: int

    class Config:
        orm_mode = True