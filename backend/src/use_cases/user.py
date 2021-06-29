import logging

from typing import Optional

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject

from src.infrastructure.adapters.database.container import DBContainer
from src.infrastructure.adapters.database.services.user import UserService

from src.entities.user import PydanticUser


@inject
async def get_user(
    user_id: str,
    user_service: UserService = Provide[DBContainer.user_service],
) -> Optional[PydanticUser]:

    user = await user_service.get_user_by_id(user_id)

    return PydanticUser.from_orm(user) if user else None


@inject
async def create_user(
    user_service: UserService = Provide[DBContainer.user_service],
):

    user = await user_service.create_user()
    logging.info(f"user {user.id} - {user.__dict__} - {type(user.id)}")
    return PydanticUser.from_orm(user) if user else None
