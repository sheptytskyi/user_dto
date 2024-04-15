import typing as t
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from schemas import UserCreateDTO, UserDTO


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('', response_class=JSONResponse)
def get_user_by_id(user_id: int) -> UserDTO:
    return UserDTO


@router.post('', response_class=JSONResponse)
def create_user(user: t.Annotated[UserCreateDTO, Depends()]):
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=UserCreateDTO)
