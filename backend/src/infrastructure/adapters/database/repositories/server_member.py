from typing import Iterator

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.adapters.database.tables.server import ServerMember


class ServerMemberRepository:
    def __init__(self, session_factory: AsyncSession) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> Iterator[ServerMember]:
        async with self.session_factory() as session:
            return await session.query(ServerMember).all()

    async def get_by_id(self, server_member_id: int) -> ServerMember:
        async with self.session_factory() as session:
            user = (
                await session.query(ServerMember)
                .filter(ServerMember.id == server_member_id)
                .first()
            )
            if not user:
                raise ServerMemberNotFoundError(server_member_id)
            return user

    async def add(self, server_role: ServerMember) -> ServerMember:
        async with self.session_factory() as session:
            session.add(server_role)
            await session.commit()
            await session.refresh(server_role)
            return server_role

    async def delete_by_id(self, server_member_id: int) -> None:
        async with self.session_factory() as session:
            entity: ServerMember = (
                await session.query(ServerMember)
                .filter(ServerMember.id == server_member_id)
                .first()
            )
            if not entity:
                raise ServerMemberNotFoundError(server_member_id)
            session.delete(entity)
            await session.commit()


class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id: int) -> None:
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class ServerMemberNotFoundError(NotFoundError):

    entity_name: str = "ServerRole"
