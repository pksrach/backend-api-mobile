import logging
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category_model import CategoryModel
from app.schemas.category_schema import CategoryRequest


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_categories(self):
        stmt = select(CategoryModel).order_by(CategoryModel.created_at.desc())
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def get_category(self, id):
        stmt = select(CategoryModel).where(CategoryModel.id == id)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def create_category(self, req: CategoryRequest):
        stmt = select(CategoryModel).where(CategoryModel.name == req.name)
        result = await self.session.execute(stmt)
        category = result.scalar()
        if category:
            return {
                "data": None,
                "message": "Category already exists",
            }

        category = CategoryModel(name=req.name, attachment=req.attachment)
        self.session.add(category)
        await self.session.commit()
        return {
            "data": category,
            "message": "Category created successfully",
        }

    async def update_category(self, id, req: CategoryRequest):
        stmt = select(CategoryModel).where(CategoryModel.id == id)
        result = await self.session.execute(stmt)
        category = result.scalar()
        if not category:
            return {
                "data": None,
                "message": "Category not found",
            }

        if req.name != category.name:
            stmt = select(CategoryModel).where(CategoryModel.name == req.name)
            result = await self.session.execute(stmt)
            existing_category = result.scalar()
            if existing_category:
                return {
                    "data": None,
                    "message": "Category already exists",
                }

        category.name = req.name
        category.attachment = req.attachment if req.attachment else category.attachment
        await self.session.commit()
        return {
            "data": category,
            "message": "Category updated successfully",
        }

    async def delete_category(self, id):
        stmt = select(CategoryModel).where(CategoryModel.id == id)
        result = await self.session.execute(stmt)
        category = result.scalar()
        if not category:
            return {
                "data": None,
                "message": "Category not found",
            }

        await self.session.delete(category)
        await self.session.commit()
        return {
            "data": None,
            "message": "Category deleted successfully",
        }
