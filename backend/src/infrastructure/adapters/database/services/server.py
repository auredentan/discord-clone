import logging

from uuid import uuid4
from typing import Iterator
from typing import List
from typing import Optional

from src.infrastructure.adapters.database.repositories.server import ServerRepository
from src.infrastructure.adapters.database.repositories.server import ServerNotFoundError

from src.infrastructure.adapters.database.tables.server import Server
from src.infrastructure.adapters.database.tables.server import ServerMember


class ServerService:
    def __init__(self, server_repository: ServerRepository) -> None:
        self._repository: ServerRepository = server_repository

    async def get_servers(self) -> Iterator[Server]:
        return await self._repository.get_all()

    async def get_server_by_id(self, server_id: int) -> Optional[Server]:
        try:
            return await self._repository.get_by_id(server_id)
        except ServerNotFoundError:
            logging.warning(f"Server {server_id} not found")
            return None

    async def create_server(self, name: str, members: List[ServerMember]) -> Server:
        uid = uuid4()

        server = Server(id=uid, name=name, members=members)

        return await self._repository.add(server)

    async def delete_server_by_id(self, server_id: int) -> None:
        try:
            return await self._repository.delete_by_id(server_id)
        except ServerNotFoundError:
            logging.warning(f"Server {server_id} not found")
            raise

    async def add_members(self, server_id: str, members: List[ServerMember]) -> Server:
        return await self._repository.add_members(server_id, members)
