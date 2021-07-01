from backend.src.infrastructure.adapters.database.tables.user import User
import logging

from uuid import uuid4
from typing import Iterator
from typing import List
from typing import Optional

from src.infrastructure.adapters.database.repositories.server_member import (
    ServerMemberNotFoundError,
)
from src.infrastructure.adapters.database.repositories.server_member import (
    ServerMemberRepository,
)

from src.infrastructure.adapters.database.tables.server import ServerMember
from src.infrastructure.adapters.database.tables.server import ServerRole


class ServerMemberService:
    def __init__(self, server_role_repository: ServerMemberRepository) -> None:
        self._repository: ServerMemberRepository = server_role_repository

    async def get_server_members(self) -> Iterator[ServerMember]:
        return await self._repository.get_all()

    async def get_server_member_by_id(
        self, server_member_id: int
    ) -> Optional[ServerMember]:
        try:
            return await self._repository.get_by_id(server_member_id)
        except ServerMemberNotFoundError:
            logging.warning(f"ServerMember {server_member_id} not found")
            return None

    async def create_server_member(
        self, name: str, roles: List[ServerRole], user: User
    ) -> ServerMember:
        uid = uuid4()

        server = ServerMember(id=uid, name=name, roles=roles, user=user)

        return await self._repository.add(server)

    async def delete_server_member_by_id(self, server_member_id: int) -> None:
        try:
            return await self._repository.delete_by_id(server_member_id)
        except ServerMemberNotFoundError:
            logging.warning(f"ServerMember {server_member_id} not found")
            raise
