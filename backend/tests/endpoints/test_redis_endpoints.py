import pytest
from fastapi.testclient import TestClient

from src.entrypoints.api import app
from src.infrastructure.adapters.redis.service import RedisService


@pytest.mark.asyncio
async def test_redis(test_async_client: TestClient, fake_redis_service: RedisService):
    expected_value = "value"
    fake_redis_service.process.return_value = expected_value

    with app.redis_container.service.override(fake_redis_service):
        response = await test_async_client.get("/redis")

    assert response.status_code == 200
    assert response.json() == expected_value
