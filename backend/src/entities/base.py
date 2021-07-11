from typing import Optional

from datetime import datetime

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
