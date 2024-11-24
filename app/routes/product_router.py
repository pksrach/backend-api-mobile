from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.config.database import get_session
from app.schemas.product_schema import ProductRequest
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


@product_router.get("/{product_id}", status_code=200)
async def get_product(product_id, session: AsyncSession = Depends(get_session)):
    product_service = ProductService(session)

    return await product_service.get_product(product_id)


@product_router.post("", status_code=201)
async def create_product(
    req: ProductRequest, session: AsyncSession = Depends(get_session)
):
    product_service = ProductService(session)

    return await product_service.create_product(req)


@product_router.put("/{product_id}", status_code=200)
async def update_product(
    product_id, req: ProductRequest, session: AsyncSession = Depends(get_session)
):
    product_service = ProductService(session)

    return await product_service.update_product(product_id, req)


@product_router.delete("/{product_id}", status_code=200)
async def delete_product(product_id, session: AsyncSession = Depends(get_session)):
    product_service = ProductService(session)

    return await product_service.delete_product(product_id)