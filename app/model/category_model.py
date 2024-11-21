from sqlalchemy import UUID, Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from app.model.base_model import BaseModel


class ProductModel(BaseModel):
    __tablename__ = "products"

    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    attachment = Column(String)

    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))

    # Define the relationship to Product
    category = relationship("CategoryModel", back_populates="products")
