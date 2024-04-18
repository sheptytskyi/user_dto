from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    username: str


class UserDTO(UserCreateDTO):
    id: int
