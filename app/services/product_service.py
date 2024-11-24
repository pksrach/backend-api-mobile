from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category_model import CategoryModel
from app.models.product_model import ProductModel
from app.schemas.product_schema import ProductRequest


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

    async def get_product(self, product_id):
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def create_product(self, req: ProductRequest):
        stmt = select(ProductModel).where(ProductModel.name == req.name)
        result = await self.session.execute(stmt)
        product = result.scalars().first()

        if product:
            return {
                "data": None,
                "message": "Product already exists",
            }

        # Check exist category or not based on req.category_id
        # If not exist, return error message
        # If exist, create new product
        category_stmt = select(CategoryModel).where(CategoryModel.id == req.category_id)
        category_result = await self.session.execute(category_stmt)
        category = category_result.scalars().first()

        if not category:
            return {
                "data": None,
                "message": "Category does not exist",
            }

        product = ProductModel(
            name=req.name,
            description=req.description,
            price=req.price,
            category_id=req.category_id,
        )

        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)

        return {
            "data": product,
            "message": "Product created successfully",
        }

    async def update_product(self, product_id, req: ProductRequest):
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        product = result.scalars().first()

        if not product:
            return {
                "data": None,
                "message": "Product does not exist",
            }

        if product.name != req.name:
            stmt = select(ProductModel).where(ProductModel.name == req.name)
            result = await self.session.execute(stmt)
            existing_product = result.scalars().first()

            if existing_product:
                return {
                    "data": None,
                    "message": "Product already exists",
                }
        # Check exist category or not based on req.category_id
        # If not exist, return error message
        # If exist, update product
        category_stmt = select(CategoryModel).where(CategoryModel.id == req.category_id)
        category_result = await self.session.execute(category_stmt)
        category = category_result.scalars().first()

        if not category:
            return {
                "data": None,
                "message": "Category does not exist",
            }

        product.name = req.name
        product.description = req.description
        product.price = req.price
        product.category_id = req.category_id

        await self.session.commit()

        return {
            "data": product,
            "message": "Product updated successfully",
        }

    async def delete_product(self, product_id):
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        product = result.scalars().first()

        if not product:
            return {
                "data": None,
                "message": "Product does not exist",
            }

        await self.session.delete(product)
        await self.session.commit()

        return {
            "data": None,
            "message": "Product deleted successfully",
        }
