import logging

from typing import Iterator

from src.infrastructure.adapters.database.tables.user import User


class UserRepository:
    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> Iterator[User]:
        async with self.session_factory() as session:
            return await session.query(User).all()

    async def get_by_id(self, user_id: int) -> User:
        async with self.session_factory() as session:
            user = await session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            return user

    async def add(
        self, email: str, password: str, is_active: bool = True
    ) -> User:
        async with self.session_factory() as session:
            user = User(
                email=email,
                hashed_password=password,
                is_active=is_active,
            )
            logging.info(f"user; {user} - {session}")
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def delete_by_id(self, user_id: int) -> None:
        async with self.session_factory() as session:
            entity: User = await session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            await session.commit()


class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):

    entity_name: str = "User"
