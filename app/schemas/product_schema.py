from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class ProductRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    attachment: Optional[str] = None
    category_id: UUID | str
