import logging

from typing import Any
from typing import AsyncIterator
from typing import List

from aioredis import Redis
from aioredis import create_redis_pool

from dependency_injector import containers
from dependency_injector import providers

from src.infrastructure.adapters.redis.service import RedisService
from src.infrastructure.configuration import RedisConfiguration


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

    service: RedisService = providers.Factory(
        RedisService,
        redis=redis_pool,
    )


def setup_redis(injectable_modules: List[Any]) -> RedisContainer:
    container = RedisContainer()

    config: RedisConfiguration = RedisConfiguration()
    logging.debug(f"Using redis on {config.redis_host}:{config.redis_port}")
    container.config.from_pydantic(config)

    container.wire(modules=injectable_modules)
    return container
