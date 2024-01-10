from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession

from database import sessionmaker


class Session(ABC):
    async def create_session() -> AsyncSession:
        async with sessionmaker() as session:
            yield session
            await session.commit()


class SessionReadOnly(ABC):
    async def create_session() -> AsyncSession:
        async with sessionmaker() as session:
            await session.execute("SET TRANSACTION READ ONLY")
            yield session
