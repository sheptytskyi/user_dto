import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker

from models.user import UserModel
from services.user import UserRepository
from schemas.user import UserCreateDTO
from backend.database import Base


@pytest.fixture
async def async_engine():
    engine = create_async_engine('sqlite+aiosqlite:///:memory:', echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest.fixture
async def async_session(async_engine: AsyncEngine):
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session


@pytest.fixture
async def create_user(async_session: AsyncSession) -> UserModel:
    model = UserModel(username='test_user')
    async_session.add(model)
    await async_session.flush()
    await async_session.commit()
    return model


@pytest.fixture
async def user_repository(async_session: AsyncSession) -> UserRepository:
    async with async_session as session:
        return UserRepository(session=session)


@pytest.mark.asyncio
async def test_get_user_by_id(create_user: UserModel, user_repository: UserRepository):
    instance = await user_repository.get_by_id(obj_id=create_user.id)
    assert instance == create_user


@pytest.mark.asyncio
async def test_add_user(user_repository: UserRepository):
    test_user = UserCreateDTO(username='test_user')
    instance: UserModel = await user_repository.add_one(test_user)
    assert instance.username == test_user.username
