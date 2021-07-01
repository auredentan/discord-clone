from fastapi import APIRouter

from src.entities.server import PydanticServer

from src.infrastructure.adapters.database.tables.user import User

from src.use_cases.server import create_server as create_server_use_case

router = APIRouter()


@router.put("/servers/")
async def create_server() -> PydanticServer:

    connected_user: User = User()
    created_server = await create_server_use_case(
        name="server", connected_user=connected_user
    )

    return created_server
