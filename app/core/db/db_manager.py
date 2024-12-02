from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
from app.core import settings

class DBManager:
    def __init__(self, url: str, echo: bool, echo_pool:bool, pool_size:int, max_overflow:int):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_siz=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autocommit = False,
            autoflush = False,
            expire_on_commit=False,
        )

    async def dispone(self):
        await self.engine.dispose()

    async def get_session(self):
        async with self.session_factory() as session:
            yield session

db_manager = DBManager(
    url=settings.db.url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)