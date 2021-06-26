import logging

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
    logging.debug(f"chatroom_ws: {channel_id}")
    await websocket.accept()
    await run_until_first_complete(
        (chatroom_ws_receiver, {"websocket": websocket, "channel_id": channel_id}),
        (chatroom_ws_sender, {"websocket": websocket, "channel_id": channel_id}),
    )


@inject
async def chatroom_ws_receiver(
    websocket: WebSocket,
    channel_id: str,
    broadcast_service: BroadcastService = Depends(Provide[BroadcastContainer.service]),
):
    logging.debug(f"chatroom_ws_receiver: {channel_id} - {broadcast_service}")
    async for message in websocket.iter_text():
        await broadcast_service.broadcast.publish(channel=channel_id, message=message)


@inject
async def chatroom_ws_sender(
    websocket,
    channel_id: str,
    broadcast_service: BroadcastService = Depends(Provide[BroadcastContainer.service]),
):
    logging.debug(f"chatroom_ws_sender: {channel_id} - {broadcast_service}")
    async with broadcast_service.broadcast.subscribe(channel=channel_id) as subscriber:
        async for event in subscriber:
            await websocket.send_text(event.message)
