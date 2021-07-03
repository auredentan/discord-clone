from typing import Any
from typing import AsyncIterator


class Event:
    pass


class IBroadcast:
    def __init__(self, url: str) -> None:
        raise NotImplementedError()

    async def connect(self) -> None:
        raise NotImplementedError()

    async def disconnect(self) -> None:
        raise NotImplementedError()

    async def subscribe(self, channel: str) -> AsyncIterator[Any]:
        raise NotImplementedError()

    async def unsubscribe(self, channel: str) -> None:
        raise NotImplementedError()

    async def publish(self, channel: str, message: Any) -> None:
        raise NotImplementedError()
