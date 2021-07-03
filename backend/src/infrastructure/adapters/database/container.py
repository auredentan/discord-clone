import logging

from typing import Any
from typing import AsyncIterator
from typing import List
from typing import Optional

from dependency_injector import containers
from dependency_injector import providers

from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta

from src.infrastructure.adapters.database.database import AsyncDatabase
from src.infrastructure.adapters.database.repositories.server import ServerRepository
from src.infrastructure.adapters.database.repositories.server_member import (
    ServerMemberRepository,
)
from src.infrastructure.adapters.database.repositories.server_role import (
    ServerRoleRepository,
)
from src.infrastructure.adapters.database.repositories.user import UserRepository
from src.infrastructure.adapters.database.services.server import ServerService
from src.infrastructure.adapters.database.services.server_member import (
    ServerMemberService,
)
from src.infrastructure.adapters.database.services.server_role import ServerRoleService
from src.infrastructure.adapters.database.services.user import UserService
from src.infrastructure.adapters.database.tables import metadata

from src.infrastructure.configuration import DBConfiguration


async def init_db(
    database_host: str,
    database_name: str,
    database_user: str,
    database_password: str,
    database_verbose: bool,
    database_pool_size: int,
    database_pool_max_overflow: int,
    sa_metadata: Optional[DeclarativeMeta] = None,
) -> AsyncIterator[AsyncSession]:
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
            logging.info("create all")
            await conn.run_sync(sa_metadata.create_all)

    async_database = AsyncDatabase(engine)

    yield async_database

    await engine.dispose()


class DBContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    async_db = providers.Resource(
        init_db,
        database_host=config.database_host,
        database_name=config.database_name,
        database_user=config.database_user,
        database_password=config.database_password,
        database_verbose=config.database_verbose,
        database_pool_size=config.database_pool_size,
        database_pool_max_overflow=config.database_pool_max_overflow,
        sa_metadata=metadata,
    )

    # User
    user_repository: UserRepository = providers.Factory(
        UserRepository,
        session_factory=async_db.provided.session,
    )

    user_service: UserService = providers.Factory(
        UserService,
        user_repository=user_repository,
    )

    # Server
    server_repository: ServerRepository = providers.Factory(
        ServerRepository,
        session_factory=async_db.provided.session,
    )

    server_service: ServerService = providers.Factory(
        ServerService,
        server_repository=server_repository,
    )

    # Server Member
    server_member_repository: ServerMemberRepository = providers.Factory(
        ServerMemberRepository,
        session_factory=async_db.provided.session,
    )

    server_member_service: ServerMemberService = providers.Factory(
        ServerMemberService,
        server_member_repository=server_member_repository,
    )

    # Server Role
    server_role_repository: ServerRoleRepository = providers.Factory(
        ServerRoleRepository,
        session_factory=async_db.provided.session,
    )

    server_role_service: ServerRoleService = providers.Factory(
        ServerRoleService,
        server_role_repository=server_role_repository,
    )


def setup_db(injectable_modules: List[Any]) -> DBContainer:
    container = DBContainer()

    config: DBConfiguration = DBConfiguration()
    logging.debug(f"Using db on {config.database_host}/{config.database_name}")
    container.config.from_pydantic(config)

    container.wire(modules=injectable_modules)
    return container
