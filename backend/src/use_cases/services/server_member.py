import logging
from typing import Iterator, List, Optional
from uuid import uuid4

from src.infrastructure.adapters.database.repositories.server_member import (
    ServerMemberNotFoundError,
    ServerMemberRepository,
)
from src.infrastructure.adapters.database.tables.server import ServerMember, ServerRole
from src.infrastructure.adapters.database.tables.user import User


class ServerMemberService:
    def __init__(self, server_member_repository: ServerMemberRepository) -> None:
        self._repository: ServerMemberRepository = server_member_repository

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

        server = ServerMember(id=uid, name=user.email, roles=roles, user_id=user.id)

        return await self._repository.add(server)

    async def delete_server_member_by_id(self, server_member_id: int) -> None:
        try:
            return await self._repository.delete_by_id(server_member_id)
        except ServerMemberNotFoundError:
            logging.warning(f"ServerMember {server_member_id} not found")
            raise
