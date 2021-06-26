from src.infrastructure.adapters.broadcast.broadcast import Broadcast


class BroadcastService:
    def __init__(self, broadcast: Broadcast) -> None:
        self.broadcast = broadcast
