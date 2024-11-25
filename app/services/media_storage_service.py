import logging
import os
import uuid
from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi import UploadFile, Request
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.custom_exceptions import CustomHTTPException
from app.models.media_storage_model import MediaStorageModel
from app.utils.common import get_file_path, is_valid_file_type

logger = logging.getLogger(__name__)


class MediaStorageService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_media_storage(self, file: UploadFile, request: Request):
        # Max file size is 3MB
        max_file_size = 3 * 1024 * 1024
        contents = await file.read()
        file_size = len(contents)

        if file_size > max_file_size:
            raise CustomHTTPException(
                status_code=400, message="File size exceeds the maximum limit of 3MB."
            )

        file_extension = os.path.splitext(file.filename)[1]
        if not is_valid_file_type(file_extension):
            raise CustomHTTPException(
                status_code=400,
                message="Invalid file type. Only JPG, JPEG, and PNG are allowed.",
            )

        unique_name = f"{uuid.uuid4()}{file_extension}"
        file_path = get_file_path(unique_name)

        # Create the MediaStorage object
        base_url = str(request.base_url)
        media_storage = MediaStorageModel(
            id=uuid.uuid4(),
            unique_name=unique_name,
            name=file.filename,
            extension=file_extension,
            uri=f"{base_url}uploads/{unique_name}",
        )

        try:
            # Save the file to the file system
            with open(file_path, "wb") as buffer:
                buffer.write(contents)

            # Add media storage record to the database
            self.session.add(media_storage)
            await self.session.commit()
            await self.session.refresh(media_storage)

            return media_storage

        except Exception as ex:
            raise CustomHTTPException(
                status_code=500,
                message=f"Failed processing file {file.filename}. {str(ex)}",
            )
