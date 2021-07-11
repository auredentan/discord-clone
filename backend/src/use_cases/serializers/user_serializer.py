from src.entities.user import PydanticUser  # type: ignore[attr-defined]

from src.infrastructure.adapters.database.tables.user import User


def user_sqlachemy_to_pydantic(user: User) -> PydanticUser:
    return PydanticUser(
        id=str(user.id),
        email=user.email,
        hashed_password=user.hashed_password,
        is_active=user.is_active,
    )
