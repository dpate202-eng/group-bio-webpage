from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    user_id: int
    item_id: int
    rating: int
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    review_id: int

    class Config:
        orm_mode = True