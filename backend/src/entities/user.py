from pydantic.main import BaseModel

from src.infrastructure.adapters.database.tables.user import User


class PydanticUser(BaseModel):
    id: str
    email: str
    hashed_password: str
    is_active: str

    @classmethod
    def from_orm(cls, user: User) -> "PydanticUser":
        user.id = str(user.id)
        return cls.from_orm(user)
