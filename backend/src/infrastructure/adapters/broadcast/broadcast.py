from contextlib import asynccontextmanager
from typing import AsyncIterator, Any

import aioredis

from src.interfaces.broadcast import IBroadcast


class Broadcast(IBroadcast):
    def __init__(self, redis_port: int, redis_host: str) -> None:
        self.redis_port = redis_port
        self.redis_host = redis_host

        self.redis_url = f"redis://{redis_host}:{redis_port}"

        self.pub = None
        self.sub = None

    async def __aenter__(self) -> "Broadcast":
        await self.connect()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        await self.disconnect()

    async def connect(self):
        self.pub = await aioredis.create_redis(self.redis_url)
        self.sub = await aioredis.create_redis(self.redis_url)

    async def disconnect(self):
        self.sub.close()
        self.pub.close()

    async def publish(self, channel: str, message: dict):
        self.pub.publish(channel, message)

    async def unsubscribe(self, channel: str):
        await self.sub.unsubscribe(channel)

    @asynccontextmanager
    async def subscribe(self, channel: str) -> AsyncIterator[aioredis.Channel]:
        try:
            channels = await self.sub.subscribe(channel)
            if channels:
                yield channels[0]
        finally:
            await self.unsubscribe(channel)
