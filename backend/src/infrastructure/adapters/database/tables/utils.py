import uuid

from typing import Any

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import CHAR
from sqlalchemy.types import TypeDecorator


class GUID(TypeDecorator):  # pylint: disable=abstract-method)
    """Platform-independent GUID type.

    Uses PostgreSQL's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    """

    impl = CHAR

    def load_dialect_impl(self, dialect: Any) -> Any:
        if dialect.name == "postgresql":
            return dialect.type_descriptor(UUID())
        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value: Any, dialect: Any) -> Any:
        if dialect.name == "postgresql":
            return str(value)
        if not isinstance(value, uuid.UUID):
            return "%.32x" % uuid.UUID(value).int
        # hexstring
        return value if value is None else "%.32x" % value.int

    def process_result_value(self, value: Any, dialect: Any) -> Any:
        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return value
