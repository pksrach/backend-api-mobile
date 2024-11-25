import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel


class MediaStorageModel(BaseModel):
    __tablename__ = "media_storages"

    name = Column(String, nullable=True)
    unique_name = Column(String, nullable=True)
    extension = Column(String, nullable=True)
    uri = Column(String, nullable=True)
