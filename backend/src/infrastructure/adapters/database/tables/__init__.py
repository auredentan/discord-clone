from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData(schema="public")
SqlAlchemyBase: Any = declarative_base(metadata=metadata)  # type: ignore