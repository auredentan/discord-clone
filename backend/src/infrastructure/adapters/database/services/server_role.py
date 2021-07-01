import logging

from uuid import uuid4
from typing import Iterator
from typing import Optional

from src.infrastructure.adapters.database.repositories.server_role import (
    ServerRoleNotFoundError,
)
from src.infrastructure.adapters.database.repositories.server_role import (
    ServerRoleRepository,
)

from src.infrastructure.adapters.database.tables.server import ServerRole


class ServerRoleService:
    def __init__(self, server_role_repository: ServerRoleRepository) -> None:
        self._repository: ServerRoleRepository = server_role_repository

    async def get_server_roles(self) -> Iterator[ServerRole]:
        return await self._repository.get_all()

    async def get_server_role_by_id(self, server_role_id: int) -> Optional[ServerRole]:
        try:
            return await self._repository.get_by_id(server_role_id)
        except ServerRoleNotFoundError:
            logging.warning(f"ServerRole {server_role_id} not found")
            return None

    async def create_server_role(self, name: str) -> ServerRole:
        uid = uuid4()

        server = ServerRole(id=uid, name=name)

        return await self._repository.add(server)

    async def delete_server_role_by_id(self, server_role_id: int) -> None:
        try:
            return await self._repository.delete_by_id(server_role_id)
        except ServerRoleNotFoundError:
            logging.warning(f"ServerRole {server_role_id} not found")
            raise
