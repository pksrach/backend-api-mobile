from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from app.models.category_model import CategoryModel  # Ensure this import is correct

class ProductModel(BaseModel):
    __tablename__ = "products"

    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    attachment = Column(String)

    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))

    # Define the relationship to Category
    category = relationship("CategoryModel", back_populates="products")