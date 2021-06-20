from fastapi import APIRouter
from fastapi import Depends
from fastapi import WebSocket

from starlette.concurrency import run_until_first_complete

from dependency_injector.wiring import inject
from dependency_injector.wiring import Provide

from src.infrastructure.adapters.broadcast.container import BroadcastContainer
from src.infrastructure.adapters.broadcast.service import BroadcastService

router = APIRouter()


@router.websocket("/channel/{channel_id}/chat")
async def chatroom_ws(websocket: WebSocket, channel_id: str):
    await websocket.accept()
    await run_until_first_complete(
        (chatroom_ws_receiver, {"websocket": websocket}),
        (chatroom_ws_sender, {"websocket": websocket}),
    )


@inject
async def chatroom_ws_receiver(
    websocket: WebSocket,
    broadcast_service: BroadcastService = Depends(Provide[BroadcastContainer]),
):
    async for message in websocket.iter_text():
        await broadcast_service.publish(channel="chatroom", message=message)


@inject
async def chatroom_ws_sender(
    websocket,
    broadcast_service: BroadcastService = Depends(Provide[BroadcastContainer]),
):
    async with broadcast_service.subscribe(channel="chatroom") as subscriber:
        async for event in subscriber:
            await websocket.send_text(event.message)
