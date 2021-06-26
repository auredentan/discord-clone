from fastapi.testclient import TestClient

import pytest
from unittest import mock
from httpx import AsyncClient

from src.entrypoints.api import app
from src.infrastructure.adapters.redis.service import RedisService


@pytest.fixture
def test_client() -> TestClient:
    yield TestClient(app)


@pytest.fixture
def test_async_client(event_loop):
    client = AsyncClient(app=app, base_url="http://test")
    yield client
    event_loop.run_until_complete(client.aclose())


@pytest.fixture
def fake_redis_service() -> RedisService:
    service_mock = mock.AsyncMock(spec=RedisService)
    yield service_mock
