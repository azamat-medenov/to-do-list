from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncEngine,
)

from config import db_config

engine = create_async_engine(
    url=db_config.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

sessionmaker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker() as session:
        yield session
