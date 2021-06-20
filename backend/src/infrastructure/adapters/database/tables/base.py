from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import Column

from src.infrastructure.adapters.database.tables import SqlAlchemyBase


class Auditable(SqlAlchemyBase):  # pylint: disable=too-few-public-methods
    __abstract__ = True

    created_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
    created_by = Column(Text, nullable=False)
    updated_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
    updated_by = Column(Text, nullable=False)
