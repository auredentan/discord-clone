from typing import Iterator
from typing import List

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.adapters.database.tables.server import Server
from src.infrastructure.adapters.database.tables.server import ServerMember


class ServerRepository:
    def __init__(self, session_factory: AsyncSession) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> Iterator[Server]:
        async with self.session_factory() as session:
            return await session.query(Server).all()

    async def get_by_id(self, server_id: int) -> Server:
        async with self.session_factory() as session:
            server = await session.query(Server).filter(Server.id == server_id).first()
            if not server:
                raise ServerNotFoundError(server_id)
            return server

    async def add(self, server: Server) -> Server:
        async with self.session_factory() as session:
            session.add(server)
            await session.commit()
            await session.refresh(server)
            return server

    async def delete_by_id(self, server_id: int) -> None:
        async with self.session_factory() as session:
            entity: Server = (
                await session.query(Server).filter(Server.id == server_id).first()
            )
            if not entity:
                raise ServerNotFoundError(server_id)
            session.delete(entity)
            await session.commit()

    async def add_members(self, server_id: str, members: List[ServerMember]) -> Server:
        async with self.session_factory() as session:
            server = await session.query(Server).filter(Server.id == server_id).first()
            if not server:
                raise ServerNotFoundError(int(server_id))

            # Update
            full_members: List[ServerMember] = server.members or [] + members
            query = (
                update(Server)
                .where(Server.id == server_id)
                .values(members=full_members)
            )

            await session.execute(query)
            await session.refresh(server)
            return server


class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id: int) -> None:
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class ServerNotFoundError(NotFoundError):

    entity_name: str = "Server"
