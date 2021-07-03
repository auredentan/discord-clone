import pytest

from src.entrypoints.api import app
from src.infrastructure.adapters.database.repositories.server import ServerRepository
from src.infrastructure.adapters.database.repositories.server_member import (
    ServerMemberRepository,
)
from src.infrastructure.adapters.database.repositories.server_role import (
    ServerRoleRepository,
)
from src.infrastructure.adapters.database.tables.server import Server
from src.infrastructure.adapters.database.tables.user import User
from src.use_cases.server import create_server


@pytest.mark.asyncio
async def test_create_server(
    fake_user: User,
    server_repository_mock: ServerRepository,
    server_member_repository_mock: ServerMemberRepository,
    server_role_repository_mock: ServerRoleRepository,
):
    # When
    expected_name = "server_name"

    server_repository_mock.add_members.return_value = Server(
        id="d", name=expected_name, members=[]
    )

    # create_server_role

    #
    with app.db_container.server_repository.override(server_repository_mock):
        with app.db_container.server_role_repository.override(
            server_role_repository_mock
        ):
            with app.db_container.server_member_repository.override(
                server_member_repository_mock
            ):
                created_server = await create_server(expected_name, fake_user)

    # Then
    assert created_server
    assert created_server.name == expected_name

    server_repository_mock.add.assert_called_once()
    server_repository_mock.add.assert_called_once()
    server_member_repository_mock.add.assert_called_once()
