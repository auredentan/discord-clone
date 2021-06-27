import logging

from typing import Callable

from contextlib import asynccontextmanager
from contextlib import AbstractContextManager

from asyncio import current_task

from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)


class AsyncDatabase:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        self._session_factory = async_scoped_session(
            sessionmaker(engine, class_=AsyncSession), scopefunc=current_task
        )

    @asynccontextmanager
    async def session(self):
        session: AsyncSession = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            await session.rollback()
            raise
        finally:
            await session.close()
