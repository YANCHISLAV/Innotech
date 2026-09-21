from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker


class DataBase:
    def __init__(self,
                 url: PostgresDsn,
                 echo: bool,
                 echo_pool: bool,
                 pool_size: int,
                 max_overflow: int
                 ):

        self.engine : AsyncEngine =create_async_engine(
            url=str(url),
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

    async def dispose(self):
        await self.engine.dispose()
