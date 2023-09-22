import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

from config import db_config

engine = create_async_engine(
    url=db_config.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

async def get123():
    async with engine.connect() as conn:
        result = await conn.execute(text('SELECT VERSION()'))
        print(result)


asyncio.run(get123())