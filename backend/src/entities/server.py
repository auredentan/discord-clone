from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from src.infrastructure.adapters.database.tables.server import Server
from src.infrastructure.adapters.database.tables.server import ServerMember
from src.infrastructure.adapters.database.tables.server import ServerRole


_PydanticServer = sqlalchemy_to_pydantic(Server)


class PydanticServer(_PydanticServer):
    @classmethod
    def from_orm(cls, server: _PydanticServer) -> _PydanticServer:
        server.id = str(server.id)
        return _PydanticServer.from_orm(server)


_PydanticServerMember = sqlalchemy_to_pydantic(ServerMember)


class PydanticServerMember(_PydanticServerMember):
    @classmethod
    def from_orm(cls, server_member: _PydanticServerMember) -> _PydanticServerMember:
        server_member.id = str(server_member.id)
        return _PydanticServerMember.from_orm(server_member)


_PydanticServerRole = sqlalchemy_to_pydantic(ServerRole)


class PydanticServerRole(_PydanticServerRole):
    @classmethod
    def from_orm(cls, server_role: _PydanticServerRole) -> _PydanticServerRole:
        server_role.id = str(server_role.id)
        return _PydanticServerRole.from_orm(server_role)
