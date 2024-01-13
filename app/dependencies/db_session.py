from abc import ABC

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from app.config import PostgresqlConfig


class DatabaseConnector(ABC):
    engine = create_async_engine(url=PostgresqlConfig().DSN)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)


class Session(ABC):
    async def create_session() -> AsyncSession:
        async with DatabaseConnector.sessionmaker() as session:
            yield session
            await session.commit()


class SessionReadOnly(ABC):
    async def create_session() -> AsyncSession:
        async with DatabaseConnector.sessionmaker() as session:
            await session.execute(text("SET TRANSACTION READ ONLY"))
            yield session
