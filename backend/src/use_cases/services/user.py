import logging
from typing import Iterator, Optional
from uuid import uuid4

from src.infrastructure.adapters.database.repositories.user import (
    UserNotFoundError,
    UserRepository,
)
from src.infrastructure.adapters.database.tables.user import User


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    async def get_users(self) -> Iterator[User]:
        return await self._repository.get_all()

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        try:
            return await self._repository.get_by_id(user_id)
        except UserNotFoundError:
            logging.warning(f"User {user_id} not found")
            return None

    async def create_user(self) -> User:
        uid = uuid4()
        return await self._repository.add(
            email=f"{uid}@emaikl.dlcom", password="pdkwld"
        )

    async def delete_user_by_id(self, user_id: int) -> None:
        try:
            return await self._repository.delete_by_id(user_id)
        except UserNotFoundError:
            logging.warning(f"User {user_id} not found")
            raise
