from typing import Any
from typing import Optional

from pydantic import BaseModel

class ChannelInvitesRequest(BaseModel):
    maxAge: int
    maxUses: Optional[int] = None
    # Temporary member status
    # User are kicked when disconnected
    temporary: bool = False

class ChannelInvitesResponse(BaseModel):
    channel: dict
    code: str
    createdAt: str
    guild: dict
    inviter: dict
    maxAge: int
    maxUses: Optional[int] = None
    temporary: bool = False
    uses: int