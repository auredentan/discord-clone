from src.entities.base import BaseModel


class PydanticUserCreate(BaseModel):
    email: str
    hashed_password: str
    is_active: str


class PydanticUser(PydanticUserCreate):
    id: str
