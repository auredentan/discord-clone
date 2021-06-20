from sqlalchemy import Column
from sqlalchemy import relationship
from sqlalchemy import Text
from sqlalchemy import backref


from src.infrastructure.adapters.database.tables.base import Auditable
from src.infrastructure.adapters.database.tables.user import User
from src.infrastructure.adapters.database.tables.utils import GUID


class ServerRole(Auditable):

    __tablename__ = "serverRole"

    id = Column(GUID, primary_key=True)
    name = Column(Text, unique=True)


class ServerMember(Auditable):

    __tablename__ = "serverMember"

    id = Column(GUID, primary_key=True)

    # One to many
    # One user can have multiple role
    roles = relationship(
        ServerRole, backref=backref("serverMember", uselist=True, cascade="delete,all")
    )

    # One to One
    # One user can only be one server member
    user = relationship(User, backref=backref("user", uselist=False))


class Server(Auditable):

    __tablename__ = "server"

    id = Column(GUID, primary_key=True)
    name = Column(Text, unique=True)

    # One to many
    # One server can have one or several members
    members = relationship(
        ServerMember, backref=backref("server", uselist=True, cascade="delete,all")
    )
