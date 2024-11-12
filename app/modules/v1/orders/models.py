from datetime import datetime
from typing import Literal, Optional

from core.schemas import ObjectIdStr
from pydantic import BaseModel


class Orders(BaseModel):
    status: Literal["active", "pending"]
    amount: int
    discount_amount: Optional[int] = None
    tax_rate: float
    vat_amount: int
    total_amount: int
    promotion_code: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    created_by: ObjectIdStr
    updated_at: Optional[datetime] = None
    updated_by: Optional[ObjectIdStr] = None
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[ObjectIdStr] = None
