import uuid

from sqlalchemy import Boolean, Column, Text
from sqlalchemy_utils import UUIDType

from src.infrastructure.adapters.database.tables.base import Auditable


class User(Auditable):

    __tablename__ = "user"

    id = Column(
        UUIDType(binary=False),
        primary_key=True,
        default=str(uuid.uuid4()),
    )
    email = Column(Text, unique=True)
    hashed_password = Column(Text)
    is_active = Column(Boolean, default=True)
