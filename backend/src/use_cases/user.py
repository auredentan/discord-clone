from typing import Optional

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject

from src.entities.user import PydanticUser

from src.infrastructure.adapters.database.container import DBContainer

from src.use_cases.services.user import UserService
from src.use_cases.serializers.user_serializer import user_sqlachemy_to_pydantic


@inject
async def get_user_by_id(
    user_id: int,
    user_service: UserService = Provide[DBContainer.user_service],
) -> Optional[PydanticUser]:

    user = await user_service.get_user_by_id(user_id)

    return user_sqlachemy_to_pydantic(user) if user else None


@inject
async def create_user(
    user_service: UserService = Provide[DBContainer.user_service],
) -> Optional[PydanticUser]:

    created_user = await user_service.create_user()
    return user_sqlachemy_to_pydantic(created_user) if created_user else None
