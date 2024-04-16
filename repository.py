from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import UserDTO, UserCreateDTO
from models import UserModel


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, user: UserCreateDTO) -> UserModel:
        user_data = user.model_dump()
        user_model = UserModel(**user_data)
        self.session.add(user_model)
        await self.session.flush()
        await self.session.commit()
        return await self.get_by_id(user_id=user_model.id)

    async def get_by_id(self, user_id: int) -> UserModel | None:
        query = select(UserModel).where(UserModel.id == user_id)
        result = await self.session.execute(query)
        user = result.scalars().first()
        return user
