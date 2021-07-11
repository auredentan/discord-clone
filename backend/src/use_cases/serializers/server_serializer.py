from src.entities.server import PydanticServer  # type: ignore[attr-defined]
from src.entities.server import PydanticServerMember  # type: ignore[attr-defined]
from src.entities.server import PydanticServerRole  # type: ignore[attr-defined]

from src.infrastructure.adapters.database.tables.server import Server
from src.infrastructure.adapters.database.tables.server import ServerMember
from src.infrastructure.adapters.database.tables.server import ServerRole

from src.use_cases.serializers.user_serializer import user_sqlachemy_to_pydantic


def server_sqlalchemy_to_pydantic(server: Server) -> PydanticServer:
    return PydanticServer(
        id=str(server.id),
        name=server.name,
        members=[server_member_sqlalchemy_to_pydantic(m) for m in server.members],
    )


def server_member_sqlalchemy_to_pydantic(
    server_member: ServerMember,
) -> PydanticServerMember:
    return PydanticServerMember(
        id=str(server_member.id),
        name=server_member.name,
        roles=[server_role_sqlalchemy_to_pydantic(r) for r in server_member.roles],
        user_id=server_member.user_id,
        server_id=server_member.server_id,
    )


def server_role_sqlalchemy_to_pydantic(server_role: ServerRole) -> PydanticServerRole:
    return PydanticServerRole(
        id=str(server_role.id),
        name=server_role.name,
    )
