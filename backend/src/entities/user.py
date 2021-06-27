from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from src.infrastructure.adapters.database.tables.user import User

_PydanticUser = sqlalchemy_to_pydantic(User)


class PydanticUser(_PydanticUser):
    @classmethod
    def from_orm(cls, user: _PydanticUser) -> _PydanticUser:
        user.id = str(user.id)
        return _PydanticUser.from_orm(user)
