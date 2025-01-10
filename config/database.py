from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from config.settings import settings


engine = create_async_engine(settings.DB_URL, echo = True)

async_session = sessionmaker(
  bind=engine,
  class_ = AsyncSession,
  expire_on_commit = False
)

async def get_session() -> AsyncGenerator:
  async with async_session() as session:
    yield session
