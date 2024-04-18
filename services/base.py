from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from backend.database import Base as Model


class BaseRepository:
    model: Model

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, data: BaseModel) -> Model:
        data_dict = data.model_dump()
        model = self.model(**data_dict)
        self.session.add(model)
        await self.session.flush()
        await self.session.commit()
        return await self.get_by_id(obj_id=model.id)

    async def get_by_id(self, obj_id: int) -> Model | None:
        query = select(self.model).where(self.model.id == obj_id)
        result = await self.session.execute(query)
        instance = result.scalars().first()
        return instance
