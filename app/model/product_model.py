from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.model.base_model import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = "categories"

    name = Column(String(100), nullable=False, unique=True)
    attachment = Column(String, nullable=True)

    # Define the relationship to Product
    products = relationship("ProductModel", back_populates="category")
