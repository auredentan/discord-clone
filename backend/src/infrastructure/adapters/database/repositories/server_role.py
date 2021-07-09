from typing import Iterator

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.adapters.database.tables.server import ServerRole
from src.infrastructure.adapters.database.repositories.errors import NotFoundError


class ServerRoleRepository:
    def __init__(self, session_factory: AsyncSession) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> Iterator[ServerRole]:
        async with self.session_factory() as session:
            return await session.query(ServerRole).all()

    async def get_by_id(self, server_role_id: int) -> ServerRole:
        async with self.session_factory() as session:
            user = (
                await session.query(ServerRole)
                .filter(ServerRole.id == server_role_id)
                .first()
            )
            if not user:
                raise ServerRoleNotFoundError(server_role_id)
            return user

    async def add(self, server_role: ServerRole) -> ServerRole:
        async with self.session_factory() as session:
            session.add(server_role)
            await session.commit()
            await session.refresh(server_role)
            return server_role

    async def delete_by_id(self, server_role_id: int) -> None:
        async with self.session_factory() as session:
            entity: ServerRole = (
                await session.query(ServerRole)
                .filter(ServerRole.id == server_role_id)
                .first()
            )
            if not entity:
                raise ServerRoleNotFoundError(server_role_id)
            session.delete(entity)
            await session.commit()


class ServerRoleNotFoundError(NotFoundError):

    entity_name: str = "ServerRole"
