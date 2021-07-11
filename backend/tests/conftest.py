from typing import Generator

from unittest import mock

import pytest

from fastapi.testclient import TestClient

from httpx import AsyncClient

from src.entrypoints.api import app
from src.infrastructure.adapters.database.repositories.server import ServerRepository
from src.infrastructure.adapters.database.repositories.server_member import (
    ServerMemberRepository,
)
from src.infrastructure.adapters.database.repositories.server_role import (
    ServerRoleRepository,
)
from src.infrastructure.adapters.database.tables.user import User
from src.infrastructure.adapters.redis.service import RedisService

from src.use_cases.services.server import ServerService
from src.use_cases.services.server_member import (
    ServerMemberService,
)
from src.use_cases.services.server_role import ServerRoleService


@pytest.fixture
def test_client() -> TestClient:
    yield TestClient(app)


@pytest.fixture
def test_async_client(event_loop):
    client = AsyncClient(app=app, base_url="http://test")
    yield client
    event_loop.run_until_complete(client.aclose())


@pytest.fixture
def fake_user() -> User:
    return User(id="fake", email="fake@fake.com", hashed_password="ada", is_active=True)


###########
# Service #
###########


@pytest.fixture
def fake_redis_service() -> Generator[RedisService, None, None]:
    service_mock = mock.AsyncMock(spec=RedisService)
    yield service_mock


@pytest.fixture
def fake_server_service() -> Generator[ServerService, None, None]:
    service_mock = mock.AsyncMock(spec=ServerService)
    yield service_mock


@pytest.fixture
def fake_server_role_service() -> Generator[ServerRoleService, None, None]:
    service_mock = mock.AsyncMock(spec=ServerRoleService)
    yield service_mock


@pytest.fixture
def fake_server_member_service() -> Generator[ServerMemberService, None, None]:
    service_mock = mock.AsyncMock(spec=ServerMemberService)
    yield service_mock


####
# Repository
####


@pytest.fixture
def server_repository_mock() -> Generator[ServerRepository, None, None]:
    server_repository_mock = mock.AsyncMock(spec=ServerRepository)
    yield server_repository_mock


@pytest.fixture
def server_role_repository_mock() -> Generator[ServerRoleRepository, None, None]:
    server_role_repository_mock = mock.AsyncMock(spec=ServerRoleRepository)
    yield server_role_repository_mock


@pytest.fixture
def server_member_repository_mock() -> Generator[ServerMemberRepository, None, None]:
    server_member_repository_mock = mock.AsyncMock(spec=ServerMemberRepository)
    yield server_member_repository_mock
