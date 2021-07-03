from datetime import datetime

from sqlalchemy import Column, DateTime

from src.infrastructure.adapters.database.tables import SqlAlchemyBase


class Auditable(SqlAlchemyBase):  # pylint: disable=too-few-public-methods
    __abstract__ = True

    created_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
