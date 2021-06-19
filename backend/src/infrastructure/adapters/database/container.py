import logging

from typing import Optional
from typing import AsyncIterator
from typing import List
from typing import Any


from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta

from dependency_injector import containers, providers

from src.infrastructure.configuration import DBConfiguration

from src.infrastructure.adapters.database.repositories.user import UserRepository
from src.infrastructure.adapters.database.services.user import UserService


async def init_db(
    database_host: str,
    database_name: str,
    database_user: str,
    database_password: str,
    database_verbose: bool,
    database_pool_size: int,
    database_pool_max_overflow: int,
    sa_metadata: Optional[DeclarativeMeta] = None,
) -> AsyncIterator[Engine]:
    uri = "postgresql+asyncpg://{user}:{password}@{host}/{database}".format(
        host=database_host,
        database=database_name,
        user=database_user,
        password=database_password,
    )
    engine: Engine = create_async_engine(
        uri,
        echo=database_verbose,
        pool_size=database_pool_size,
        max_overflow=database_pool_max_overflow,
    )

    if sa_metadata:
        async with engine.begin() as conn:
            await conn.run_sync(sa_metadata.create_all)

    yield engine

    await engine.dispose()


class DBContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    db = providers.Resource(
        init_db,
        database_host=config.database_host,
        database_name=config.database_name,
        database_user=config.database_user,
        database_password=config.database_password,
        database_verbose=config.database_verbose,
        database_pool_size=config.database_pool_size,
        database_pool_max_overflow=config.database_pool_max_overflow,
        sa_metadata=None,
    )

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )


def setup_db(endpoints: List[Any]):
    container = DBContainer()

    config: DBConfiguration = DBConfiguration()
    logging.debug(f"Using db on {config.database_host}/{config.database_name}")
    container.config.from_pydantic(config)

    container.wire(modules=endpoints)
