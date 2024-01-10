from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)

from config import PostgresqlConfig


engine = create_async_engine(url=PostgresqlConfig().DSN)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
