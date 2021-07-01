from typing import Optional

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject


from src.entities.server import PydanticServer

from src.infrastructure.adapters.database.services.server_role import (
    ServerRoleService,
)
from src.infrastructure.adapters.database.services.server_member import (
    ServerMemberService,
)
from src.infrastructure.adapters.database.services.server import ServerService

from src.infrastructure.adapters.database.tables.user import User

from src.infrastructure.adapters.database.container import DBContainer


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
        name="admin"
    )
    connected_user_server_member = await server_member_service.create_server_member(
        connected_user.email, roles=[connected_user_server_member_role]
    )
    created_server = await server_service.add_members([connected_user_server_member])

    return PydanticServer.from_orm(created_server) if created_server else None
