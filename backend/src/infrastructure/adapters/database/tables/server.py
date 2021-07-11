from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import Boolean

from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from sqlalchemy_utils import UUIDType

from src.infrastructure.adapters.database.tables.base import Auditable
from src.infrastructure.adapters.database.tables.user import User

from . import metadata

server_member_role_association_table = Table(
    "server_member_role_association",
    metadata,
    Column("server_role_id", UUIDType, ForeignKey("serverRole.id")),
    Column("server_member_id", UUIDType, ForeignKey("serverMember.id")),
)


class ServerRole(Auditable):

    __tablename__ = "serverRole"

    id = Column(UUIDType(binary=False), primary_key=True)
    name = Column(Text, unique=True)

    server_members = relationship(
        "ServerMember",
        secondary=server_member_role_association_table,
        back_populates="roles",
    )


class ServerMember(Auditable):

    __tablename__ = "serverMember"

    id = Column(UUIDType(binary=False), primary_key=True)
    name = Column(Text, unique=True)

    # Many to many
    # One serverMember can have multiple role
    # and
    # one ServerRole can be assigned to several serverMember
    roles = relationship(
        "ServerRole",
        secondary=server_member_role_association_table,
        back_populates="server_members",
    )

    # One to One
    # One user can only be one server member
    user_id = Column(UUIDType(binary=False), ForeignKey("user.id"))

    # Server foreign key
    server_id = Column(UUIDType(binary=False), ForeignKey("server.id"))


class Server(Auditable):

    __tablename__ = "server"

    id = Column(UUIDType(binary=False), primary_key=True)
    name = Column(Text, unique=True)

    # One to many
    # One server can have one or several members
    members = relationship("ServerMember")


class ServerInvitation(Auditable):

    __tablename__ = "serverInvitation"

    id = Column(UUIDType(binary=False), primary_key=True)
    code = Column(Text, unique=True, index=True)
    server_id = Column(UUIDType(binary=False), ForeignKey("server.id"))
    creator = Column(UUIDType(binary=False), ForeignKey("user.id"))
    max_age = Column(Integer)
    max_uses = Column(Integer)
    uses = Column(Integer)
    temporary = Column(Boolean)