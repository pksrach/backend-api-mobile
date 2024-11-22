from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.config.database import get_session
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
