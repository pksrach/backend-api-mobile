from typing import Optional

from pydantic import BaseModel, Field

class CategoryRequest(BaseModel):
    name: str = Field(default="Table")
    attachment: Optional[str] = None