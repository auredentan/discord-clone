import logging

from typing import Any

from fastapi import APIRouter  # type: ignore[attr-defined]
from fastapi import Depends  # type: ignore[attr-defined]
from fastapi import WebSocket  # type: ignore[attr-defined]

from starlette.concurrency import run_until_first_complete

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject

from src.infrastructure.adapters.broadcast.container import BroadcastContainer
from src.infrastructure.adapters.broadcast.service import BroadcastService

from src.use_cases.dtos.channels import ChannelInvitesResponse
from src.use_cases.dtos.channels import ChannelInvitesRequest

router = APIRouter()


@router.websocket("/channels/{channel_id}/chat")
async def chatroom_ws(websocket: WebSocket, channel_id: str) -> Any:
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
) -> Any:
    async for message in websocket.iter_text():
        await broadcast_service.broadcast.publish(channel=channel_id, message=message)


@inject
async def chatroom_ws_sender(
    websocket: WebSocket,
    channel_id: str,
    broadcast_service: BroadcastService = Depends(Provide[BroadcastContainer.service]),
) -> Any:
    async with broadcast_service.broadcast.subscribe(channel=channel_id) as subscriber:
        async for event in subscriber:
            await websocket.send_text(event.message)


@router.post("/channels/{channel_id}/invites", response_model=ChannelInvitesResponse)
async def get_invites(request: ChannelInvitesRequest) -> ChannelInvitesResponse:
    logging.debug(f"get_invites: {request} ")
    ## TODO: create an invite link
    # eg: discord.gg/<number>
    # number encrypts the infos
    pass
