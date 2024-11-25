from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Request, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_session
from app.services.media_storage_service import MediaStorageService


media_router = APIRouter(
    prefix="/media-storage",
    tags=["Media Storage API"],
    responses={404: {"description": "Not found"}},
)


@media_router.post("", status_code=201)
async def upload_media_storage(
    file: UploadFile,
    request: Request,
    session: AsyncSession = Depends(get_session),
):
    service = MediaStorageService(session)
    return await service.create_media_storage(file, request)
