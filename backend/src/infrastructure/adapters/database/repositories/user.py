from typing import Iterator

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.adapters.database.tables.user import User
from src.infrastructure.adapters.database.repositories.errors import NotFoundError

from src.entities.user import PydanticUser

class UserRepository:
    def __init__(self, session_factory: AsyncSession) -> None:
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

    async def add(self, user: User) -> User:
        async with self.session_factory() as session:
            
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

    async def update(self, user: PydanticUser) -> User:
        async with self.session_factory() as session:
            existing_user = await self.get_by_id(user.id)

            for key, value in user.dict(exclude={"id"}).items():
                if hasattr(existing_user, key):
                    setattr(existing_user, key, value)

            await session.commit()
            await session.refresh(existing_user)
            return existing_user


class UserNotFoundError(NotFoundError):

    entity_name: str = "User"
