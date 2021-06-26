from typing import Any


class Event:
    pass


class IBroadcast:
    def __init__(self, url: str) -> None:
        raise NotImplementedError()

    async def connect(self) -> None:
        raise NotImplementedError()

    async def disconnect(self) -> None:
        raise NotImplementedError()

    async def subscribe(self, group: str) -> None:
        raise NotImplementedError()

    async def unsubscribe(self, group: str) -> None:
        raise NotImplementedError()

    async def publish(self, channel: str, message: Any) -> None:
        raise NotImplementedError()
