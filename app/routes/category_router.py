import logging
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.config.database import get_session
from app.schemas.category_schema import CategoryRequest
from app.services.category_service import CategoryService


category_router = APIRouter(
    prefix="/categories",
    tags=["Category API"],
    responses={404: {"description": "Not found"}},
)


@category_router.get("", status_code=200)
async def get_categories(session: AsyncSession = Depends(get_session)):
    service = CategoryService(session)

    return await service.get_categories()


@category_router.get("/{id}", status_code=200)
async def get_category(id, session: AsyncSession = Depends(get_session)):
    service = CategoryService(session)

    return await service.get_category(id)


@category_router.post("", status_code=201)
async def create_category(
    req: CategoryRequest, session: AsyncSession = Depends(get_session)
):
    service = CategoryService(session)

    return await service.create_category(req)


@category_router.put("", status_code=200)
async def update_category(
    id, req: CategoryRequest, session: AsyncSession = Depends(get_session)
):
    service = CategoryService(session)

    return await service.update_category(id, req)


@category_router.delete("/{id}", status_code=200)
async def delete_category(id: str, session: AsyncSession = Depends(get_session)):
    try:
        uuid_id = uuid.UUID(id)
    except ValueError:
        return {
            "data": None,
            "message": "Invalid ID format",
        }
    service = CategoryService(session)
    response = await service.delete_category(id=str(uuid_id))
    return response
