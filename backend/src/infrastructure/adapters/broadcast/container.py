from typing import Any, AsyncIterator, List

from dependency_injector import containers, providers

from src.infrastructure.adapters.broadcast.broadcast import Broadcast
from src.infrastructure.adapters.broadcast.service import BroadcastService
from src.infrastructure.configuration import BroadcastConfiguration


async def init_broadcast(redis_host: str, redis_port: int) -> AsyncIterator[Broadcast]:
    broadcast = Broadcast(redis_host=redis_host, redis_port=redis_port)
    await broadcast.connect()
    yield broadcast
    await broadcast.disconnect()


class BroadcastContainer(containers.DeclarativeContainer):

    config: BroadcastConfiguration = providers.Configuration()

    broadcast = providers.Resource(
        init_broadcast,
        redis_host=config.redis_config.redis_host,
        redis_port=config.redis_config.redis_port,
    )

    service: BroadcastService = providers.Factory(
        BroadcastService,
        broadcast=broadcast,
    )


def setup_broadcast(injectable_modules: List[Any]) -> BroadcastContainer:
    container = BroadcastContainer()

    config: BroadcastConfiguration = BroadcastConfiguration()
    container.config.from_pydantic(config)

    container.wire(modules=injectable_modules)
    return container
