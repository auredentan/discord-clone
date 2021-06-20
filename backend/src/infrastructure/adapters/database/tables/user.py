from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean

from src.infrastructure.adapters.database.tables.base import Auditable
from src.infrastructure.adapters.database.tables.utils import GUID


class User(Auditable):

    __tablename__ = "user"

    id = Column(GUID, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
