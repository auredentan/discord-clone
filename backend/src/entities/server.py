#  type: ignore
from enum import Enum
from typing import List

from src.entities.base import BaseModel
from src.entities.user import PydanticUser

from src.infrastructure.adapters.database.tables.server import (
    Server,
)
from src.infrastructure.adapters.database.tables.server import Server, ServerMember
from src.infrastructure.adapters.database.tables.server import (
    ServerRole,
)


class BaseServerRole(Enum):
    admin = "admin"
    anonymous = "anonymous"


###############
# Server Role #
###############


class PydanticServerRoleCreate(BaseModel):
    name: str


class PydanticServerRole(PydanticServerRoleCreate):
    id: str


#################
# Server Member #
#################


class PydanticServerMemberCreate(BaseModel):
    name: str
    roles: List[PydanticServerRole]
    user_id: str
    server_id: str


class PydanticServerMember(PydanticServerMemberCreate):
    id: str


##########
# Server #
##########


class PydanticServerCreate(BaseModel):
    name: str
    members: List[PydanticServerMember]


class PydanticServer(PydanticServerCreate):
    id: str
