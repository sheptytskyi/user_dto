import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker

from backend.database import Base
from models.user import UserModel
from services.user import UserRepository


@pytest.fixture
async def async_engine() -> None:
    engine = create_async_engine('sqlite+aiosqlite:///:memory:', echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest.fixture
async def async_session(async_engine: AsyncEngine) -> None:
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session


@pytest.fixture(scope='session')
async def create_user(async_session: AsyncSession) -> UserModel:
    model = UserModel(username='test_user')
    async_session.add(model)
    await async_session.flush()
    await async_session.commit()
    return model


@pytest.fixture(scope='session')
async def user_repository(async_session: AsyncSession) -> UserRepository:
    return UserRepository(session=async_session)
