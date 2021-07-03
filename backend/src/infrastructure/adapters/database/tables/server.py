from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import Table
from sqlalchemy_utils import UUIDType

from src.infrastructure.adapters.database.tables.base import Auditable

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
