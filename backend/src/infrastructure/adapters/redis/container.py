import logging

from typing import List
from typing import AsyncIterator
from typing import Any

from aioredis import create_redis_pool
from aioredis import Redis

from dependency_injector import containers
from dependency_injector import providers

from src.infrastructure.configuration import RedisConfiguration
from src.infrastructure.adapters.redis.service import RedisService


async def init_redis_pool(host: str, port: int) -> AsyncIterator[Redis]:
    pool = await create_redis_pool(f"redis://{host}:{port}")
    yield pool
    pool.close()
    await pool.wait_closed()


class RedisContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    redis_pool = providers.Resource(
        init_redis_pool,
        host=config.redis_host,
        port=config.redis_port,
    )

    service = providers.Factory(
        RedisService,
        redis=redis_pool,
    )


def setup_redis(endpoints: List[Any]):
    container = RedisContainer()

    config: RedisConfiguration = RedisConfiguration()
    logging.debug(f"Using redis on {config.redis_host}:{config.redis_port}")
    container.config.from_pydantic(config)

    container.wire(modules=endpoints)
