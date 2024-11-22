from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.config.database import get_session
from app.services.product_service import ProductService


product_router = APIRouter(
    prefix="/products",
    tags=["Product API"],
    responses={404: {"description": "Not found"}},
)


@product_router.get("", status_code=200)
async def get_products(session: AsyncSession = Depends(get_session)):
    product_service = ProductService(session)

    return await product_service.get_products()
