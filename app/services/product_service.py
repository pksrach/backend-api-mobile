from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product_model import ProductModel


class ProductService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_products(self):
        stmt = (
            select(ProductModel)
            # .options(selectinload(ProductModel.category))
            .order_by(ProductModel.created_at.desc())
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
