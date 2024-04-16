import typing as t
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import UserCreateDTO
from database import get_async_session
from repository import UserRepository

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('', response_class=JSONResponse)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    user_repository = UserRepository(session=session)
    if user := await user_repository.get_by_id(user_id=user_id):
        return user
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=f"User with ID {user_id} not found"
    )


@router.post('', response_class=JSONResponse)
async def create_user(
    user: t.Annotated[UserCreateDTO, Depends()],
    session: AsyncSession = Depends(get_async_session)
):
    user_repository = UserRepository(session=session)
    return await user_repository.add_one(user=user)
