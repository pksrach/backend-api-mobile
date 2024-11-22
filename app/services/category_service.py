from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category_model import CategoryModel


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_categories(self):
        stmt = select(CategoryModel).order_by(CategoryModel.created_at.desc())
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
