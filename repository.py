from schemas import UserDTO, UserCreateDTO


class UserRepository:
    async def add_one(self, user: UserCreateDTO) -> UserCreateDTO:
        ...

    async def get_by_id(self, user_id: int) -> UserDTO:
        ...
