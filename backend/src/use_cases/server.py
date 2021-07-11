from typing import Optional

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject

from src.entities.server import BaseServerRole  # type: ignore[attr-defined]
from src.entities.server import PydanticServer  # type: ignore[attr-defined]

from src.infrastructure.adapters.database.container import DBContainer
from src.infrastructure.adapters.database.tables.user import User

from src.use_cases.services.server import ServerService
from src.use_cases.services.server_member import (
    ServerMemberService,
)
from src.use_cases.services.server_role import ServerRoleService

from src.use_cases.serializers.server_serializer import server_sqlalchemy_to_pydantic


@inject
async def create_server(
    name: str,
    connected_user: User,
    server_service: ServerService = Provide[DBContainer.server_service],
    server_member_service: ServerMemberService = Provide[
        DBContainer.server_member_service
    ],
    server_role_service: ServerRoleService = Provide[DBContainer.server_role_service],
) -> Optional[PydanticServer]:

    # Server
    created_server = await server_service.create_server(name=name, members=[])

    # Add the user as admin
    connected_user_server_member_role = await server_role_service.create_server_role(
        name=BaseServerRole.admin.value
    )
    connected_user_server_member = await server_member_service.create_server_member(
        connected_user.email,
        roles=[connected_user_server_member_role],
        user=connected_user,
    )
    created_server = await server_service.add_members(
        created_server.id, [connected_user_server_member]
    )

    return server_sqlalchemy_to_pydantic(created_server) if created_server else None
