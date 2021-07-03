import logging
from typing import Optional

from dependency_injector.wiring import Provide, inject

from src.entities.user import PydanticUser
from src.infrastructure.adapters.database.container import DBContainer
from src.infrastructure.adapters.database.services.user import UserService


@inject
async def get_user_by_id(
    user_id: str,
    user_service: UserService = Provide[DBContainer.user_service],
) -> Optional[PydanticUser]:

    user = await user_service.get_user_by_id(user_id)

    return PydanticUser.from_orm(user) if user else None


@inject
async def create_user(
    user_service: UserService = Provide[DBContainer.user_service],
) -> Optional[PydanticUser]:

    created_user = await user_service.create_user()
    return PydanticUser.from_orm(created_user) if created_user else None
